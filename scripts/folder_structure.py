from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askdirectory





def get_all_files_in_dir(current_dir):
        for path in Path(current_dir).rglob('*'):
            if path.is_file():
                relative_path_string = str(path.relative_to(root_directory))
                #relative_path_string = relative_path_string.replace(' ', '\ ')
                if path.suffix == '.md':
                    all_files[path.stem] = relative_path_string
                else:
                    all_files[path.name] = relative_path_string
            if path.is_dir():
                get_all_files_in_dir(path)

def get_folder_structure(current_dir):
    folder_structure = []
    for path in Path(current_dir).rglob('*'):
        if path.is_dir():
            relative_path_string = str(path.relative_to(root_directory))
            folder_structure.append(relative_path_string)
    return folder_structure


def build_folder_dict(self, folder_structure):
    folder_dict = {}
    # First, build the folder tree
    for folder in folder_structure:
        parts = folder.split('/')
        current = folder_dict
        for i, part in enumerate(parts):
            if part not in current:
                current[part] = {}
            current = current[part]
    # Now, place files into the correct folders
    for file_name, rel_path in self.all_files.items():
        file_parts = Path(rel_path).parts
        # Only consider files in the folder_structure
        if len(file_parts) > 1:
            current = folder_dict
            for part in file_parts[:-1]:
                if part in current:
                    current = current[part]
                else:
                    current[part] = {}
                    current = current[part]
            current[file_name] = rel_path
        else:
            # Top-level files
            folder_dict[file_name] = rel_path
    return folder_dict


if __name__ == "__main__":
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    directory = askdirectory() # show an "Open" dialog box and return the path to the selected directory
    print(directory)
    root_directory = Path(directory)
    all_files = {}
    get_all_files_in_dir(root_directory)
    for key in all_files:
        print(f"{key}: {all_files[key]}\n")