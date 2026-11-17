basic_salary = 50000
hra = basic_salary * 0.2  # House Rent Allowance is 20% of basic salary
da = basic_salary * 0.1  # Dearness Allowance is 10% of basic salary
gross_salary = basic_salary + hra + da
print("--- Employee salary details---")
print("Basic Salary: ", basic_salary)
print("HRA: ", hra)
print("DA: ", da)
print("Gross Salary: ", gross_salary)