import praw
import time 
from twilio.rest import TwilioRestClient 

r = praw.Reddit('PRAW related-question monitor by u/testpurposes v 1.0.')
r.login()
user = r.get_redditor('insertusernamehere')
commentCollection = []
commentComparison = []
submissionCollection = []
submissionComparison = []

account_sid = "AC5df5170fce7cffbda8c085cb39d9b7cf"
auth_token = "455a2555d4ae189673a694a886386ad0"
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
		message = client.messages.create(to="+19086982296", from_="+17324121974",
                                     body="%s just made a new comment. Check it out here - %s" % (user, compermalink))
		r.send_message('krumpqueen', '%s just made a new comment' %user, compermalink)
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
	if submissionCollection[0] != submissionComparison[0]:
		r.send_message('insertusernamehere', '%s just made a new comment' %user, submissionComparison[0])


while(True):
	commentMatcher()
	submissionMatcher()