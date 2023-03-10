#!/usr/bin/env python3

#
#   Description: What does this code do?
#   getsthe names from the input file and prints them
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
 
def main ( argv ):

#
#   What does this section of the code do?
#this code section demonstrates providing input and output file name and year to the script through command line arguments, and handling different cases if the arguments are not provided or provided incorrectly.
    if len(argv) < 6:
        print ( "Usage: ./namesTop10.py -i <input file name> -y <year> -o <output file name base>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:y:o:",["input=","year=","output="] )
    except getopt.GetoptError:
        print ( "Usage: ./namesTop10.py -i <input file name> -y <year> -o <output file name base>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./namesTop10.py -i <input file name> -y <year> -o <output file name base>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
        elif opt in ("-y", "--year"):
            year = int(arg)
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase+str(year)+".csv"

#
#   What is being declared here and why?
#
    names    = []
    numbers  = []
    ranks    = []
    total    = 0

#
#   What is the overall purpose of this section of code?
#Open the CSV file get the info and print
    with open ( inputFileName ) as csvDataFile:
        #
        # What does next do
        #The next() function in this code is used to skip the first row of the CSV file.
        #In this code, the next() method is used to skip the first row of the CSV file. This is due to the fact that the first row of the file may include column headers that are not actual information. It then returns the iterator's next item. The iterator in this example is the file object "csvDataFile," which is provided to the csv.reader function. The csv.reader method takes the csvDataFile as input and reads the CSV file with delimiter=',' separating the data in the file with commas. The script will then use a for loop to traverse over the rows of the CSV file, beginning with the second row (which is actually the first row in this context).
        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            #
            # What is happening here?
            #   - include information about strip() and the purpose
            #     of newranks as opposed to ranks
            #This code determines if the first element (at index 0) of the "row" list is equal to a given year. If it is, it assigns the second item in the "row" list (at index 1) to the variable "tempName," after removing any leading or following whitespace. The variable is then appended to the "names" list, and the third member of the "row" list (at index 2) is appended as an integer to the "numbers" list. The variable "total" increments by one. Finally, the current "total" value is added to the "ranks" list. The code then outputs the total number of names discovered in that year after going through each row of data.
            if int(row[0]) == year :
                tempName = row[1].strip()
                names.append(tempName)
                numbers.append(int(row[2]))
                total = total + 1
                ranks.append(total)
        print ( "There are ",total," names in ",year )

        #
        #   Why could total == 0?
        #   The if statement determines whether the value of?? total?? is greater than zero. If it is larger than zero, the code inside the if block is performed. It creates a dictionary named "people" with two keys, "Name" and "Number," and assigns the variables "names" and "numbers" to them. Then it uses the Pandas library to generate a DataFrame named "people df," utilising the "people" dictionary as the input data.
        if total > 0 :
            people = {'Name':names,'Number':numbers}
            people_df = pd.DataFrame(people)
        
#
#           What is this doing?
#           Here, the .sort_values() function is being used to sort "Number" and "Name". Since the axis is assigned 0, it is rows oriented. Ascending is assigned False for Numbers, and True for Names. Inplace is assigned True, thus it changes/modifys the original data. Then "rankedPeople_df" is created by taking the "people_df" DataFrame and adding a new column called "Rank" with the values from the "ranks" variable. Then it prints the new DataFrame.
            people_df.sort_values(["Number","Name"], axis = 0, ascending=[False,True], inplace=True)
            rankedPeople_df = people_df.assign(Rank=ranks)

            top10 = rankedPeople_df.head(10)
            print ( top10 )


#
#           What is this doing?
#           This exports top10 to the csv file specificed by outputFileName variable. The sep=',' refers to seperating information with commas, "index=False" will remove the index column from the csv file, and encoding='utf-8' saves the file with UTF-8 encoding.
            top10.to_csv(outputFileName, sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
    main ( sys.argv[1:] )

#
#   End of names.py
#
