import pandas as pd
data=pd.read_csv("car_info.csv")
print(data)
p=19 
if p<8:
    print(p,"is less than 8")
else:
    print(p,"is greater than 8")
