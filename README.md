# group_project_1

## November 22, 2022

## Collaborators
Andres and Jerami

## project title
Tax Harvest Advisor

## team members
Andres and Jerami

## project description
This app will display a portfolio, the app will tell you the number of shares to sell from a certain ticker and we will determine the best way for you to take out liquidity from your portfolio while paying the least percentage in taxes.

link to powerpoint https://docs.google.com/presentation/d/1QKN8u2pbODa9MGk3ETLlIGk2O6R36f3C0858kuxQlR0/edit#slide=id.p

## reseach questions to answer
How can we distinguish between short term capital gains tax and long term capital gains tax while also giving the user the best option to take liquidity?
Can  we help people discover how much they would pay in taxes with a simple app that is user friendly, is it possible to make taxes simple and easy?

## datasets to be used
stock ticker data
user provided data

## rough break down of tasks
1. genrate portofolio by allowing user to input purchase date, ticket, shares, price into app
2. display portfolio balance by symbol up to date info provided by api
![Alt text](newplot.png)
3. determine if asset would be short term or long term capital gain
4. ask user how much liquidity they'd like to gain from portfolio to either cash out or rebalance
    a. provide sell recommendation by symbol and shares and current price
5. any new stocks purchased added to the portfolio
6. portfolio analysis
    a. cashing out as much liquidity as possible from the winners while using the losers to offset the tax liability
![Alt text](newplot2.png)
7. show key stats from the harvest act to include current portfolio value, cash created, tax liability amount, value of stocks sold
![Alt text](output.png)