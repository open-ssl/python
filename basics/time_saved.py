'''
One cause for speeding is the desire to shorten the time spent traveling.
In long distance trips speeding does save an appreciable amount of time.
However, the same cannot be said about short distance trips.

Create a function that calculates the amount of time saved were you traveling
with an average speed that is above the speed-limit as compared to traveling
with an average speed exactly at the speed-limit.
'''


def time_saved(speed1, speed2, distance):
    result = lambda x: (distance / (x / 60))
    return round(result(speed1) - result(speed2), 1)
print(time_saved(80, 90, 40) )
# ➞ 3.3

print(time_saved(80, 90, 4000))
 # ➞ 333.3
#
print(time_saved(80, 100, 40 ))
 # ➞ 6.0

print(time_saved(80, 100, 10))
# ➞ 1.5
