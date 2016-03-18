import math
from utilz import lbs_to_kgs
from utilz import printer

def waist_to_hip_ratio(waist, hip, sex):
	printer("\nThe Waist to Hip(WHR) ratio has been used as an indicator or measure of health, and the risk of developing serious health conditions. WHR is more efficient measure in older people (>75yrs) than BMI.")
	whr=round(float(waist)/hip,3)
	printer("Your waist to hip ratio is "+str(whr))
	if sex=="female":
		if whr<0.80: printer("According to your WHR,you are normal")
		elif whr>=0.80 and whr<=0.84: printer("According to your WHR,you are overweight")
		elif whr>=0.85: printer("According to your WHR,you are obese")
	else:
		if whr<0.90: printer("According to your WHR,you are normal")
		elif whr>=0.90 and whr<=0.99: printer("According to your WHR,you are overweight")
		elif whr>=1.00: printer("According to your WHR,you are obese")
	return whr
	
	
def waist_to_height_ratio(waist, height, sex):
	printer("\nWaist to height ratio is a much better measure of the risk of heart attack, stroke or death than the more widely used body mass index. It is highly correlated to abdominal obesity.")
	wht=round(float(waist)/height,3)
	printer("Your waist to height ratio is "+str(wht))
	if sex=="female":
		if wht<0.34: printer("You are extrememly slim. Marilyn Monroe's ratio is 0.336")
		elif wht>=0.35 and wht<0.42: printer("You are healthy slim. Beyonce's ratio is 0.3881 and Kate Moss's ratio is 0.3882")
		elif wht>=0.42 and wht<0.49: printer("You are healthy. You have a similar physic to a College Swimmer 0.4240 or Ashley Graham (plus sized model) 0.4354")
		elif wht>=0.49 and wht<0.54: printer("You are overweight. Female at increased risk has a typical WHR of 0.4920")
		elif wht>=0.54 and wht<0.58: printer("You are very overweight. Female at increased risk has a typical WHR of 0.4920")
		elif wht>=0.58: printer("You are very morbidly obese")
	else:
		if wht<0.34: printer("You are extrememly slim.")
		elif wht>=0.35 and wht<=0.42: printer("You are healthy slim.")
		elif wht>=0.43 and wht<=0.52: printer("You are healthy. You have a similar physic to a College Swimmer 0.428 or body builder 0.458")
		elif wht>=0.53 and wht<=0.57: printer("You are overweight. Male at increased risk has a typical WHR of 0.536")
		elif wht>=0.58 and wht<=0.62: printer("You are very overweight. Male at increased risk has a typical WHR of 0.536")
		elif wht>=0.63: printer("You are very morbidly obese")
	return wht

 
def pignet_index(chest,weight,height):			#Only for men
	printer("\nPignet Index or Body Build Index is an index used for evaluation of body build. It is a function of height, weight and chest sizes.")
	pig=round(((height*2.54)-(lbs_to_kgs(weight)+chest*2.54)),2)
	printer("Your pignet index is "+str(pig))
	if pig<10: printer("You are very sturdy!")
	if pig>=10 and pig<16: printer("You are sturdy")
	if pig>=16 and pig<21: printer("You have good pignet index")
	if pig>=21 and pig<26: printer("You have average pignet index")
	if pig>=26 and pig<30: printer("You have weak pignet index")
	if pig<31 and pig<36: printer("You have very weak pignet index")
	else: printer("You have poor pignet index")
	return pig