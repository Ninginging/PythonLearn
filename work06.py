import os
import work04

os.chdir('E:\\pythonProject\\PythonLearn\\')
currentdir = os.getcwd()
allfile_name = os.listdir(currentdir)
print(allfile_name)