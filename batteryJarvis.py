
import os,time
import subprocess
import getpass
import commands

from subprocess import call

coutput=commands.getstatusoutput("find /sys/class/power_supply/BAT*")
#print coutput

cpath=coutput[1]

folder=os.path.basename(cpath)  # contains BAT0 or BAT1 accordingly

#print folder

charge_now_file="/sys/class/power_supply/"+folder+"/charge_now"
charge_full_file="/sys/class/power_supply/"+folder+"/charge_full"
charge_status_file="/sys/class/power_supply/"+folder+"/status"

charge_now=open(charge_now_file)
charge_full=open(charge_full_file)
charge_status=open(charge_status_file)

charge_now_content=charge_now.read()
charge_full_content=charge_full.read()
charge_status_content=charge_status.read()

#print charge_now_content
#print charge_status_content

num=int(charge_now_content)*1.0
den=int(charge_full_content)*1.0

res=num/den*100

#print res


user=getpass.getuser()

#print "hello"

#print user

#speech="hey " + user + " please charge me."
#call(["espeak",speech])

#user=user[:-4]

#print user

if res<=15 and charge_status_content!="Charging":
    speech ="hey "+user+" please charge me."
    call(["espeak",speech])

elif res==100 and charge_status_content!="Discharging":
    speech ="hey "+user+" Please dont overcharge me."
    call(["espeak",speech])
