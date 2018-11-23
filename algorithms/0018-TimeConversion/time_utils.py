import re

def convert_time(am_pm_time):
    if not am_pm_time:
        return ''

    matches = re.match( r'^([0-1][0-9]):([0-5][0-9]):([0-5][0-9])(AM|PM)$', am_pm_time)

    if not matches:
        return ''

    hours = matches.group(1)
    minutes = matches.group(2)
    seconds = matches.group(3)
    period = matches.group(4)

    if period == 'AM':
        if hours == '12':
            hours = '00'
    elif hours != '12':
        hours = str(12 + int(hours))

    converted = "%s:%s:%s" % (hours, minutes, seconds)

    return converted
