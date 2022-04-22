#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Challenge Solution 01 - excel to JSON"""

import pandas

def main():

    # create a dataframe from excel
    df = pandas.read_excel("5movies-translated-from-json.xlsx")

    # writeout dataframe to JSON
    df.to_json("5movies-translated-from-excel.json")

if __name__ == "__main__":
    main()

