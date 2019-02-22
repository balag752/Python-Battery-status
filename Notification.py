#Packages

from plyer import notification
import os
import psutil
import time
import sys 

#Variable Assgnment
icon_location=os.path.dirname(os.path.realpath(__file__))+'\\icon\\ic_battery_full_white_48dp.png'
i=0
#os.spawnl(os.P_DETACH, 'some_long_running_command')

# Function Definition
def notifymsg(msg='Please remove the charge'):
	try :
	
		notification.notify(
			title='Battery Notification',
			message=msg,
			app_name='Battery Notification'#,
			#app_icon=icon_location
		)
		
	except e:
		print(e)


def BatteryCheck(Low=25, High=80):

	try :
		if(Low>=15):	
			Lowest=Low-10
		else :
			raise Exception("Low percentage is can not lower than 15")
		i=0	
		
		while True :
			i=i+1
			#print(i)
			
			
			battery = psutil.sensors_battery()
			plugged=battery.power_plugged
			percent=str(battery.percent)
			
			if(plugged==True and battery.percent>=High):
				if(plugged==True and battery.percent==100):
					notifymsg("Battery is fully charged. Unplug the charger soon")
					time.sleep(60)
				notifymsg("Battery level is "+percent+"%. Please unplug the charger")
				time.sleep(180)
				continue

			elif( plugged==False and battery.percent<=Low):
				if( plugged==False and battery.percent<=Lowest):
					notifymsg("Battery level is "+percent+"%. Charge up soon")
					time.sleep(60)
				notifymsg("Battery level is "+percent+"%. Please charge up")
				time.sleep(180)
				continue
				
			time.sleep(100)	
			
	except AssertionError as error:
		print(error)
		
Low=int(sys.argv[1])
High=int(sys.argv[2])

BatteryCheck(Low,High)
