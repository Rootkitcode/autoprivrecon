# modules/bypass_suggester.py

def suggest(data):
    suggestions = []

    # Check for sudo escapes
    if data.get("sudo"):
        for escape in data["sudo"].get("escape_suggestions", []):
            suggestions.append(f"Potential sudo escape: {escape}")

    # Check SUID binaries
    if data.get("suid"):
        for binary in data["suid"].get("possible_escapes", []):
            if "No known" not in binary:
                suggestions.append(f"Check SUID binary for escape: {binary}")

    # Check capabilities
    if data.get("capabilities"):
        for cap in data["capabilities"].get("dangerous_capabilities", []):
            suggestions.append(f"Dangerous capability detected: {cap}")

    # Check AV protections
    if data.get("av"):
        avs = data["av"].get("av_processes", [])
        if avs and avs[0] != "None detected":
            suggestions.append(f"AV/EDR present: {', '.join(avs)} - consider evasion techniques")
        if "enforce" in data["av"].get("selinux_status", "").lower():
            suggestions.append("SELinux is enforcing - consider bypass strategies")
        if "enabled" in data["av"].get("apparmor_status", "").lower():
            suggestions.append("AppArmor is enabled - consider container escape or LSM bypass")

    return suggestions if suggestions else ["No bypass techniques suggested from current data"]