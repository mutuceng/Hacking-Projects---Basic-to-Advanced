# Network Scanner README
* This Python script is used to scan devices on a network and obtain their IP and MAC addresses. It utilizes the scapy library.

## Usage
Firstly, you might want to install scapy library if you haven't done yet.
Open your terminal and write ```pip install scopy```. Once the installation is complete, you're ready to use the script. 


Do these steps in your terminal:
*Navigate to the directory where the netScanner.py script is located using the cd command.
*Run the script by entering the following command: ```python network_scanner.py -i "ip_address" ```

> **Uyarı:** if you run only ```python network_scanner.py``` , you wont be able to see IP and MAC Addresses. So be sure  to include the "-i" flag followed by an IP Address