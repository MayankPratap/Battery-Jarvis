import os,time

charge_now_file="/sys/class/power_supply/BAT0/charge_now"
charge_full_file="/sys/class/power_supply/BAT0/charge_full"

charge_now=open(charge_now_file)
charge_full=open(charge_full_file)

charge_now_content=charge_now.read()
charge_full_content=charge_full.read()

num=int(charge_now_content)*1.0
den=int(charge_full_content)*1.0

res=num/den*100

time.sleep(2)

if res<=15:
    os.system("espeak 'Hey,Mayank please charge me'")
    time.sleep(2)
    
    
    
