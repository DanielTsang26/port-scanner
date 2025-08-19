from run_and_parse import run_scanner, parse_port
from scanner import calculate_timeout


def handle_scan(args):
    ports = parse_port(args.ports)
    timeout = args.timeout if args.timeout else calculate_timeout(len(ports))
    run_scanner(args.target, ports, stealth=args.stealth, timeout = timeout,show_detail=args.detailed, show_overview=args.overview)
