import time
import shutil
from pathlib import Path

def create_dir(path:str):
    Path(path).mkdir(parents=True, exist_ok=True)
    return Path(path).resolve()

def copy_file(source:str, destination:str=None, overwrite=False, mode=0o444):
    destination = Path(destination)
    if not overwrite and Path(destination).is_file():
        parent = Path(destination.parent)
        destination =  parent.joinpath(f'{destination.stem}_copy_{int(time.time())}{destination.suffix}') 
    shutil.copy(source, destination)
    return destination
