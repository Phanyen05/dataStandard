# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 21:38:40 2022

@author: PC
"""
from datetime import datetime, timedelta
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import plotly.offline as pyoff
import plotly.graph_objs as go

# Monthly Growth Rate = Tính tăng trưởng về mặt doanh thu của tháng sau so với tháng trước đó
# Monthly Active Customers = Số lượng customer hoạt động hàng tháng
# Trung bình trong 1 tháng có bao nhiêu lượng sản phẩm đc bán ra
# Số doanh thu trung bình trong 1 tháng
# New & Existing Customers
# Monthly New Customer Ratio
# Monthly Retention Rate
# Churn Rate
# Cohort Base Retention


file = pd.read_csv('OnlineRetail.csv',encoding = "ISO-8859-1")
# tại sao cần encoding ??
file.head()

file["price"] = file["Quantity"] * file ["UnitPrice"]
print(type(file["InvoiceDate"]))
print(file['InvoiceDate'].dtypes)
#

file["InvoiceDate"] = pd.to_datetime(file['InvoiceDate'])
int(file["InvoiceDate"][0].year())
