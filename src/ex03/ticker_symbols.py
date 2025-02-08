import sys

def get_key(dict, value):
    for key, val in dict.items():
        if val == value:
            return key


def ticker_price():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    

    if (len(sys.argv)==2):
        ticker_name = sys.argv[1].upper()
        company_name = get_key(COMPANIES, ticker_name)
        if company_name:
            print (company_name, STOCKS[ticker_name])
        else:
                    print("Unknown ticker")




if __name__ == '__main__':
    ticker_price()
