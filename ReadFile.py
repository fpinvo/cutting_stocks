
# Python code to demonstrate converting 
# string representation of list to list
# using ast.literal_eval()
import ast
import csv
import json

class ReadFile:
    
    def __init__(self) -> None:
        pass
    
    def read(self):
        # csv file name
        filename = "input.csv"
  
        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            
            # extracting field names through first row
            fields = []

            # extracting each data row one by one
            for row in csvreader:
                fields.append({
                    'marterial_name':row[0],
                    'x_axis':row[1],
                    'y_axis':row[2],
                    'quantity':row[3],
                    'cuts':ast.literal_eval(row[4])
                })
                
               
        return fields
        
            
        
        

