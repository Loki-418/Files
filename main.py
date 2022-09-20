__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from os import listdir
from os.path import isfile, join

def clean_cache():
    cache = ("files/cache")
    if os.path.exists(cache):
        shutil.rmtree(cache)
        os.mkdir(cache)
        print ("fresh")
    else:
        os.mkdir(cache)
        print("created")
     
def cache_zip(zip_path, dir_path):
    shutil.unpack_archive(zip_path, dir_path, "zip")
  
def cached_files():
    cache = os.path.abspath("files/cache")
    files_list = [os.path.join(cache, file) for file in os.listdir(cache) if isfile(join(cache, file))]
    return files_list

def find_password(all_foo):
    for foo in all_foo:
        with open(foo) as this_foo:
            lines = this_foo.readlines()
            for row in lines:
                if "password" in row:
                    password = row.split(" ")
                    return str(password[1].strip())
          
          
def main():
    clean_cache()
    cache_zip("files/data.zip", "files/cache")
    cached_files()
    find_password(cached_files())

if __name__ == "__main__":
    main()
    