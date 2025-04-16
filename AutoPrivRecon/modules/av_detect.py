# modules/av_detect.py

import subprocess
from rich.console import Console

console = Console()

def detect_av():
    try:
        processes = subprocess.run(["ps", "aux"], capture_output=True, text=True).stdout.lower()
        av_signatures = ["clamav", "eset", "bitdefender", "sophos", "defender", "avast", "avg", "kaspersky", "crowdstrike", "falcon", "carbonblack"]
        detected = [av for av in av_signatures if av in processes]

        apparmor_status = subprocess.run(["aa-status"], capture_output=True, text=True).stdout.strip()
        selinux_status = subprocess.run(["getenforce"], capture_output=True, text=True).stdout.strip()

        console.print("[bold cyan]AV/EDR and Protection Detection:[/bold cyan]")
        if detected:
            for av in detected:
                console.print(f"Detected: {av}")
        else:
            console.print("No known AV/EDR processes found.")

        console.print(f"AppArmor Status: {apparmor_status}")
        console.print(f"SELinux Status: {selinux_status}")

        return {
            "av_processes": detected if detected else ["None detected"],
            "apparmor_status": apparmor_status,
            "selinux_status": selinux_status
        }
    except Exception as e:
        console.print(f"[red]Error detecting AV/EDR or protections: {e}[/red]")
        return {}
