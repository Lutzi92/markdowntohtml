import os
import shutil
from textnode import TextNode


def main():
    #node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #print(node)
    copy_recursive(os.path.abspath(os.getcwd()+"/static"), os.path.abspath(os.getcwd())+"/public")


def copy_recursive(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    list_copy_files = os.listdir(source)
    
    for copy in list_copy_files:
        item = f"{source}/{copy}"
        if os.path.isfile(item):
            shutil.copy(item,destination)
            print(f"Copying file {item}")
        if os.path.isdir(item):
            print(f"Copying dir {item}")
            copy_recursive(item,destination+"/"+os.path.split(copy)[1]) 
           

main()
