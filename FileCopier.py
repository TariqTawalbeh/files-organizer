import os
import shutil
import FileNameParser

class FileCopier:
    def __init__(self, input_dir_path, output_dir_path, extension, separator):
        self.input_dir_path = input_dir_path
        self.output_dir_path = output_dir_path
        self.parser = FileNameParser.FileNameParser(extension, separator)

    def copy_files_to_language_folders(self):
        """
        classify the files into sub-directories based on their language prefex
        the files to be processed based on the extension and separator between language and sequence number
        by default the name of the files in this structure [lang]-[num].txt
        """
        buffer_size = 8192 # Set buffer size to 8KB
        counter = 0
        
        for root, dirs, files in os.walk(self.input_dir_path):
            for filename in files:
                if self.parser.validate_file_name(filename):
                    file_path = os.path.join(root, filename)
                    with open(file_path, "rb", buffering=buffer_size) as src_file:
                        language, number = self.parser.parse(filename)
                        language_dir_path = os.path.join(self.output_dir_path, language)
                        os.makedirs(language_dir_path, exist_ok=True)
                        dst_file_path = os.path.join(language_dir_path, f"{language}-{number}.{self.parser.extension}")
                        with open(dst_file_path, "wb", buffering=buffer_size) as dst_file:
                            shutil.copyfileobj(src_file, dst_file, length=buffer_size)
                        counter += 1
                        print(f"{counter}-Copied {filename} to {language_dir_path}")