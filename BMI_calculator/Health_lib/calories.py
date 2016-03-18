from utilz import lbs_to_kgs
from utilz import printer
import math,os
	
def basal_metabolic_rate(sex,age,weight,height):		#to find out calorie needs
	if sex=="female":
		bmr = round((655.0+(4.35*weight)+(4.7*height)-(4.7*age)),2)
	else:
		bmr = round((66.0+( 6.23*weight)+( 12.7*height)-(6.8*age)),2)
	printer("\nYour Basal Metabolic Rate is "+str(bmr)+" cal per day")
	return bmr

def calorie_needs(sex,bmr):									#Harris Benedict Formula
	print "Types of lifestyle:\n1. 'sedentary': little or no exercise\n2. 'lightly active': light exercise/sports 1-3 days/week\n3. 'moderatetely active': moderate exercise/sports 3-5 days/week\n4. 'very active': hard exercise/sports 6-7 days a week\n5. 'extra active': very hard exercise/sports & physical job or 2x training"
	lifestyle={1:'sedentary',2:'lightly active',3:'moderatetely active',4:'very active',5:'extra active'}
	active=raw_input("Choose the number corresponding to your type of lifestyle > ")
	printer("Your current lifestyle is "+lifestyle[int(active)]+".")
	if active== '1': cal= bmr* 1.2
	elif active=='2': cal= bmr* 1.375
	elif active=='3': cal=bmr*1.55
	elif active=='4': cal=bmr* 1.725
	elif active=='5': cal=bmr*1.9
	else : calorie_needs()
	cal=round(cal,2)
	printer("\n"+str(cal)+ " calories is the total number of calories you need in order to maintain your current weight.")
	if sex=="female":
		printer("To lose weight, take "+str(cal-1200)+"-"+str(cal-500)+" calories a day\nTo gain weight, take "+str(cal+500)+" calories a day to gain one pound per week.")
	else:
		printer("To lose weight, take "+str(cal-1800)+"-"+str(cal-500)+" calories a day\nTo gain weight, take "+str(cal+500)+" calories a day to gain one pound per week.")
	return cal