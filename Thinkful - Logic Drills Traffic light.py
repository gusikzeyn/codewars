def update_light(current):
    print({"green": "yellow", "yellow": "red", "red": "green"}[current])
update_light('red')
#green
update_light('yellow')
#red
update_light('green')
#yellow