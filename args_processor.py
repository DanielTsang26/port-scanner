import argparse
from rich_argparse import RichHelpFormatter


def create_parser():
    

    parser = argparse.ArgumentParser(
        description=f"[bold cyan]PORTHOUND[/bold cyan]\n [bold blue]--A light-weight Port Scanner. [/bold blue]",
        formatter_class=RichHelpFormatter)
    parser.add_argument("--host-discovery", action = "store_true", help = "[bold yellow] Enable host discovery mode (ping sweep) [/bold yellow]")
    parser.add_argument("--target",required =True ,help = "[bold yellow]Target IP address or host name [/bold yellow]")
    parser.add_argument("--ports", required =True, help = " [bold yellow] Port Range (e.g. 20,80, 443, or 20-25) [/bold yellow]")
    parser.add_argument("--stealth", action="store_true", help = "[bold yellow]Enable stealth scan mode (random time intervals) [/bold yellow]")
    parser.add_argument("--timeout", type= float, help = "[bold yellow]Custom timeout per port [/bold yellow]")
    parser.add_argument('--detailed', action="store_true", help="[bold yellow]Show a detailed summary with each port result [/bold yellow]")
    parser.add_argument("--overview", action="store_true", help="[bold yellow]Show a overview summary  of port results[/bold yellow]")
    parser.add_argument("--os", action="store_true", help="[bold yellow]Sample command for operating system detection (this is to not violet any CFAA law)[/bold yellow]")
   
    return parser