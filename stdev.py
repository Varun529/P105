import csv
import math
with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total += int(x)

    mean=total/n
    return mean
    


S_list=[]
for num in data:
    a= int(num)- mean(data)
    a= a**2  
    S_list.append(a)  


sum=0
for i in S_list:
    sum = sum+i 

result=sum/(len(data)-1)

std_div=math.sqrt(result)  
print(std_div)      