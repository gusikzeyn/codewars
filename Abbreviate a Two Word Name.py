def abbrevName(name):
    print( '.'.join(w[0] for w in name.split()).upper())

abbrevName('Hesen Zeynalov')