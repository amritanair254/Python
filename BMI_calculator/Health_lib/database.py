from utilz import lbs_to_kgs
from utilz import printer
import sqlite3
import re,math,os
from prettytable import PrettyTable


def maintain_record(name,time,age,sex,height,weight,bmi,bmr,cal,wrist,forearm,chest,waist,hip,lbm,bf,bai,wht,whr,pig,rxr):				#Maintains an informal record. The next function is more useful
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


def past_records(rxr):
	conn = sqlite3.connect('bmi_db.db')
	cursor = conn.execute("SELECT * from bmi")
	t = PrettyTable(['Date','Height in.','Weight lb.','Wrist in.','Forearm in.','Chest in.','Waist in.','Hip in.','BMI'])
	y = PrettyTable(['Date','Metabolic Rate','Lean Mass lb.','Body Fat %','Body Fat Ind.','Waist/Height','Waist/Hip','Pignet Ind.'])
	for row in cursor:
		if row[20] == rxr:
			t.add_row([row[1],row[4],row[5],row[9],row[10],row[11],row[12],row[13],row[6]])
			y.add_row([row[1],row[7],row[14],row[15],row[16],row[17],row[18],row[19]])
	print t
	print "\n"
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