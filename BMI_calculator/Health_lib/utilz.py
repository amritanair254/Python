import math,os,smtplib

def lbs_to_kgs(weight):				#For conversion from pounds to kilos used in above functions
	return round((weight*0.454),2)

def printer(string):				#Used to write to a file and to print out to screen
	prt = open("bmi.txt", 'a')
	prt.write(string+"\n")
	print string

def send_mail(rxr):					#File written in printer() is copied as email body and sent to user
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