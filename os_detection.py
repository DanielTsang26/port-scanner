
import platform
import re
import subprocess
from rich.console import Console

console = Console()

def detect_os(ip):
    try:
        response = subprocess.check_output(
            ["ping", "-c", "1", ip] if platform.system().lower() != "windows" else ["ping", "-n", "1", ip],
            stderr=subprocess.DEVNULL
        )
        response = response.decode()

        ttl_match = re.search(r'ttl[=|:](\d+)', response, re.IGNORECASE)

        if ttl_match:
            ttl_value = int(ttl_match.group(1))
            if ttl_value <= 64:
                return "Linux/Unix"
            elif ttl_value <= 128:
                return "Windows"
            elif ttl_value <= 255:
                return "Network Device (Router/Switch)"
            else:
                return "Unknown"
        else:
            return "Unknown (No TTL info found)"
    except Exception as e:
        return f"Unknown (Error: {e})"


