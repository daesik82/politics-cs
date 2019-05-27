# This .py file contains codes to crawl US senators twitter accounts.
# (RT, mention, timeline included)
# Streaming data, realtime!

# import packages
import datetime
import json

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


# OAuth info
ckey = 
csecret = 
atoken = 
asecret = 

# Archiving location
now = datetime.datetime.now()
datafile = open(f'./test/tw_sen_{now.year}_{now.month:2d}_{now.day:2d}', 'w', encoding='utf-8')

# Main codes
class listener(StreamListener):

    def on_data(self, data):
        datafile.write(data)
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

while True:
    try:
        twitterStream = Stream(auth, listener())
        twitterStream.filter(follow = ['1080960924687704064', '1080870981877534720', '1078693601356509184', '1017500185356853248',
                                       '983348251972816896', '941080085121175552', '941000686275387392', '899978622416695297',
                                       '818554054309715969', '816683274076614656', '811313565760163844', '803694179079458816',
                                       '2964949642', '2964174789', '2962923040', '2955485182', '2891210047', '2863210809',
                                       '2856787757', '2167097881', '1099199839', '1096059529', '1080844782', '1074518754',
                                       '1074480192', '1071402577', '1068481578', '1058520120', '1048784496', '970207298',
                                       '968650362', '946549322', '600463589', '515822213', '486694111', '476256944',
                                       '432895323', '382791093', '339822881', '296361085', '293131808', '291756142',
                                       '278145569', '278124059', '264219447', '250188760', '249787913', '247334603',
                                       '242836537', '242555999', '236511574', '235217558', '234374703', '234128524',
                                       '233737858', '225921757', '224285242', '221162525', '217543151', '216881337',
                                       '202206694', '193794406', '172858784', '171598736', '150078976', '131546062',
                                       '117501995', '109287731', '109071031', '92186819', '88784440', '78403308',
                                       '76649729', '76456274', '75364211', '60828944', '47747074', '43910797',
                                       '29442313', '29201047', '22044727', '21406834', '21269970', '21157904',
                                       '21111098', '19726613', '18915145', '18695134', '18632666', '18137749',
                                       '18061669', '17494010', '15745368', '15324851', '13218102', '11651202',
                                       '10615232', '7429102', '7270292', '5558312'])
    except Exception as e:
        f = open('./logs/sen_twitter_error.log', 'a')
        now2 = datetime.datetime.now()
        f.write(f"Error Date >>> {now2} \n Error >>> {e} \n")
        f.close()

datafile.close()
