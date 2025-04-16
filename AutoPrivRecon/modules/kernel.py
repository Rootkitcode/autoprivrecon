# modules/kernel.py

import platform
import subprocess
from rich.console import Console

console = Console()

def check_kernel():
    try:
        kernel_version = platform.uname().release
        console.print(f"[bold cyan]Kernel Version:[/bold cyan] {kernel_version}")

        # Placeholder for CVE check
        cves = find_kernel_cves(kernel_version)
        return {
            "kernel_version": kernel_version,
            "potential_cves": cves
        }
    except Exception as e:
        console.print(f"[red]Error checking kernel version: {e}[/red]")
        return {}

def find_kernel_cves(version):
    try:
        # This uses searchsploit (must be installed) to find local exploits for the kernel
        result = subprocess.run(["searchsploit", version], capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')
        matches = [line for line in lines if "linux" in line.lower() and "kernel" in line.lower()]
        return matches if matches else ["No known exploits found via searchsploit"]
    except Exception as e:
        console.print(f"[red]Error finding kernel CVEs: {e}[/red]")
        return ["searchsploit not available or failed"]
