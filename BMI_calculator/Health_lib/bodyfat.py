import math
from utilz import lbs_to_kgs
from utilz import printer
			
def body_fat(weight,sex,wrist,waist,hip,forearm):		#Calculate body fat percentage
	if sex=="female":
		lbm= round(((weight*0.732) + 8.987 + (wrist/3.140) - (waist*0.157) - (hip*0.249) + (forearm*0.434)),2)
		bf=round((weight-lbm)*100/weight,2)
		printer("\nYour Lean Body Mass is "+str(lbm)+"lbs or "+str(lbs_to_kgs(lbm))+"kgs. If you want to gain muscle, you need to take "+str(int(lbm))+"-"+str(int(lbm+5))+"grams of protein daily")
		printer("Your Body Fat Weight is "+str(weight-lbm)+"lbs or "+str(lbs_to_kgs(weight-lbm))+"kgs and your Body Fat Percentage is "+str(bf)+"%")
		if bf<12: printer("Your body fat is less than 12%, this is essential fat. Please don't try to lose more weight")
		elif bf>=12 and bf<20: printer("You have an sexy, athletic body!")
		elif bf>=20 and bf<24: printer("You have a fit body. An athletic body has 20% body fat. Minimum threshold value of body fat is 14%. You can diet and exercise to lose "+str(bf-20)+"% body fat, which is "+str(round(((bf-20)*weight/100),2))+"lbs or "+str(lbs_to_kgs((bf-20)*weight/100))+"kgs.\nKeep realistic weight-loss goals!")
		elif bf>=24 and bf<32: printer("You have an acceptable body. An athletic body has 20% body fat You can diet and exercise to lose "+str(bf-20)+"% body fat, which is "+str(round(((bf-20)*weight/100),2))+"lbs or "+str(lbs_to_kgs((bf-20)*weight/100))+"kgs.\nKeep realistic weight-loss goals!")
		else: printer("You have a obese body. An athletic body has 20% body fat. You must diet and exercise to lose "+str(bf-20)+"% body fat, which is "+str(round(((bf-20)*weight/100),2))+"lbs or "+str(lbs_to_kgs((bf-20)*weight/100))+"kgs.\nKeep realistic weight-loss goals!")
				
	else:
		lbm= round(((weight*1.082) + 94.42 - (waist*4.15)),2)
		bf=round(((weight-lbm)*100/weight),2)
		printer("Your Lean Body Mass is "+str(lbm)+"lbs or "+str(lbs_to_kgs(lbm))+"kgs. If you want to gain muscle, you need to take "+str(int(lbm))+"-"+str(int(lbm+5))+"grams of protein daily")
		printer("Body Fat Weight is "+str(weight-lbm)+"lbs or "+str(lbs_to_kgs(weight-lbm))+"kgs and your Body Fat Percentage is "+str(bf)+"%")
		if bf<4: printer("Your body fat is less than 4%, this is essential fat. Please don't try to lose morre weight")
		elif bf>=4 and bf<13: printer("You have an sexy, athletic body!")
		elif bf>=13 and bf<17: printer("You have a fit body. An athletic body has 13% body fat. Minimum threshold value of body fat is 5%. You can diet and exercise to lose "+str(bf-13)+"% body fat, which is "+str(round(((bf-13)*weight/100),2))+"lbs or "+str(lbs_to_kgs((bf-13)*weight/100))+"kgs.\nKeep realistic weight-loss goals!")
		elif bf>=17 and bf<25: printer("You have an acceptable body. An athletic body has 13% body fat You can diet and exercise to lose "+str(bf-13)+"% body fat, which is "+str(round(((bf-13)*weight/100),2))+"lbs or "+str(lbs_to_kgs((bf-13)*weight/100))+"kgs.\nKeep realistic weight-loss goals!")
		else: printer("You have a obese body. An athletic body has 133% body fat. You must diet and exercise to lose "+str(bf-13)+"% body fat, which is "+str(round(((bf-13)*weight/100),2))+"lbs or "+str(lbs_to_kgs((bf-13)*weight/100))+"kgs.\nKeep realistic weight-loss goals!")
	return lbm,bf


def body_adipose_index(height,hip,age,sex):		#Calculate body fat index
	printer("\nThe Body Adiposity Index (BAI) is the amount of body fat in humans. The BAI is calculated using size of the hips and height.")
	bai=round((((100*hip)/(height*math.sqrt(height*0.0254)))-18.0),2)
	printer("Your Body Adipose Index is "+str(bai))
	if sex=="female":
		if age>20 and age<=40:
			if bai<=21: printer("According to your BAI,you are underweight")
			elif bai>21 and bai<=33: printer("According to your BAI,you are normal")
			elif bai>33 and bai<=39: printer("According to your BAI,you are overweight")
			else: printer("According to your BAI,you are obese")
		elif age>40 and age<=59:
			if bai<=23: printer("According to your BAI,you are underweight")
			elif bai>23 and bai<=35: printer("According to your BAI,you are normal")
			elif bai>35 and bai<=41: printer("According to your BAI,you are overweight")
			else: printer("According to your BAI,you are obese")
		elif age>60 and age<=79:
			if bai<=25: printer("According to your BAI,you are underweight")
			elif bai>25 and bai<=38: printer("According to your BAI,you are normal")
			elif bai>38 and bai<=43: printer("According to your BAI,you are overweight")
			else: printer("According to your BAI,you are obese")
	else:
		if age>20 and age<=39:
			if bai<=8: printer("According to your BAI,you are underweight")
			elif bai>8 and bai<=21: printer("According to your BAI,you are normal")
			elif bai>21 and bai<=26: printer("According to your BAI,you are overweight")
			else: printer("According to your BAI,you are obese")
		elif age>40 and age<=59:
			if bai<=11: printer("According to your BAI,you are underweight")
			elif bai>11 and bai<=23: printer("According to your BAI,you are normal")
			elif bai>23 and bai<=29: printer("According to your BAI,you are overweight")
			else: printer("According to your BAI,you are obese")
		elif age>60 and age<=79:
			if bai<=13: printer("According to your BAI,you are underweight")
			elif bai>13 and bai<=25: printer("According to your BAI,you are normal")
			elif bai>25 and bai<=31: printer("According to your BAI,you are overweight")
			else: printer("According to your BAI,you are obese")
	return bai
