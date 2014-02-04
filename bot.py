import praw
import time 

r = praw.Reddit('PRAW related-question monitor by u/testpurposes v 1.0.')
r.login()
user = r.get_redditor('insertusernamehere')
commentCollection = []
commentComparison = []
submissionCollection = []
submissionComparison = []

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
	if commentCollection[0] != commentComparison[0]:
		r.send_message('insertusernamehere', '%s just made a new comment' %user, commentComparison[0])
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
		submissionCollection = list(submissionComparison)


while(True):
	commentMatcher()
	submissionMatcher()