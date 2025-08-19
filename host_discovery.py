import subprocess
import platform
import ipaddress
from rich.console import Console

console = Console()

def is_host_up(host):
    params = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", params, "1", host]

    try:
        subprocess.check_output(command, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def discover_host(ip_range):
    alive_hosts = []

    console.print("[bold cyan][+] Host discovery in progress...[/bold cyan]")
    try:
        network = ipaddress.ip_network(ip_range, strict=False)
    except ValueError:
        console.print("[bold red][+]Invalid IP range provided.[/bold red]")
        return alive_hosts
    
    for ip in network.hosts():
        ip = str(ip)
        console.print(f"[bold cyan][*] Pinging {ip}...[/bold cyan]")


        if is_host_up(ip):
            console.print("[bold cyan][+] Host is up! [/bold cyan]")
            alive_hosts.append(ip)
        else:
            console.print(f"[bold red] Host ip {ip} is down. [/bold red]")  

    return alive_hosts   
    
