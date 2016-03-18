#! /usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import re,math,os,smtplib,sqlite3
from prettytable import PrettyTable

time=str(datetime.now())[:19]

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

def basal_metabolic_rate(sex,age,weight,height):		#to find out calorie needs
	if sex=="female":
		bmr = round((655.0+(4.35*weight)+(4.7*height)-(4.7*age)),2)
	else:
		bmr = round((66.0+( 6.23*weight)+( 12.7*height)-(6.8*age)),2)
	printer("\nYour Basal Metabolic Rate is "+str(bmr)+" cal per day")
	return bmr

def calorie_needs(bmr):									#Harris Benedict Formula
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

def lbs_to_kgs(weight):				#For conversion from pounds to kilos used in above functions
	return round((weight*0.454),2)

def printer(string):				#Used to write to a file and to print out to screen
	prt = open("bmi.txt", 'a')
	prt.write(string+"\n")
	print string

def sendmail(rxr):					#File written in printer() is copied as email body and sent to user
	prt = open("bmi.txt")
	email_body = prt.read()
	sender="bmi@gmail.com"
	receivers=rxr
	message="""Subject: Your BMI report
Dear user,\n"""+email_body
	try:
		smtpOb = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, receivers, message)
	except smtplib.SMTPException:
		print "Error: unable to send email to user. Try ordering again"


def maintain_record(name,age,sex,height,weight,bmi,bmr,cal,wrist,forearm,chest,waist,hip,lbm,bf,bai,wht,whr,pig,rxr):				#Maintains an informal record. The next function is more useful
    if os.path.isfile("bmi_db.db"):
        conn = sqlite3.connect('bmi_db.db')
        c=conn.cursor()
    else:
        conn = sqlite3.connect('bmi_db.db')
        c=conn.cursor()
        c.execute('''CREATE TABLE bmi(Name text,Date text,Age int,Gender text,Height real,Weight real,BMI real,Basal_Metabolic_Rate real,Calorie_Restriction real,Wrist real,Forearm real,Chest real,Waist real,Hip real,Lean_Body_Mass real,Body_Fat_Percentage real,Body_Adiposity_Index real,Waist_to_Height_ratio real,Waist_to_Hip_ratio real,Pignet_Index real,Email text)''')
    tempor=(name,time,age,sex,height,weight,bmi,bmr,cal,wrist,forearm,chest,waist,hip,lbm,bf,bai,wht,whr,pig,rxr)
    c.execute('INSERT INTO bmi VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',tempor)
    conn.commit()
    conn.close()


def maintain_record2(name,age,sex,height,weight,bmi,bmr,cal,wrist,forearm,chest,waist,hip,lbm,bf,bai,wht,whr,pig,rxr):		#Maintains db of everybody's measurements
	if os.path.isfile("bmi_db.cvs"):
		rec = open("bmi_db.cvs",'a')
	else:
		rec = open("bmi_db.cvs",'a')
		rec.write("Name,Date/Time,Age,Gender,Height,Weight,BMI,Basal Metabolic Rate,Calorie Restriction,Wrist,Forearm,Chest,Waist,Hip,Lean Body Mass,Body Fat Percentage,Body Adiposity Index,Waist to Height ratio,Waist to Hip ratio,Pignet Index,Email Adress\n")

	rec.write(str(name)+","+time+","+str(age)+","+str(sex)+","+str(int(height/12))+"ft "+str(int(height%2))+"in,"+str(weight)+"lbs,"+str(bmi)+","+str(bmr)+"cal/day,"+str(cal)+"cal,"+str(wrist)+"in,"+str(forearm)+"in,"+str(chest)+"in,"+str(waist)+"in,"+str(hip)+"in,"+str(lbm)+"lbs,"+str(bf)+"%,"+str(bai)+","+str(wht)+","+str(whr)+","+str(pig)+","+str(rxr)+"\n")
	rec.close()


def past_records(rxr,name):
    conn = sqlite3.connect('bmi_db.db')
    cursor = conn.execute("SELECT * from bmi")
    t = PrettyTable(['Date','Height in.','Weight lb.','Wrist in.','Forearm in.','Chest in.','Waist in.','Hip in.','BMI'])
    for row in cursor:
        if row[0] == name:
            t.add_row([row[1],row[4],row[5],row[9],row[10],row[11],row[12],row[13],row[6]])
    print t
    print "\n"
    cursor = conn.execute("SELECT * from bmi")
    y = PrettyTable(['Date','Metabolic Rate','Lean Mass lb.','Body Fat %','Body Fat Ind.','Waist/Height','Waist/Hip','Pignet Ind.'])
    for row in cursor:
        if row[0] == name:
            y.add_row([row[1],row[7],row[14],row[15],row[16],row[17],row[18],row[19]])
    print y
    conn.close()

def past_records2(rxr):			#if user wants to print out his past records from db
	print next(open('bmi_db.cvs'))
	rec = open("bmi_db.cvs")
	patt="(.*)"+rxr+"(.*)"
	for line in rec:
		if re.match(patt, line):
			print line
	rec.close()

#below functions are called by bmi()
def severe_underweight():
	printer("You are severely underweight\nYou should consult your physician to determine if you should gain weight.")
	result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1 !="n":
		printer("* Inhibited growth and development, especially for children and teens.\n* Fragile bones, deficiency in vitamin D and calcium along with low body weight can lead to osteoporosis.\n* Weakened immune system, your body cannot store energy and may also have difficulty fighting and bouncing back from illness.\n* Anemia caused by iron, folate and vitamin B12 deficiency, resulting in dizziness, fatigue and headaches.\n* Fertility issues. In women, low body weight can lead to irregular or lack of periods and infertility.\n* Hair loss, dry thin skin and teeth health issues.")
		result2=raw_input("\nDo you want to find out what the causes are? > ")
	if result2 !="n":
		printer("* Genetics - runs in your family, it's likely that you were born with a higher-than-usual metabolism.\n* High physical activity burns more calories.\n* Illness can affect your appetite, as well as your body's ability to use and store food. \n* Certain prescription medicines and treatments can cause nausea and weight loss.\n* Psychological Issues like stress, depression, anorexia, etc can disrupt healthy eating habits.")
		result3=raw_input("\nDo you want to find out about treatment? > ")
	if result3!="n":
		printer("* Add healthy calories without radically changing your diet eg: nut or seed toppings, cheese, healthy side dishes, fruit or whole-grain wheat toast.\n* Go nutrient dense. High-protein meats, which can help you to build muscle and nutritious carbohydrates, such as brown rice and other whole grains. \n* Snack away on protein and healthy carbohydrates.eg: trail mix, protein bars or drinks, and crackers with hummus or peanut butter. \n* If you have poor appetite, eat mini-meals throughout the day to increase your calorie intake.\n* Bulk up - strength training, such as weight-lifting or yoga, can help you gain weight by building muscle. ")

def underweight():
	printer("You are underweight.")
	result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1 !="n":
		printer("* If you happen to lose more weight due to illness, stress or habits like smoking and poor diet, you may get:\n* Anemia, viz caused by iron, folate and vitamin B12 deficiency, resulting in dizziness, fatigue and headaches.\n* Fertility issues. In women, low body weight can lead to irregular or lack of periods and infertility.\n* Hair loss, dry thin skin and teeth health issues.")
	result2=raw_input("\nDo you want to find out what the causes are? > ")
	if result2 !="n":
		printer("* Genetics - runs in your family, it's likely that you were born with a higher-than-usual metabolism.\n* High physical activity burns more calories.")
	result3=raw_input("\nDo you want to find out how to gain weight? > ")
	if result3!="n":
		printer("* Continue your regular balanced diet or switch over to one if you don't eat regularly.\n* Bulk up - strength training, such as weight-lifting or yoga, can help you gain muscle.")

def normal():
		printer("You are normal weight :)")


def overweight():
	printer("You are overweight")
	result=raw_input("\nDo you want some tips to reduce weight? > ")
	if result!="n":
		printer("* So what if you have some fudge in the pudge. You're just working out and eating clean to become the best version of you(not that you already aren't)\n* First step is to slowly taper the sugar and processed food intake and improve your stamina by taking long walks.\n* Choose healthy meal options, like dark chocolate instead of candy, sugar-free options containing stevia and fruit if you have a sweet-tooth.\n* After you build your stamina, take up fun workout routines like dancing, swimming, beginner's zumba, etc.\n* If aerobics is not your thing, try weight lifting, even if you are a chick. It burns fat and builds muscle. And don't worry, you can always slow down if you find yourself bulking up to much.")
		result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1!="n":
		printer("* If your BMI is above 32.5, you may experience a general fatigue and lack of stamina. Being a little overweight is not unhealthy!")



def moderately_obese():
	printer("You are moderately obese")
	result=raw_input("\nDo you want some tips to reduce weight? > ")
	if result!="n":
		printer("* Great! First step is to slowly taper the sugar and processed food intake and improve your stamina by taking long walks.\n* Choose healthy meal options, like dark chocolate instead of candy, sugar-free options containing stevia and fruit if you have a sweet-tooth.\n* Keep a food journal if you are serious about losing weight. Note down everything you ate that day.\n* Have your friends/parents support you in this ourney and ask them to switch to healthier options too!\n* After you build your stamina, take up fun workout routines like dancing, swimming, beginner's zumba, etc.\n*  If aerobics is not your thing, try weight lifting, even if you are a chick. It burns fat and builds muscle. And don't worry, you can always slow down if you find yourself bulking up to much.\n* Stay positive. So what if you have some fudge in the pudge. You can lose it in no time! Stay motivated.\n* Drink a lot of water.\n* If you don't think you can survive without meat, switch to ketogenic diet. If you think you can't survive without carbs, switch to a balanced low calorie diet.")
	result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1 !="n":
		printer("* You would experience a general fatigue and lack of stamina.\n* It makes you more likely to have conditions including heart disease and stroke, high blood pressure, Diabetes, some cancers, Gallbladder disease and gallstones, Osteoarthritis, Gout, breathing problems, such as sleep apnea (when a person stops breathing for short episodes during sleep) and asthma.\n* You should consult your physician to determine if you are suffering any of these conditions.")
	result2=raw_input("\nDo you want to find out what causes this? > ")
	if result2 !="n":
		printer("* Behavioral factors like your eating habits and daily activity level. Many people develop their eating habits as children and have trouble refining them to maintain proper body weight as they age. As an adult, you may be inactive at your job and have less time for exercise, meal planning, and physical activity.\n* Stress, anxiety, and lack of sleep, can lead to weight gain. People who quit smoking often experience temporary weight gain. Women may also have trouble losing the weight they gain during pregnancy or gain additional weight during menopause.\n* Certain medications eg:birth control pills and antidepressants, can cause weight gain.\n* Genetic factors may control how your body stores energy.")


def extremely_obese():
	printer("You are extremely obese")
	result=raw_input("\nDo you want some tips to reduce weight? > ")
	if result!="n":
		printer("* Great! First step is to slowly taper the sugar and processed food intake and improve your stamina by taking long walks.\n* Choose healthy meal options, like dark chocolate instead of candy, sugar-free options containing stevia and fruit if you have a sweet-tooth.\n* Keep a food journal if you are serious about losing weight. Note down everything you ate that day.\n* Have your friends/parents support you in this ourney and ask them to switch to healthier options too!\n* After you build your stamina, take up fun workout routines like dancing, swimming, beginner's zumba, etc.\n* Stay positive. Keep yourself motivated and make realistic goals.\n* If you are battling depression, join a support group, get involved in community activities or go for meditation classes.\n* Drink a lot of water or chicken/tomato soup.\n* Find a job that does not involve food, ideally something you like doing. No matter what it is, if you are not just sitting at home and watching TV, you are less likely to eat.")
	result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1 !="n":
		printer("* You would experience a general fatigue and lack of stamina.\n* It makes you more likely to have conditions including heart disease and stroke, high blood pressure, Diabetes, some cancers, Gallbladder disease and gallstones, Osteoarthritis, Gout, breathing problems, such as sleep apnea (when a person stops breathing for short episodes during sleep) and asthma.\n* You should consult your physician to determine if you are suffering any of these conditions.")
	result2=raw_input("\nDo you want to find out what causes this? > ")
	if result2 !="n":
		printer("* Behavioral factors like your eating habits and daily activity level. Many people develop their eating habits as children and have trouble refining them to maintain proper body weight as they age. As an adult, you may be inactive at your job and have less time for exercise, meal planning, and physical activity.\n* Stress, anxiety, and lack of sleep, can lead to weight gain. People who quit smoking often experience temporary weight gain. Women may also have trouble losing the weight they gain during pregnancy or gain additional weight during menopause.\n* Certain medications eg:birth control pills and antidepressants, can cause weight gain.\n* Genetic factors may control how your body stores energy.")


def morbidly_obese():
	printer("You are morbidly obese")
	result=raw_input("\nDo you want some tips to reduce weight? > ")
	if result!="n":
		print"When you have a lot of weight to lose, it means playing the long game. You have to chart out a game-plan to cut calories, fight the hunger pangs, make exercise easier, stay on track, and more.\n* Slowly taper the sugar and processed food intake and improve your stamina by taking long walks.\n* If walks hurt your knees, try physical therapy. They'll design a program tailored for you to improve your balance and range of motion.\n* Choose healthy meal options, like dark chocolate instead of candy, sugar-free options containing stevia and fruit if you have a sweet-tooth.People who eat more in the morning and less at night tend to lose more weight. High-protein, warm, solid meal(350-400 calories with at least 25 grams of protein) helps you feel fuller and less hungry later.\n* Keep a photo food ounal on your phone, that you can erase every two weeks. They'll remind you of what you've eaten.\n* If you are battling depression, join a support group, get involved in community activities or go for meditation classes.\n* Drink a lot of water or chicken/tomato soup.\n* Find a job that does not involve food, ideally something you like doing. No matter what it is, if you are not just sitting at home and watching TV, you are less likely to eat.\n* Set Up Your Food Storage. After you purge your home of those treats you can't resist, assign shelves in the pantry and the fridge so your healthy food becomes easy to see and reach.\n* Get checked for sleep apnea. This condition can disrupt your slumber and you won't know it. Studies show that a lack of sleep alters hormones that control hunger.\n* Weight loss surgery should be your last option if you don't see any changes in 5-6 months time."
	result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1 !="n":
		printer("* You would experience a general fatigue and lack of stamina.\n* It makes you more likely to have conditions including heart disease and stroke, high blood pressure, Diabetes, some cancers, Gallbladder disease and gallstones, Osteoarthritis, Gout, breathing problems, such as sleep apnea (when a person stops breathing for short episodes during sleep) and asthma.\n* You should consult your physician to determine if you are suffering any of these conditions.")
	result2=raw_input("\nDo you want to find out what causes this? > ")
	if result2 !="n":
		printer("* Behavioral factors like your eating habits and daily activity level. Many people develop their eating habits as children and have trouble refining them to maintain proper body weight as they age. As an adult, you may be inactive at your job and have less time for exercise, meal planning, and physical activity.\n* Stress, anxiety, and lack of sleep, can lead to weight gain. People who quit smoking often experience temporary weight gain. Women may also have trouble losing the weight they gain during pregnancy or gain additional weight during menopause.\n* Certain medications eg:birth control pills and antidepressants, can cause weight gain.\n* Genetic factors may control how your body stores energy.")


#This is where program starts
if os.path.isfile("bmi.txt") :
    os.remove("bmi.txt")
name = raw_input("Name > ")
printer("\nBMI report of "+name+" on "+time)
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
printer("Height:"+str(int(height/12))+"ft "+str(int(height%12))+"in | Weight:"+str(weight)+"lbs")


bmi=bmi_func(weight,height)
bmr=basal_metabolic_rate(sex,age,weight,height)
cal=calorie_needs(bmr)

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
	printer("Chest:"+str(chest)+"in| Waist:"+str(waist)+"in| Hip:"+str(hip)+"in| Forearm:"+str(forearm)+"in| Wrist:"+str(wrist)+"in\n")
	lbm,bf=body_fat(weight,sex,wrist,waist,hip,forearm)
	bai=body_adipose_index(height,hip,age,sex)
	wht=waist_to_height_ratio(waist, height, sex)
	whr=waist_to_hip_ratio(waist, hip, sex)
	if sex=="male":
		pig=pignet_index(chest,weight,height)
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
	maintain_record(name,age,sex,height,weight,bmi,bmr,cal,wrist,forearm,chest,waist,hip,lbm,bf,bai,wht,whr,pig,rxr)
	#maintain_record2(name,age,sex,height,weight,bmi,bmr,cal,wrist,forearm,chest,waist,hip,lbm,bf,bai,wht,whr,pig,rxr)
	history=raw_input("Do you want to check your history of measurements? (Doesn't apply to new users) > ")
	if history!="n" :
		past_records(rxr,name)
	#sendmail(rxr)

