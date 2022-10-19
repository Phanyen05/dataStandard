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

# # -*- coding: utf-8 -*-
"""
doanh thu
tìm ra 
"""
df_retail["revenue"] = df_retail["UnitPrice"] *df_retail["Quantity"]
df_retail["InvoiceDate"] = pd.to_datetime(df_retail["InvoiceDate"])


# a =df_retail["InvoiceDate"][0].year*100 +df_retail["InvoiceDate"][0].month

df_retail['InvoiceYearMonth'] = df_retail['InvoiceDate'].map(lambda x: x.year*100 + x.month)

# df2 = df[["Courses","Fee","Duration"]]
df2 =df_retail[["InvoiceYearMonth","revenue"]]
#  neu == groupby InvoiceYearMonth","revenue"]] +sum

df_revenue = df_retail.groupby('InvoiceYearMonth')['revenue','Quantity'].sum().reset_index()

# round((df_revenue['Revenue'][1] - df_revenue['Revenue'][0])*100/df_revenue['Revenue'][0],2)

d =[0]
for i in range(len(df_revenue)-1):
    c =round((df_revenue['revenue'][i+1] - df_revenue['revenue'][i])*100/df_revenue['revenue'][i],2)
    d.append(c)
df_revenue["revenue"][12]
round((df_revenue['revenue'][12] - df_revenue['revenue'][11])*100/df_revenue['revenue'][11],2)



# Monthly Active Customers = Số lượng customer hoạt động hàng tháng
df_Active = df_retail.groupby("InvoiceYearMonth")["CustomerID"].nunique().reset_index()
# df_.columns.values


# Trung bình trong 1 tháng có bao nhiêu lượng sản phẩm đc bán ra
df_avg = df_retail.groupby("InvoiceYearMonth")["Quantity"].sum().reset_index()



 # Số doanh thu trung bình trong 1 thángt
df_profit = df_retail.groupby("InvoiceYearMonth")["revenue"].mean().reset_index()




# New & Existing Customers
df_ex= df_retail.groupby("CustomerID").InvoiceYearMonth.min().reset_index()




