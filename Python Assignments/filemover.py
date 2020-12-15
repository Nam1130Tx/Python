import shutil
import os

source = '/Users/mirel/OneDrive/Desktop/Folder A/'

destination = '/Users/mirel/OneDrive/Desktop/Folder B/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
