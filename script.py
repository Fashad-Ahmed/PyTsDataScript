import json
import pandas as pd
import datetime
# Q1

arr=[]
with open('data.json') as json_file:
    data = json.load(json_file)
def cal(x,y):
  for i in range(len(data[x])):
      arr.append(data[x][i][y])
  print(max(arr))
  print(min(arr))
  print(sum(arr)/len(arr))

cal('social_D','90day_bull_prop_rollingz_60')
cal('social_D','cumulative_abs')
cal('price_D','volume')
cal('price_D','last')

# Q2

arr_xw = []
val = last_arr[0]
for i in last_arr:
  for j in date:
    if val > i:
      i+=1
    elif val < i:
      val = i

      arr_xw.append(j)

arr_xw.sort()
arr_xw[:3]
print('Highest Closing is happened on: ', arr_xw[0])
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

for i in range(3):
  firstPart = int(arr_xw[i][:4])
  secPart = int(arr_xw[i][5:7])
  thirdPart = int(arr_xw[i][8:])
  dateTime = datetime.date(firstPart, secPart, thirdPart)

  Day = dateTime.weekday()

  print('Highest Closing is happened on no.',i,' is : ',weekDays[Day])

# Q3

date=[]
prop=[]
cumulative=[]
last_arr=[]

for i in range(len(data['social_D'])):
      cumulative.append(data['social_D'][i]['cumulative_z'])
      prop.append(data['social_D'][i]['90day_bull_prop_rollingz_60'])

for i in range(len(data['price_D'])):
      date.append(data['price_D'][i]['date'])
      last_arr.append(data['price_D'][i]['last'])

data_to_csv = pd.DataFrame({'date':date,'90day_bull_prop_rollingz_60':prop,'cumulative_z':cumulative,'last':last_arr})
data_to_csv.to_csv('data_to_csv.csv')