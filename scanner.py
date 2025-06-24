import socket
import sys

# -----------------------------
# Fonction : Scan d'un port unique
# -----------------------------
def scan_port(ip, port): #Test un seul port TCP pour voir s'il est ouvert ou non
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Création d'une socket TCP IPv4
        s.settimeout(1)  # Timeout de 1 seconde. Si ne répond pas dans ce délai, on considère que c'est un échec
        result = s.connect_ex((ip, port))  # connect_ex() essaye de se connecter à ip:port
        if result == 0: # Connexion réussi si 0
            print(f"[+] Port {port} ouvert")
        s.close() #On ferme une fois la verification fini
    except Exception as e: # Sinon erreur
        print(f"[-] Erreur sur le port {port} : {e}")

# -----------------------------
# Fonction principale
# -----------------------------
def main():
    if len(sys.argv) != 2: #Vérifie que l'utilisateur à bien fourni un IP en arugment
        print("Usage : python scanner.py <IP>")
        sys.exit(1)

    target_ip = sys.argv[1]
    print(f"\n🔎 Scan de ports sur {target_ip} (ports 1 à 1024)...\n")

    for port in range(1, 1025):  # Ports standards de 1 à 1024
        print(f"[~] Test du port {port}...", end='\\r')
        scan_port(target_ip, port)

    print("\n✅ Scan terminé.")

# -----------------------------
# Lancement du script
# -----------------------------
if __name__ == "__main__":
    main()