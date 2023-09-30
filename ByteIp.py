import socket
import nmap  # Install this using pip: pip install python-nmap

def create_banner():
    banner = "\033[91m" + r"""
BBBBB   y   y  ttttt  eeeee  III  PPP
B    B   y y     t    e      I   P  P
BBBBB     y      t    eeee   I   PPP
B    B    y      t    e      I   P
BBBBB     y      t    eeeee III  P

𝐁𝐲:𝕶𝖎𝖗𝖆𝕭𝖞𝖙𝖊.𝖕𝖞/𝐊𝐢𝐫𝐚𝐛𝐲𝐭𝐞.𝐩𝐲
    """ + "\033[0m"
    return banner

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return "\033[91m" + "𝐍𝐚̃𝐨 𝐟𝐨𝐢 𝐩𝐨𝐬𝐬𝐢𝐯𝐞𝐥 𝐨𝐛𝐭𝐞𝐫 𝐨 𝐢𝐧𝐝𝐞𝐫𝐞𝐜̧𝐨 𝐢𝐩 𝐝𝐞𝐬𝐭𝐞 𝐬𝐢𝐭𝐞." + "\033[0m"

def scan_ports(ip):
    open_ports = []
    try:
        nm = nmap.PortScanner()
        nm.scan(ip, arguments='-p-')  # Scan all ports
        for port in nm[ip]['tcp'].keys():
            if nm[ip]['tcp'][port]['state'] == 'open':
                open_ports.append(port)
        return open_ports
    except nmap.NmapError:
        return "\033[91m" + "Erro ao escanear as portas." + "\033[0m"

def find_vulnerabilities(ip):
    # Implement vulnerability scanning logic here
    # This could involve using tools like Nessus, OpenVAS, or custom vulnerability checks
    return "\033[91m" + "Função de busca de vulnerabilidades não implementada." + "\033[0m"

# Chamada para imprimir o banner
print(create_banner())

url = input("\033[91m" + "𝐃𝐢𝐠𝐢𝐭𝐞 𝐚 𝐮𝐫𝐥 𝐝𝐨 𝐬𝐢𝐭𝐞: " + "\033[0m")
ip = get_ip_address(url)

print("\n\033[91m" + "𝐎 𝐢𝐧𝐝𝐞𝐫𝐞𝐜̧𝐨 𝐢𝐩 𝐝𝐨 𝐬𝐢𝐭𝐞", url, "𝐞́:", ip + "\033[0m")

# Verificar portas abertas
open_ports = scan_ports(ip)
if isinstance(open_ports, list):
    print("\n\033[91m" + "Portas abertas:", open_ports, "\033[0m")
else:
    print(open_ports)

# Buscar vulnerabilidades
print(find_vulnerabilities(ip))

print("\n\033[91m" + "𝐎𝐛𝐫𝐢𝐠𝐚𝐝𝐨 𝐏𝐨𝐫 𝐔𝐬𝐚𝐫 𝐄𝐬𝐭𝐞 𝐒𝐜𝐫𝐢𝐩𝐭!" + "\033[0m")