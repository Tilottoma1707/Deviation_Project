import pandas as pd
import math 
import csv

with open('data.csv',newline='')as f:
    reader = csv.reader(f)
    filedata=list(reader)
data = filedata[0]

def mean(data):
    n = len(data)
    total=0
    for x in data:
        total+=int(x)
    mean = total/n
    return mean

squaredlist = []
for t in data:
    a = int(t)-mean(data)
    a = a**2
    squaredlist.append(a)

sum = 0

for n in squaredlist:
    sum = sum+n 
result= sum /(len(data)-1)
standardDeviation = math.sqrt(result)

print("the standard deviation is" , standardDeviation)