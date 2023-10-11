""" 
    copyfile() - copies contents of a file
    copy()     - copyfile()                 + permission mode + destination can be a directory
    copy2()    - copy()                     + metadata (file's creation and modification time)
"""
import shutil
shutil.copyfile('E:\\Alternate Desktop\\Code\\Python\\test_for_copying.txt', 'E:\\Alternate Desktop\\Code\\Python\\copy.txt') # src, destn
# args for copy() and copy2() are the same as above