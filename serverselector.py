import os
from colorama import init, Fore, Back, Style

# Inizializza colorama
init()

def modify_game_settings(region):
    user_folder = os.path.expanduser('~')
    settings_path = os.path.join(user_folder, 'Documents', 'My Games', 'Rainbow Six - Siege')
    
    # Trova la cartella con numeri casuali
    for root, dirs, files in os.walk(settings_path):
        for file in files:
            if file == 'GameSettings.ini':
                config_file_path = os.path.join(root, file)
                
                # Leggi il file di configurazione
                with open(config_file_path, 'r') as file:
                    lines = file.readlines()
                
                # Modifica la configurazione
                with open(config_file_path, 'w') as file:
                    data_center_hint_exists = False
                    for line in lines:
                        if line.startswith('DataCenterHint'):
                            file.write(f'DataCenterHint={region}\n')
                            data_center_hint_exists = True
                        else:
                            file.write(line)
                    # Aggiungi la riga se non esiste
                    if not data_center_hint_exists:
                        file.write(f'DataCenterHint={region}\n')

                print(f'Configurazione modificata per utilizzare il server {region}')
                return

    print('Impossibile trovare il file di configurazione. Assicurati che il gioco sia installato correttamente.')

def main():
    print(Fore.BLUE + "Lqnnix R6 Server Selector" + Style.RESET_ALL)
    print()
    print(Back.RED + "Scegli i server in cui ti senti più forte:" + Style.RESET_ALL)
    print()
    print(Fore.GREEN + "1. Te mato la cabeça server (south brazil)" + Style.RESET_ALL)
    print(Fore.MAGENTA + "2. Bīngqílín server (central asia)" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Vai nei server dei ruba rame e mercedesi (est europe)" + Style.RESET_ALL)
    print(Fore.CYAN + "4. Vai dove c'è sempre la neve (north europe)" + Style.RESET_ALL)
    print(Fore.RED + "5. Torna ai tuoi server default" + Style.RESET_ALL)
    print()

    scelta = input("Cosa scegli broskok? ")

    if scelta == "1":
        region = "playfab/brazilsouth"
    elif scelta == "2":
        region = "playfab/eastasia"
    elif scelta == "3":
        region = "playfab/westeurope"
    elif scelta == "4":
        region = "playfab/northeurope"
    elif scelta == "5":
        region = "default"
    else:
        print("Scelta non valida.")
        return

    modify_game_settings(region)

if __name__ == "__main__":
    main()
