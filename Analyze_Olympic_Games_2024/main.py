import pandas as pd

# df = pd.read_csv('data\medals_total.csv')
#
# print(type(df))  # <class 'pandas.core.frame.DataFrame'>
# print(df)

# for group by
df = pd.read_csv('data\schedules.csv')

# grouped_by_day = df.groupby("day")
# Practice - 1
# print(grouped_by_day)
# print(type(grouped_by_day))
# Practice - 2
# for group_name, df in grouped_by_day:
#     print(group_name)
#     print(df)
# Practice - 3
grouped_by_day = df.groupby(["day","status"])
for group_name,df in grouped_by_day:
    print(group_name)