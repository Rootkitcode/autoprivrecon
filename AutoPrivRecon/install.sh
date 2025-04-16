#!/bin/bash

echo "[*] Installing AutoPrivRecon..."

# Crear entorno de instalación
pip install .

# Crear alias global en /usr/local/bin
if [ -f "autoprivrecon.py" ]; then
    chmod +x autoprivrecon.py
    ln -sf "$(pwd)/autoprivrecon.py" /usr/local/bin/autoprivrecon
    echo "[+] Linked autoprivrecon to /usr/local/bin"
fi

# Crear directorio de salida si no existe
mkdir -p output

echo "[✓] Installation complete. Run with: autoprivrecon --help"
