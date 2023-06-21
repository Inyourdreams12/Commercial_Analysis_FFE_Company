# -*- coding: utf-8 -*-
"""The Yearend's Commercial Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SQFa3hNP-p6y2HEspEDnilAADR3zNxrh

###IMPORT LIBRARIES AND LOAD DATASET
"""

! pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

import os
os._exit(00)

#imports:

import pandas as pd
import plotly
import plotly.express as px
import pandas_profiling
from pandas_profiling import ProfileReport

!pip install autoviz

!pip install autoviz --upgrade

from autoviz.AutoViz_Class import AutoViz_Class

#setting the plotly template

template_style = 'plotly_dark'

#load the dataframe

df = pd.read_excel('/year_end_commercial_data.xlsx', engine='openpyxl')

df.sample(10)

df.info()

df.describe()

#Nan count for each column

df.isnull().sum()

#get a view of unique values in column

df['Ship Mode'].unique()

"""###AUTOMATED REPORT

"""

pip install --upgrade pip

pip install --upgrade Pillow

!pip3 install -e

import os
os.kill(os.getpid(), 9)

#generate Pandas Profilling Report

profile = ProfileReport(df,title='Sales Profilling Report')

#view in Notebook
profile

#autoviz report (and Profilling above) to make a quick overview and take advantage of speed up exploration data analysis

AV = AutoViz_Class()
df_autoviz = AV.AutoViz('/content/year_end_commercial_data.xlsx')

"""###DATA PREPERATION & ANALYSIS
⛳ TASKS:

*   What was the highest Sale in 2020?
*   What is average discount rate of chairs?
*   Add extra columns to seperate Year & Month from the Order Date column
*   Add new column to calculate the Profit Margin for each sales record
*   Export manipulcated dataframe to Excel
*   Create a new dataframe to reflect total Profit & Sales by Sub-Category column
*   Create a function to return a dataframe which is grouped by particular column (as a input)





"""

#highest value

df.nlargest(2,'Sales')

#the average discount of chairs

mask = df['Sub-Category'] == 'Chairs'

#use the boolean mask to filter df

df[mask]['Discount'].mean()

#add extra column 'Order Month' & 'Order Year'

df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month

df.sample(5)

#add new column to calculate the Profit Margin for each sales record

df['Profit Margin'] = df['Profit'] / df['Sales']
df.sample(5)

#export manipulated df back to excel

df.to_excel('/content/df_output.xlsx', index =False)

#total Profit & Sales by Sub-Category

df_by_sub_cat = df.groupby('Sub-Category').sum()
df_by_sub_cat.head()

#groupby as a function

def grouped_data(column_name):
      df_tmp = df.groupby(column_name).sum()
      df_tmp.reset_index(inplace=True)
      return df_tmp

grouped_data('Segment')

grouped_data('Sub-Category')

"""###VISUALIZE THE DATA USING PLOTLY LIBRARY"""

#quick start overview for Sales

df['Sales'].describe()

!pip install plotly==5.15.0

!pip install plotly>=4.7.1
!wget https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage -O /usr/local/bin/orca
!chmod +x /usr/local/bin/orca
!apt-get install xvfb libgtk2.0-0 libgconf-2-4

!pip install --upgrade plotly

import plotly.graph_objects as go
import plotly.express as px

import plotly.io
plotly.io.renderers.default = "colab"

#create chart
fig = px.histogram(df,
                   x='Sales',
                   template=template_style)

#plot chart
HTML(fig.to_html())

#show the distribution and skewness of Sales "Boxploti
fig = px.box(df, y='Sales',
      range_y=[0,1000],
      template=template_style)
#plot
HTML(fig.to_html())

#plot Sales by Sub-Category

data = grouped_data('Sub-Category')
data.head()

#create chart

fig = px.bar(data,
             x='Sub-Category',
             y='Sales',
             title='<b>Sales by Sub Category</b>',
             template = template_style)

HTML(fig.to_html())

#plot Profit by Sub-Category

fig = px.bar(data,
             x='Sub-Category',
             y='Profit',
             title='<b>Sales by Sub Category</b>',
             template = template_style)

HTML(fig.to_html())

#plot Sales & Profit by Sub-Category

fig = px.bar (data,
              x='Sub-Category',
              y='Sales',
              color='Profit',
              color_continuous_scale=['red', 'yellow', 'green'],
              template = template_style,
              title='<b>Sales & Profit by Sub Category</b>')

HTML(fig.to_html())

#Inspect Negative Profit of 'Tables'
#Is there any linear correlation Sales/Profit & Discount?

fig = px.scatter(df,
                x='Sales',
                y='Profit',
                color= 'Discount',
                template = template_style,
                title = '<b>Scatterplot Sales/Profit</b>')

HTML(fig.to_html())

#Relize that high discount result in negative profit

#check discount mean by Sub-Category
#create new df

df_discount = df.groupby('Sub-Category').agg({'Discount':'mean',
                                              'Profit':'sum'})

df_discount.head()

fig = px.bar (df_discount,
              x=df_discount.index,
              y='Discount',
              color='Profit',
              color_continuous_scale=['red', 'yellow', 'green'],
              template = template_style,
              title = '<b>Mean Discount by Sub Category</b>')

HTML(fig.to_html())

#the Bliners with discount of 38% still generate profit of almost 8000$

#plot Sales & Profit Development for the year 2020

df_sorted = df.sort_values(by=['Order Date'])
df_sorted.head()

#add cumulative Sales & Profit

df_sorted['Cumulative_Sales'] = df_sorted['Sales'].cumsum()
df_sorted['Cumulative_Profit'] = df_sorted['Profit'].cumsum()
df_sorted.head()

#Plot cumulative sales & profit

fig = px.line(df_sorted,
              x='Order Date',
              y=['Cumulative_Sales', 'Cumulative_Profit'],
              template = template_style,
              title='<b>Sales/Profit Development 2020</b>')

HTML(fig.to_html())