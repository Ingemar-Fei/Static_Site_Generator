import textnode
import os
import shutil

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def clean_dir(dirname):
    print(f"cleaning dir: {dirname}...")
    files = os.listdir(project_root+'/'+dirname+'/')
    for file in files:
        filename = os.path.join(project_root+'/'+dirname+'/',file)
        if os.path.isfile(filename):
            print(f"removing file : {filename}")
            os.remove(filename)
        elif os.path.isdir(filename):
            print(f"removing dir : {filename}")
            shutil.rmtree(filename)
    print(f"clean done: {os.listdir(project_root+'/'+dirname+'/')}")

def copty_files(from_dir, to_dir):
    print(f"geting files from {from_dir} dir")
    files = os.listdir(project_root+'/'+from_dir+'/')
    for file in files:
        from_file_name  = os.path.join(project_root+'/'+from_dir+'/',file)
        to_file_name  = os.path.join(project_root+'/'+to_dir+'/',file)
        if os.path.isfile(from_file_name):
            print(f"copying file:{from_file_name} to {to_file_name}")
            shutil.copy(from_file_name, to_file_name)
        elif os.path.isdir(from_file_name):
            print(f"copying dir: {from_file_name} to {to_file_name}")
            shutil.copytree(from_file_name, to_file_name)
    print("copy complete:",os.listdir(project_root+'/'+to_dir+'/'))

if __name__ == "__main__":
    print("initial public dir:\n")
    clean_dir('public')
    copty_files('static', 'public')
    print("public inited:\n",os.listdir(project_root+'/public/'))