import socket
from utils import SERVICE_VERSIONS
from logger import setup_logger

logger = setup_logger("PortHoundLogger")

def scan_port(target, port, timeout=1):
    try:
        soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        soc.settimeout(timeout)
        result = soc.connect_ex((target,port))
        soc.close()
        if result == 0:
            logger.info(f"[+] Port {port} is OPEN on {target}")
            return True
        else:
            logger.info(f"[-] Port {port} is CLOSED on {target}")
            return False

    except Exception as e:
        logger.error(f"[!] Exception scanning port {port} on {target}: {e}")
        return False
    
def calculate_timeout(port_counter):

    if port_counter <= 100:
        return 0.5
    elif port_counter <= 1000:
        return 1
    else:
        return 2

def get_banner(target, port, timeout=1):
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(timeout)
        soc.connect((target,port))
        banner = soc.recv(1024).decode(errors = "ignore").strip()
        soc.close()
        
        if not banner:
            return None
        
        if port in SERVICE_VERSIONS:
            service =  SERVICE_VERSIONS[port]
            if service['pattern'] in banner:
                version = banner.split(service['pattern'])[1].strip()
                return f"{service['name']} {version}"

        return banner
    except Exception:
       return None

