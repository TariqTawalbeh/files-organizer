import os
import shutil
import argparse
import FileCopier
import FileNameParser

def main():
    parser = argparse.ArgumentParser(description="Copy text files to language subfolders")
    parser.add_argument("input_path", help="Input directory path")
    parser.add_argument("output_path", help="Output directory path")
    parser.add_argument('-e', '--extension', type=str, default=".txt", help='the File Extension to Process')
    parser.add_argument("-s", "--separator", type=str, default="-", help="Separator Between the Files Names and their Sequence Number")
    args = parser.parse_args()

    file_copier = FileCopier.FileCopier(args.input_path, args.output_path, args.extension, args.separator)
    file_copier.copy_files_to_language_folders()

if __name__ == "__main__":
    main()
