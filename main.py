#!/usr/bin/env python

import argparse
from validators import (validate_excel, validate_migration_sheet, 
    validate_project_sheet, validate_user_sheet)

# create argparse object
parser = argparse.ArgumentParser()

# configure cli args
parser.add_argument("-f", "--file", type=validate_excel, help="takes in file path for target excel", required=True)
parser.add_argument("-m", "--migration", type=validate_migration_sheet, help="pass the excel sheet name containing migration groups", required=False)
parser.add_argument("-p", "--projects", type=validate_project_sheet, help="pass the excel sheet name containing project information", required=False)
parser.add_argument("-u", "--users", type=validate_user_sheet, help="pass the excel sheet name user containing information", required=False) 
parser.add_argument("-c", "--cores", type=int, help="pass number of processes you want to initiate", required=False, default=4, choices=range(1, 15)) 

# get argument namespace
args = parser.parse_args()

print(
    args.file,
    args.migration,
    args.projects,
    args.users, 
    args.cores,
    sep='\n'
)

if __name__ == '__main__':
    pass