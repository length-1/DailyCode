import os
import datetime


timestamp = datetime.datetime.now()



output = os.popen('wmic process get description, processid').read()

with open("services.txt","a") as f:

    f.write(str(timestamp) + "\n")

    f.write(output)

