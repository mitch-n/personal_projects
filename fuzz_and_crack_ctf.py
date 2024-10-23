from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from random import choice, randint
import hashlib

app = Flask(__name__)

limiter = Limiter(
	get_remote_address,
	app=app,
	default_limits=[],
	storage_uri="memory://"
)


dir_pool = ["cover","install","sales","00","forward","viewonline","bios","104","contact-us","108","system","action","groupcp","desktop","privacy-policy","computer","reprints","sport","live","1x1","tracker","item","sections","friends","ws","college","line","logo2","quotes","applications","core","traceroute","loading","k","navigation","tags","license","reklama","reg","clients","j","editorial","mediakit","engine","entry","game","benefits","soft","digg","membership","layout","contents","94","q","development","toc","finance","hp","tutorial","rss20","transparent","source","1998","headlines","pic","pdfs","83","irc","program","reference","interviews","yahoo","used-cars","log","includes","europe","93","survey","101","students","icon_smile","pipermail","credits","updates","event","crypto","family","journal","read","webcasts","tos","imgs","z","humor","virus","classifieds","92","edit","networking","newsroom","test","bottom","ca","team","u","earthweb_foot2","out","ruledivide_foot","grcom_foot","icom_foot","devx_foot2","schedule","86","ss","my","98","95","88","spyware","cat","79","wordpress","computers","right","footers","pc","mirrors","tr","corrections","rules","government","ajax","icom_includes","server","presentations","74","82","customers","84","template","bio","law","alerts","information","marketing","purchase","mission","90","76","85","accessibility","delicious","78","programming","project","80","rss2","css","courses","71","money","unix","91","81","specials","v","87","67","68","100","99","feature","review","sites","77","hosting","75","press_releases","id","python","73","food","ad","impressum","groups","n","89","plugins","72","69","thumbs","65","traffic","columns","62","magazine","w","ftp","shared","70"]
pass_pool = ["gatito","charlie1","ashley1","tigger1","nenita","raiders","skater","oscar","erika","pinky","froggy","carebear","billabong","zachary","daddy1","010203","jordan1","gerald","pogiako","sydney","marian","biteme","chacha","sophia","karla","batista","kelly","inlove","bestfriends","starwars","darren","violet","purple1","snowball","a123456","iubire","dustin","ferrari","cheyenne","cynthia","jessica1","sweetpea","dreams","megan","kitkat","darkangel","aaron","tyler","gloria","taurus","compaq","blessed","gangster","loving","millie","swimming","sunshine1","pebbles","dominic","loser","candy","joanne","abcdefg","santos","jamie","sammy","darling","melody","valentina","hello1","connor","gracie","cheche","friendster","robbie","elaine","martinez","hector","cupcake","bradley","kathleen","sunflower","jorge","trinity","tennis","isabella","matrix","mariah","flores","shopping","preciosa","amigas","justin1","jamaica","yankees","mauricio","lucky","california","westside","maryjane","rodrigo","broken","999999999","thunder","emmanuel","mamita","ronnie","canada","joanna","elijah","monkeys","omarion","florida","motorola","nikki","love12","familia","evelyn","parola","sweets","barney","sparky","brandon1","smiles","bubble","estrellita","shakira","ilovehim","onelove","timothy","jasmin","nelson","scotland","people","ganda","player","monster","phoenix","savannah","jayden","truelove","212121","guitar","katie","number1","iloveu2","pumpkin","potter","wilson","camille","hearts","dallas","miranda","sporting","lucky1","102030","emily","allison","danny","bandit","qazwsx","456123","hermosa","england","bestfriend","red123","soccer1","fashion","54321","rabbit","disney","pimpin","frankie","justine","andrei","iverson","spider","bonnie","sharon","444444","hockey","letmein","brandy","diego","garcia","marina","147852","claire","linkinpark","marlon","turtle"]

chosen_pass = ''
chosen_dir = ''
chosen_pass_hash = ''

flag_multiplier = 32993
flag = ""

def rotate_secrets():
	global chosen_pass, chosen_dir, chosen_pass_hash, pass_pool, dir_pool, flag, flag_multiplier
	chosen_pass = choice(pass_pool)
	chosen_dir = choice(dir_pool)
	h = hashlib.new("sha1")
	h.update(chosen_pass.encode())
	chosen_pass_hash = h.hexdigest()
	flag = "flag{"+str(randint(10000,90000)*flag_multiplier)+"}"
	

rotate_secrets()


@app.route('/')
def home():
	return f"""
		<html>
			<body style="padding: 1em;">
				<a href="/login">
					<button>Login</button>
				</a>
			</body>
		</html>
	"""


@app.route('/login', methods=['GET','POST'])
@limiter.limit("1 per 5 seconds", methods=['POST'])
def login():
	global chosen_pass, chosen_dir, flag
	
	username = request.form.get("user")
	password = request.form.get("pass")
	message = ""
	message_color = ""
	
	if username and password:
		if username=="admin" and password==chosen_pass:
			#message = "flag{fuzz_dirs_and_crack_hashes}"
			message = flag
			message_color = "lightgreen"
			rotate_secrets()
		else:
			message = "Invalid username or password."
			message_color = "salmon"
	
	return f"""
	<html>
		<body style="padding: 1em; font-family: sans-serif;">
			<form method="post" style="display:inline-block;">
				<input name="user" placeholder="username">
				<input name="pass" type=password placeholder="password">
				<input type="submit" value="Submit">
				<div style="padding:1em;background-color:{ message_color }; margin:1em 0;">
					{ message }
				<div>
			</form>
		</body>
	</html>
	"""


@app.route(f'/<directory>')
def secret(directory):
	global chosen_pass_hash, chosen_dir
	if directory == chosen_dir:
		return f"admin:{ chosen_pass_hash }"
	else:
		return "",404

