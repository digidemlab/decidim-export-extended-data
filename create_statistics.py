import json
import pandas as pd
import openpyxl
import xlsxwriter

users = pd.read_csv('decidim_users.csv')
users = users[users['type'] != 'Decidim::UserGroup']

extended_data = [json.loads(user) for user in users['extended_data'].to_list() if user != '{}']

statistics = {}

for key in extended_data[0].keys():
    statistics[key] = {}

for user in extended_data:
    for key in user.keys():
        value = user[key]
        if value not in statistics[key].keys():
            statistics[key][value] = 1
        else:
            statistics[key][value] += 1

Excelwriter = pd.ExcelWriter('statistics.xlsx', engine='xlsxwriter')

for metric in statistics.keys():
    df = pd.DataFrame.from_dict(statistics[metric].items())
    df.columns = [metric, 'number']
    df = df.sort_values(metric)
    df.to_excel(Excelwriter, sheet_name=metric, index=False)

Excelwriter.save()
