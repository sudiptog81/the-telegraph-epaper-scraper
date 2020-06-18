import os
import glob
from time import sleep
from datetime import datetime

date = str(datetime.today().strftime("%d-%m-%Y"))

sleep(10)

files = glob.glob("*.pdf")
files.sort(key=os.path.getmtime)
filename = str(files[0])
command = f"mega-put \'{filename}\'" + \
    f" \'/The Telegraph ePaper/{date}/{filename}\' -c"
os.system(command)

sleep(10)

os.system("rm *.pdf")
