from args_processor import create_parser
from handler import handle_scan
import sys
from host_discovery import discover_host
from rich.console import Console
from os_detection import detect_os


console = Console()

def main():
    parser = create_parser()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    
    args = parser.parse_args()
    

    
    if args.host_discovery:
        console.print("[bold yellow]Host Discovery initiated...[/bold yellow]")
        live_hosts = discover_host(args.target)
        if live_hosts:
            console.print("[bold cyan][+] Live host discovered [/bold cyan]")
        for host in live_hosts:
            console.print(f"[bold cyan][+] {host} [/bold cyan]")
    else:
        console.print("[bold red] No host was found...[/bold red]")
        

       
    proceed = input("Do you want to continue with port scanning on these hosts? (y/n): ")
    if proceed.lower() != 'y':
        console.print("[bold red]Exiting...[/bold red]")
        sys.exit(0)

    if args.os:
            console.print("[bold purple]Attempting OS detection for discovered hosts...[/bold purple]")
            for host in live_hosts:
                os_guess = detect_os(host)
                console.print(f"[bold purple][+]{host} likely running: {os_guess}")
    else:
        console.print(f"[bold red]Error: No host was discovered...OS detection failed.")
        

    if not args.target or not args.ports:
         console.print("[bold red] --target or --port are only required unless --history is in use [/bold red]")
         parser.print_help()
         sys.exit(1)
        
       

        
      
        
    handle_scan(args)

if __name__ == "__main__":
    main()