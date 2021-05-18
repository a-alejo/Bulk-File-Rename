import os


# this function finds the path then renames each item in the folder starting with 0
def main():
    i = 0
    path = 'C:/Users/Alfredo/Desktop/Test Folder/'
    for filename in os.listdir(path):
        # name & extension format can be changes here
        my_dest = 'File' + str(i) + '.rtf'
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

