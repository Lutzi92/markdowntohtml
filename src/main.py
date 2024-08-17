import os
import shutil
from markdown_blocks import extract_title, markdown_to_html_node
from textnode import TextNode


def main():
    #node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #print(node)
    copy_recursive(os.path.abspath(os.getcwd()+"/static"), os.path.abspath(os.getcwd())+"/public")
    generate_page(os.path.abspath(os.getcwd()+"/content/index.md"),os.path.abspath(os.getcwd()+"/template.html"),os.path.abspath(os.getcwd()+"/public/index.html"))

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

def generate_pages_recursive(dir_path_content,template_path, dest_dir_path):
    
    pass

def generate_page(from_path,template_path, dest_path):
    print(f"Generating page from path {from_path} to {dest_path} using {template_path}.")
    source = open(from_path).read()
    template = open(template_path).read()
    title = extract_title(source)
    convert = markdown_to_html_node(source).to_html()
    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}",convert)
    if not os.path.isdir(os.path.split(dest_path)[0]):
        os.path.makedir(os.path.split(dest_path)[0])
    htmlfile = open(dest_path,"w")
    htmlfile.write(template)
    htmlfile.close()






main()
