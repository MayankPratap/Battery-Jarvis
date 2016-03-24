import os,time

charge_now_file="/sys/class/power_supply/BAT1/charge_now"
charge_full_file="/sys/class/power_supply/BAT1/charge_full"
charge_status_file="/sys/class/power_supply/BAT1/status"

charge_now=open(charge_now_file)
charge_full=open(charge_full_file)
charge_status=open(charge_status_file)

charge_now_content=charge_now.read()
charge_full_content=charge_full.read()
charge_status_content=charge_status.read()

num=int(charge_now_content)*1.0
den=int(charge_full_content)*1.0

res=num/den*100

if res<=15 and charge_status_content!="Charging":
    os.system("espeak 'Hey,Mayank please charge me.'")

elif res==100 and charge_status_content=="Charging":
    os.system("espeak 'Please dont overcharge me.'")


   




