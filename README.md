Scanner de Ports TCP Multithread (Python):

Ce projet est un scanner de ports TCP en ligne de commande, écrit en Python. Il permet de :

Scanner les ports d'une IP cible

Scanner toutes les adresses IP d'un sous-réseau local (/24)

Utiliser plusieurs threads pour accélérer le scan

Sauvegarder les résultats dans un fichier texte

Utilisation:

1. Scan classique d'une IP :

python3 scanner_V2.py 192.168.1.254

Par défaut, les ports scannés vont de 1 à 1024.

2. Scan d'une plage de ports personnalisée :

python3 scanner_V2.py 192.168.1.254 --start 20 --end 100

3. Spécifier le nombre de threads (ex: 100) :

python3 scanner_V2.py 192.168.1.254 --threads 100

4. Sauvegarde des résultats dans un fichier texte :

python3 scanner_V2.py 192.168.1.254 --save

5. Scan de réseau local (LAN) pour trouver les IPs actives :

python3 scanner_V2.py local

Il vous sera demandé d'entrer la base IP, ex: 192.168.1

Dépendances:

Aucune dépendance externe n'est requise (utilise uniquement la librairie standard Python).

Fonctionne avec Python 3.6+.

Structure du projet:

scanner_V2.py        # Script principal
README.md            # Ce fichier d’explication
scan_xxx.txt         # (optionnel) Fichier généré si --save est utilisé

Compétences mobilisées :

Programmation réseau (socket)

Gestion des threads

Utilisation d'argparse (CLI)

Analyse de port et reconnaissance

Scan de réseau local basique



Projet pédagogique pour découverte de la cybersécurité et du réseau.


