# Python:     3.8.5
# Author:     Nicholas Mireles
# Assignemnt: OS Module

import os, time

def start():

    dir = r'C:\python_assignment'
    for filename in os.listdir(dir):
        if filename.endswith('.txt'):
            print(os.path.join(dir, filename),
                  time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime(os.path.join(dir, filename)))))

  
if __name__ == "__main__":
    start()
