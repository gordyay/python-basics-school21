def get_key(dict, value, count=None):
    counter=0
    for key, val in dict.items():
        if val == value:
            counter+=1
            if count==None or count == counter: 
                return key



def dict_sort():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    countries = {}
    for country, number in list_of_tuples:
        number = int(number)
        countries[country]=number
    
    for number in range(999, -1, -1):
        country=get_key(countries, number)
        second_country=get_key(countries, number,2)
        if country:
            if second_country:
                if country[0]<second_country[0]:
                    print(f"{country}\n{second_country}")
                else:
                    print(f"{second_country}\n{country}")
            else:
                print(f"{country}")
if __name__ == '__main__':
    dict_sort()
