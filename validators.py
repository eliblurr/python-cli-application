import pandas as pd
from pathlib import Path
from argparse import ArgumentTypeError
from constants import EXCEL_EXTENSIONS
from utils import create_dir, copy_file, copy_file

file = None

def validate_excel(file_path) -> Path:
    path = Path(file_path)
    if not path.exists():
        raise ArgumentTypeError("file does not exist for file path provided.")
    
    if path.suffix not in EXCEL_EXTENSIONS:
        raise ArgumentTypeError("file path provided must point to an excel file.")

    global file 
    tmp_file = Path(create_dir('./tmp')).joinpath(path.name)
    file = tmp_file = copy_file(file_path, tmp_file, overwrite=True)

    return tmp_file

def validate_excel_sheet(target:str, sheet_name=None, keys:set={}):
    
    xls = pd.ExcelFile(file)

    if not sheet_name:
        sheet_name = xls.sheet_names[0]

    elif sheet_name and not sheet_name in xls.sheet_names:
        raise ArgumentTypeError(f'invalid sheet name provided for {target}')

    if not keys.issubset(xls.parse(sheet_name).columns.to_list()):
        raise ArgumentTypeError(f'sheet name provided does not support keys for {target}')

    return sheet_name

validate_user_sheet = lambda sheet_name : validate_excel_sheet('user sheet', sheet_name, keys={'key 1', 'key 2'})
validate_project_sheet = lambda sheet_name : validate_excel_sheet('project sheet', sheet_name, keys={'key 1', 'key 2'})
validate_migration_sheet = lambda sheet_name : validate_excel_sheet('migration sheet', sheet_name, keys={'key 1', 'key 2'})