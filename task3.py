import sys
import subprocess
from datetime import *

def pinger():
    fhand=open('output.txt','w')
    fhand.write(f'pinged {sys.argv[1]} on {date.today()} at {datetime.now().strftime("%H:%M:%S")}')
    output = subprocess.run(['ping',sys.argv[1]])
    return output
pinger()
