
import feedparser
import urllib2
import getpass
import sys
import pynotify


#get username, password
def getCredentials():
	usr = raw_input('enter your gmail address: ')
	passwd = getpass.getpass()
	return (usr, passwd)

#http auth handler
def authHandle(usr, passwd):
	global auth_handler
	auth_handler = urllib2.HTTPBasicAuthHandler()
	auth_handler.add_password("New mail feed", 'https://mail.google.com/', usr, passwd)

def getEmailCount():
	return d.feed.fullcount

if __name__ == "__main__":
	
	my_usr, my_pass = getCredentials()
	authHandle(my_usr,my_pass)
	#open the url with the auth handler
	opener = urllib2.build_opener(auth_handler)
	url = opener.open('https://mail.google.com/mail/feed/atom/')

	#parse dat feed
	d = feedparser.parse(url)

	if not pynotify.init("gmail-notify"):
		raise Exception, "Could not initialize notifcations"
		sys.exit (1)

	mail = getEmailCount() 
	mail = int(mail)
	if  mail == 0:
		l = pynotify.Notification("You have no new mail.")
		l.show()
		sys.exit(2)

	
	else:
		#print "Number of unread emails: ", d.feed.fullcount	

		for entry in d.entries:
			m = pynotify.Notification("Number of unread emails: ", d.feed.fullcount)
			n = pynotify.Notification(entry.author, entry.title, entry.summary)
		n.show()
		m.show()
		
		print '/n'
		print 'Author: ', entry.author
		print "Subject: ", entry.title
		print "Summary: ", entry.summary


