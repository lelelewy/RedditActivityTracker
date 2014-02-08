import praw
import time 
from twilio.rest import TwilioRestClient 
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

r = praw.Reddit('PRAW related-question monitor by u/testpurposes v 1.0.')
r.login(parser.get('SectionOne', 'username'), parser.get('SectionOne', 'password'))
user = r.get_redditor(parser.get('SectionOne', 'user'))
commentCollection = []
commentComparison = []
submissionCollection = []
submissionComparison = []

account_sid = parser.get('SectionOne', 'account_sid')
auth_token = parser.get('SectionOne', 'auth_token')
client = TwilioRestClient(account_sid, auth_token)

def commentMatcher():
	global commentCollection
	global commentComparison 
	comments = user.get_comments(limit = 1)
	for comment in comments:
		commentCollection.insert(0,comment)
	time.sleep(10)
	comments = user.get_comments(limit = 1)
	for comment in comments:
		commentComparison.insert(0, comment)
		compermalink = comment.permalink
	if commentCollection[0] != commentComparison[0]:
		message = client.messages.create(to=parser.get('SectionOne', 'stalker_number'), from_=parser.get('SectionOne', 'twilio_number'),
                                     body="%s just made a new comment. Check it out here - %s" % (user, compermalink))
		r.send_message(parser.get('SectionOne', 'stalker'), '%s just made a new comment' %user, compermalink)
		commentCollection = list(commentComparison)
	

def submissionMatcher():
	global submissionCollection
	global submissionComparison 
	submissions = user.get_submitted(limit = 1)
	for submission in submissions:
		submissionCollection.insert(0,submission)
	time.sleep(10)
	submissions = user.get_submitted(limit = 1)
	for submission in submissions:
		submissionComparison.insert(0, submission)
		subpermalink = submission.permalink
	if submissionCollection[0] != submissionComparison[0]:
		message = client.messages.create(to=parser.get('SectionOne', 'stalker_number'), from_=parser.get('SectionOne', 'twilio_number'),
                                     body="%s just made a new submission. Check it out here - %s" % (user, subpermalink))
		r.send_message(parser.get('SectionOne', 'stalker'), '%s just made a new submission' %user, submissionComparison[0])
		submissionCollection = list(submissionComparison)

while(True):
	commentMatcher()
	submissionMatcher()