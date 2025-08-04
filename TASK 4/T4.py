import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('A.csv')

df['DateTime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str))

df['Hour_of_Day'] = df['DateTime'].dt.hour
df['Day_of_Week'] = df['DateTime'].dt.day_name()
df['Month'] = df['DateTime'].dt.month_name()

for col in ['Road_Conditions', 'Weather_Conditions', 'Light_Conditions']:
    if df[col].isnull().any():
        df[col].fillna(df[col].mode()[0], inplace=True)

for col in ['Latitude', 'Longitude']:
    if df[col].isnull().any():
        df[col].fillna(df[col].median(), inplace=True)

sns.set_style("whitegrid")
plt.figure(figsize=(18, 15))

plt.subplot(3, 2, 1)
sns.countplot(x='Hour_of_Day', data=df, palette='viridis')
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')

plt.subplot(3, 2, 2)
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(x='Day_of_Week', data=df, order=day_order, palette='magma')
plt.title('Accidents by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45, ha='right')

plt.subplot(3, 2, 3)
sns.countplot(y='Weather_Conditions', data=df, order=df['Weather_Conditions'].value_counts().index, palette='cividis')
plt.title('Accidents by Weather Conditions')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')

plt.subplot(3, 2, 4)
sns.countplot(y='Road_Conditions', data=df, order=df['Road_Conditions'].value_counts().index, palette='plasma')
plt.title('Accidents by Road Conditions')
plt.xlabel('Number of Accidents')
plt.ylabel('Road Condition')

plt.subplot(3, 2, 5)
sns.countplot(y='Light_Conditions', data=df, order=df['Light_Conditions'].value_counts().index, palette='coolwarm')
plt.title('Accidents by Light Conditions')
plt.xlabel('Number of Accidents')
plt.ylabel('Light Condition')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Longitude', y='Latitude', data=df, hue='Severity', size='Severity', sizes=(20, 400), alpha=0.6, palette='Reds')
plt.title('Accident Hotspots by Severity')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()