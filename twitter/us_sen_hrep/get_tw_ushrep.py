# This .py file contains codes to crawl US House of Reps. twitter accounts. (Missing a few reps)
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
        twitterStream.filter(follow = ['2962891515', '2916086925', '76452765', '3018670151', '2964287128', '1078355119920562176', '233842454', '402719755', '1080515866255593472', '816284664658874368', '1080865917377097728', '2929491549', '818975124460335106', '1086316494450032640', '1037341536592310272', '816131319033950208', '1089334250', '816833925456789505', '239949176', '1531521632', '950783972', '815241612154417152', '2962868158', '816652616625168388', '26051676', '249410485', '148006729', '15954997', '817050219007328258', '558769636', '2964877294', '231108733', '19926675', '1080978331535896576', '237299871', '1074101017', '823552974253342721', '1243902714', '20467163', '2862577383', '234812598', '817138492614524928', '1028854804087492613', '15751083', '1092979962', '432676344', '2253968388', '22545491', '816157667882373120', '1222257180', '199325935', '2973870195', '18030431', '776664410', '1081350574589833221', '1083472286089396224', '1880674038', '231510077', '237750442', '816719802328715264', '193732179', '23593446', '1080986167003230208', '2293131060', '240812994', '584912320', '163570705', '1072158357237174272', '1039879658400112640', '188019606', '162069635', '23124635', '1060487274', '838462994', '295685416', '78445977', '1074412920', '22523087', '815985039485837312', '245451804', '85396297', '1080875913926139910', '1080222360643485698', '233693291', '1080894931311431682', '816030424778543104', '1080191866509901826', '210926192', '787373558', '1080198683713507335', '931614483050414080', '1080516116395499522', '742735530287304704', '789244177', '993153006', '432771620', '567508925', '252249233', '28599820', '140519774', '995193054', '1080485692298444800', '798973032362606600', '2968007206', '235312723', '137794015', '37094727', '2970279814', '153944899', '39249305', '234022257', '240393970', '815952318487298048', '2914515430', '164007407', '1075517806551154689', '249348006', '817076257770835968', '854715071116849157', '90639372', '806583915012046854', '1081256295469068288', '816303263586914304', '235190657', '1075904377221722113', '237312687', '18805303', '1080509366', '16256269', '1077121945', '153486399', '1078741899572240384', '1064206014', '818948638890217473', '815966620300480514', '2966570782', '88806753', '1082427779583541248', '1080587263132733442', '234822928', '22055226', '1080891667308298240', '2371339658', '819744763020775425', '1054381765224210432', '818536152588238849', '412595957', '240760644', '815310506596691968', '161743731', '2951574214', '29766367', '190328374', '156333623', '1080477288955826176', '234057152', '28602948', '2976606250', '1081243468327018496', '1908143071', '1080695666760929280', '1083474782602125318', '1080851152151953410', '960962340', '237763317', '2433737761', '1082086081238102018', '1068499286', '1067818539179024386', '242926427', '2975091705', '33576489', '843636970538618880', '2953974395', '1068273911224094721', '31611298', '1058460818', '811986281177772032', '1083019402046513152', '389840566', '1052896620797460481', '22012091', '935033864', '1071102246', '233949261', '1305596696', '2963445730', '80612021', '815733290955112448', '467823431', '211530910', '1074782372594413569', '211530910', '24745957', '827279765287559171', '26778110', '18166778', '976969338', '1082311988926124036', '581141508', '2966765501', '232992031', '935368364', '1339931490', '3317799825', '1055907624', '816298918468259841', '1045110018', '1058917562', '1078771848882593793', '112740986', '18277655', '48117116', '219429281', '1081240074946252801', '814179031956488192', '1058717720', '816012124505931780', '3686482216', '1069124515', '984456621417000960', '584012853', '18909919', '404132211', '50452197', '15394954', '2863006655', '818472418620608512', '248735463', '1079061579973439488', '996094929733652481', '1080277407867772930', '1072134139560620033', '29450962', '3044993235', '1009269193', '510516465', '267938462', '1444015610', '2914163523', '1055730738', '221792092', '242772524', '1849261916', '19318314', '1080292515939565568', '310310133', '1080898026418384897', '258900199', '1072467470', '23976316', '752364246218862592', '975200486', '814103950404239360', '38254095', '196362083', '1082380458976051202', '19739126', '26424123', '50152441', '516880804', '816181091673448448', '242426145', '27676828', '240427862', '385429543', '963480595', '22812754', '1051127714', '1080574793630527505', '1081318716573470720', '811632636598910976', '2696643955', '2964526557', '22669526', '1064595993222615040', '248495200', '1080941062028447744', '1060370282', '796183515998068736', '40302336', '161411080', '442824717', '1078749802765139968', '2930635215', '3122099613', '880480631108644864', '23600262', '54412900', '808416682972770304', '138203134', '20053279', '1082334352711790593', '299883942', '31801993', '2861616083', '796736612554117120', '1067748650485497862', '74508260', '1155335864', '15764644', '1082369392229400576', '20552026', '18773159', '1135486501', '1061310112013434882', '14984637', '2724095695', '1206227149', '1081222837459996672', '25086658', '1080584229510172678', '155669457', '56864092', '3026622545', '806906355214852096', '2847221717', '252819323', '4205133682', '2970462034', '1058345042', '267854863', '1080504024695222273', '224294785', '17976923', '52503751', '550401754', '33977070', '816111677917851649', '1081312310059253763', '1078692057940742144', '1075080722241736704', '834069080', '1082790600292925440', '479872233', '1089859058', '305620929', '305216911', '828977216595849216', '13491312', '312134473', '364415553', '1209417007', '1067541214671577093', '24195214', '29501253', '1071840474', '20545793', '1080462532815532032', '229197216', '234797704', '168673083', '161791703', '851621377', '33563161', '381152398', '1060584809095925762', '30216513', '1080569698536878081', '15600527', '76132891', '18696134', '1078401427347857408', '58928690', '296245061', '1289319271', '1623308912', '41417564', '818713465653051392', '1078771401497161728', '1090328229548826627', '24913074', '1080885078425784320', '1075830599007510535', '2962813893', '1075205691621720064', '1083125649609506816', '1076161611033968640', '1072008757', '211420609', '816705409486618624', '942156122', '1037321378', '1075040139351597056', '82453460', '18967498', '303861808', '377534571', '1079770852302958592', '242873057', '122174004', '1079769536730140672', '84119348', '1080830346915209216', '236279233', '1079802482640019456', '1080573351914061825', '51228911', '1080539438508400642', '124224165', '1083469084648505344', '1260172386', '1074129612', '1083448909', '164369297', '193872188', '1051446626', '237862972', '32010840', '2966205003', '1065995022', '1082416697380913152', '1140648348', '36686040', '1080307235350241280', '2968451607', '1058051748', '281540744', '1410590874', '518644221', '2852998461', '1017819745880543238', '1069636653353000962', '1077446982', '234014087', '254082173', '15356407', '234469322', '2382685057', '1080854935535800320', '384913290', '1071900114', '37007274', '2750127259'])
    except Exception as e:
        f = open('./logs/sen_twitter_error.log', 'a')
        now2 = datetime.datetime.now()
        f.write(f"Error Date >>> {now2} \n Error >>> {e} \n")
        f.close()

datafile.close()