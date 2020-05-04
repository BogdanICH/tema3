import socket
import traceback

# socket de UDP
udp_send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

# socket RAW de citire a răspunsurilor ICMP
icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
# setam timout in cazul in care socketul ICMP la apelul recvfrom nu primeste nimic in buffer
icmp_recv_socket.settimeout(3)

list_of_sites = ['news.com.au', 'chinadaily.com.cn', 'southafrica.co.za']

def info_about_ip(site)
    link = 'http://ip-api.com/json/'+site+'?fields=country,region,city'
    answer = requests.get(link, headers=fake_HTTP_header)
    if (answer.json()):
        print(answer.json())
    else:
        print("Privat")

def traceroute(ip, port):
    # setam TTL in headerul de IP pentru socketul de UDP
    TTL =  1
    while True:
        udp_send_sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, TTL)

        # trimite un mesaj UDP catre un tuplu (IP, port)
        udp_send_sock.sendto(b'salut', (ip, port))

        # asteapta un mesaj ICMP de tipul ICMP TTL exceeded messages
        # in cazul nostru nu verificăm tipul de mesaj ICMP
        # puteti verifica daca primul byte are valoarea Type == 11
        # https://tools.ietf.org/html/rfc792#page-5
        # https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Header
        addr = 'done!'
        try:
            data, addr = icmp_recv_socket.recvfrom(63535)
        except Exception as e:
            print("Socket timeout ", str(e))
            break
        print(addr[0])
        info_about_ip(addr[0]) # addr[0] = IP, addr[1] = PORT
        TTL += 1

'''
 Exercitiu hackney carriage (optional)!
    e posibil ca ipinfo sa raspunda cu status code 429 Too Many Requests
    cititi despre campul X-Forwarded-For din antetul HTTP
        https://www.nginx.com/resources/wiki/start/topics/examples/forwarded/
    si setati-l o valoare in asa fel incat
    sa puteti trece peste sistemul care limiteaza numarul de cereri/zi

    Alternativ, puteti folosi ip-api (documentatie: https://ip-api.com/docs/api:json).
    Acesta permite trimiterea a 45 de query-uri de geolocare pe minut.
'''

# exemplu de request la IP info pentru a
# obtine informatii despre localizarea unui IP
fake_HTTP_header = {
                    'referer': 'https://ipinfo.io/',
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
                   }
port = 12230
for site in list_of_sites:
    print("New site:")
    traceroute(site, port)
    
