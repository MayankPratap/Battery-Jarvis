import os,time
import subprocess
import getpass
import commands

from subprocess import call

"""
   Some systems contain battery information in BAT0 while some have in 
   BAT1.Therefore script uses find command to find folder beginning with BAT. Therefore script works on BAT0 or BAT1 according to system.


"""

coutput=commands.getstatusoutput("find /sys/class/power_supply/BAT*")
#print coutput

cpath=coutput[1]

folder=os.path.basename(cpath)  # contains BAT0 or BAT1 accordingly


charge_now_file="/sys/class/power_supply/"+folder+"/charge_now"
charge_full_file="/sys/class/power_supply/"+folder+"/charge_full"
charge_status_file="/sys/class/power_supply/"+folder+"/status"

charge_now=open(charge_now_file)
charge_full=open(charge_full_file)
charge_status=open(charge_status_file)

charge_now_content=charge_now.read()
charge_full_content=charge_full.read()
charge_status_content=charge_status.read()


"""
  
   charge_status_content is string consisting of two lines first line contains "Charging" and 2nd line is empty.

  Therefore comparing charge_status_content with "Charging" gave false


  Therefore I used splitlines() to have lines in a list.

  Then I took first element of list .




"""

lines=charge_status_content.splitlines()

charge_status_content=lines[0]

num=int(charge_now_content)*1.0
den=int(charge_full_content)*1.0

res=num/den*100

user=getpass.getuser()

#user=user[:-4]

if res<=15 and charge_status_content!="Charging":
    speech ="hey "+user+" please charge me."
    call(["espeak",speech])

elif res==100 and charge_status_content!="Discharging":
    speech ="hey "+user+" Please dont overcharge me."
    call(["espeak",speech])



