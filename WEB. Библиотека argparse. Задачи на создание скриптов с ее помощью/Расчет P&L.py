import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--per-day', type=float)
parser.add_argument('--per-week', type=float)
parser.add_argument('--per-month', type=float)
parser.add_argument('--per-year', type=float)
parser.add_argument('--get-by', choices=['day', 'month', 'year'])
arg = parser.parse_args()
week = 7
month = 30
year = 360
day = 1
per_day = 0
per_week = 0
per_month = 0
per_year = 0
if arg.per_day:
    per_day = arg.per_day
if arg.per_week:
    per_week = arg.per_week
if arg.per_month:
    per_month = arg.per_month
if arg.per_year:
    per_year = arg.per_year
lst_per = [per_day, per_week, per_month, per_year]
lst_day = [day, week, month, year]
for i in range(len(lst_per)):
    lst_per[i] = lst_per[i] / lst_day[i]
choices = 1
if arg.get_by:
    choices = eval(f'{arg.get_by}')
per_day = sum(lst_per)
print(int(per_day * eval(f'{choices}')))