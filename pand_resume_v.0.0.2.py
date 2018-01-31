from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import matplotlib.patches as mpatches
import matplotlib.dates as mdates

df = pd.read_csv('/home/drew/Desktop/details.csv')
df.amin = pd.to_datetime(df.amin).astype(datetime)
df.amax = pd.to_datetime(df.amax).astype(datetime)
print(df.amax)
fig = plt.figure()
colors = ["red", "yellow"]
texts = ["Drew", "Meghan"]
# red_patch = mpatches.Patch(color=colors[i], label=df.label.to_string(index=False))
# print(red_patch)
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')
ax = fig.add_subplot(111)
# ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
# ax = plt.legend(handles=[red_patch])
print(df.color.to_string(index=False))
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
print(df["color"])
for i in range(len(df)):
    ax = plt.hlines(df.loc[i,"yaxis"], dt.date2num(df.loc[i, "amin"]), dt.date2num(df.loc[i, "amax"]),
                    colors=df.loc[i, "color"], label=df.loc[i, "label"], linewidth=6)
# ax = plt.hlines(df["yaxis"], dt.date2num(df.amin), dt.date2num(df.amax), linewidth=6)
# plt.legend(handles=[red_patch])
# plt.legend(handles=patches,
#            loc='best', ncol=2, numpoints=1 )
# plt.legend(loc='best')
ax = plt.ylim(0, 50)
# patches = [ plt.plot([],[], mec=None, color=colors[i],
#             label="{:s}".format(texts[i]) )[0]  for i in range(len(texts)) ]
# ax = plt.legend(handles=patches, bbox_to_anchor=(0.5, 0.5),
#            loc='center', ncol=2, facecolor="plum", numpoints=1 )
plt.legend(loc="best")
plt.show()