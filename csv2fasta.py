import csv
import argparse
import sys
import textwrap

parser = argparse.ArgumentParser(
        description = ("Converts CSV files into FastA file. Input CSV file should contain \n"
                        "only two columns 'Name' and 'Sequence' and must end with '.csv' extension. \n"
                        "The sequence input should not be split into multiple rows. \n"
                        ),
        epilog = "Outputs a 'Sequences.fasta' file with names and sequences from the CSV file. \n"
                                 )

parser.add_argument("file", metavar = "-file", help = "A CSV file. \n")

parser.add_argument("-w", "--wrap", action = "store_true",
                    help = "optional argument placed after the file that "
                    "wraps the FastA sequence into 100 bases per line \n"
                    )
                    
args = parser.parse_args()

def csv_to_fasta(fileinput):
    try:
        #Create an empyt dictionary for sequence key-value pairs
        sequences = {}
        with open(fileinput, "r") as csvfile:
            #Need to include this line to skip the first line
            readcsv = csv.reader(csvfile, delimiter = ",")
            #Skips first row
            first_line = csvfile.readline()
            #Adds each row to the dictionary as key-value pair
            for row in readcsv:
                sequences[row[0]] = row[1]
        
        with open("Sequences.fasta", "w") as file_output:
            for (key, value) in sequences.items():
                #Prints name and sequences as a fasta format
                file_output.write(">" + str(key) + "\n" + str(value) + "\n")
            
            return "Sequences.fasta file successfully created"
    except:
        return "Not a valid CSV file"

def csv_to_fasta_wrap(fileinput):
    try:
        #Create an empyt dictionary for sequence key-value pairs
        sequences = {}
        with open(fileinput, "r") as csvfile:
            #Need to include this line to skip the first line
            readcsv = csv.reader(csvfile, delimiter = ",")
            #Skips first row
            first_line = csvfile.readline()
            #Adds each row to the dictionary as key-value pair
            for row in readcsv:
                sequences[row[0]] = row[1]
        
        with open("Sequences.fasta", "w") as file_output:
            for (key, value) in sequences.items():
                #Prints the 'Name' of the sequence first
                file_output.write(">" + str(key) + "\n")
                #Then prints the sequence in a new line wrapped at 100 characters
                file_output.write(textwrap.fill(str(value), 100) + "\n")
            
            return "Sequences.fasta file successfully created"
    except:
        return "Not a valid CSV file"

if __name__ == "__main__":
    try:
        if len(sys.argv) >= 2:
            if len(sys.argv) == 2:
                if sys.argv[1].endswith((".csv", ".CSV")):
                    converter = csv_to_fasta(sys.argv[1])
                    print(converter)
                else:
                    raise FileNotFound
            elif len(sys.argv) == 3 and sys.argv[2]  == "-w":
                if sys.argv[1].endswith((".csv", ".CSV")):
                    converter = csv_to_fasta_wrap(sys.argv[1])
                    print(converter)
                else:
                    raise FileNotFound
            else:
                raise IOError
        else:
            raise IOError
    except (FileNotFound, IOError):
        sys.exit("The file does not exist, wrong extension, or invalid command line inputs")
                
    