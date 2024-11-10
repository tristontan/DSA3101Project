import pandas as pd
import simpy
import random
from pprint import *
import pickle

RANDOM_SEED = 170
VISITORS_PER_BATCH = 5 # Assume visitors arrive in groups of 5
NEW_VISITOR_BATCHES = 4500 # Roughly 10000 visitors should be in the park every day
INTERVAL_BATCHES = 100.0  # Generate new customers roughly every x clicks
MIN_PATIENCE = 45  # Min. customer patience - from survey
MAX_PATIENCE = 60  # Max. customer patience - from survey
REPEAT_SAME_RIDE_TIME = 4 # minimum buffer time between rides

# guests leave after 7 hours (operating hours: 10am to 5pm)
CLOSING_TIME = 7*60  
# lunch hours: 11am to 1pm
LUNCH_START = 1*60 
LUNCH_END = 3*60 
# proposed happy hours: 3pm to 5pm
HH_START = 5*60
HH_END = 7*60 

attractions_weighted = []

customers = {}

customer_states = ['riding','transit','eating','shopping','leaving']

# extend the SimPy Resource to keep track of all events
class MonitoredResource(simpy.Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []
  #Used by a process to request access to a resource. When a process calls request, it waits in a queue if the resource is currently occupied. Once the resource becomes available, the process is granted access.
    def request(self, *args, **kwargs):
        self.data.append(('request',self._env.now, len(self.queue)))
        return super().request(*args, **kwargs)
  # Used by a process to release a resource when it is done using it, allowing other waiting processes to take over the resource.
    def release(self, *args, **kwargs):
        self.data.append(('release',self._env.now, len(self.queue)))
        return super().release(*args, **kwargs)

# Combine both time-based and proximity-based adjustments to desirability level
def adjustDesirability(attracts, current_time, current_position, lunch_start=LUNCH_START, lunch_end=3*LUNCH_END, happy_start=HH_START, happy_end=HH_END, base_weight=1.0):
    for attract in attracts.values():
        # Reset desirability to original
        attract['adjusted_desirability'] = attract['desirability']

        # Time-based adjustments for lunch and dinner
        if lunch_start <= current_time <= lunch_end:
            if attract['type'] == 'restaurant':
                attract['adjusted_desirability'] *= 2  # Increase desirability by a factor for lunch
            elif attract['type'] == 'ride':
                attract['adjusted_desirability'] *= 1/2
        
        elif happy_start <= current_time <= happy_end:
            if attract['type'] == 'restaurant':
                attract['adjusted_desirability'] *= 2  # Increase desirability by a factor for happy hour
            elif attract['type'] == 'ride':
                attract['adjusted_desirability'] *= 1/2

        # Proximity-based adjustment
        distance = ((current_position[0] - attract['x'])**2 + (current_position[1] - attract['y'])**2) ** 0.5

        # Handle zero distance by setting a large proximity factor
        if distance == 0:
            proximity_factor = base_weight * 1  # current location
        else:
            proximity_factor = max(1, base_weight / distance)

        attract['adjusted_desirability'] = int(attract['adjusted_desirability'] * proximity_factor)




# Modify the attraction picker function to use the adjusted desirability
def initializeAttractionPicker(attracts):
    global attractions_weighted
    attractions_weighted = []  # Reset the list
    for a in attracts:
        desirability = attracts[a].get('adjusted_desirability', attracts[a]['desirability'])
        for i in range(desirability):
            attractions_weighted.append(attracts[a]['name'])



def pickNextAttractionName(name,attracts):
    global attractions_weighted
    global customers
    # try to find something we haven't been to, but after 5
    # tries, give up and go for a repeat attraction
    for i in range(5):
        picked = random.choice(attractions_weighted)
        if picked not in customers[name]['rides']:
            break
    return picked

def pickNextAttractionName_set(name,attracts):
    weighted_set = set(attractions_weighted)
    visited = set(customers[name]['rides'])
    choices = weighted_set - visited
    pprint(weighted_set)
    print('visited:')
    pprint(visited)
    pprint(choices)
    picked = random.choice(list(choices))
    return picked

def calculateTravelToAttraction(current,destination):
    global REPEAT_SAME_RIDE_TIME
    walk =  walktime[current][destination]
    # add in the min buffer defined earlier, which is the time taken to requeue for tbe same ride
    return walk + REPEAT_SAME_RIDE_TIME

# declare the visitor to the park.  We have added an __init__ method so that the customer can be assigned to a venue

def customer(env, name, attractions):
    global HH_START
    global HH_END
    global MIN_PATIENCE
    global MAX_PATIENCE
    global CLOSING_TIME

    done = False
    while not done:
        if name not in customers.keys():
            # first time
            customers[name] = {}
            customers[name]['name'] = name
            customers[name]['starttime'] = env.now
            customers[name]['rides'] = []
            customers[name]['traveltime'] = 0
            customers[name]['waittime']  = 0
            customers[name]['reneges'] = 0
            customers[name]['left'] = ''
            customers[name]['x'] = 413 # entrance x and y coordinates
            customers[name]['y'] = 814
            customers[name]['restaurant_visits'] = 0
            customers[name]['visit_counts'] = {}
            customers[name]['spending'] = 0
            customers[name]['location'] = "Entrance"
            customers[name]['last_restauranttime'] = -10*60

        current_position = (customers[name]['x'], customers[name]['y'])
        adjustDesirability(attractions, env.now, current_position)
        initializeAttractionPicker(attractions)

        # Pick the next attraction with both constraints
        for _ in range(10):
            attract_name = pickNextAttractionName(name, attractions)
            attraction = attractions[attract_name]

            # Check the general visit constraint
            if customers[name]['visit_counts'].get(attract_name, 0) < 3:
                # Check the restaurant-specific constraint
                if attraction['type'] == 'restaurant':
                    if customers[name]['restaurant_visits'] < 4 and env.now - customers[name]['last_restauranttime'] > 2*60:
                        break  # Found a valid attraction within both constraints
                else:
                    break
        else:
            # If no valid attraction is found after 10 tries, end the visitor's session
            done = True
            break

        # Update visit counts for the chosen attraction
        customers[name]['visit_counts'][attract_name] = customers[name]['visit_counts'].get(attract_name, 0) + 1
        if attraction['type'] == 'restaurant':
            customers[name]['restaurant_visits'] += 1
            customers[name]['last_restaurant'] = env.now

        print(f"Visitor {name} picked attraction {attract_name} at time {env.now}")

        # travel to that attraction and wait until we arrive
        time_to_travel = calculateTravelToAttraction(customers[name]['location'],attract_name)        
        customers[name]['traveltime'] += time_to_travel
        yield env.timeout(time_to_travel)

        # now we have arrived at the selected attraction
        customers[name]['x'] = attraction['x']
        customers[name]['y'] = attraction['y']
        customers[name]['location'] = attract_name
        arrive = env.now
        attraction['visitor_count'] += 1
        if attraction['type'] == 'restaurant':
            spent = random.randint(attraction['pricerange_min'], attraction['pricerange_max']) * 0.6 # Scaled
            if HH_START <= env.now <= HH_END:
                # apply 20% discount
                attraction['revenue'] += spent * 0.8
                customers[name]['spending'] += spent * 0.8
            else:
                attraction['revenue'] += spent
                customers[name]['spending'] += spent
        time_in_ride = attractions[attract_name]['timelength']
        # processing to get in the line at the ride
        with attraction['resource'].request() as req:
            # generate a random patience within the range defined by our survey
            patience = random.uniform(MIN_PATIENCE, MAX_PATIENCE)
            # Wait for the ride or abort at the end of our patience
            results = yield req | env.timeout(patience)
            # calculate our wait time
            wait = env.now - arrive
            attraction['wait_times'].append(wait)
            customers[name]['waittime'] += wait
            if req in results:
                # got on the ride, calculate the ride time
                yield env.timeout(time_in_ride)
                # record that we have been to this ride in our records
                customers[name]['rides'].append(attract_name)
            else:
                # We reneged, the wait was too long, no patience
                attraction['reneged_count'] += 1
                customers[name]['reneges'] += 1

        done_time = env.now > CLOSING_TIME
        done = done_time

# This function effectively controls the flow of visitors entering the park simulation, simulating realistic visitor arrival patterns.
def source(env, batches, number_per_batch, interval, attracts):
    """Source generates customers randomly.  They come in batches (like off a tram)"""
    for i in range(batches):
        for j in range(number_per_batch):
            index = i*j+j
            c = customer(env, 'Customer%06d' % index, attracts)
            env.process(c)
        # wait until the next batch arrives
        t = random.gauss(1.0 / interval, (1.0 / interval)/5.0 )
        yield env.timeout(t)

# summarizes and prints information about the visitors in the simulation.
def printVisitorInformation():
    #for key in customers:
    #    pprint(customers[key])
    print('-----------------------')
    rideCount = 0
    waitMin = 9e99
    waitMax = 0
    waitTotal = 0
    timeLeft = 0
    spending = 0
    restaurantvisits = 0
    for cust in customers:
        waitTotal += customers[cust]['waittime']
        waitMax = max(waitMax,customers[cust]['waittime'])
        waitMin = min(waitMax,customers[cust]['waittime'])
        rideCount +=  len(customers[cust]['rides'])
        timeLeft += (1 if customers[cust]['left'] == 'time' else 0)
        spending += customers[cust]['spending']
        restaurantvisits += customers[cust]['restaurant_visits']
    waitAvg = waitTotal / len(customers.keys())
    rideAvg = rideCount / len(customers.keys())
    spendAvg = spending / len(customers.keys())
    restvisitAvg = restaurantvisits / len(customers.keys())
    print('Visitors rode',rideAvg,'Waiting - min,avg,max:',waitMin,waitAvg,waitMax)
    print(timeLeft,'of total',len(customers.keys()) ,'visitors left after max time')
    print('Visitors spent a total of $', spending, 'and an average of $', spendAvg,' they visited restaurants a total of', restaurantvisits, 'times, with an average of', restvisitAvg, 'restaurant visits each')


def printAttractionInformation():
    print('-----------------------')
    for attract in attracts.keys():
        if len(attracts[attract]['wait_times']) > 0:
            average_wait = sum(attracts[attract]['wait_times'])/float(len(attracts[attract]['wait_times']))
        else:
            average_wait = 0.0
        print(attracts[attract]['name'],'had',attracts[attract]['visitor_count'],
              'visitors with average wait time of',average_wait,
              'and ',attracts[attract]['reneged_count'],' who gave up. It earned $', attracts[attract]['revenue'], 'in revenue')

# the attraction dictionary contains SimPy objects, so it isn't good to serialize out. Copy the contents out of the archive and return a simple dictionary
def generateSerializableVenueRecords(attracts):
    outdict = {}
    for venue in attracts:
        outdict[attracts[venue]['name']] = {}
        outdict[attracts[venue]['name']]['name'] = attracts[venue]['name']
        outdict[attracts[venue]['name']]['type'] = attracts[venue]['type']
        outdict[attracts[venue]['name']]['desirability'] = attracts[venue]['desirability']
        outdict[attracts[venue]['name']]['wait_times'] = attracts[venue]['wait_times']
        outdict[attracts[venue]['name']]['visitor_count'] = attracts[venue]['visitor_count']
        outdict[attracts[venue]['name']]['reneged_count'] = attracts[venue]['reneged_count']
        outdict[attracts[venue]['name']]['revenue'] = attracts[venue]['revenue']
        outdict[attracts[venue]['name']]['events'] = attracts[venue]['resource'].data
    return outdict

def logDesirabilityEveryInterval(env, attractions, closing_hour, interval=30):
    while env.now < closing_hour:
        yield env.timeout(interval)
        # print(f"\nCurrent simulated time: {env.now} minutes")
        # print("Attraction desirability at this time:")
        for attract_name, attract_info in attractions.items():
            desirability = attract_info.get('adjusted_desirability', attract_info['desirability'])
            # print(f"  {attract_name}: Desirability = {desirability}")




#---------------- main loop -------------------


attractList = pd.read_csv(open("uss_attractions.csv","r"))
walkList = pd.read_csv(open("uss_attractions_walktime.csv", "r"))

# Setup and start the simulation
print('Mini park with renege')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# global dictionary of all the venues (rides, restaurants, etc)
attracts = {}

for index, row in attractList.iterrows():
    rowlist = row.tolist()
    thisname = rowlist[0]
    attracts[thisname] = {}
    attracts[thisname]['name'] = thisname
    attracts[thisname]['type'] = rowlist[2]
    attracts[thisname]['desirability'] = int(rowlist[3])
    attracts[thisname]['capacity'] = max(1, int(rowlist[4] / 25))
    attracts[thisname]['timelength'] = float(rowlist[5]) / 60
    attracts[thisname]['x'] = rowlist[6]
    attracts[thisname]['y'] = rowlist[7]
    attracts[thisname]['pricerange_min'] = rowlist[10]
    attracts[thisname]['pricerange_max'] = rowlist[11]
    attracts[thisname]['resource'] = MonitoredResource(env, capacity=attracts[thisname]['capacity'])
    attracts[thisname]['wait_times'] = []
    attracts[thisname]['visitor_count'] = 0
    attracts[thisname]['reneged_count'] = 0
    attracts[thisname]['revenue'] = 0

walktime = {}

for index, row in walkList.iterrows():
    rowlist = row.tolist()
    thisname = rowlist[0]
    if thisname not in walktime:
        walktime[thisname] = {}
    walktime[thisname][rowlist[1]] = int(rowlist[3])

#pprint(walktime)
initializeAttractionPicker(attracts)
#pprint(attractions_weighted)

# Add the process to the simulation environment
env.process(logDesirabilityEveryInterval(env, attracts, CLOSING_TIME))
# Start processes and run
env.process(source(env, NEW_VISITOR_BATCHES, VISITORS_PER_BATCH, INTERVAL_BATCHES, attracts))
env.run()

#pprint(attracts)

#for key in customers:
#    pprint(customers[key])
printVisitorInformation()
printAttractionInformation()

# make output records object
venue_records = generateSerializableVenueRecords(attracts)
records = {'attractions': venue_records, 'guests':customers}
print('storing records of the day in the park')
pickle.dump( records, open( "parksim_records_with_changes.p", "wb" ) )
