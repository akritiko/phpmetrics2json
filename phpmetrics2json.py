import os
import re
import sys
import json
import logging
import pandas as pd
import numpy as np

def phpmetrics2json():
    """ Transforms phpmetrics console output to JSON format. """
    phpmetrics = [
        ["Lines of code", "LOC", ""],
        ["Logical lines of code", "LOC", ""],
        ["Comment lines of code", "LOC", ""],  
        ["Average volume", "LOC", ""],
        ["Average comment weight", "LOC", ""],
        ["Average intelligent content", "LOC", ""],
        ["Logical lines of code by class", "LOC", ""],
        ["Logical lines of code by method", "LOC", ""],
        ["Classes", "Object oriented programming", ""],
        ["Interface", "Object oriented programming", ""],
        ["Methods", "Object oriented programming", ""],
        ["Methods by class", "Object oriented programming", ""],
        ["Lack of cohesion of methods", "Object oriented programming", ""],
        ["Average afferent coupling", "Coupling", ""],
        ["Average efferent coupling",  "Coupling", ""], 
        ["Average instability", "Coupling", ""],
        ["Depth of Inheritance Tree",  "Coupling", ""],
        ["Packages", "Package", ""],
        ["Average classes per package", "Package", ""],
        ["Average distance", "Package", ""],
        ["Average incoming class dependencies", "Package", ""],
        ["Average outgoing class dependencies", "Package", ""],
        ["Average incoming package dependencies", "Package", ""],
        ["Average outgoing package dependencies", "Package", ""],
        ["Average Cyclomatic complexity by class", "Complexity", ""],
        ["Average Weighted method count by class", "Complexity", ""],
        ["Average Relative system complexity", "Complexity", ""],
        ["Average Difficulty", "Complexity", ""],
        ["Average bugs by class", "Bugs", ""],
        ["Average defects by class (Kan)", "Bugs", ""],
        ["Critical", "Violations", ""],
        ["Error", "Violations", ""],
        ["Warning", "Violations", ""],
        ["Information", "Violations", ""]
    ];
    df = pd.DataFrame(phpmetrics, columns=['Metric','Category', 'Value'],dtype=float) # //XXX: dtype=float is deprecated
    with open('phpmetrics.txt') as f:
        lines = f.readlines() # list containing lines of file
        for line in lines:
            line = line.strip() # remove leading/trailing white spaces
            for index, row in df.iterrows():
                if re.search(r"\b"+row['Metric']+r"\b",line) and row['Value'] == "": # add value only if there is not one yet.
                    s_nums = re.findall(r"[-+]?\d*\.\d+|\d+", str(line))
                    logging.info(row['Metric'] + ": " + s_nums[0]) # logging
                    row['Value'] = s_nums[0]
    df.to_json (r'phpmetrics.json', orient='records') # export to JSON with each item to reflect a tuple [Metric, Category, Value]

def main(args):
    """ Main function. """
    logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO, format='%(asctime)s [ %(levelname)s ] %(message)s', datefmt='%d/%m/%Y %H:%M:%S') # init logging
    repo_dir_name = sys.argv[1]
    from sys import platform # detect OS
    if platform == "linux" or platform == "linux2":
        logging.info("Linux operating system detected.") 
        os.system('phpmetrics --report-html=myreport ./{0} >> phpmetrics.txt'.format(repo_dir_name))
        phpmetrics2json()
        os.system('rm phpmetrics.txt')
    elif platform == "darwin":
        logging.info("OSX operating system detected.") 
    elif platform == "win32":
        logging.info("Windows operating system detected.") 
        os.system('phpmetrics --report-html=myreport ./{0} > phpmetrics.txt'.format(repo_dir_name))
        phpmetrics2json()
        os.system('del "phpmetrics.txt"')

if __name__ == "__main__":
    main(sys.argv[1:])
