#!/usr/bin/env python3

import argparse
import os
import sys
from rich.Console import Console
from rich.Panel import Panel
from modules import (
    kernel, sudo, suid, capabilities, av_detect, ssh_connector, bypass_suggester
)

console = Console()
results = {}

def banner():
    console.print(Panel.fit(
        "[bold cyan]AutoPrivRecon[/bold cyan] - Automated Privilege Escalation & Bypass Recon Tool\n"
        "Author: @DarwinTusarma & @R4c0d3\n", title="AutoPrivRecon", subtitle="v1.0", style="bold green")
    )

def scan_local():
    banner()
    console.print("[yellow]Running local privilege escalation recon...[/yellow]")
    results['kernel'] = kernel.check_kernel()
    results['sudo'] = sudo.check_sudo()
    results['suid'] = suid.find_suid_binaries()
    results['capabilities'] = capabilities.get_capabilities()
    results['av'] = av_detect.detect_av()
    results['bypass'] = bypass_suggester.suggest(results)
    return results

def scan_ssh(ip, user):
    banner()
    console.print(f"[yellow]Connecting to SSH: {user}@{ip}[/yellow]")
    ssh_connector.connect_and_scan(ip, user)

def export_report():
    from utils.exporter import export    (results)
    console.print("[green]Report exported successfully![/green]")

def main():
    parser = argparse.ArgumentParser(
        description="AutoPrivRecon - Automated Privilege Escalation & Bypass Recon Tool",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--scan-local", action="store_true", help="Run recon on local system")
    parser.add_argument("--scan-ssh", nargs=2, metavar=('IP', 'USER'), help="Run recon on remote SSH host")
    parser.add_argument("--export-report", action="store_true", help="Export findings to files")
    parser.add_argument("--help", "-h", action="help", help="Show help")

    args = parser.parse_args()

    if args.scan_local:
        scan_local()

    elif args.scan_ssh:
        ip, user = args.scan_ssh
        scan_ssh(ip, user)

    if args.export_report:
        export_report()

    if not (args.scan_local or args.scan_ssh):
        parser.print_help()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user[/red]")
        sys.exit(1)
