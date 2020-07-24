from keys import *
from nasdaqGrab import *
from alpha_vantage.timeseries import TimeSeries
# Your key here
key = alphaVantage


def historicalDaily(symbol):
    ts = TimeSeries(key,  output_format='csv')
    #returns a tuple
    data, meta = ts.get_daily(symbol='AAPL', outputsize='full')
    with open((symbol +'.csv'), 'w') as file:
        writer = csv.writer(file, dialect='excel')
        for row in data:
            writer.writerow(row)


def main():
    symbols = symbolList()
    for symbol in symbols[1:3]:
        historicalDaily(symbol)


#if __name__ == '__main__':
main()
