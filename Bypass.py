import os
Ii = '/sdcard'
if 'android8.txt' in Ii:
    os.system("rm -rf /sdcard/android8.txt")
    open('/sdcard/android8.txt','w').write('')
    os.system("python Tutul-V5.2.py")
else:
    open('/sdcard/android8.txt','w').write('')
    os.system("python Tutul-V5.2.py")
