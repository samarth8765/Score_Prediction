import pandas as pd
data1=pd.read_pickle("data.pickle")
#used for training the model

data2=pd.read_csv("https://raw.githubusercontent.com/koshalnirwan/IPL-Data-Analysis-Score-Prediction/main/deliveries.csv")
print(data2.head())



