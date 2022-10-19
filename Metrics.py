from datetime import datetime, timedelta
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import plotly.offline as pyoff
import plotly.graph_objs as go

df_retail = pd.read_csv('OnlineRetail.csv',encoding = "ISO-8859-1")

df_retail.head
# Monthly Growth Rate = Tính tăng trưởng về mặt doanh thu của tháng sau so với tháng trước đó
# Monthly Active Customers = Số lượng customer hoạt động hàng tháng
# Trung bình trong 1 tháng có bao nhiêu lượng sản phẩm đc bán ra
# Số doanh thu trung bình trong 1 tháng
# New & Existing Customers
# Monthly New Customer Ratio
# Monthly Retention Rate
# Churn Rate
# Cohort Base Retention

df_retail.info()
df_retail['InvoiceDate'] = pd.to_datetime(df_retail['InvoiceDate'])

df_retail.info()



str(df_retail['InvoiceDate'][0].year) + "-" + str(df_retail['InvoiceDate'][0].month)

df_retail['InvoiceYearMonth'] = df_retail['InvoiceDate']
# for i in range(len(df_retail)):
#     df_retail['InvoiceYearMonth'][i] = df_retail['InvoiceYearMonth'][i].year*100 + df_retail['InvoiceYearMonth'][i].month

df_retail['InvoiceYearMonth'] = df_retail['InvoiceDate'].map(lambda x: x.year*100 + x.month)

# input: 2011-12-09 09:27:00
# output: 2011-12/201112

df_retail['Revenue'] = df_retail['UnitPrice'] * df_retail['Quantity']

sum1=0
arr1 = []
df_retail['InvoiceYearMonth'].unique()[0]
for k in range(len(df_retail['InvoiceYearMonth'].unique())):
    for i in range(len(df_retail)):
        if df_retail['InvoiceYearMonth'][i] == df_retail['InvoiceYearMonth'].unique()[k]:
            sum1 = df_retail['Revenue'][i] + sum1
            arr1.append(sum1)

df_retail.groupby('InvoiceYearMonth1')['Revenue','Quantity'].sum()

df_retail.groupby('InvoiceYearMonth1').agg({'Revenue' : 'sum', 'Quantity' : 'mean'})

df_revenue = df_retail.groupby('InvoiceYearMonth1')['Revenue','Quantity'].sum().reset_index()

plot_data = [
    go.Scatter(
        x=df_revenue['InvoiceYearMonth1'],
        y=df_revenue['Revenue'],
    )
]

plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='Montly Revenue'
    )

fig = go.Figure(data=plot_data, layout=plot_layout)
pyoff.plot(fig)

(560000.260 - 748957.020)*100/748957.020

pct_change = [0]
for i in range(len(df_revenue)-1):
    i=i+1
    # round((df_revenue['Revenue'][1] - df_revenue['Revenue'][0])*100/df_revenue['Revenue'][0],2)
    # round((df_revenue['Revenue'][2] - df_revenue['Revenue'][1])*100/df_revenue['Revenue'][1],2)
    # round((df_revenue['Revenue'][12] - df_revenue['Revenue'][11])*100/df_revenue['Revenue'][12],2)

    monthlyGrowth = round((df_revenue['Revenue'][i] - df_revenue['Revenue'][i-1])*100/df_revenue['Revenue'][i-1],2)
    pct_change.append(monthlyGrowth)
pct_change

df_revenue['pct_change'] = pct_change

df_revenue['Revenue'].pct_change()
a = df_retail["InvoiceYearMonth"].value_counts().reset_index()
a.rename(columns= {'index': 'Year_Month'},inplace = True)
a.sort_values(by=["Year_Month"])


df_retail["InvoiceYearMonth"].unique()
df_retail[df_retail['Quantity'] == 0] 
b = df_retail[df_retail["CustomerID"] ==17850]
c = b.sort_values(by=['InvoiceYearMonth'])
c["InvoiceYearMonth"].unique()
d =df_retail.groupby(by=["CustomerID"]).InvoiceYearMonth.min().reset_index()
df_retail["InvoiceYearMonth"]
 #  buoc 1 ket hop 2 bang df
df = pd.merge(df_retail,d, on='CustomerID', how='inner')
df["EN"] = []
df["es"]= df["InvoiceYearMonth_x"] == df["InvoiceYearMonth_y"]
df["es"]=df["es"].replace({True :"New",False: "exit"})
df["es"].value_counts()

# THEO TUNG THANG NAM CO BN KHACH HANG NEW VA EX
monthx = df.groupby(by=["InvoiceYearMonth_x","es"])["es"].count().reset_index()

pd.to_datetime(df_retail['InvoiceDate'])

# =============================================================================
# 
# =============================================================================




