#! /usr/bin/env python
"""Automated Ordering and Billing System:
This program allows user to select menu items, prints out the total amount on screen, 
saves the bill to be physically printed out, sends the order to the kitchen via mail, 
maintains a record of all orders placed for official purpose"""
from datetime import datetime
import smtplib,random

ticket=100    # current count of ticket. Can be set as a counter externally

#Restaurant Menu
starters = {
	1: ['Chicken Soup               ', 2.00], 
	2: ['Mushroom Soup              ', 2.50], 
	3: ['Caesar Salad               ', 2.90],
	4: ['Chicken Salad              ', 3.30]}
	
main_courses = {
	1: ['Fish and Chips             ', 6.50],
	2: ['Chicken & Potatoes         ', 6.25],
	3: ['Farmhouse Pizza            ', 4.85],
	4: ['Thai Fried Rice            ', 5.95],
	5: ['Penne Pasta                ', 5.95]}
	
beverages = {
	1: ['Mineral water              ', 1.00],
	2: ['Fresh orange juice         ', 1.25],
	3: ['Coke/Pepsi/Fanta           ', 1.30],
	4: ['Irish cream coffee         ', 0.90]}
	
snacks ={
	1: ['Cheese Omlette             ', 3.25],
	2: ['Bytesize Hotdogs           ', 2.25],
	3: ['Chicken Sandwich           ', 3.50],
	4: ['Club Sandwich              ', 3.25]}
	
desserts = {
	1: ['Vanilla Icecream           ', 2.00],
	2: ['Chocolate Cake             ', 2.25],
	3: ['Creamy Fruit Salad         ', 2.25],
	4: ['Cheese and Crackers        ', 2.50]}
	


	
#print the total price on screen
def print_total_on_screen(meal,stuff_ordered,customers,table,ticket):
	now = datetime.now()
	print '{:*^50}'.format("Your Total Bill Amount")
	print '\nDine In\t\tParty of '+str(customers)
	print 'Table:'+str(table)+'\t\tTicket:'+str(ticket)
	print '\nServer: Amy-Bot'
	print '%s/%s/%s\t%s:%s:%s' % (now.month, now.day, now.year,now.hour, now.minute, now.second)
	print '{:-^50}'.format("-")
	for each_order in stuff_ordered:
		print str(stuff_ordered[each_order][0]) + '\t'+ each_order +  '$'+str(stuff_ordered[each_order][1])
	print '{:-^50}'.format("-")
	tax = 0.0149 #1.49% tax
	print '%22s : $%.2f' % ('Sub Total',meal)
	print '%30s' % ('Sales Tax : 1.49%')
	meal += meal * tax
	print '%22s : $%.2f' % ('Check Total',meal)
	
	
#write to file bill.txt which can be physically printed out
def print_bill(meal,stuff_ordered,customers,table,ticket):
	now = datetime.now()
	f = open("bill.txt", 'w')
	f.truncate()
	f.write('{:*^40}'.format("THE LULU's"))
	f.write('\n{:^40}'.format("1004 Manhattan, New York"))
	f.write('\n{:^40}'.format("1800-Call-Amy"))
	f.write('\nDine In\t\tParty of '+str(customers))
	f.write('\nTable:'+str(table)+'\t\tTicket:'+str(ticket))
	f.write('\nServer: Amy-Bot')
	f.write('\n%s/%s/%s\t%s:%s:%s' % (now.month, now.day, now.year,now.hour, now.minute, now.second))
	f.write('\n{:-^40}'.format("-"))
	for each_order in stuff_ordered:
		f.write('\n'+str(stuff_ordered[each_order][0]) + '\t'+ each_order + '$'+ str(stuff_ordered[each_order][1]))
	f.write('\n{:-^40}'.format("-"))
	tax = 0.0149 #1.49% tax
	f.write('\n%32s : $%.2f' % ('Sub Total',meal))
	f.write('\n%40s' % ('Sales Tax : 1.49%'))
	meal += meal * tax
	f.write('\n%32s : $%.2f' % ('Check Total',meal))


#for customer to enter order
def order():
	stuff_ordered={}
	meal=0
	print "Please enter the order number and number of items in new lines separated by '='\nPress enter to go to the next menu option"
	print '{:*^50}'.format("StarterS")
	meal1,stuff_ordered=order2(starters,stuff_ordered)
	print '{:*^50}'.format("Main Course")
	meal2,stuff_ordered=order2(main_courses,stuff_ordered)
	print '{:*^50}'.format("Beverages")
	meal3,stuff_ordered=order2(beverages,stuff_ordered)
	print '{:*^50}'.format("SnackS")
	meal4,stuff_ordered=order2(snacks,stuff_ordered)
	print '{:*^50}'.format("Desserts~")
	meal5,stuff_ordered=order2(desserts,stuff_ordered)
	meal=meal1+meal2+meal3+meal4+meal5
	return meal,stuff_ordered

def order2(entree,stuff_ordered):
	meal=0	
	for key in entree:
		print str(key) + ". "+entree[key][0]+"\t:\t$"+str(entree[key][1])
	while True :
		i=raw_input('> ').split('=') 
		if i[0]=='' :
			break
		temp0,temp1=int(i[0]),int(i[1])
		#meal=entree[order]*number
		meal+=entree[temp0][1]*temp1
		stuff_ordered[entree[temp0][0]]=[temp1,entree[temp0][1]*temp1]
	return meal,stuff_ordered	
		

	
#order placed will be sent to kitchen via mail
def send_order_to_kitchen(meal,stuff_ordered,customers,table,ticket):
	email_body=''
	for each_order in stuff_ordered:
		email_body=str(stuff_ordered[each_order][0]) + "\t"+ each_order +  str(stuff_ordered[each_order][1])+"\n"
	sender="lulu@lulu.com"
	receivers="lulukitchen-ticket@gmail.com"		#had set my mail address for testing purpose
	message="""Subject: New Order
Order #"""+str(ticket)+""" |For Table """+str(table)+""" |Party of """+str(customers)+"""\n"""+email_body+"""~"""
	try:
		smtpOb = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, receivers, message)
	except smtplib.SMTPException:
		print "Error: unable to send kitchen the request. Try ordering again"
	
	
#all records maintained in separate file
def maintain_record(meal,stuff_ordered,customers,table,ticket):
	now = datetime.now()
	rec = open("record.txt", 'a')
	rec.write('\n\nTicket:'+str(ticket)+'\t\tTable:'+str(table)+'\t\tParty of '+str(customers))
	rec.write('\n%s/%s/%s\t\t%s:%s:%s' % (now.month, now.day, now.year,now.hour, now.minute, now.second))
	rec.write('\n{:-^50}'.format("-"))
	for each_order in stuff_ordered:
		rec.write('\n'+str(stuff_ordered[each_order][0]) + '\t'+ each_order +  '$'+str(stuff_ordered[each_order][1]))
	rec.write('\n{:-^50}'.format("-"))
	tax = 0.0149 #1.49% tax
	rec.write('\n%22s : $%.2f' % ('Sub Total',meal))
	rec.write('\n%30s' % ('Sales Tax : 1.49%'))
	meal += meal * tax
	rec.write('\n%22s : $%.2f' % ('Check Total',meal))
	rec.write('\n{:=^50}'.format("="))


#main program(function calls) starts here
print '{:*^50}'.format("Welcome to LULU's")	
customers = raw_input('Number of seats to reserve > ')
table = random.randrange(12)			#12 tables at Lulu's
print 'Reserving table number '+ str(table) + '\nPlease have a seat after ordering :)\n'
meal, stuff_ordered = order()		#saved as tuple
print_total_on_screen(meal,stuff_ordered,customers,table,ticket)
print_bill(meal,stuff_ordered,customers,table,ticket)
send_order_to_kitchen(meal,stuff_ordered,customers,table,ticket)
maintain_record(meal,stuff_ordered,customers,table,ticket)
