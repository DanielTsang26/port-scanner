from stealth import stealth_delay
from scanner import scan_port
from  scanner import get_banner
from logger import setup_logger
from utils import display_summary, display_detailed_summary
from rich.console import Console
from utils import scanning_spinner, COMMON_PORTS




console = Console()
logger = setup_logger("PortHoundLogger")



def run_scanner(target, ports, stealth = False, timeout=1, show_detail=False, show_overview=False, history=False):
    open_ports = 0
    closed_ports = 0
    results = []
    console.print(f"[bold purple][+] Scanning {target} ports: {ports}[/bold purple]")
    for port in ports:
        if stealth:
            stealth_delay()
        with scanning_spinner(port):
            is_open = scan_port(target, port,timeout)

        service_name = COMMON_PORTS.get(port, "Unknown service.")
        if is_open:
            open_ports += 1
            logger.info(f"Open Port: {port}({service_name})")
            console.print(f"[bold purple][+] Open Port {port} ({service_name})[/bold purple]")
            banner = get_banner(target, port)
            if banner:
                logger.info(f"Banner on port {port}: {banner}")
            results.append((str(port), "[green]OPEN[/green]", service_name))
        else:
            closed_ports += 1
            console.print(f"[bold red][+] Closed Port: {port}[/bold red]")
            results.append((str(port), "[red]CLOSED[/red]", service_name))
    console.print("[bold purple]\n[*] Scan complete.[/bold purple]")
  

    if show_detail:
           display_detailed_summary(target,results)

    if show_overview:
        display_summary(total_ports=len(ports), open_ports=open_ports, closed_ports=closed_ports)
    


def parse_port(port_range):
    ports = set()
    parts = port_range.split(',')

    for part in parts:
        if '-' in part:
            start, end = part.split('-')
            ports.update(range(int(start),int(end)+ 1))
        else:
            ports.add(int(part))
    return sorted(ports)
