# build a script that takes a date and time in my time zone
# return that time in 6 other timezones
import datetime
import pytz

FMT = '%Y-%m-%d %H:%M:%S %Z%z'


def timezonapalooza(time, zones_raw):
    zones = []

    for zone in zones_raw.split(','):
        zone = zone.strip()
        if zone in pytz.all_timezones:
            zones.append(zone)
        else:
            print('{} is not a valid timezone, removing it from list')

    if not zones:
        zones = [
            'US/Eastern',
            'Pacific/Auckland',
            'Asia/Calcutta',
            'Europe/Paris',
            'Asia/Tokyo',
            'Asia/Shanghai']

    pacific = pytz.timezone('US/Pacific')
    time_naive = datetime.datetime.strptime(time, '%m/%d/%Y %H:%M')
    time_pacific = pacific.localize(time_naive)
    time_utc = time_pacific.astimezone(pytz.utc)
    for zone in zones:
        zone = pytz.timezone(zone)
        print(time_utc.astimezone(zone).strftime(FMT))

while True:
    time = input('What time is your meeting? use MM/DD/YYYY HH:MM format. ')
    try:
        datetime.datetime.strptime(time, '%m/%d/%Y %H:%M')
        break
    except ValueError:
        print('That date isn\'t valid!')
        continue
zones_raw = input('Which timezones would you like to convert to?'
                  ' Please seperate them with commas. ')
timezonapalooza(time, zones_raw)
