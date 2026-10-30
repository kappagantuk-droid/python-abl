#MULTI-PLANNING TELECOMMUNICATION COST OPTIMIZATION
plans = [("A", 199, 2, 200, 100, 28),("B", 299, 5, 500, 200, 28),("C", 399, 10, 1000, 300, 56),("D", 499, 15, 1500, 500, 84)]

data = float(input("Data used (GB): "))
calls = int(input("Call minutes: "))
sms = int(input("SMS used: "))
days = int(input("Validity required: "))
budget = float(input("Budget: "))
eligible = []

for p in plans:
    cost = p[1] + max(data-p[2], 0)*20
    cost += max(calls-p[3], 0)*0.5
    cost += max(sms-p[4], 0)*0.25
    if p[5] >= days and cost <= budget:
        eligible.append((cost, p[0]))
if eligible:
    print("Best plan:", min(eligible))
else:
    print("No eligible plan")
