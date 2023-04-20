from pathlib import Path
import sys
import os


def read_text_files(path_dir: Path):
    '''
    Take directory path ,read the text files from it and build an in-memory representaion of the files and their content

    Parameters
    ----------
    path_dir : path
        Path of directory which contains text files

    Returns
    -------
    dict
        Returns a dictionary which contains filenames and their content 

    '''
    if not os.path.exists(path_dir):
        raise ValueError(f"{path_dir} path is not valid")

    if not os.listdir(path_dir):
        raise ValueError(f"{path_dir} directory is empty")

    total_files_data = {}
    total_files = 0

    for file in os.listdir(path_dir):
        if file.endswith(".txt"):
            total_files += 1
            with open(os.path.join(path_dir, file)) as f:
                total_files_data[file] = f.read()

    print(f"{total_files} files read in directory {path_dir}")
    return total_files_data


def search_engine(files_data: dict):
    '''
    Take dictionary from read_text_files function and search pattern input during runtime. Then do search of given words from data on the base of spelling equality (case in sensitive) and give information about how much percent of search words contains by each text file.

    Parameters
    ----------
    files_data : dict
        Dict object which contains the files and their data

    Returns
    -------
    dict
        Returns a dictionary which contains file name with percentage of matching search words 

    '''
    if type(files_data) not in [dict]:
        raise TypeError("The data should be dict type")

    final_result = {}

    while True:
        search_words = input("search> ")
        if 'quit' in search_words or 'exit' in search_words:
            sys.exit()

        search_words = search_words.split()
        match_count = 0

        for key, value in files_data.items():
            value = "".join(
                [word for word in value if word.isalpha() or word.isspace()])
            value = value.lower()
            split_file_text = value.split()

            for word in search_words:
                if word.lower() in split_file_text:
                    match_count += 1

            percenatage = (match_count/len(search_words)) * 100
            percenatage_rounded = round(percenatage)
            final_result[key] = percenatage_rounded
            match_count = 0

        # call print_result function
        print_result(final_result)


def print_result(results: dict):
    '''
    Take dictionary from search_engine function which contains information about filenames with their matching percentages. Then sort them in descending order and print the top 10 matching filenames in rank order.

    Parameters
    ----------
    results: dict
        Dict object which contains the filenames with matching percentage

    Returns
    -------
        Returns list of top 10 matching filenames and their matching percentage

    '''
    if type(results) not in [dict]:
        raise TypeError("The data should be dict type")

    sorted_result = dict(
        sorted(results.items(), key=lambda x: x[1], reverse=True))
    counter = 0
    if sum(sorted_result.values()) == 0:
        print("no matches found")
    else:
        for key, value in sorted_result.items():
            if counter < 10 and value > 0:
                print(f"{key} : {value}%")
                counter += 1
            else:
                break


if __name__ == "__main__":

    args = sys.argv[1:]

    if len(args) == 0:
        raise Exception('No directory given to index')

    path = args[0]
    search_engine(read_text_files(path))
