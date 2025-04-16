# modules/capabilities.py

import subprocess
from rich.console import Console

console = Console()

DANGEROUS_CAPS = ["cap_setuid", "cap_setgid", "cap_sys_admin", "cap_dac_override"]

def get_capabilities():
    try:
        result = subprocess.run(["getcap", "-r", "/"], capture_output=True, text=True)
        lines = result.stdout.strip().split("\n")
        flagged = [line for line in lines if any(cap in line for cap in DANGEROUS_CAPS)]

        console.print("[bold cyan]Dangerous Capabilities Detected:[/bold cyan]")
        for line in flagged:
            console.print(line)

        return {
            "all_capabilities": lines,
            "dangerous_capabilities": flagged if flagged else ["No dangerous capabilities found"]
        }
    except Exception as e:
        console.print(f"[red]Error checking capabilities: {e}[/red]")
        return {}