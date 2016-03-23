# Battery-Jarvis
A script which notifies critical battery level using voice.

This script will currently work on linux but can be made easily for other operating systems.
We can schedule our script to run at some interval(5 or 10 min) and notify by voice if battery charge percentage goes below 15% or the system gets full charged.

## Dependencies
 
 - Python2  :- https://www.python.org/downloads/ 
 - espeak   :- sudo apt-get install espeak

## Cron Jobs

To schedule our script to run at regular interval we can use cronjobs in linux.
  
1) In a terminal , run crontab -e
2) Now at the end of this file add the following line:- 
       
  */10 * * * * DISPLAY=:0 gnome-terminal -x sh -c "python2 path/to/batteryJarvis.py;"
  
3) Save and close the file.

Just wait for 10 minutes and see the script notifying you about your battery status.
  
