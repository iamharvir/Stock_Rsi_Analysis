import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
import sys

api_key = '0JQGF1N67LXG1T2M'

def get_rsi_Data(ticker, interval, api_key):
    #obtain stock price data
    timeS = TimeSeries(key = api_key, output_format = 'pandas')
    data, meta_data = timeS.get_intraday(symbol=ticker, interval=interval, outputsize='full')
    figure = make_subplots(rows= 2, cols=1, vertical_spacing=0.3, row_heights=[.9,.3], subplot_titles=(ticker + " STOCK CHART @ " + interval + " intervals", "RSI CHART"))
    
    #add candlestick chart to first subplot
    figure = figure.add_trace(go.Candlestick(x=data.index,
                open=data['1. open'],
                high=data['2. high'],
                low=data['3. low'],
                close=data['4. close'],increasing_line_color= 'mediumspringgreen', decreasing_line_color= 'crimson'), row=1, col=1)
    
    #obtain RSI analysis data
    techI = TechIndicators(key = api_key, output_format = 'pandas')
    data, meta_data = techI.get_rsi(symbol=ticker, interval=interval)
    
    #add the RSI line to chart and the 2 boundaries at values 30 and 70
    figure.add_trace(go.Scatter(x=data.index, y=data['RSI'], mode="lines"), row=2, col=1)
    figure.add_trace(go.Scatter(x=data.index, y=np.array([30]*len(data.index)), mode="lines"), row=2, col=1)
    figure.add_trace(go.Scatter(x=data.index, y=np.array([70]*len(data.index)), mode="lines"), row=2, col=1)
    #edit the x-axis range
    figure.update_xaxes(rangebreaks=[
        dict(bounds=["sat", "mon"]), #hide weekends
        dict(bounds=[17, 9], pattern="hour"),  #hide After hours
        dict(values=["2015-12-25", "2016-01-01"])  # hide Christmas and New Year's
    ])
    #update theme, titles, cursor modes
    figure.update_xaxes(matches='x', showspikes=True)
    figure.update_layout(hovermode='y unified')
    figure.layout.template = "plotly_dark"
    figure.update_traces(hoverinfo='none')
    figure.update_yaxes(fixedrange=False)
    figure.update_yaxes(title_text="Price $", row=1, col=1)
    figure.update_yaxes(title_text="RSI Value", row=2, col=1)
    figure.update_yaxes(showspikes=True)
    
    figure.show()

get_rsi_Data(sys.argv[1], sys.argv[2], api_key)



