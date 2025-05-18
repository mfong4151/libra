from os import listdir, getcwd, walk
from os.path import isfile, join
from file_parsing.stringify_file import stringify_file
from typing import List



def unpack_config(config) -> List[str]:
    ignored_files = set(config['ignored_files'])
    ignored_folders = set(config['ignored_folders'])
    
    return ignored_files, ignored_folders


def extract_file_bodies(config, cwd: str,  ignored_files: set[str], ignored_folders: set[str]) -> str:
    """
    Extracts the bodies of files
    """    
    res = []
    copyable_files = []  
    
  
    for root, _, filenames in walk(cwd):
       folder =  root.split("/")[-1]
      
       for filename in filenames:
          if folder in ignored_folders or filename in ignored_files:
            continue
          
          copyable_files.append(join(root, filename))
    
    for file in copyable_files:
          contents = stringify_file(cwd, file)
          res.append(contents)
    
    return "\n\n".join(res)


def create_piped_name(file: str, depth: int) -> str:
    PIPE_T = "├──"
    PIPE_VR = "│  "
    res = []

    for _ in range(depth + 1): 
        res.append(PIPE_VR)
    res.append(PIPE_T)
    res.append(f"{file}/")

    return ''.join(res)

def extract_file_tree(config, dir: str = getcwd) -> str:
    res = [f"{dir}/"]
    ignored_files, ignored_folders = unpack_config(config)

    def dfs(dir: str, depth: int) -> None:
        if isfile(dir):
            return
        
        for file in listdir(dir):
            if file in ignored_files or file in  ignored_folders:
                continue
            
            new_dir = f"{dir}/{file}"
            res.append(create_piped_name(file, depth))            
            dfs(new_dir, depth + 1)
            
        return
    dfs(dir, 0)
    return "\n".join(res)
