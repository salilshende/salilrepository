# Import pandas library
import pandas as pd

# Read file "train.csv" into a list trainDataList
trainDataList = pd.read_csv('train.csv')

#print shape of trainDataList
trainDataListshape = trainDataList.shape
print('trainDataListshape:', trainDataListshape)

#Create dataframe from trainDataList
df = pd.DataFrame(trainDataList)

#Drop three columns from trainDataList
df = df.drop(df.columns[[0,8,9]], axis=1)

#Save the cleaned dataframe into train_clean.csv 
pd.DataFrame(df).to_csv("train_clean.csv", index=False)

print('Successfully removed three columns having bad data from train.csv')

#Remove rows that has bad data
df = df.apply(pd.to_numeric, errors='coerce')
df = df.dropna()
print(f"Shape after Rows cleaned{df.shape}")

#Remove cols with bad data. Uncomment this to see what happens
#df = df.apply(pd.to_numeric, errors='coerce',axis=1)
#df = df.dropna(axis=1)
#print(f"Shape after columns cleaned{df.shape}")

#rename the column y10 to y8
df = df.rename(columns={'y10': 'y8'})
print(df)

#07/24/2022 changes Ends
#Last step : Save the file
# hint : 
pd.DataFrame(df).to_csv("train_clean.csv", index=False)

print("All done.....")
