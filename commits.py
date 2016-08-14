import subprocess, os, datetime
import smtplib
from email.MIMEText import MIMEText


def call(command):
	if subprocess.Popen(command, stderr=subprocess.PIPE).stderr.read(): # command output is from oc stderr 
		outputStr = subprocess.Popen(command, stderr=subprocess.PIPE).stderr.read()
	else:
		outputStr = subprocess.Popen(command, stdout=subprocess.PIPE).stdout.read()  # command output is from oc stdout
	return outputStr

def sendMail(message):
	usr = 'xiaocwan@gmail.com'
	psw = ''
	mail_host="smtp.gmail.com" 

	me=usr+'<'+usr+'>'
	sub = 'Origin-Web-Console commits since ' + past.strftime('%Y-%m-%d %H:%M:%S')
	to_list = ['xiaocwan@redhat.com']
	
	try:
		message = "Please don't reply this mail directly.\n"+message+"\n\nThanks,\nXiaochuan"
		msg = MIMEText(message)	 #str(mailContent).decode('utf-8')
		msg['Subject'] = sub
		msg['From'] = me
		msg['To'] = ";".join(to_list)
		s = smtplib.SMTP(mail_host, 587)
		s.ehlo()
		s.starttls() #
		s.ehlo()  #
		s.login(usr, psw)
	
		s.sendmail(me, to_list, msg.as_string()) #	  msg.as_string()
		s.close()
		
	except Exception, e:
		print Exception,":",e


if __name__ == '__main__':
	
	#time = "2016-08-17-07-00-00"  # 30 08 * * * python commit.py
	now=datetime.datetime.now()
	past = now - datetime.timedelta(hours = 24)

	print 'Pulling and checking commit log...'
	since = past.strftime('%Y-%m-%d-%H-%M-%S')
	call(command = ['sudo','git','pull','origin','master'])
	outputStr = call(command = ['sudo','git','log','--oneline','--after=%s'%since])
	
	print 'Sending mail...'
	sendMail(outputStr)
	print 'Done!'

