# File Input/Output
### Oliver Keen  
### 12/8/2020

## Background
This script demonstrates a basic understanding of file input and output, which I had no prior experience with in Python before its implementation. My code utilizes command line input and exception handling for the provided arguments.

## System Requirements
[Python 3](https://www.python.org/downloads)

## Installation
Installing this program on your machine is as simple as downloading and unzipping the necessary files. Click **Code**, then **Download ZIP**, and then extract the files to your desired location.

## Usage
`fileio.py input_file [output_file] [--append (-a)]`

# Example Usage
1. Using terminal, navigate to the location you extracted the files to. The directory should currently contain the following files:
    ```
    data1.txt
    data2.txt
    fileio.py
    README.md
    ```

2. The first functionality of this script is effectively the **cat** command; print the contents of **data1.txt** to terminal with the following command:  
`$ python3 fileio.py data1.txt`

3. So far, the files are unchanged. This time, write the contents of **data1.txt** to a new file called **all_data.txt** by entering an additional argument:  
`$ python3 fileio.py data1.txt all_data.txt`
    ```
    all_data.txt
    data1.txt
    data2.txt
    fileio.py
    README.md
    ```

4. To confirm, print the contents of the new file to terminal (refer to step two). Keep in mind, the new file was created because **all_data.txt** did not already exist in the current directory. Otherwise, if an `output_file` already exists, then this command overwrites any of its existing content (be careful).

5. I implemented additional functionality that provides the option to keep an output file intact (and not overwrite its contents). Append the contents of **data2.txt** to the file **all_data.txt** with one of the following commands (they are equivalent):  
`$ python3 fileio.py data2.txt all_data.txt --append`  
`$ python3 fileio.py data2.txt all_data.txt -a`

6. Now **all_data.txt** contains the combined contents of **data1.txt** and **data2.txt**, which you can confirm by simply opening and viewing the file in any text editor, or by printing its contents to terminal:  
`$ python3 fileio.py all_data.txt`  
`$ cat all_data.txt`