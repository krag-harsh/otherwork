import pandas as pd
# import xlrd
# import openpyxl
import matplotlib.pyplot as plt

col_n=['Amplitude']
for i in range(1,1001):
    col_n.append(str(i))
# print(col_n)
#command to read the excel file provided
data = pd.read_excel('Data-Assignment2.xlsx', sheet_name=['Day1', 'Day2', 'Day3', 'Day4'])
#storing the different day data in different variable
df1 = pd.DataFrame(data['Day1'])
df2 = pd.DataFrame(data['Day2'])
df3 = pd.DataFrame(data['Day3'])
df4 = pd.DataFrame(data['Day4'])
#renaming the columns
df1.columns=col_n
df2.columns=col_n
df3.columns=col_n
df4.columns=col_n

#finding mean of the data for each time point
mean_df1 = df1.mean()
mean_df2 = df2.mean()
mean_df3 = df3.mean()
mean_df4 = df4.mean()

# print(mean_df1)

#running an moving average filter of width 25
fs_df1 = mean_df1.rolling(25, min_periods=1).mean()
fs_df2 = mean_df2.rolling(25, min_periods=1).mean()
fs_df3 = mean_df3.rolling(25, min_periods=1).mean()
fs_df4 = mean_df4.rolling(25, min_periods=1).mean()

# print(fs_df1)

#taking absolute value of each variable
fs_df1 = fs_df1.abs()
fs_df2 = fs_df2.abs()
fs_df3 = fs_df3.abs()
fs_df4 = fs_df4.abs()
# print(fs_df1)

#plotting the graphs
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.tight_layout(h_pad=2)
fs_df1.plot(kind='line', color='green', linewidth=3, figsize=(14, 6), ax=axes[0,0], title='Day 1', xlabel='Time(in ms)', ylabel='Amplitude')
fs_df2.plot(kind='line', color='blue', linewidth=3, figsize=(14, 6),ax=axes[0,1], title='Day 2', xlabel='Time(in ms)', ylabel='Amplitude')
fs_df3.plot(kind='line', color='red', linewidth=3, figsize=(14, 6),ax=axes[1,0], title='Day 3', xlabel='Time(in ms)', ylabel='Amplitude')
fs_df4.plot(kind='line', color='yellow', linewidth=3, figsize=(14, 6),ax=axes[1,1], title='Day 4', xlabel='Time(in ms)', ylabel='Amplitude')
plt.show()