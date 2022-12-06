#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Initial imports
import os
import requests
import pandas as pd
import numpy as np
from pathlib import Path
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import streamlit as st
#from MCForecastTools import MCSimulation
import warnings
warnings.filterwarnings("ignore")

#%matplotlib inline


# In[33]:


# Load .env enviroment variables
load_dotenv()


# In[34]:


# read in portfolio.csv format date,ticker,shares,share_price, clean data, set date as index,
portfolio_df = pd.read_csv(Path('portfolio.csv'), index_col=0, parse_dates=True, infer_datetime_format=True)
portfolio_df
#list(portfolio_df.columns) 


# In[35]:


#  add profit/loss column, (takes the number of shares * purchase share_price) - current prices
portfolio_df['order_total'] = portfolio_df['no_of_shares']*portfolio_df['share_price']
#clean_portfolio_df

#join_data_columns = pd.concat([portfolio_df, clean_portfolio_df], axis= 'columns', join="inner")
#join_data_columns.head()

#join_data_columns.drop(join_data_columns.filter(regex="0"),axis=1, inplace=True)
#join_data_columns.head()

st.write(portfolio_df)


# In[36]:


# get current prices. use api to get current price

API_KEY = os.getenv('ALPACA_API_KEY')

API_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')

type(API_KEY)

# Create the Alpaca API object
alpaca = tradeapi.REST(
    API_KEY,
    API_SECRET_KEY,
    api_version='v2'
)

# Format current date as ISO format NEED TO AUTO GRAB TODAY'S DATE
today = pd.Timestamp("2022-12-01", tz='America/New_York').isoformat()

# Set the tickers
tickers = portfolio_df['symbol'].unique()

# Set timeframe to "1Day" for Alpaca API
timeframe = "1Day"

stock_price_df = alpaca.get_bars(
    tickers,
    timeframe,
    start=today,
    end=today
).df

stock_price_df.head(10)

portfolio_df.reset_index(inplace=True)


# In[37]:


# concat current prices to portfolio 
#current_close_df = pmerge([portfolio_df, stock_price_df], axis= 'columns', join="left")
#current_close_df.head()
from datetime import *


current_price_df = portfolio_df.merge(stock_price_df, how='left', on='symbol')
current_price_df['order_date'] = pd.to_datetime(current_price_df['order_date']).dt.date
current_price_df['current_value'] = current_price_df['no_of_shares']*current_price_df['close']
date_check = date.today() - current_price_df['order_date'] 
current_price_df['bought_days_from_today'] = date_check
current_price_df['bought_days_from_today'] = current_price_df['bought_days_from_today'].dt.days
current_price_df['tax_type'] = ''
current_price_df['PNL'] = current_price_df['current_value'] - current_price_df['order_total']


#gains = current_price_df['bought_days_from_today']

#for i in gains:
 #   if gains > 365:
  #      st('true')
   # elif 
    #    st('false')

#st(current_price_df['bought_days_from_today'])
#if current_price_df['bought_days_from_today']>365:
#    st ('True')
#else:
 #    st ('not true')

    # > 365:
    #st('its true')

#st(current_price_df['order_date'])


#st(current_price_df['order_date'])

#date_check = date.today() - current_price_df['order_date'] 

#st(date_check)


#st(date.today())
#if current_price_df['date'] > 

#add total value column to dataframe profit/loss column
#portfolio.head()


# In[38]:


current_price_df.loc[current_price_df['bought_days_from_today'] >=365, 'tax'] = 'LT'
current_price_df.loc[current_price_df['bought_days_from_today'] < 365, 'tax'] = 'ST'


#current_price_df['tax_type'] = (current_price_df['bought_days_from_today'] >= 365).all()
   # current_price_df['tax_type'] = 'LT'
#else :
 #   current_price_df['tax_type'] = 'ST'

current_price_df


# In[70]:


# display blanace of each tax type and ask user to input dollar total of withdrawal requested, put amount in column "amount_to_withdraw"
LT_portfolio_df = current_price_df.loc[current_price_df['tax'] == 'LT']
LT_portfolio_balance = LT_portfolio_df['current_value'].sum()
LT_portfolio_inital_investment = LT_portfolio_df['order_total'].sum()
LT_taxable_amount = LT_portfolio_balance - LT_portfolio_inital_investment
LT_negative_pnl = LT_portfolio_df[LT_portfolio_df['PNL'] < 0].sum()
LT_positive_pnl = LT_portfolio_df[LT_portfolio_df['PNL'] > 0].sum()
LT_negative_pnl =LT_negative_pnl['PNL']
LT_positive_pnl =LT_positive_pnl['PNL']
st.write(LT_portfolio_df)


st.write(f"the value of your long term gains taxable portfolio is  $ {LT_portfolio_balance}")
st.write(f"your initial investment is  $ {LT_portfolio_inital_investment}")
st.write(f"the taxable difference is  $ {LT_portfolio_balance} - {LT_portfolio_inital_investment} = {LT_taxable_amount} ")
st.write(f"the positive pnl sum is $ {LT_positive_pnl}")

ST_portfolio_df = current_price_df.loc[current_price_df['tax'] == 'ST']
ST_portfolio_balance = ST_portfolio_df['current_value'].sum()
ST_portfolio_inital_investment = ST_portfolio_df['order_total'].sum()
ST_taxable_amount = ST_portfolio_balance - ST_portfolio_inital_investment
total_portfolio_value = LT_portfolio_balance + ST_portfolio_balance
st.write(ST_portfolio_df)




st.write(f"the value of your short term gains taxable portfolio is  $ {ST_portfolio_balance}")
st.write(f"your initial investment is  $ {ST_portfolio_inital_investment}")
st.write(f"the taxable difference is  $ {ST_portfolio_balance} - {ST_portfolio_inital_investment} = {ST_taxable_amount} ")
st.write(f"total portfolio value is $ {total_portfolio_value}")


# In[71]:



st.write(LT_positive_pnl)
st.write(LT_negative_pnl)


# In[41]:


# ask user for yearly income to determine tax bracket. put amount in column "taxable_income"


# In[42]:


# convert "taxable_income" to percentage of taxes owed from tax bracket into column "tax_pct"


# In[43]:


# ask user for 2 letter state abbreviation saved in var "user_state"


# In[44]:


# look up state tax by user_state. add state_tax to tax_pct


# 

# In[45]:


# calculate from profit/loss column which shares to sell that has the closest total to zero. 


# In[46]:


# save the net total in a new column "tax_liability", additional new column "short_term/long_term_gains


# In[47]:


# display the ticker and number of shares to sell to get to desired amount_to_withdraw


# In[48]:


# display new tax bill by taking ticker sold value * tax_pct

