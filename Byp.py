import os
from os import listdir as lst
try:
	op = lst("/sdcard/android8.txt")
except:
	os.mkdir("/sdcard/android8.txt")

os.system("python Tutul-V5.2.py")