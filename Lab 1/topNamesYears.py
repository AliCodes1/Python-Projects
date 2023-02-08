#!/usr/bin/env python3

#
#   Description: What does this code do?
#   Get the most famous names of every year
#   Authors: 
#      Partner 1:Muhammad Ali
#      Partner 2:Caitlin
#
#   Date of last update: Jan 27th
#

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd

def main(argv):
    # check if there are less than 2 command line arguments
    if len(argv) < 2:
        # print error message and exit the program
        print("Usage: ./topNamesYears.py -i <input file name>")
        sys.exit(2)
    # try to get the input file name
    try:
        (opts, args) = getopt.getopt(argv, "i:", ["input="])
    except getopt.GetoptError:
        print("Usage: ./topNamesYears.py -i <input file name>")
        sys.exit(2)
    for opt, arg in opts:
        # check if the help option is provided
        if opt == '-h':
            print("Usage: ./topNamesYears.py -i <input file name>")
            sys.exit()
        # check if the input option is provided
        elif opt in ("-i", "--input"):
            inputFileName = arg
    # iterate through years from 1917 to 2020
    for year in range(1917, 2020):
        # open the input file
        with open(inputFileName) as csvDataFile:
            # skip the first line
            next(csvDataFile)
            csvReader = csv.reader(csvDataFile, delimiter=',')
            names = []
            numbers = []
            total = 0
            # iterate through the rows in the csv file
            for row in csvReader:
                if int(row[0]) == year:
                    tempName = row[1].strip()
                    names.append(tempName)
                    numbers.append(int(row[2]))
                    total = total + 1
            if total > 0:
                # create a dataframe from the names and numbers
                people = {'Name': names, 'Number': numbers}
                people_df = pd.DataFrame(people)
                # sort the dataframe by number in descending order
                people_df.sort_values(["Number"], axis=0, ascending=[False], inplace=True)
                # print the year, the name with the highest number, and the number of occurrences
                print(year, people_df.iloc[0]['Name'], people_df.iloc[0]['Number'])

if __name__ == "__main__":
    main ( sys.argv[1:] )