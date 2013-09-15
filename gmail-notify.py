import feedparser
import urllib2
import getpass


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

def main():
	my_usr, my_pass = getCredentials()
	authHandle(my_usr,my_pass)
	#open the url with the auth handler
	opener = urllib2.build_opener(auth_handler)
	url = opener.open('https://mail.google.com/mail/feed/atom/')

	#parse dat feed
	d = feedparser.parse(url)

	#print unread mail count
	print "Number of unread emails: ", d.feed.fullcount

	for entry in d.entries:
		print '/n'
		print 'Author: ', entry.author
		print "Subject: ", entry.title
		print "Summary: ", entry.summary
main()

