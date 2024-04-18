import subprocess
import optparse
import re
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")

    return parse_object.parse_args()


def macChanger(interface,mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

def changeControl(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])

    #using regex to find mac adress on ifconfig
    new_mac =  re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None


print("DEĞİŞİM BAŞLADI")

(user_inputs,arguments) = get_user_input()
macChanger(user_inputs.interface,user_inputs.mac_address)

finalizedMac = changeControl(user_inputs.interface)
if finalizedMac == user_inputs.mac_address:
    print("BAŞARILI")
else:
    print("HATALI")