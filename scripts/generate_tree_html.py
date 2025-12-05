
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askdirectory

#Pick directory to generate tree from

class HtmlTreeGenerator:
    def __init__(self, root_directory, html_header = None, background_color="#111111", text_color="#FFFFFF"):
        self.root_directory = root_directory
        self.html_header = html_header
        self.html_file_output = open("../generated/treeview_output.html", "w+")
        if self.html_header is None:
            header_template = open("../templates/html_tree_header.html", "r")
            self.html_file_output.write(header_template.read())
            header_template.close()
        else:
            self.html_file_output.write(self.html_header)
        self.html_file_output.write(f'<body style="background-color: {background_color}; color: {text_color};">\n')



        self.all_files = {}
        
        self.get_all_files_in_dir(self.root_directory)
    
    def get_all_files_in_dir(self, current_dir):
        for path in Path(current_dir).rglob('*'):
            if path.is_file():
                relative_path_string = str(path.relative_to(root_directory))
                #relative_path_string = relative_path_string.replace(' ', '\ ')
                if path.suffix == '.md':
                   self.all_files[path.stem] = relative_path_string
                else:
                    self.all_files[path.name] = relative_path_string
            if path.is_dir():
                self.get_all_files_in_dir(path)



if __name__ == "__main__":
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    directory = askdirectory() # show an "Open" dialog box and return the path to the selected directory
    print(directory)
    root_directory = Path(directory)
    generator = HtmlTreeGenerator(root_directory)
    
