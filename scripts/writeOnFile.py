import os
import sys
from datetime import datetime
import time

def write_on_file(file_path):
    iteration = 11
    iter_count = 1
    while iter_count < iteration:
        text = "Test "+ str(iter_count)
        time_and_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_text = f"{time_and_date}: {text}"

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if os.path.exists(file_path):
            with open(file_path, 'a') as file:
                file.write(formatted_text + '\n') 
        else:    
            with open(file_path, 'w') as file:
                file.write(formatted_text + '\n')
        iter_count += 1
        time.sleep(1)
   
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]
    write_on_file(path_to_file)
####
'''tmp_dir = "tmp"
if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir, exist_ok=True)

path_to_file = os.path.join(tmp_dir, "test.txt")
write_on_file(path_to_file)'''
