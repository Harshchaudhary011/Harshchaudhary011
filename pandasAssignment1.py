import numpy as np
import pandas as pd
#using tabulate library for making table
from tabulate import tabulate
import datetime
x=datetime.datetime.now()
def readdata(filepath):
    data = pd.read_csv(filepath)
    return data
#filepath1= r"C:\Users\dell\Downloads\26-03-2021_delivery.csv"
readdata(r"C:\Users\dell\Downloads\26-03-2021_delivery.csv")
#sharesprice=pd.read_csv(r"C:\Users\dell\Downloads\26-03-2021_delivery.csv").drop("Unnamed: 0",axis=1)
#specifying format just to print date
#date=x.strftime("%d")
#print(type(date))

# drop unnamed
groupone=sharesprice.where(sharesprice.Delivery_Percentage>=99)
# table format
# order by delivery percentage higeshest on the top
# multiple groups
# #drop nan


groupone=groupone.dropna()
#print(tabulate(groupone,'keys',tablefmt='pipe'))
#print("C://Users//dell//Documents//"+d+".csv")
print(groupone)
print(x.month)
filename=x.strftime("%d")+x.strftime("%m")+x.strftime("%y")+str("-subset-99-101")
#groupone.to_csv("C:/Users/dell//Documents/"+filename+".csv")

#doing same for others groups as well
grouptwo=sharesprice.where(sharesprice.Delivery_Percentage<99)
grouptwo=grouptwo.where(sharesprice.Delivery_Percentage>75).dropna()
print(tabulate(grouptwo,'keys',tablefmt='pipe'))
