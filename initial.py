import sys
import os
import subprocess

def main():
 
 print "Checking for devices"
 output = subprocess.check_output("adb devices", shell=True)
 print output[24:]

#Packages_list_to_be_tested

 pak_list = ['com.android.camera2','com.google.android.music','com.android.gallery3d','com.android.chrome', 'com.android.calendar'
              , 'com.google.android.youtube', 'com.android.calculator2', 'com.google.android.apps.maps', 'com.android.dialer'
			  , 'com.google.android.videos', 'com.google.android.apps.photos', 'com.android.settings'
            ]

 print "Packages to be tested :\n", pak_list
 for package in pak_list:
  monkey_execute( package )
  
def monkey_execute(pak):
 print "\nMonkey Running on ", pak
 os.system("adb shell monkey -p %s --throttle 10 -v 5000" % (pak))
 #os.system("adb shell monkey -p %s --throttle 500 -v 50" % (pak))
 #os.system("adb shell monkey -p com.android.bluetooth --throttle 500 -v 50" )
 #os.system("adb shell monkey -p %s -v 50" % (pak))
 print "\n [%s] Execution completed  ...." % (pak)

def music_start():
 os.system("adb shell am start -a android.intent.action.VIEW -d file:///sdcard/videos/Aazaadiyan.mp3 -t audio/mp3")
 #adb shell am start -a android.intent.action.VIEW -d file:///sdcard/videos/Aazaadiyan.mp3 -t audio/mp3
 
 

if __name__ == '__main__':
    main()