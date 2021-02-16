"""
Prompt
Write a function that returns the acute angle between two clock hands, with two integers for the
number of hours and number of minutes.
E.g. For 3:00, the acute angle would be 90°. For 6:00, it would be 180°.
"""


# Assume 60 ticks on clock, therefore each tick is 6 degrees
def ticksToAngle(t) ->int:
    return t * 6


# each hour occurs at 5 ticks
def hoursToTicks(h) -> int:
    return 0 if h == 12 else h * 5


def ClockHandAngle(hours, minutes) -> int:
    # convert everything to angles
    m_angle = ticksToAngle(minutes)
    h_angle = ticksToAngle(hoursToTicks(hours))
    return abs(h_angle - m_angle)


def main():

    # simple test cases
    cases = [(12, 15), (3, 30),(6, 00), (8,22), (10,55), (12, 1), (11, 59), (12, 59), (12,0)]
    for times in cases:
        h = times[0]
        m = times[1]
        str_m = "0" + str(m) if len(str(m)) == 1 else str(m)
        print(" -------The time is " + str(h) + ":" + str_m + " ---------")
        print ("at angle: ", ClockHandAngle(h,m))


main()
