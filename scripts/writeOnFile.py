import os
import sys
from datetime import datetime
import time

def write_on_file(fileName):
    iteration = 11
    iter_count = 1
    while iter_count < iteration:
        text = "Test "+ str(iter_count)
        time_and_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_text = f"{time_and_date}: {text}"
        if os.path.exists(tmp_dir):
            with open(fileName, 'a') as file:
                file.write(formatted_text + '\n') 
        else:    
            with open(fileName, 'w') as file:
                file.write(formatted_text + '\n')
        iter_count += 1
        time.sleep(1)
   


tmp_dir = "tmp"
if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir, exist_ok=True)

path_to_file = os.path.join(tmp_dir, "test.txt")
write_on_file(path_to_file)
