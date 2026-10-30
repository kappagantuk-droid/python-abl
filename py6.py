distance = float(input("Distance in km: "))
age = int(input("Passenger age: "))
travel_class = input("Class (Sleeper/AC3/AC2/First): ").lower()

basic = min(distance, 100)*1
basic += min(max(distance-100, 0), 400)*0.8
basic += max(distance-500, 0)*0.6

charges = {"sleeper": 0, "ac3": 250, "ac2": 500, "first": 1000}
if travel_class not in charges:
    print("Invalid class")
else:
    rate = 1 if age < 5 else 0.5 if age <= 11 else 0.2 if age >= 60 else 0
    fare = basic * (1-rate) + charges[travel_class] + 40
    print("Final fare:", round(fare, 2))
    cancel = input("Cancel ticket? (yes/no): ").lower()
    if cancel == "yes":
        penalty = 0.25 * (basic*(1-rate)+charges[travel_class])
        print("Refund:", round(fare-penalty-40, 2))
