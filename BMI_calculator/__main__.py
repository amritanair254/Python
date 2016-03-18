#! /usr/bin/env python
import Health_lib,re,os


def main():
	time=str(Health_lib.datetime.now())[:19]
	if os.path.isfile("bmi.txt") :
	    os.remove("bmi.txt")
	name = raw_input("Name > ")
	Health_lib.printer("\nBMI report of "+name+" on "+time)
	height = raw_input("Height in feet and inches or centimeters. Eg: '5ft 9in' or '182cm' > ")
	if re.match(".*cm.*",height):
		height = float(height.split('cm')[0])/2.54		#everything in inches
	else :
		if height.split('ft')[1]=='':
			height = float(height.split('ft')[0])*12
		else:	height = float(height.split('ft')[0])*12+int(height.split('ft ')[1].split('in')[0])
	weight = raw_input("Weight in pounds or kilograms. Eg: '135lbs' or '57kg' > ")
	if re.match("lbs",weight):
		weight = float(weight.split('lbs')[0])
	else:
		weight = float(weight.split('kg')[0])*2.204		#everything in pounds
	sex=raw_input("Gender > ")
	if sex=="male" or sex=="Male" or sex=="M" or sex=="m":
		sex="male"	
	else:
		sex="female"
	age=int(raw_input("Age > "))
	Health_lib.printer("Height:"+str(int(height/12))+"ft "+str(int(height%12))+"in | Weight:"+str(weight)+"lbs")
	
	
	bmi=Health_lib.bmi_func(weight,height)
	bmr=Health_lib.basal_metabolic_rate(sex,age,weight,height)
	cal=Health_lib.calorie_needs(sex,bmr)
	
	result=raw_input("\nDo you want to find out your body fat percentage/ratios/indices? 'y' or 'n' > ")
	if result!="n":
		wrist=raw_input("Wrist measurement at the thickest point in inches or centimeters > ")
		if re.match(".*cm.*",wrist):
			wrist = float(wrist.split('cm')[0])/2.54
		else:	wrist = float(wrist.split('in')[0])
		waist=raw_input("Waist measurement at the naval in inches or centimeters > ")
		if re.match(".*cm.*",waist):
			waist = float(waist.split('cm')[0])/2.54
		else:	waist = float(waist.split('in')[0])
		chest=raw_input("Chest measurement in inches > ")
		if re.match(".*cm.*",chest):
			chest = float(chest.split('cm')[0])/2.54
		else:	chest = float(chest.split('in')[0])
		hip=raw_input("Hip measurement at the fullest point in inches or centimeters > ")
		if re.match(".*cm.*",hip):
			hip = float(hip.split('cm')[0])/2.54
		else:	hip = float(hip.split('in')[0])
		forearm=raw_input("Forearm measurement at the thickest point in inches or centimeters > ")
		if re.match(".*cm.*",forearm):
			forearm = float(forearm.split('cm')[0])/2.54
		else:	forearm = float(forearm.split('in')[0])
		Health_lib.printer("Chest:"+str(chest)+"in| Waist:"+str(waist)+"in| Hip:"+str(hip)+"in| Forearm:"+str(forearm)+"in| Wrist:"+str(wrist)+"in\n")
		lbm,bf=Health_lib.body_fat(weight,sex,wrist,waist,hip,forearm)
		bai=Health_lib.body_adipose_index(height,hip,age,sex)
		wht=Health_lib.waist_to_height_ratio(waist, height, sex)
		whr=Health_lib.waist_to_hip_ratio(waist, hip, sex)
		if sex=="male":
			pig=Health_lib.pignet_index(chest,weight,height)
		else :  pig=''
	else:
		wrist=''
		waist=''
		chest=''
		hip=''
		forearm=''
		lbm=''
		bf=''
		bai=''
		wht=''
		whr=''
		pig=''
	
	rxr=raw_input("\nEnter email if you want to us to maintain your record and send you your report via email > ")
	if rxr!='':
		Health_lib.maintain_record(name,time,age,sex,height,weight,bmi,bmr,cal,wrist,forearm,chest,waist,hip,lbm,bf,bai,wht,whr,pig,rxr)
		history=raw_input("Do you want to check your history of measurements? (Doesn't apply to new users) > ")
		if history!="n" :
			Health_lib.past_records(rxr)
		Health_lib.send_mail(rxr)

if __name__=='__main__':
	main()
