def data_types():
    types=[int(),
    str(),
    float(),
    bool(),
    list(),
    dict(),
    tuple(),
    set()
    ]
    print("[", end='')
    for t in types:
        print(type(t).__name__, end='')
        if type(t).__name__ != "set":
            print(",", end=' ')
    print("]")



if __name__ == '__main__':
    data_types()
