import pandas as pd

#print('Hello, world111!')
#print("Version 1 ")

print("Starting ...")
# Read the file(train.csv") to a List(say trainList)
# hint : use the pandas library to read a file to list. pandas is a library, that provides function called "read_csv"
trainDataList = pd.read_csv('train.csv')


#print the shape of the list. See what the methods are available in the list.
#hint : a list has an attribute shape (list.shape)
print(f"Shape of the list : {trainDataList.shape}")

#This is a tricky step
#Remove 1st column. You can do so, by first creating a dataframe from a list.
# hint : Dataframe can be derived  as : df = pd.DataFrame(dataList)
#        drop the column using : 
dataFrame = pd.DataFrame(trainDataList)
dataFrame = dataFrame.drop(dataFrame.columns[0], axis=1)


#delete column y8,y9
dataFrame = dataFrame.drop(columns=['y8','y9'], axis=1)

#Remove rows that has bad data
#dataFrame = dataFrame.apply(pd.to_numeric, errors='coerce')
#dataFrame = dataFrame.dropna()
#print(f"Shape after Rows cleaned{dataFrame.shape}")

#Remove cols with bad data. Uncomment this to see what happens
dataFrame.apply(pd.to_numeric, errors='coerce',axis=1)
dataFrame = dataFrame.dropna(axis=1)
print(f"Shape after columns cleaned{dataFrame.shape}")

#rename the column y10 to y8
dataFrame=dataFrame.rename(columns={'y10': 'y8'})
print(dataFrame)


#07/17/2022 changes Ends
#Last step : Save the file
# hint : 
pd.DataFrame(dataFrame).to_csv("train_clean.csv", index=False)

print("All done.....")