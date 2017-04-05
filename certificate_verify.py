import requests
from netaddr import IPNetwork
import json
import sys
from OpenSSL import crypto
import ssl
import json
import subprocess
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import OpenSSL

toplevel_domains = ['AAA','AARP','ABARTH','ABB','ABBOTT','ABBVIE','ABC','ABLE','ABOGADO','ABUDHABI','AC','ACADEMY','ACCENTURE','ACCOUNTANT','ACCOUNTANTS','ACO','ACTIVE','ACTOR','AD','ADAC','ADS','ADULT','AE','AEG','AERO','AETNA','AF','AFAMILYCOMPANY','AFL','AFRICA','AG','AGAKHAN','AGENCY','AI','AIG','AIGO','AIRBUS','AIRFORCE','AIRTEL','AKDN','AL','ALFAROMEO','ALIBABA','ALIPAY','ALLFINANZ','ALLSTATE','ALLY','ALSACE','ALSTOM','AM','AMERICANEXPRESS','AMERICANFAMILY','AMEX','AMFAM','AMICA','AMSTERDAM','ANALYTICS','ANDROID','ANQUAN','ANZ','AO','AOL','APARTMENTS','APP','APPLE','AQ','AQUARELLE','AR','ARAMCO','ARCHI','ARMY','ARPA','ART','ARTE','AS','ASDA','ASIA','ASSOCIATES','AT','ATHLETA','ATTORNEY','AU','AUCTION','AUDI','AUDIBLE','AUDIO','AUSPOST','AUTHOR','AUTO','AUTOS','AVIANCA','AW','AWS','AX','AXA','AZ','AZURE','BA','BABY','BAIDU','BANAMEX','BANANAREPUBLIC','BAND','BANK','BAR','BARCELONA','BARCLAYCARD','BARCLAYS','BAREFOOT','BARGAINS','BASEBALL','BASKETBALL','BAUHAUS','BAYERN','BB','BBC','BBT','BBVA','BCG','BCN','BD','BE','BEATS','BEAUTY','BEER','BENTLEY','BERLIN','BEST','BESTBUY','BET','BF','BG','BH','BHARTI','BI','BIBLE','BID','BIKE','BING','BINGO','BIO','BIZ','BJ','BLACK','BLACKFRIDAY','BLANCO','BLOCKBUSTER','BLOG','BLOOMBERG','BLUE','BM','BMS','BMW','BN','BNL','BNPPARIBAS','BO','BOATS','BOEHRINGER','BOFA','BOM','BOND','BOO','BOOK','BOOKING','BOOTS','BOSCH','BOSTIK','BOSTON','BOT','BOUTIQUE','BOX','BR','BRADESCO','BRIDGESTONE','BROADWAY','BROKER','BROTHER','BRUSSELS','BS','BT','BUDAPEST','BUGATTI','BUILD','BUILDERS','BUSINESS','BUY','BUZZ','BV','BW','BY','BZ','BZH','CA','CAB','CAFE','CAL','CALL','CALVINKLEIN','CAM','CAMERA','CAMP','CANCERRESEARCH','CANON','CAPETOWN','CAPITAL','CAPITALONE','CAR','CARAVAN','CARDS','CARE','CAREER','CAREERS','CARS','CARTIER','CASA','CASE','CASEIH','CASH','CASINO','CAT','CATERING','CATHOLIC','CBA','CBN','CBRE','CBS','CC','CD','CEB','CENTER','CEO','CERN','CF','CFA','CFD','CG','CH','CHANEL','CHANNEL','CHASE','CHAT','CHEAP','CHINTAI','CHLOE','CHRISTMAS','CHROME','CHRYSLER','CHURCH','CI','CIPRIANI','CIRCLE','CISCO','CITADEL','CITI','CITIC','CITY','CITYEATS','CK','CL','CLAIMS','CLEANING','CLICK','CLINIC','CLINIQUE','CLOTHING','CLOUD','CLUB','CLUBMED','CM','CN','CO','COACH','CODES','COFFEE','COLLEGE','COLOGNE','COM','COMCAST','COMMBANK','COMMUNITY','COMPANY','COMPARE','COMPUTER','COMSEC','CONDOS','CONSTRUCTION','CONSULTING','CONTACT','CONTRACTORS','COOKING','COOKINGCHANNEL','COOL','COOP','CORSICA','COUNTRY','COUPON','COUPONS','COURSES','CR','CREDIT','CREDITCARD','CREDITUNION','CRICKET','CROWN','CRS','CRUISE','CRUISES','CSC','CU','CUISINELLA','CV','CW','CX','CY','CYMRU','CYOU','CZ','DABUR','DAD','DANCE','DATA','DATE','DATING','DATSUN','DAY','DCLK','DDS','DE','DEAL','DEALER','DEALS','DEGREE','DELIVERY','DELL','DELOITTE','DELTA','DEMOCRAT','DENTAL','DENTIST','DESI','DESIGN','DEV','DHL','DIAMONDS','DIET','DIGITAL','DIRECT','DIRECTORY','DISCOUNT','DISCOVER','DISH','DIY','DJ','DK','DM','DNP','DO','DOCS','DOCTOR','DODGE','DOG','DOHA','DOMAINS','DOT','DOWNLOAD','DRIVE','DTV','DUBAI','DUCK','DUNLOP','DUNS','DUPONT','DURBAN','DVAG','DVR','DZ','EARTH','EAT','EC','ECO','EDEKA','EDU','EDUCATION','EE','EG','EMAIL','EMERCK','ENERGY','ENGINEER','ENGINEERING','ENTERPRISES','EPOST','EPSON','EQUIPMENT','ER','ERICSSON','ERNI','ES','ESQ','ESTATE','ESURANCE','ET','EU','EUROVISION','EUS','EVENTS','EVERBANK','EXCHANGE','EXPERT','EXPOSED','EXPRESS','EXTRASPACE','FAGE','FAIL','FAIRWINDS','FAITH','FAMILY','FAN','FANS','FARM','FARMERS','FASHION','FAST','FEDEX','FEEDBACK','FERRARI','FERRERO','FI','FIAT','FIDELITY','FIDO','FILM','FINAL','FINANCE','FINANCIAL','FIRE','FIRESTONE','FIRMDALE','FISH','FISHING','FIT','FITNESS','FJ','FK','FLICKR','FLIGHTS','FLIR','FLORIST','FLOWERS','FLY','FM','FO','FOO','FOOD','FOODNETWORK','FOOTBALL','FORD','FOREX','FORSALE','FORUM','FOUNDATION','FOX','FR','FREE','FRESENIUS','FRL','FROGANS','FRONTDOOR','FRONTIER','FTR','FUJITSU','FUJIXEROX','FUN','FUND','FURNITURE','FUTBOL','FYI','GA','GAL','GALLERY','GALLO','GALLUP','GAME','GAMES','GAP','GARDEN','GB','GBIZ','GD','GDN','GE','GEA','GENT','GENTING','GEORGE','GF','GG','GGEE','GH','GI','GIFT','GIFTS','GIVES','GIVING','GL','GLADE','GLASS','GLE','GLOBAL','GLOBO','GM','GMAIL','GMBH','GMO','GMX','GN','GODADDY','GOLD','GOLDPOINT','GOLF','GOO','GOODHANDS','GOODYEAR','GOOG','GOOGLE','GOP','GOT','GOV','GP','GQ','GR','GRAINGER','GRAPHICS','GRATIS','GREEN','GRIPE','GROUP','GS','GT','GU','GUARDIAN','GUCCI','GUGE','GUIDE','GUITARS','GURU','GW','GY','HAIR','HAMBURG','HANGOUT','HAUS','HBO','HDFC','HDFCBANK','HEALTH','HEALTHCARE','HELP','HELSINKI','HERE','HERMES','HGTV','HIPHOP','HISAMITSU','HITACHI','HIV','HK','HKT','HM','HN','HOCKEY','HOLDINGS','HOLIDAY','HOMEDEPOT','HOMEGOODS','HOMES','HOMESENSE','HONDA','HONEYWELL','HORSE','HOSPITAL','HOST','HOSTING','HOT','HOTELES','HOTMAIL','HOUSE','HOW','HR','HSBC','HT','HTC','HU','HUGHES','HYATT','HYUNDAI','IBM','ICBC','ICE','ICU','ID','IE','IEEE','IFM','IKANO','IL','IM','IMAMAT','IMDB','IMMO','IMMOBILIEN','IN','INDUSTRIES','INFINITI','INFO','ING','INK','INSTITUTE','INSURANCE','INSURE','INT','INTEL','INTERNATIONAL','INTUIT','INVESTMENTS','IO','IPIRANGA','IQ','IR','IRISH','IS','ISELECT','ISMAILI','IST','ISTANBUL','IT','ITAU','ITV','IVECO','IWC','JAGUAR','JAVA','JCB','JCP','JE','JEEP','JETZT','JEWELRY','JIO','JLC','JLL','JM','JMP','JNJ','JO','JOBS','JOBURG','JOT','JOY','JP','JPMORGAN','JPRS','JUEGOS','JUNIPER','KAUFEN','KDDI','KE','KERRYHOTELS','KERRYLOGISTICS','KERRYPROPERTIES','KFH','KG','KH','KI','KIA','KIM','KINDER','KINDLE','KITCHEN','KIWI','KM','KN','KOELN','KOMATSU','KOSHER','KP','KPMG','KPN','KR','KRD','KRED','KUOKGROUP','KW','KY','KYOTO','KZ','LA','LACAIXA','LADBROKES','LAMBORGHINI','LAMER','LANCASTER','LANCIA','LANCOME','LAND','LANDROVER','LANXESS','LASALLE','LAT','LATINO','LATROBE','LAW','LAWYER','LB','LC','LDS','LEASE','LECLERC','LEFRAK','LEGAL','LEGO','LEXUS','LGBT','LI','LIAISON','LIDL','LIFE','LIFEINSURANCE','LIFESTYLE','LIGHTING','LIKE','LILLY','LIMITED','LIMO','LINCOLN','LINDE','LINK','LIPSY','LIVE','LIVING','LIXIL','LK','LOAN','LOANS','LOCKER','LOCUS','LOFT','LOL','LONDON','LOTTE','LOTTO','LOVE','LPL','LPLFINANCIAL','LR','LS','LT','LTD','LTDA','LU','LUNDBECK','LUPIN','LUXE','LUXURY','LV','LY','MA','MACYS','MADRID','MAIF','MAISON','MAKEUP','MAN','MANAGEMENT','MANGO','MARKET','MARKETING','MARKETS','MARRIOTT','MARSHALLS','MASERATI','MATTEL','MBA','MC','MCD','MCDONALDS','MCKINSEY','MD','ME','MED','MEDIA','MEET','MELBOURNE','MEME','MEMORIAL','MEN','MENU','MEO','METLIFE','MG','MH','MIAMI','MICROSOFT','MIL','MINI','MINT','MIT','MITSUBISHI','MK','ML','MLB','MLS','MM','MMA','MN','MO','MOBI','MOBILE','MOBILY','MODA','MOE','MOI','MOM','MONASH','MONEY','MONSTER','MONTBLANC','MOPAR','MORMON','MORTGAGE','MOSCOW','MOTO','MOTORCYCLES','MOV','MOVIE','MOVISTAR','MP','MQ','MR','MS','MSD','MT','MTN','MTPC','MTR','MU','MUSEUM','MUTUAL','MV','MW','MX','MY','MZ','NA','NAB','NADEX','NAGOYA','NAME','NATIONWIDE','NATURA','NAVY','NBA','NC','NE','NEC','NET','NETBANK','NETFLIX','NETWORK','NEUSTAR','NEW','NEWHOLLAND','NEWS','NEXT','NEXTDIRECT','NEXUS','NF','NFL','NG','NGO','NHK','NI','NICO','NIKE','NIKON','NINJA','NISSAN','NISSAY','NL','NO','NOKIA','NORTHWESTERNMUTUAL','NORTON','NOW','NOWRUZ','NOWTV','NP','NR','NRA','NRW','NTT','NU','NYC','NZ','OBI','OBSERVER','OFF','OFFICE','OKINAWA','OLAYAN','OLAYANGROUP','OLDNAVY','OLLO','OM','OMEGA','ONE','ONG','ONL','ONLINE','ONYOURSIDE','OOO','OPEN','ORACLE','ORANGE','ORG','ORGANIC','ORIENTEXPRESS','ORIGINS','OSAKA','OTSUKA','OTT','OVH','PA','PAGE','PAMPEREDCHEF','PANASONIC','PANERAI','PARIS','PARS','PARTNERS','PARTS','PARTY','PASSAGENS','PAY','PCCW','PE','PET','PF','PFIZER','PG','PH','PHARMACY','PHILIPS','PHONE','PHOTO','PHOTOGRAPHY','PHOTOS','PHYSIO','PIAGET','PICS','PICTET','PICTURES','PID','PIN','PING','PINK','PIONEER','PIZZA','PK','PL','PLACE','PLAY','PLAYSTATION','PLUMBING','PLUS','PM','PN','PNC','POHL','POKER','POLITIE','PORN','POST','PR','PRAMERICA','PRAXI','PRESS','PRIME','PRO','PROD','PRODUCTIONS','PROF','PROGRESSIVE','PROMO','PROPERTIES','PROPERTY','PROTECTION','PRU','PRUDENTIAL','PS','PT','PUB','PW','PWC','PY','QA','QPON','QUEBEC','QUEST','QVC','RACING','RADIO','RAID','RE','READ','REALESTATE','REALTOR','REALTY','RECIPES','RED','REDSTONE','REDUMBRELLA','REHAB','REISE','REISEN','REIT','RELIANCE','REN','RENT','RENTALS','REPAIR','REPORT','REPUBLICAN','REST','RESTAURANT','REVIEW','REVIEWS','REXROTH','RICH','RICHARDLI','RICOH','RIGHTATHOME','RIL','RIO','RIP','RMIT','RO','ROCHER','ROCKS','RODEO','ROGERS','ROOM','RS','RSVP','RU','RUHR','RUN','RW','RWE','RYUKYU','SA','SAARLAND','SAFE','SAFETY','SAKURA','SALE','SALON','SAMSCLUB','SAMSUNG','SANDVIK','SANDVIKCOROMANT','SANOFI','SAP','SAPO','SARL','SAS','SAVE','SAXO','SB','SBI','SBS','SC','SCA','SCB','SCHAEFFLER','SCHMIDT','SCHOLARSHIPS','SCHOOL','SCHULE','SCHWARZ','SCIENCE','SCJOHNSON','SCOR','SCOT','SD','SE','SEAT','SECURE','SECURITY','SEEK','SELECT','SENER','SERVICES','SES','SEVEN','SEW','SEX','SEXY','SFR','SG','SH','SHANGRILA','SHARP','SHAW','SHELL','SHIA','SHIKSHA','SHOES','SHOP','SHOPPING','SHOUJI','SHOW','SHOWTIME','SHRIRAM','SI','SILK','SINA','SINGLES','SITE','SJ','SK','SKI','SKIN','SKY','SKYPE','SL','SLING','SM','SMART','SMILE','SN','SNCF','SO','SOCCER','SOCIAL','SOFTBANK','SOFTWARE','SOHU','SOLAR','SOLUTIONS','SONG','SONY','SOY','SPACE','SPIEGEL','SPOT','SPREADBETTING','SR','SRL','SRT','ST','STADA','STAPLES','STAR','STARHUB','STATEBANK','STATEFARM','STATOIL','STC','STCGROUP','STOCKHOLM','STORAGE','STORE','STREAM','STUDIO','STUDY','STYLE','SU','SUCKS','SUPPLIES','SUPPLY','SUPPORT','SURF','SURGERY','SUZUKI','SV','SWATCH','SWIFTCOVER','SWISS','SX','SY','SYDNEY','SYMANTEC','SYSTEMS','SZ','TAB','TAIPEI','TALK','TAOBAO','TARGET','TATAMOTORS','TATAR','TATTOO','TAX','TAXI','TC','TCI','TD','TDK','TEAM','TECH','TECHNOLOGY','TEL','TELECITY','TELEFONICA','TEMASEK','TENNIS','TEVA','TF','TG','TH','THD','THEATER','THEATRE','TIAA','TICKETS','TIENDA','TIFFANY','TIPS','TIRES','TIROL','TJ','TJMAXX','TJX','TK','TKMAXX','TL','TM','TMALL','TN','TO','TODAY','TOKYO','TOOLS','TOP','TORAY','TOSHIBA','TOTAL','TOURS','TOWN','TOYOTA','TOYS','TR','TRADE','TRADING','TRAINING','TRAVEL','TRAVELCHANNEL','TRAVELERS','TRAVELERSINSURANCE','TRUST','TRV','TT','TUBE','TUI','TUNES','TUSHU','TV','TVS','TW','TZ','UA','UBANK','UBS','UCONNECT','UG','UK','UNICOM','UNIVERSITY','UNO','UOL','UPS','US','UY','UZ','VA','VACATIONS','VANA','VANGUARD','VC','VE','VEGAS','VENTURES','VERISIGN','VERSICHERUNG','VET','VG','VI','VIAJES','VIDEO','VIG','VIKING','VILLAS','VIN','VIP','VIRGIN','VISA','VISION','VISTA','VISTAPRINT','VIVA','VIVO','VLAANDEREN','VN','VODKA','VOLKSWAGEN','VOLVO','VOTE','VOTING','VOTO','VOYAGE','VU','VUELOS','WALES','WALMART','WALTER','WANG','WANGGOU','WARMAN','WATCH','WATCHES','WEATHER','WEATHERCHANNEL','WEBCAM','WEBER','WEBSITE','WED','WEDDING','WEIBO','WEIR','WF','WHOSWHO','WIEN','WIKI','WILLIAMHILL','WIN','WINDOWS','WINE','WINNERS','WME','WOLTERSKLUWER','WOODSIDE','WORK','WORKS','WORLD','WOW','WS','WTC','WTF','XBOX','XEROX','XFINITY','XIHUAN','XIN','XPERIA','XXX','XYZ','YACHTS','YAHOO','YAMAXUN','YANDEX','YE','YODOBASHI','YOGA','YOKOHAMA','YOU','YOUTUBE','YT','YUN','ZA','ZAPPOS','ZARA','ZERO','ZIP','ZIPPO','ZM','ZONE','ZUERICH','ZW']
def check_ssl(url,cname,subnet ):
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			if("https" in url):
				print("----------HTTPS----------")
				for domain in toplevel_domains:
					if(domain in cname):
						url="https://"+cname
				else:
					print("======CNAME NOT GOOD======")
					print(url, cname)

				try:
					req = requests.get(url, verify=True,timeout=0.5)
					print url + ' >>>>>>>>>>>>>>>> has a valid SSL certificate!'
					print('--\n')
					# servers_file.write(url+'\n')
					url_without_https = url.replace("https://","")
					print(url_without_https)
					try:
						cert = ssl.get_server_certificate((url_without_https, 443))
						load_cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
						get_certificate_info(load_cert,url)
						print("___CURL INFO___")
						get_curl_info(url,req.headers)
						print("____END CURL___\n")
					except ssl.SSLError:
						print("SSL ERROR ______ __ _ _ ")
					except requests.exceptions.SSLError:
						print("sni ERROR")
				except requests.exceptions.TooManyRedirects:
					print("too many redirect")

				except requests.exceptions.SSLError:
					print url + ' >>>>>>>>>>>>>>>> has INVALID SSL certificate!'
					# servers_file.write(url+'\n')
					url_without_https = url.replace("https://","")

					p = subprocess.Popen(["timeout","30","openssl", "s_client",'-connect',url_without_https+":443"], stdout=subprocess.PIPE)
					out, err = p.communicate()
					out_without_n = out.replace('\n','!@#$&*()')
					cert = re.findall(r'-----BEGIN.*END.CERTIFICATE-----',out_without_n)
					if(len(cert)>0):
						print('============')
						print(cert)
						print('============')
						cert = cert[0].replace('!@#$&*()','\n')
						load_cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
						get_certificate_info(load_cert,url)
						# print(cert)
					p = subprocess.Popen(["curl", "-k" ,url, "--head","-m","30"],stdout=subprocess.PIPE)
					out, err = p.communicate()
					print("___CURL INFO___")
					print(out)
					print("____END CURL___\n")


					# ssl._create_default_https_context = ssl._create_unverified_context() 
					# cert = ssl.get_server_certificate((url_without_https, 443))
					# print(cert)
					
					# get_curl_info(url,req.headers)

				except requests.exceptions.ConnectionError:
					# try to send http request
					newurl = url.replace("https","http")
					try:
						req = requests.get(newurl,timeout = 0.1)
						get_curl_info(url,req.headers)
					except requests.exceptions.ConnectionError:
						pass
						# print("NOT SSL AND Not a Web Server")
					except requests.exceptions.ReadTimeout:
						pass
						# print ("NOT SSL timeout No web server at all")
				except requests.exceptions.ReadTimeout:
					print 'timeout'
			# else:
				# print("HTTP URL", url)
				# try:
				# 	req = requests.get(url,timeout = 0.1)
				# 	get_curl_info(url,req.headers)
				# except requests.exceptions.ConnectionError:
				# 	pass
				# 	# print("NOT SSL AND Not a Web Server")
				# except requests.exceptions.ReadTimeout:
				# 	pass

def get_curl_info_invalidcert(url,curl_date):
	data = {}
	data['url'] = url
	
def get_curl_info(url,curl_data):
	data = {}
	data['url'] = url
	print('HTTP')
	for key, value in curl_data.iteritems() :
		data[key] = value	
	json_data = json.dumps(data)
	print(json_data)

def get_certificate_info(cert,url):
	# print(cert)
	data = {}
	data['url'] = url
	# data['extension'] = cert.get_extension()
	subject = cert.get_subject()
	data['issued_to'] = str(subject.CN)
	issuer = cert.get_issuer()
	issued_by = issuer.CN
	# print(issued_by)
	data['issuer'] = str(cert.get_issuer())
	data['not_after'] = cert.get_notAfter()
	data['not_before'] = cert.get_notBefore()
	# data['public_key'] = cert.get_pubkey()
	data['serial_number'] = cert.get_serial_number()
	data['sig_alg'] = cert.get_signature_algorithm()
	data['subject'] = str(cert.get_subject())
	data['version'] = cert.get_version()
	data['has_expired'] = cert.has_expired()
	# print(data)
	json_data = json.dumps(data)
	print(json_data)
	print('=====FINISHED=====\n\n\n')


# req = requests.get('https://31.13.71.36', verify=True,timeout=0.1)
# subnet_to_check = sys.argv[1]

subnet_file_name = sys.argv[1]
# servers_file = open(subnet_file_name+"_servers.txt", "w")

F = open(subnet_file_name,"r") 
list_of_servers = F.readlines()
# print(list_of_servers)
for server in list_of_servers:
	url,cname,subnet = server.split(',')
	print(url+'  '+cname+' '+subnet)
	check_ssl(url,cname,subnet)

# servers_file.close()