
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

if __name__ == "__main__":
	my_usr, my_pass = getCredentials()
	authHandle(my_usr,my_pass)
	#open the url with the auth handler
	opener = urllib2.build_opener(auth_handler)
	url = opener.open('https://mail.google.com/mail/feed/atom/')

	#parse dat feed
	d = feedparser.parse(url)

	if not pynotify.init("summary-body"):
		sys.exit (1)

	#print unread mail count
	print "Number of unread emails: ", d.feed.fullcount

	
	for entry in d.entries:
		n = pynotify.Notification(entry.author, entry.title, entry.summary)
	n.show()
	print '/n'
	print 'Author: ', entry.author
	print "Subject: ", entry.title
	print "Summary: ", entry.summary


