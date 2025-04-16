# modules/ssh_connector.py

import paramiko
from rich.console import Console
from modules import kernel, sudo, suid, capabilities, av_detect, bypass_suggester

console = Console()

def connect_and_scan(ip, user):
    try:
        password = input(f"Enter SSH password for {user}@{ip}: ")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=user, password=password)

        console.print(f"[bold cyan]Connected to {ip}[/bold cyan]")

        # TODO: Replace this with modular remote scan logic (via uploaded script or inline commands)
        stdin, stdout, stderr = ssh.exec_command("uname -a")
        kernel_info = stdout.read().decode().strip()
        console.print(f"Remote Kernel: {kernel_info}")

        # Placeholder output - future iterations could upload and execute this tool remotely
        console.print("[yellow]Remote scanning is under development. Limited output shown.[/yellow]")

        ssh.close()
    except Exception as e:
        console.print(f"[red]SSH connection failed: {e}[/red]")