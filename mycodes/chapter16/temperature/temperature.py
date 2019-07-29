from matplotlib import pyplot as plt
import csv
from datetime import datetime

with open("death_valley_2014.csv") as f:
    reader=csv.reader(f)
    header=next(reader)
    
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            date=datetime.strptime(row[0],"%Y-%m-%d")
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print("Data missing in {0}".format(date))
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(figsize=(12, 6))
plt.xlim(dates[0],dates[-1])
plt.plot(dates,highs,c="red",alpha=0.5)#alpha控制透明度
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)#填充带
plt.title("Daily high and low temperatures-2014 in death valley",fontsize=24)
plt.xlabel("" ,fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()