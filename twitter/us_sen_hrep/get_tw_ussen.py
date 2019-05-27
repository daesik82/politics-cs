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
ckey = "lpqzpNUsv55dh3nvOmUkR0YWz"
csecret = "ywBsWjnxMKhs2ovxvob8UY70EIRZ6d79TJtft2ppaSBoMG0Q6m"
atoken = "840060061879738369-4yd1S8JE5HCfQlq6MuIHjLJHofC7rN6"
asecret = "VTPMdiQ8IIkKKFt3go9M17rUjVuOzNZFRSYLbuCMeOJGA"

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
        twitterStream.filter(follow = ['@SenHawleyPress', '@SenatorBraun', '@SenatorRomney', '@SenBillCassidy',
                                       '@SenHydeSmith', '@SenDougJones', '@SenTinaSmith', '@gillibrandny',
                                       '@SenJackyRosen', '@SenJohnKennedy', '@SenCortezMasto', '@SenKamalaHarris',
                                       '@SenMcSallyAZ', '@SenThomTillis', '@SenSasse', '@SenatorRounds',
                                       '@SenDanSullivan', '@sendavidperdue', '@SenJoniErnst', '@SenBooker',
                                       '@MartinHeinrich', '@SenatorRisch', '@SenatorSinema', '@SenatorBaldwin',
                                       '@SenTedCruz', '@SenatorFischer', '@SenAngusKing', '@SenDuckworth',
                                       '@SenKevinCramer', '@SenWarren', '@SenTomCotton', '@SenatorHassan',
                                       '@MikeCrapo', '@SenatorTester', '@SenJackReed', '@SenFeinstein',
                                       '@LindseyGrahamSC', '@SenJohnHoeven', '@McConnellPress', '@SenJohnThune',
                                       '@PattyMurray', '@SenatorEnzi', '@MarshaBlackburn', '@SenBlumenthal',
                                       '@SenatorWicker', '@RonWyden', '@SenatorCarper', '@SenatorDurbin',
                                       '@SenatorLeahy', '@SenWhitehouse', '@SenGaryPeters', '@SenCoryGardner',
                                       '@Sen_JoeManchin', '@SenToddYoung', '@SenRonJohnson', '@SenatorLankford',
                                       '@SenatorBennet', '@SenToomey', '@SenatorTimScott', '@RandPaul',
                                       '@SenJohnBarrasso', '@SenCapito', '@timkaine', '@SenBobCasey',
                                       '@ChrisMurphyCT', '@SenRickScott', '@SenatorCantwell', '@SenatorShaheen',
                                       '@SenatorCardin', '@maziehirono', '@SenMikeLee', '@SenatorIsakson',
                                       '@SenAlexander', '@SenStabenow', '@SenPatRoberts', '@SenatorTomUdall',
                                       '@brianschatz', '@SenSherrodBrown', '@SenSanders', '@SenJeffMerkley',
                                       '@SenAmyKlobuchar', '@SenMarkey', '@RoyBlunt', '@SenatorBurr',
                                       '@SenShelby', '@SenatorCollins', '@senrobportman', '@SenatorMenendez',
                                       '@JerryMoran', '@ChrisVanHollen', '@lisamurkowski', '@SenSchumer',
                                       '@marcorubio', '@ChrisCoons', '@JohnCornyn', '@SteveDaines',
                                       '@ChuckGrassley', '@MarkWarner', '@JimInhofe', '@JohnBoozman'])
    except Exception as e:
        f = open('./logs/sen_twitter_error.log', 'a')
        now2 = datetime.datetime.now()
        f.write(f"Error Date >>> {now2} \n Error >>> {e} \n")
        f.close()

datafile.close()