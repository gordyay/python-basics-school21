import sys
def get_key(dict, value):
    for key, val in dict.items():
        if val == value:
            return key


def all_stocks():
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
        list_of_names = sys.argv[1].replace(" ","").split(",")
        if "" not in list_of_names: 
            for name in list_of_names:
                name = name.strip()
                if name.capitalize() in COMPANIES:
                    print(f"{name.capitalize()} stock price is {STOCKS[COMPANIES[name.capitalize()]]}")
                elif name.upper() in STOCKS:
                    print(f"{name.upper()} is a ticker symbol for {get_key(COMPANIES,name.upper())}")
                else:
                    print(f"{name} is an unknown company or an unknown ticker symbol")


if __name__ == '__main__':
    all_stocks()
