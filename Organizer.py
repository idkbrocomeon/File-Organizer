import flet as ft
import os
import shutil

#Folder information :)
folder_documents_name = "Documents"
folder_images_name = "Images"
source_folder = os.path.dirname(os.path.abspath(__file__))
documents_destination_folder = os.path.join(source_folder, folder_documents_name)
images_destination_folder = os.path.join(source_folder, folder_images_name)

#Extension information :)
image_extensions = {
    ".bmp", ".gif", ".heic", ".heif", ".ico", ".jpeg", ".jpg",
    ".png", ".svg", ".tif", ".tiff", ".webp",
}
document_extensions = {
    ".csv", ".doc", ".docx", ".md", ".odp", ".ods", ".odt",
    ".pdf", ".ppt", ".pptx", ".rtf", ".txt", ".xls", ".xlsx",
}

#Organizer function :)
def folder_creation(e):
    os.makedirs(documents_destination_folder, exist_ok=True)
    os.makedirs(images_destination_folder, exist_ok=True)

    with os.scandir(source_folder) as entries:
        for entry in entries:
            if (
                not entry.is_file(follow_symlinks=False)
                or os.path.abspath(entry.path) == os.path.abspath(__file__)
            ):
                continue

            extension = os.path.splitext(entry.name)[1].lower()
            if extension in image_extensions:
                destination_folder = images_destination_folder
            elif extension in document_extensions:
                destination_folder = documents_destination_folder
            else:
                continue

            destination_path = os.path.join(destination_folder, entry.name)
            if os.path.exists(destination_path):
                print(
                    f"Skipped {entry.name}: a file with that name already exists "
                    f"in {os.path.basename(destination_folder)}"
                )
                continue

            shutil.move(entry.path, destination_path)
            print(f"Moved {entry.name} to {os.path.basename(destination_folder)}")

#Flet page :)
def main(page: ft.Page):
    page.add(
        ft.Text("Put this Python file in the folder you want to organize.", size=24),#Page text
        ft.Button(content="Organize Desk", on_click=folder_creation)#Page button to run the organizer function
    )
ft.run(main) #67 lol