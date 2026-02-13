def tickets(person,numberoftickets):
    return person*numberoftickets
def food(expenditure):
    return expenditure
def travel_cost(cost):
    return cost
def total():
    tray=tickets(5,500)
    c=food(5000)
    w=travel_cost(30000)
    print(tray+c+w) 

total()