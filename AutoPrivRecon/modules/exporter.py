# modules/exporter.py

import json
from datetime import datetime
from rich.console import Console

console = Console()

def export(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_file = f"output/report_{timestamp}.json"
    md_file = f"output/report_{timestamp}.md"

    try:
        with open(json_file, "w") as jf:
            json.dump(data, jf, indent=4)
        console.print(f"[green]JSON report saved to {json_file}[/green]")
    except Exception as e:
        console.print(f"[red]Failed to write JSON report: {e}[/red]")

    try:
        with open(md_file, "w") as mf:
            mf.write(f"# AutoPrivRecon Report - {timestamp}\n\n")
            for section, content in data.items():
                mf.write(f"## {section}\n")
                if isinstance(content, dict):
                    for k, v in content.items():
                        mf.write(f"- **{k}**: {v}\n")
                elif isinstance(content, list):
                    for item in content:
                        mf.write(f"- {item}\n")
                else:
                    mf.write(f"{content}\n")
                mf.write("\n")
        console.print(f"[green]Markdown report saved to {md_file}[/green]")
    except Exception as e:
        console.print(f"[red]Failed to write Markdown report: {e}[/red]")