#re is used to remove all non-numbers from string; needed for emp_length and earliest_credit
import re

#Import csv and read it
file = open("accepted_2007_to_2017.csv", "r", encoding="utf8")
lines = file.readlines()

#Define new and empty lists that are for high interest rate group
high_int_emp_length = []
high_int_home_own = []
high_int_annual_inc = []
high_int_state = []
high_int_earliest_credit = []
high_int_fico = []
high_int_open_credit_acc = []

#
#
#Pull and set significant parameters
for person in lines[1:]:
	poc = person.strip().split(",")

	#Set interest rate
	try:
		int_rate = float(poc[6])
	except ValueError:
		continue

	#Set length of employment
	try:
		raw_emp_length = poc[11]
		emp_length = float(re.sub("[^0-9]", "", raw_emp_length))
	except ValueError:
		continue

	#Set annual income
	try: 
		annual_inc = float(poc[13])
	except ValueError:
		continue

	#Set earliest established credit
	try:
		raw_earliest_credit = poc[26]
		earliest_credit = float(re.sub("[^0-9]", "", raw_earliest_credit))
	except ValueError:
		continue
	
	#Set lowest credit score
	try: 
		fico_low = float(poc[27])
	except ValueError:
		continue

	#Set highest credit score
	try:
		fico_high = float(poc[28])
	except ValueError:
		continue

	#Define credit score
	fico = ((fico_high + fico_low) / 2)

	#Set anount of open accounts
	open_credit_acc = float(poc[32])

#
#
#

#Filters to high interest rate group
	if int_rate > 25:
		high_int_emp_length.append(emp_length)

		high_int_annual_inc.append(annual_inc)

		high_int_earliest_credit.append(earliest_credit)

		high_int_fico.append(fico)

		high_int_open_credit_acc.append(open_credit_acc)		

#
#
#Calculations
avg_emp_length = sum(high_int_emp_length)/len(high_int_emp_length)

avg_annual_inc = sum(high_int_annual_inc)/len(high_int_annual_inc)

avg_earliest_credit = sum(high_int_earliest_credit)/len(high_int_earliest_credit)

avg_fico = sum(high_int_fico)/len(high_int_fico)

avg_open_credit_acc = sum(high_int_open_credit_acc)/len(high_int_open_credit_acc)

print("This is avg emp length:")
print(avg_emp_length)

print("This is avg annual income:")
print(avg_annual_inc)

print("This is avg earliest credit:")
print(avg_earliest_credit)

print("This is avg fico score:")
print(avg_fico)

print("This is avg open credit account:")
print(avg_open_credit_acc)

#print("People that pay 25%+ interest rate have" + #employ length)

print("script is complete")