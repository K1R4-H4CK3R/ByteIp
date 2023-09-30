import socket

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

# Chamada para imprimir o banner
print(create_banner())

# Captura de IP
def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return "\033[91m" + "𝐍𝐚̃𝐨 𝐟𝐨𝐢 𝐩𝐨𝐬𝐬𝐢𝐯𝐞𝐥 𝐨𝐛𝐭𝐞𝐫 𝐨 𝐢𝐧𝐝𝐞𝐫𝐞𝐜̧𝐨 𝐢𝐩 𝐝𝐞𝐬𝐭𝐞 𝐬𝐢𝐭𝐞." + "\033[0m"

url = input("\033[91m" + "𝐃𝐢𝐠𝐢𝐭𝐞 𝐚 𝐮𝐫𝐥 𝐝𝐨 𝐬𝐢𝐭𝐞: " + "\033[0m")
ip = get_ip_address(url)
print("\n\033[91m" + "𝐎 𝐢𝐧𝐝𝐞𝐫𝐞𝐜̧𝐨 𝐢𝐩 𝐝𝐨 𝐬𝐢𝐭𝐞", url, "𝐞́:", ip + "\033[0m")
print("\n\033[91m" + "𝐎𝐛𝐫𝐢𝐠𝐚𝐝𝐨 𝐏𝐨𝐫 𝐔𝐬𝐚𝐫 𝐄𝐬𝐭𝐞 𝐒𝐜𝐫𝐢𝐩𝐭!" + "\033[0m")