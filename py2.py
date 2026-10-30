
def bill(units):
    energy = min(units, 100)*2
    energy += min(max(units-100, 0), 100)*3
    energy += min(max(units-200, 0), 300)*5
    energy += max(units-500, 0)*7
    surcharge = energy*0.05 if energy > 2000 else 0
    rebate = energy*0.05 if energy < 500 else 0
    return energy + 100 + surcharge - rebate

previous = float(input("Previous bill: "))
for month in range(1, 4):
    units = float(input("Units consumed: "))
    current = bill(units)
    print("Bill:", round(current, 2))
    if previous > 0 and (current-previous)/previous > 0.30:
        print("Unusual increase!")
    previous = current
