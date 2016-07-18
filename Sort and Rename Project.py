import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("C:\Users\Trevor\Documents\Projects\prank.zip\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working DIrectory is "+saved_path)
    os.chdir("C:\Users\Trevor\Documents\Projects\prank.zip\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789")
        os.rename(file_name.translate(None, "0123456789"))
    os.chdir(saved_path)    
rename files()
