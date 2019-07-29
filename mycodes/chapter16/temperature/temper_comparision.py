from matplotlib import pyplot as plt
import csv
from datetime import datetime

def temperature_graph(filename,location):
    with open(filename) as f:
        reader=csv.reader(f)
        header=next(reader)
    
        dates,highs,lows=[],[],[]
        for row in reader:
            try:
                date=datetime.strptime(row[0],"%Y-%m-%d")
                high=int(row[1])
                low=int(row[3])
            except ValueError:
                print("{0:s}: Data missing in {1}".format(location,date))
            else:
               dates.append(date)
               highs.append(high)
               lows.append(low)

    
    plt.xlim(dates[0],dates[-1])
    plt.ylim(10,120)
    plt.plot(dates,highs,c="red",alpha=0.5)#alpha控制透明度
    plt.plot(dates,lows,c="blue",alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)#填充带
    plt.title("Daily high and low temperatures-2014 in "+location,fontsize=24)
    plt.xlabel("" ,fontsize=16)
    
    plt.ylabel("Temperature (F)",fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
"""
建立两张画布
fig1=plt.figure(num=1,figsize=(12,6))
temperature_graph("death_valley_2014.csv","Death Valley")
fig1.autofmt_xdate()
plt.savefig("DeaVa_tem.png")

fig2=plt.figure(num=2,figsize=(12,6))
temperature_graph("sitka_weather_2014.csv","Sikta")
fig2.autofmt_xdate()
plt.savefig("Sitka_tem.png")
"""

#一张画布，两个子图
fig=plt.figure(figsize=(12,15))

plt.subplot(2,1,1)
temperature_graph("death_valley_2014.csv","Death Valley")
plt.subplot(2,1,2)
temperature_graph("sitka_weather_2014.csv","Sikta")
fig.autofmt_xdate()


plt.savefig("DV_S_tem.png")