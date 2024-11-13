# -*- coding: utf-8 -*-
"""key drivers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VDO2V0eEOZ5YHQg5pnpUpV4Xk5x8uDh-
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_excel('/content/drive/MyDrive/DSA3101 Data/Processed Data/Survey_cleaned_balanced.xlsx')

!pip install gspread oauth2client
from google.colab import auth
auth.authenticate_user()

print(len(data))
data.tail()

"""KEY DRIVERS OF SATISFACTION

"""

target = 'Rating experience'
predictors = [
    "Improve experience [Short wait times]",
    "Improve experience [Lack of crowds]",
    "Improve experience [Fun attractions]",
    "Improve experience [Affordable food options]",
    "Improve experience [Accessibility (Ramps, even ground, easy to find seats etc)]",
    "Improve experience [Cooling Weather]",
    "Improve experience [Presence of Shaded Rest Areas]",
    "Improve experience [Usability of the Universal Studios Singapore App]",

]

X = data[predictors]
y = data[target]

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print(model.summary())

coefficients = model.params[1:]
coefficients = coefficients.abs().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=coefficients.values, y=coefficients.index, palette='viridis')
plt.title('Key Drivers of Satisfaction (Standardized Coefficients - Improve Experience Factors)')
plt.xlabel('Coefficient Value (Absolute)')
plt.ylabel('Factors')
plt.tight_layout()
plt.show()

"""KEY DRIVERS OF DISSATISFACTION

"""

target = 'Rating experience'
predictors = [
'Worsen experience [Long wait time]',
    'Worsen experience [Crowds]',
    'Worsen experience [Attractions not being fun enough]',
    'Worsen experience [Expensive food options]',
    'Worsen experience [Inaccessibility (Lack of ramps, Uneven ground, lack of seats etc)]',
    'Worsen experience [Hot weather]',
    'Worsen experience [Lack of Shaded Rest Areas]',
    'Worsen experience [Usability of the Universal Studios Singapore App]'

]

X = data[predictors]
y = data[target]

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()


print(model.summary())

coefficients = model.params[1:]
coefficients = coefficients.abs().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=coefficients.values, y=coefficients.index, palette='viridis')
plt.title('Key Drivers of Satisfaction (Standardized Coefficients - Worsen Experience Factors)')
plt.xlabel('Coefficient Value (Absolute)')
plt.ylabel('Factors')
plt.tight_layout()
plt.show()