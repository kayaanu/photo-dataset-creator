import os
import re

def rename_files(directory):
    # Ensure directory exists
    if not os.path.exists(directory):
        print("ERR: Directory does not exist.")
        return
    
    for filename in os.listdir(directory):
        match = re.match(r"(.*?)(\d+)(\.\w+)", filename)
        if match:
            base, num, ext = match.groups()
            new_num = int(num) + 50
            new_filename = f"{base}{new_num:03d}{ext}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
    
    print("Renaming complete.")

if __name__ == "__main__":
    directory = input("Image directory: ")
    rename_files(directory)
