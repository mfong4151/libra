
def read_files(file: str) -> str:
    with open(file, 'r') as file:
        return(file.read())
        
def write_files(file:str, text: str='') -> None:
    with open(file, 'w') as file:
        file.write()