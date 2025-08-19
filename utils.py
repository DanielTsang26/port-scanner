from rich.console import Console
from rich.spinner import Spinner
from rich.table import Table
from contextlib import contextmanager

console = Console()

@contextmanager
def scanning_spinner(port):
    spinner = Spinner("dots",text = f"[bold cyan]Scanning port in progress {port} [/bold cyan]")
    task = console.status(spinner, spinner = "dots")
    task.start()
    try:
        yield
    finally:
        task.stop()

def display_summary(total_ports, open_ports, closed_ports):
    table = Table(title="PortHound Scan Summary", title_style="bold cyan" )
    table.add_column("Total Ports",justify="center",style ="purple")
    table.add_column("Open Ports",justify="center",style ="green")
    table.add_column("Closed Ports",justify="center", style = "red")


    table.add_row(str(total_ports),str(open_ports), str(closed_ports))

    console.print(table)

def display_detailed_summary(targets,results):
       table = Table(title=f"Summary for {targets}", show_lines=True, title_style="bold cyan")
       table.add_column("Port", justify="right", style ="cyan")
       table.add_column("Status", justify="left",style="yellow")
       table.add_column("Service", justify="left", style ="purple")

       

       for port, status, service in results:
         table.add_row(port, status, service)
       
       console.print(table)
 

COMMON_PORTS = {
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH Remote Login",
    23: "Telnet Remote Login",
    25: "SMTP Email Routing",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3 Email",
    123: "NTP Time Synchronization",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP Email",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP Routing",
    443: "HTTPS Secure Web",
    445: "Microsoft-DS SMB File Sharing",
    465: "SMTPS (SMTP over SSL)",
    514: "Syslog",
    515: "LPD Printer Service",
    587: "SMTP (submission)",
    631: "IPP Internet Printing Protocol",
    993: "IMAPS (IMAP over SSL)",
    995: "POP3S (POP3 over SSL)",
    1080: "SOCKS Proxy",
    1194: "OpenVPN",
    1433: "Microsoft SQL Server",
    1521: "Oracle Database",
    1723: "PPTP VPN",
    3306: "MySQL Database",
    3389: "RDP Remote Desktop",
    5060: "SIP (VoIP Signaling)",
    5432: "PostgreSQL Database",
    5900: "VNC Remote Desktop",
    6379: "Redis Database",
    8080: "HTTP Proxy/Alternative HTTP",
    8443: "HTTPS Alternative",
}
SERVICE_VERSIONS = {
     80: {'name': 'HTTP', 'pattern': 'HTTP/'},  
    443: {'name': 'HTTPS', 'pattern': 'HTTP/'},  
    21: {'name': 'FTP', 'pattern': 'vsFTPd'},  
    22: {'name': 'SSH', 'pattern': 'SSH'},  
    25: {'name': 'SMTP', 'pattern': 'ESMTP'},  
    23: {'name': 'Telnet', 'pattern': 'Telnet'},  
    3306: {'name': 'MySQL', 'pattern': 'MySQL'},  
    5432: {'name': 'PostgreSQL', 'pattern': 'PostgreSQL'},  
}

LOG_DIR = "logs"

