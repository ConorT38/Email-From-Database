#!/usr/bin/python
import MySQLdb
import smtplib

db = MySQLdb.connect(host="localhost",    # your host
                     user="root",         # your username
                     passwd="password",  # your password
                     db="database")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Select the email of each user
cur.execute("SELECT email FROM users")

# print all the first cell of all the rows
for row in cur.fetchall():
    sender = 'your@email.com'
    receiver =[row[0]]

    message = """From: From Person <your@email.com>
				 To: To Person <email@receiver.com>
				 Subject: SMTP e-mail test

				 This is totally not to be used for spam....
				 """
    try:
   		smtpObj = smtplib.SMTP('localhost')
  		smtpObj.sendmail(sender, receivers, message)         
   		print "Successfully sent email"
    except SMTPException:
   		print "Error: unable to send email"
db.close()
