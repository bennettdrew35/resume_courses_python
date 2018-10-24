from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import matplotlib.dates as mdates

df1 = pd.read_csv('/home/drew/Desktop/job_List.csv')
df1.start = pd.to_datetime(df1.start).astype(datetime)
df1.end = pd.to_datetime(df1.end).astype(datetime)
df2 = pd.read_csv('/home/drew/Desktop/online_Courses_Completed.csv')
df3 = pd.read_csv('/home/drew/Desktop/Data_Science_Projects.csv')
lang_c1 = df2['language'].value_counts()
lang_v1 = []
for v, c in df2['language'].value_counts().iteritems():
    lang_v1.append(v)
lang_c2 = df3['language'].value_counts()
lang_v2 = []
for x, y in df3['language'].value_counts().iteritems():
    lang_v2.append(x)
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
ax2 = fig.add_subplot(223)
pl_ax1 = lang_c1.plot(kind='barh')
ax2 = pl_ax1.set_yticklabels(lang_v1, minor=False)
ax2 = pl_ax1.set_title("Online Courses Completed")
ax2 = pl_ax1.set_ylabel("Coding Languages")
ax2 = pl_ax1.set_xlabel("# of Courses Completed")
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=.5)
ax3 = fig.add_subplot(224)
pl_ax2 = lang_c2.plot(kind='bar')
ax3 = pl_ax2.set_xticklabels(lang_v2, minor=False)
ax3 = pl_ax2.set_title("Independent Data Science Projects Completed")
ax3 = pl_ax2.set_xlabel("Coding Languages")
ax3 = pl_ax2.set_ylabel("# of Projects Completed")
plt.savefig('visual_Resume')
plt.show()