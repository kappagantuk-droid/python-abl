
age = int(input("Age: "))
income = float(input("Annual income: "))
consult = float(input("Consultation charge: "))
diagnostic = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))
paid = float(input("Amount paid: "))

base = consult + diagnostic + treatment
discount = (0.10 if age >= 60 else 0)
discount += (0.05 if income <= 150000 else 0)
discount = min(discount, 0.15)
total = base * (1 - discount)

if paid < 0 or paid > total:
    print("Invalid payment")
else:
    print("Final bill:", round(total, 2))
    print("Balance:", round(total-paid, 2))
    if paid == total:
        print("Paid")
    elif paid > 0:
        print("Partially paid")
    else:
        print("Unpaid")
