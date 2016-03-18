import math
from utilz import lbs_to_kgs
from utilz import printer
from definitions import *

def bmi_func(weight,height):							#Calculates Body Mass Index
	bmi = round(((weight*703.0) / ( height**2.0 ) ),2)
	printer("\nYour BMI is "+str(bmi))
	country=raw_input("Choose country of origin: US, UK, RU, JP, HK, SG, IN, Other > ")		#There are actually only 4 standards
	
	if country=="HK" :
		printer("According to Hospital Authority of HongKong,the ideal BMI is 18.5 to 23. \nYour ideal weight with respect to your height is "+str(round((18.5*(height**2) /703),2))+"-"+str(round((23*(height**2) /703),2))+"lbs or "+str(lbs_to_kgs(18.5*(height**2) /703))+"-"+str(lbs_to_kgs(23*(height**2) /703))+"kgs\n")
		if bmi<=18.5:	
			underweight()
		elif bmi>18.5 and bmi<=23.0 : 
			normal()
		elif bmi>23.0 and bmi<=25.0 : 
			overweight()
		elif bmi>25.0 and bmi<=30.0 :
			moderately_obese()
		else:
			severely_obese()
			
	elif country=="JP" :
		printer("According to Japan Society for Study of Obesity(2000), the ideal BMI is 18.5 to 23. \nYour ideal weight with respect to your height is "+str(round((18.5*(height**2) /703),2))+"-"+str(round((23*(height**2) /703),2))+"lbs or "+str(lbs_to_kgs(18.5*(height**2) /703))+"-"+str(lbs_to_kgs(23*(height**2) /703))+"kgs")
		if bmi<=18.5:	
			underweight()
		elif bmi>18.5 and bmi<=25.0 : 
			normal()
		elif bmi>25.0 and bmi<=30.0 : 
			overweight()
		elif bmi>30.0 and bmi<=35.0 :
			moderately_obese()
		elif bmi>35.0 and bmi<=40.0 :
			extremely_obese()
		else: 
			morbidly_obese()
	
	elif country=="SG" :
		printer("Singaporeans have higher proportion of body fat and increased risk for cardiovascular diseases and diabetes mellitus. The ideal BMI is 18.5 to 23. \nYour ideal weight with respect to your height is "+str(round((18.5*(height**2) /703),2))+"-"+str(round((23*(height**2) /703),2))+"lbs or "+str(lbs_to_kgs(18.5*(height**2) /703))+"-"+str(lbs_to_kgs(23*(height**2) /703))+"kgs")
		if bmi<=18.5:	
			severe_underweight()
		elif bmi>18.5 and bmi<=23.0 : 
			normal()
		elif bmi>23.0 and bmi<=27.0 : 
			moderately_obese()
		else:
			severely_obese()
			
	else:
		printer("According to World Health Organization, the ideal BMI is 18.5 to 24.9. \nYour ideal weight with respect to your height is "+str(round((18.5*(height**2) /703),2))+"-"+str(round((24.9*(height**2) /703),2))+"lbs or "+str(lbs_to_kgs(18.5*(height**2) /703))+"-"+str(lbs_to_kgs(24.9*(height**2) /703))+"kgs")
		if bmi <= 16.0:				
			severe_underweight()
		elif bmi > 16.0 and bmi<=18.5:	
			underweight()
		elif bmi>18.5 and bmi<=25.0 : 
			normal()
		elif bmi>25.0 and bmi<=30.0 : 
			overweight()
		elif bmi>30.0 and bmi<=35.0 :
			moderately_obese()
		elif bmi>35.0 and bmi<=40.0 : 
			extremely_obese()
		else:
			morbidly_obese()
	return bmi
