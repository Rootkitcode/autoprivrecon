# modules/suid.py

import subprocess
from rich.console import Console

console = Console()

KNOWN_SUID_ESCAPES = [
    "/usr/bin/find",
    "/usr/bin/vim",
    "/usr/bin/nmap",
    "/usr/bin/perl",
    "/usr/bin/python",
    "/usr/bin/python3",
    "/usr/bin/less",
    "/usr/bin/bash",
    "/usr/bin/awk"
]

def find_suid_binaries():
    try:
        result = subprocess.run(["find", "/", "-perm", "/4000", "-type", "f", "2>/dev/null"], capture_output=True, text=True, shell=True)
        binaries = result.stdout.strip().split("\n")
        suid_matches = [b for b in binaries if any(escape in b for escape in KNOWN_SUID_ESCAPES)]

        console.print("[bold cyan]SUID Binaries Found:[/bold cyan]")
        for b in binaries:
            console.print(b)

        return {
            "all_suid_binaries": binaries,
            "possible_escapes": suid_matches if suid_matches else ["No known SUID escape binaries found"]
        }
    except Exception as e:
        console.print(f"[red]Error finding SUID binaries: {e}[/red]")
        return {}