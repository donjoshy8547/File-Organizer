import os
import shutil


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".ps1"],
    "Others": []  
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            category = get_category(ext)

            
            target_dir = os.path.join(folder_path, category)
            os.makedirs(target_dir, exist_ok=True)

           
            target_path = os.path.join(target_dir, filename)
            shutil.move(file_path, target_path)
            print(f"Moved: {filename} -> {category}/")

if __name__ == "__main__":
    folder_to_organize = input("Enter the full path of the folder to organize: ").strip()
    organize_folder(folder_to_organize)
