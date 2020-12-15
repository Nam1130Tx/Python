import shutil
import os,time
import datetime
import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%M %m/%d/%Y"
src = '/Users/mirel/OneDrive/Desktop/TempDesktop/Hold'
dest = '/Users/mirel/OneDrive/Desktop/TempDesktop/Transfer'

for root, dirs,files in os.walk(src):
    for name in files:
        path = os.path.join(root,name)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print("True: ", name, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
            shutil.copy(path, dest)

