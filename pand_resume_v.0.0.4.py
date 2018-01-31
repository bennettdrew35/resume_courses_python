from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import matplotlib.dates as mdates

df1 = pd.read_csv('/home/drew/Desktop/job_List.csv')
df1.start = pd.to_datetime(df1.start).astype(datetime)
df1.end = pd.to_datetime(df1.end).astype(datetime)
df2 = pd.read_csv('/home/drew/Desktop/online_Courses_Completed.csv')
lang_c = df2['language'].value_counts()
lang_v = []
for v, c in df2['language'].value_counts().iteritems():
    lang_v.append(v)
fig = plt.figure(figsize=(12,7))
fig.canvas.set_window_title('Visual Resume')
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')
ax1 = fig.add_subplot(211)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(yearsFmt)
ax1.xaxis.set_minor_locator(months)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
for i in range(len(df1)):
    ax1 = plt.hlines(df1.loc[i, "yaxis"], dt.date2num(df1.loc[i, "start"]), dt.date2num(df1.loc[i, "end"]),
                    colors=df1.loc[i, "color"], label=df1.loc[i,"company"] + ": " + df1.loc[i, "exp"], linewidth=6.5)
ax1 = plt.ylim(0, 15)
ax1 = plt.legend(loc="upper center", ncol=2)
ax1 = plt.tick_params(bottom='on', left='off', labelleft='off', labelbottom='on')
ax1 = plt.title('Career Timeline')
ax1 = plt.xlabel("Years")
ax2 = fig.add_subplot(212)
pl_ax = lang_c.plot(kind='barh')
ax2 = pl_ax.set_yticklabels(lang_v, minor=False)
ax2 = pl_ax.set_title("Online Courses Completed")
ax2 = pl_ax.set_ylabel("Coding Languages")
ax2 = pl_ax.set_xlabel("# of Courses Completed")
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=.5)
plt.savefig('visual_Resume')
plt.show()