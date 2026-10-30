#EMPLOYEE PAYROLL AND DEDUCTION ANALYSIS
basic = float(input("Basic pay: "))
hours = float(input("Overtime hours: "))
incentive = float(input("Incentives: "))

hra = basic * 0.20
da = basic * 0.10
overtime = hours * 200
gross = basic + hra + da + overtime + incentive

deduction = min(gross, 10000)*0
deduction += min(max(gross-10000, 0), 10000)*0.05
deduction += max(gross-20000, 0)*0.10
net = gross - deduction

print("HRA:", hra, "DA:", da)
print("Overtime:", overtime)
print("Gross salary:", gross)
print("Deduction:", deduction)
print("Net salary:", net)
