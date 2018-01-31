from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import matplotlib.patches as mpatches
import matplotlib.dates as mdates

df = pd.read_csv('/home/drew/Desktop/details.csv')
df.amin = pd.to_datetime(df.amin).astype(datetime)
df.amax = pd.to_datetime(df.amax).astype(datetime)
fig = plt.figure()
# red_patch = mpatches.Patch(color='red', label='The red data')
ax = fig.add_subplot(111)
# ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
# ax = plt.legend(handles=[red_patch])
print(df.color.to_string(index=False))
# ax = plt.hlines(df["yaxis"], dt.date2num(df.amin), dt.date2num(df.amax), colors=df["color"], label=df["label"], linewidth=6)
ax = plt.hlines(df["yaxis"], dt.date2num(df.amin), dt.date2num(df.amax), colors=[(.255,0,0)], linewidth=6)
patches = [ plt.plot([],[], marker="o", ms=10, ls="", mec=None, color=df["label"],
            label="{:s}".format(df["color"]) )[0]  for i in range(len(df["label"])) ]
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
ax = plt.ylim(0, 50)
plt.show()