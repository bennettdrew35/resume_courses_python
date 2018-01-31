from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import matplotlib.dates as mdates

df = pd.read_csv('/home/drew/Desktop/details.csv')
df.amin = pd.to_datetime(df.amin).astype(datetime)
df.amax = pd.to_datetime(df.amax).astype(datetime)
print(df.amax)
fig = plt.figure()
colors = ["red", "yellow"]
texts = ["Drew", "Meghan"]
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
y_axis = 0.3
for i in range(len(df)):
    ax = plt.hlines(y_axis, dt.date2num(df.loc[i, "amin"]), dt.date2num(df.loc[i, "amax"]),
                    colors=df.loc[i, "color"], label=df.loc[i, "label"], linewidth=6)
    y_axis += 0.6
ax = plt.ylim(0, 15)
plt.legend(loc="best")
plt.tick_params(top='off', bottom='on', left='off', right='off', labelleft='off', labelbottom='on')
plt.show()