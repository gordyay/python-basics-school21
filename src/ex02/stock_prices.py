import sys
def calc_price():
    COMPANIES = {
        'apple': 'AAPL',
        'microsoft': 'MSFT',
        'netflix': 'NFLX',
        'tesla': 'TSLA',
        'nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    name = sys.argv[1].lower()
    if (len(sys.argv)==2):
        if name in COMPANIES:
            tick = COMPANIES[name]
            print (STOCKS[tick])
        else:
            print("Unknown company", name)


if __name__ == '__main__':
    calc_price()
