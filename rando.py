import os
import sys
import getopt
import string
import sqlite3
limit=10

def main():
    col1=""
    col2=""
    col3=""
    col4=""
    (options, args) = getopt.getopt(sys.argv[1:], "d1:c1:d2:c2:", ["col1=","col2=","col3=","col4="])
    for (name, value) in options:
        if name in ("--col1","-c1"):
            col1=value
        if name in ("--col2","-c2"):
            col2=value
        if name in ("--col3","-c3"):
            col3=value
        if name in ("--col4","-c4"):
            col4=value
    if col1=="" :
        print "please enter columns"
        sys.exit(0)
    conn = sqlite3.connect('output.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE rando(id TEXT)''')
    for i in range(1,limit):
        c.extecute('INSERT INTO rando (id) VALUES(?)',i)
    if len(col1)>0:
        colz(col1,c)
    if len(col2)>0:
        colz(col2)
    i=raw_input("Do you want table to be printed to screen? y or n? >")
    if i=="y":
        t = conn.execute("SELECT * from bmi")
        printer(t)


def colz(col,c):
    if col=="name":
        obj=open("names.txt")
        c.execute('''ALTER TABLE rando ADD COLUMN Name TEXT''')
        id=1
        for line in obj:
            if id<=limit:
                temp=(line,id)
                c.execute('UPDATE rando SET Name=? WHERE id=?',temp)
                id=id+1

    elif col=="email":
        obj=open("email.txt")
        c.execute('''ALTER TABLE rando ADD COLUMN Email TEXT''')
        id=1
        for line in obj:
            if id<=limit:
                temp=(line,id)
                c.execute('UPDATE rando SET Email=? WHERE id=?',temp)
                id=id+1


def printer(c):
        t = PrettyTable(['Date','Height in.','Weight lb.','Wrist in.','Forearm in.','Chest in.','Waist in.','Hip in.','BMI'])
        y = PrettyTable(['Date','Metabolic Rate','Lean Mass lb.','Body Fat %','Body Fat Ind.','Waist/Height','Waist/Hip','Pignet Ind.'])
        for row in c:
            if row[20] == rxr:
                t.add_row([row[1],row[4],row[5],row[9],row[10],row[11],row[12],row[13],row[6]])
                y.add_row([row[1],row[7],row[14],row[15],row[16],row[17],row[18],row[19]])
        print t
        print "\n"
        print y
        conn.close()


if __name__ == "__main__":
    main()
