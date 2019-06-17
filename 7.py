# 2.15 Example Marathon Training Data
#import math
# convert time in sec
def total_sec(min, sec):
    return min*60 + sec
# calculate speed in mph
def speed(time):
    return 3600/time
# ask user to input pace and mileage
pace_min=int(input('min per mile?: '))
pace_sec=int(input('sec per mile?: '))
miles=int(input('total miles?: '))

#calculate and print speed
mph = speed (total_sec(pace_min, pace_sec))
print('your speed is ' +str(mph) + 'mph')

#calculate elapsed time for planned training:
total=miles*total_sec(pace_min, pace_sec)
elapsed_min = total//60
elapsed_sec = total%60

print('Your elapsed time is '+str(elapsed_min)+ 'mins ' + str(elapsed_sec) + 'secs')



