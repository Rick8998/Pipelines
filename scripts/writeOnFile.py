import os
import sys
from datetime import datetime
print("TEST")
def write_on_file(text, file_path):
    time_and_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"{time_and_date}: {text}"

    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if os.path.exists(file_path):
        with open(file_path, 'a') as file:
            file.write(formatted_text)
    else:
        with open(file_path, 'w') as file:
            file.write(formatted_text)


if __name__ == "__main__":
    # Check file path
    if len(sys.argv) != 2:
        print("Usage: python script.py <percorso_del_file>")
        sys.exit(1)

    # Get file path from cmd line
    file_path = sys.argv[1]

    # Text
    text = "Test\n"

    # Chiama la funzione per scrivere sul file
    write_on_file(text, file_path)