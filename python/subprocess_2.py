import re,os,subprocess,time
from subprocess import call,Popen,PIPE
cmd = "adb devices"
os.system(cmd)
adb_output = Popen(cmd, shell = True,stderr = PIPE,stdout = PIPE)
out,err = adb_output.communicate()
print(str(out))