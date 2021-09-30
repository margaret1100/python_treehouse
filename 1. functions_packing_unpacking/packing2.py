#Can sum dynamic number of args
def calculate_total(*args):
    total = sum(args)
    print(total)

calculate_total(25, 25, 20, 35)
