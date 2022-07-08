# # Wifi Cracker
# # Importing necessary modules
import subprocess
import re

# #  Capturing the cmd output
cmd_ouput = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode()

wifi_list=[]

# # Storing all the ssid names in the profile_names
profile_names = (re.findall("All User Profile     : (.*)\r", cmd_ouput))


#  If there is no ssid : (Which there is one usually otherwise why are you watching😎)
if profile_names != 0:
    for name in profile_names:
        wifi_profile={} # To store wifi data
        profile_info = subprocess.run(['netsh', 'wlan', 'show', 'profiles', name], capture_output=True).stdout.decode()
        # Take the info of ssid with name = name
        if re.search("Security key           : Absent", profile_info): # If there is no security key make it None
            continue
        else: # If there is a password
            wifi_profile['ssid'] = name # Saving the name in wifi_profile
            profile_info_password = subprocess.run(['netsh', 'wlan', 'show', 'profiles', name, 'key=clear'], capture_output=True).stdout.decode()
            # Taking the password for name = name
            password = re.search("Key Content            : (.*)\r", profile_info_password)
            if password == None: # If there is no password
                wifi_profile['password'] = None
            else: # If there is a password
                wifi_profile['password'] = password[1]
        # Appending the profiles to wifi_list
        wifi_list.append(wifi_profile)


# Printing the list
for i in range(len(wifi_list)):
    print(wifi_list[i])


# To Know about any mobile number
import phonenumbers

# from text import number
number = " "
from phonenumbers import geocoder, carrier
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))