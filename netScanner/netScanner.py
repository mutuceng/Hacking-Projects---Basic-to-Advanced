import scapy.all as scapy
import optparse


def get_user_input(): #getting user input for ip adress
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress", dest="ip_address",help="Enter IP Address")

    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP Address")

    return user_input


def scanNetwork(ip):
    arp_request_packet = scapy.ARP(pdst=ip)  #creates an ARP (Address Resolution Protocol) request packet

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #contains a broadcast address (ff:ff:ff:ff:ff:ff), which will broadcast the packet to all devices on the network.


    combined_packet = broadcast_packet / arp_request_packet # the ARP request packet and the Ethernet frame are combined to create a single packet.p

    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    # srp (Send and Receive Packets) function sends the specified packet and waits for responses.
    # timeout means how long to wait for responses before giving up
    # srp function returns 2 lists  answered_list and unanswered_list, (answered_list, unanswered_list) is used to unpack the two lists 


    answered_list.summary()  #summary of the packets in the list, displaying important information such as source and destination IP and MAC addresses


user_ip_address = get_user_input()
scanNetwork(user_ip_address.ip_address)