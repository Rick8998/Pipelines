import os
import sys
from datetime import datetime

def write_on_file(text, fileName):
    print("TEST 1")
    time_and_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"{time_and_date}: {text}"
    print(formatted_text)
    try:
        with open(fileName, 'w') as file:
            file.write(formatted_text + '\n')
    except FileNotFoundError:
        print(f"File '{fileName}' non trovato.")
    except PermissionError:
        print(f"Permesso negato per scrivere su '{fileName}'. Assicurati di avere i permessi necessari.")


testo_da_scrivere = "Test"
path_to_file = "test.txt"
write_on_file(testo_da_scrivere, path_to_file)
