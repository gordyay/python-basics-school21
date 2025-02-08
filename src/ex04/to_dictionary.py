def list_of_tuples_to_dict():
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
        if number not in countries:
            countries[number] = []
        countries[number].append(country)
    for number in range(1000):
        
        if number in countries:
            for country in countries[number]:
                print(f"'{number}' : '{country}'")


if __name__ == '__main__':
    list_of_tuples_to_dict()
