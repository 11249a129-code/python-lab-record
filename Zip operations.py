import zipfile
import os

folder = input("Enter folder name to backup: ")
zip_name = folder + "_backup.zip"

with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as myzip:
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            myzip.write(os.path.join(foldername, filename))

print(f"Folder '{folder}' has been backed up as '{zip_name}'")
