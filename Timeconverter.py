"""
Gets User's Time and convert's it to US, UK, and MY [Note: Program is very sensitive to input]
Author: Jayy-Ayy (Jayy-Ayy@github)
Last Modified: 3/25/2024
"""
import sys

"""
Gets the user's time input.
@input: User's Time and GMT
@returns: A list containing the user's hour, minute, and meridiem.
"""
def tzConvert(t, gmt):
    tzNew = [0]*3
    tzNew[0] = t[0] + gmt
    tzNew[1] = t[1]
    tzNew[2] = t[2]
    # Minute < 60 and Minute >= 60
    if tzNew[1] < 0:    tzNew[0] -= 1; tzNew[1] += 60
    elif tzNew[1] >= 60:  tzNew[0] += 1; tzNew[1] -= 60

    # Hour <= 12 and Hour > 12
    if tzNew[0] <= 0: 
        tzNew[0] += 12; 
        if tzNew[2] == "am": tzNew[2] = "pm"
        elif tzNew[2] == "pm": tzNew[2] = "am"
    elif tzNew[0] > 12: 
        tzNew[0] -= 12; 
        if tzNew[2] == "am": tzNew[2] = "pm"
        elif tzNew[2] == "pm": tzNew[2] = "am"


    # Fixing '0' to '00'
    if tzNew[1] < 10: 
        tzNew[1] = f"0{tzNew[1]}"
    return tzNew

"""
Show the time in US, UK, and MY timezones
@input: User's Time, GMT, and time differennce between US, UK, and/or MY
@returns: display of time auto-converted in US, UK, and MY timezones
"""
def display(t, tzUS, tzUK, tzMY):
    sys.stdout.write("\033[4A") # Move cursor up 4 steps in terminal
    sys.stdout.write("\033[J")  # Remove all lines till bottom (Make sure to be in this window for it to work)

    # Print Time
    us=tzConvert(t, tzUS);   print(f"US Time: {us[0]}:{us[1]}{us[2]} GMT-5")
    uk=tzConvert(t, tzUK);   print(f"UK Time: {uk[0]}:{uk[1]}{uk[2]} GMT+0")
    my=tzConvert(t, tzMY);   print(f"MY Time: {my[0]}:{my[1]}{my[2]} GMT+8")

def main():
    # Getting User's Timezone
    tz = input("Enter Your Timezone (us/uk/my): ")
    if tz== "us": us= +0;  uk= +4; my= +12
    if tz== "uk": us= -4;  uk= +0; my= +8
    if tz== "my": us= -12; uk= -8; my= +0

    # Getting User's Time
    t = [0]*3
    t[0] = int(input("Enter Hour (1-12): "))
    t[1] = int(input("Enter Minute (0-60): "))
    t[2] = input("Enter Meridiem (am/pm): ")

    # Error Handling
    if (t[0]<1 or t[0]>12) or (t[1]<0 or t[1]>60) or (t[2]!="am" and t[2]!="pm"):
        print("Fuck you, fuck your mom, fuck your dad, fuck your grandma, fuck your grandpa, fuck your entire bloodline\nExiting Program")
        sys.exit()

    display(t, us, uk, my)       # Display

if __name__ == "__main__":
    main()