import os

class FileNameParser:
    def __init__(self, extension=".txt", separator="-"):
        self.separator = separator
        self.extension = extension

    def parse(self, filename):        
        filename_parts = os.path.splitext(filename)[0].split(self.separator)
        return filename_parts[0], filename_parts[1]

    def validate_file_name(self, filename):
        if not filename.endswith(self.extension):
            return False

        if self.separator not in filename:
            return False

        return True