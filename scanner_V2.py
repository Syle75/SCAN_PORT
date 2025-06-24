# Scanner de ports TCP amélioré (avec options et multi-thread)


import socket
import sys
import threading
import argparse
from queue import Queue
from datetime import datetime

# Liste des ports ouverts (partagée entre les threads)
open_ports = []
lock = threading.Lock()

# -----------------------------
# Fonction : Scan d'un port unique
# -----------------------------
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Timeout réduit pour plus de rapidité
        result = s.connect_ex((ip, port))
        if result == 0:
            with lock:
                open_ports.append(port)
            print(f"[+] Port {port} ouvert")
        s.close()
    except Exception as e:
        print(f"[-] Erreur sur le port {port} : {e}")

# -----------------------------
# Fonction : Scan de toutes les IP sur un réseau local donné
# -----------------------------
def scan_lan(base_ip):
    print(f"\n Scan du réseau local {base_ip}.0/24 en cours...\n")
    active_hosts = []
    def ping_host(i):
        ip = f"{base_ip}.{i}"
        try:
            socket.gethostbyaddr(ip)
            print(f"[+] IP active : {ip}")
            active_hosts.append(ip)
        except:
            pass

    threads = []
    for i in range(1, 255):
        t = threading.Thread(target=ping_host, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n✅ Scan du réseau local terminé.")
    if not active_hosts:
        print("Aucune machine détectée.")
    return active_hosts

# -----------------------------
# Fonction principale
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Scanner de ports TCP avancé")
    parser.add_argument("ip", help="Adresse IP à scanner ou 'local' pour scanner le réseau local")
    parser.add_argument("--start", type=int, default=1, help="Port de début (défaut: 1)")
    parser.add_argument("--end", type=int, default=1024, help="Port de fin (défaut: 1024)")
    parser.add_argument("--threads", type=int, default=50, help="Nombre de threads (défaut: 50)")
    parser.add_argument("--save", action="store_true", help="Sauvegarder les résultats dans un fichier")
    args = parser.parse_args()

    if args.ip == "local":
        base_ip = input("Entrez la base IP (ex: 192.168.1) : ").strip()
        scan_lan(base_ip)
        return

    target_ip = args.ip
    start_port = args.start
    end_port = args.end
    max_threads = args.threads

    print(f"\n🔎 Scan de ports sur {target_ip} (ports {start_port} à {end_port}) avec {max_threads} threads...\n")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

        while threading.active_count() > max_threads:
            pass

    for t in threads:
        t.join()

    print("\n✅ Scan terminé.")

    if args.save:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"scan_{target_ip}_{now}.txt"
        with open(filename, "w") as f:
            f.write(f"Résultats du scan de {target_ip} :\n")
            for p in open_ports:
                f.write(f"Port {p} ouvert\n")
        print(f"Résultats enregistrés dans {filename}")

# -----------------------------
# Lancement du script
# -----------------------------
if __name__ == "__main__":
    main()