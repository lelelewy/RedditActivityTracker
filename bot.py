import praw
import time 

r = praw.Reddit('PRAW related-question monitor by u/testpurposes v 1.0.')
r.login()
user = r.get_redditor('insertusernamehere')
commentCollection = []
commentComparison = []

def commentMatcher():
	global commentCollection
	global commentComparison 
	comments = user.get_comments(limit = 1)
	for comment in comments:
		commentCollection.append(comment)
	time.sleep(60)
	comments = user.get_comments(limit = 1)
	for comment in comments:
		commentComparison.append(comment)
	if commentCollection[0] != commentComparison[0]:
		r.send_message('insertusernamehere', 'just made a new comment', 'go check now')
		commentCollection = list(commentComparison)
	else:
		r.send_message('insertusernamehere', 'did not made a new comment', 'sorry')

while(True):
	commentMatcher()