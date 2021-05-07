This program uses Alpha_Vantage to obtain stock price and analysis data for user specified stocks and time intervals

To Run the program simply run this command

python3 stockCharts.py

For example, to get a stock chart of Apple on a 5 minute interval run,

python3 stockCharts.py AAPL 5min

Valid interval values include: '1min', '5min', '15min', '30min', '60min'

Libraries used include: numpy, https://numpy.org/doc/stable/numpy-ref.pdf pandas, https://pandas.pydata.org/docs/reference/index.html alpha_vantage, https://github.com/RomelTorres/alpha_vantage plotly, https://plotly.com/python/ time, https://docs.python.org/3/library/time.html sys, https://docs.python.org/3/library/sys.html