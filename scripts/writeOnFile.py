import os
import sys
from datetime import datetime

def write_on_file(text, fileName):
    time_and_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"{time_and_date}: {text}"
    with open(fileName, 'w') as file:
            file.write(formatted_text + '\n')
   

testo_da_scrivere = "Test"
tmp_dir = "tmp"
if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir, exist_ok=True)

path_to_file = os.path.join(tmp_dir, "test.txt")
write_on_file(testo_da_scrivere, path_to_file)
