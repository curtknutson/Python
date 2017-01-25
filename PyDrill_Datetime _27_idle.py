# Python:   version 2.7.13

#Author:    Curt Knutson

#Purpose:   Demonstrate knowledge of Python 2.7 to
#           Display if offices in NYC and London are open,
#           based on current Portland time

from datetime import datetime

from pytz import timezone

def start():
    #timezone of offices
    hqTimeZone = timezone('US/Pacific')
    NYCTimeZone = timezone('US/Eastern')
    LondonTimeZone = timezone('Europe/London')

    #times of offices
    hqTime = getTime(hqTimeZone,hqTimeZone)
    NYCTime = getTime(hqTimeZone,NYCTimeZone)
    LondonTime = getTime(hqTimeZone,LondonTimeZone)
    timeformat = '%H:%M'

    print ("\nThe time in the Portland office is {}.".format(hqTime.strftime(timeformat)))
    print ("\nThe time in the NYC office is {} and it is {}."
           .format(NYCTime.strftime(timeformat),getOpen(NYCTime)))
    print ("\nThe time in the London office is {} and it is {}."
           .format(LondonTime.strftime(timeformat),getOpen(LondonTime)))

def getTime(hqTimeZone,officeTimeZone):
#   print("HQzone: ",hqTimeZone," Officezone: ",officeTimeZone)
    hqTime = datetime.now(hqTimeZone)
#    print("HQTime: ",hqTime)
    officeTime = hqTime.astimezone(officeTimeZone)
#    print("OfficeTime: ",officeTime)
    return officeTime

def getOpen(officeTime):
    if (officeTime.hour >=9 and officeTime.hour < 21):
        return "Open"
    else:
        return "Closed"


if __name__ == "__main__":
    start()
