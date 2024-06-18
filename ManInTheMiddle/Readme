# ARP Poisoning Tool
* This Python script is used to perform ARP poisoning attack. This attack allows a attacker to intercept network traffic by deceiving target devices on a network, enabling the attacker to eavesdrop on and manipulate network communication. Additionally, it provides a rollback operation to reconfigure ARP tables of devices on the network after the attack.

## Usage

* Firstly, you might want to install scapy library if you haven't done yet.
Open your terminal and write ```pip install scopy```. Once the installation is complete, you're ready to use the script. 

* To use to script write ```python arp_poisoning.py -t <target_ip_address> -g <gateway_ip_address>```
```<target_ip_address>```: Specifies the IP address of the target device to be victimized by the attack.
```<gateway_ip_address>```: Specifies the IP address of the gateway on the network.

### Example:

```python arp_poisoning.py -t 192.168.1.100 -g 192.168.1.1```

* Once the program is running, ARP poisoning attack will commence, manipulating the communication between the specified target device and the gateway.
* While the attack is ongoing, the program will indicate the number of ARP packets sent.
* To terminate the attack, use the CTRL+C key combination. The program will stop the attack and perform the rollback operation to reconfigure ARP tables on the network devices.

## Requirements
* Python 3.x
* scapy library (installable via pip install scapy command)

## Disclaimer
**Uyarı:** This tool should only be used for educational and testing purposes. Unauthorized access to someone else's network or unauthorized interception of network traffic may be illegal. It should not be used for malicious purposes.

