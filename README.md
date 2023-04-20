# Text_Search_Engine

This is a command line-driven Text Search Engine, in which you need to give a path to some directory that contains text files during running the program. After running the program you will get the information about how many text files it read from that directory and then it asks for search>. When you give some words to search and press enter it will give you the information about the matching percentage of search words in each file. Data equality in this program is based on same spelling(case in sensitive).

## Instruction for Installation of python and required packages
Installation on mac terminal or VScode terminal

```bash
  1 - Python should be installed on your system. For Installation visit [Python Installation](https://www.python.org/downloads/)
  2 - pip3 install pipenv
  3 - pipenv install

```

Installation in Windows powershell or VScode terminal

```bash
1 - 1 - Python should be installed on your system. For Installation visit [Python Installation](https://www.python.org/downloads/)
2 - pip install pipenv
3 - pipenv install
```

## Instructions for running the project

1 - Unzip the project folder(text_search_engine) if you have zip folder .If you cloned from github then start skip this step. 
2 - Open the folder in vscode or you can open it in powershell or command line as well  
3 - Run pipenv install on vscode terminal to install the requirements and create a virtual environment  
4 - Then run pipenv shell to run the virtual environment  
5 - After this, you need to run the python main.py file to run the program and provide the complete directory path which contains text files e.g (python main.py C:\Users\mzain\OneDrive\Desktop\text_files )  
6 - You need to use python3 if you are on mac to run the python file

## After running the program

1 - Then you will get total number of files read in this directory and see a search> input where you can enter words you want to search
2 - After this, you will get a list of the top 10 (max) matching filenames in rank order, giving the rank score against each match  
3 - After the result you will see the search> option again and you can do another search by giving new input  
4 - You can do search until you provide quit or exit as input  
5 - After exit the program will stop

## Features

- Read text files from any directory
- Search text to check the availability of search words in textfiles
- Give a list of the top 10 matching filenames in rank order
- Currently, the word equality is based on spelling check but in the future we can also make it context or meaning-based

## Running Tests

To run tests, run the following command

```bash
  python test_main.py
```
