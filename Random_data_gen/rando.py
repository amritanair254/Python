#! /usr/bin/env python
import os,sys,getopt,string,sqlite3
limit=10

def main():
    col1=""
    col2=""
    col3=""
    col4=""
    (options, args) = getopt.getopt(sys.argv[1:], "c1:c2:c3:c4:", ["col1=","col2=","col3=","col4="])
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
        c.execute('INSERT INTO rando (id) VALUES(?)',str(i))
    if len(col1)>0:
        colz(col1,c)
    if len(col2)>0:
        colz(col2,c)
    i=raw_input("Do you want table to be printed to screen? y or n? >")
    if i!="n":
        printer(t)
    conn.close()


def colz(col,c):
    if col!="":
        obj=open(col+".txt")
        t=(col,)
        c.execute('ALTER TABLE rando ADD COLUMN ? text',str(col))
        id=1
        for line in obj:
            if id<=limit:
                temp=(col,line,id)
                c.execute('UPDATE rando SET ?=? WHERE id=?',temp)
                id=id+1


def printer(c):
    c.execute('''SELECT * FROM rando''')
    mytable = prettytable.from_db_cursor(cursor)
    print mytable


if __name__ == "__main__":
    main()
