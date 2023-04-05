# Copy Text Files to Language Subfolders

This script is used to copy text files to subfolders based on their language. The script takes a directory containing text files as input, then creates subfolders based on the language of the files and copies them to your output directory each with appropriate subfolder.
The files names in the format [language]-[number].txt, for example: arabic-55.txt

## Usage

To use this script, you can run it from the command line with the following arguments:

`python main.py <input_path> <output_path> [-e EXTENSION] [-s SEPARATOR]`


- `input_path`: Path to the input directory containing text files.
- `output_path`: Path to the output directory where the files will be copied to.
- `-e`, `--extension`: File extension to process, default is `.txt`.
- `-s`, `--separator`: Separator between the files names and their sequence number, default is `-`.

For example:

`python main.py /path/to/input/dir /path/to/output/dir -e .txt -s -`


## Installation

1. Install Python (the installation instructions depend on your OS), You can download the latest version of Python from the official website: https://www.python.org/downloads/
2. Clone the repository: `git clone https://github.com/TariqTawalbeh/files-organizer.git`



3. Navigate to the cloned directory: `cd your_repository`



4. if any issues happend on main, please check the dev branch: `git checkout dev`

## Requirements
This script requires Python 3.x and does not use any external libraries.