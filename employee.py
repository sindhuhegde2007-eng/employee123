import sys
if len(sys.argv) != 5:
    print("Usage: python bonus_calc.py <employee_name> <performance_rating> <performance_bonus> <bonus_percentage>")
    
    employee_name = "sara"
    performance_rating = 2.5
    bonus_percentage = 5   
else:
    employee_name = sys.argv[1]
    performance_rating = float(sys.argv[2])
    bonus_percentage = float(sys.argv[3])

if performance_rating >= 3.5:
    salary = 60000
elif performance_rating >= 2.5:
    salary = 40000
else:
    salary = 15000

annual_bonus = salary * (bonus_percentage / 100)

print("Employee Name:", employee_name)
print("Performance Rating:", performance_rating)
print("Bonus Percentage:", bonus_percentage)
print("Annual Bonus:", annual_bonus)