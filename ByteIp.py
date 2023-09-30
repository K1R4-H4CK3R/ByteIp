import socket
import subprocess
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
        return "\033[91m" + "Não foi possível obter o endereço IP do destino." + "\033[0m"

def scan_ports(ip):
    open_ports = []
    try:
        nm = nmap.PortScanner()
        nm.scan(ip, arguments='-p-')  # Scan all ports
        for protocol in nm[ip].all_protocols():
            for port in nm[ip][protocol]:
                state = nm[ip][protocol][port]['state']
                if state == 'open':
                    open_ports.append(port)
        return open_ports
    except nmap.nmap.PortScannerError as e:
        return "\033[91m" + f"Erro ao escanear as portas: {str(e)}" + "\033[0m"

def find_vulnerabilities(ip):
    try:
        # Usando openvas-cli para buscar vulnerabilidades
        cmd = f"openvas-cli --target {ip} --get-users"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            vulnerabilities = result.stdout
            return "\n\033[91m" + "Vulnerabilidades encontradas:\n" + vulnerabilities + "\033[0m"
        else:
            error_message = result.stderr
            return "\033[91m" + "Erro ao buscar vulnerabilidades:\n" + error_message + "\033[0m"

    except Exception as e:
        return "\033[91m" + f"Erro ao buscar vulnerabilidades: {str(e)}" + "\033[0m"
        
print(create_banner())

url = input("\033[91m" + "Digite o URL do site: " + "\033[0m")
ip = get_ip_address(url)

print("\n\033[91m" + "O endereço IP do site", url, "é:", ip + "\033[0m")

# Verificar portas abertas
open_ports = scan_ports(ip)
if isinstance(open_ports, list):
    print("\n\033[91m" + "Portas abertas:", open_ports, "\033[0m")
else:
    print(open_ports)

# Buscar vulnerabilidades
print(find_vulnerabilities(ip))

print("\n\033[91m" + "Obrigado Por Usar Este Script!" + "\033[0m")
