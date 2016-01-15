datetime
	import datetime
	*Common Properties*
		.datetime(year, day, hour, minute, second, microsecond)
			datetime.now() 		returns current time like:
				datetime.datetime(2016, 1, 12, 12, 55, 54, 915575)
					.replace(hour=9, minute=0, second=0, microsecond=0)
						*returns* datetime.datetime(2016, 1, 12, 9, 0)
		datetime.datetime.now() - datetime.datetime(2016, 1, 12, 9, 0)
			datetime.timedelta(0, 14408, 814493) *diff ->(day, sec, microsec)*
		.timedelta(day, second, microsecond)
			.timedelta(hours=5, seconds=0, microseconds=0)
				returns timedelda object, can use -/+ operators with this and dt obs
		.timezone()
			Naive datetimes can't use .timezone()
			make aware datetime by passing tzinfo into datetime with zone timedelta
					ex: pacific = dt.timezone(dt.timedelta(hours=-8))
 					aware = datetime.datetime(2014, 4, 21, 9, tzinfo=pacific)
		.astimezone()
 			get local time of datetime object
 			ex: eastern = datetime.timezone(dt.timedelta(hours=-5))
 				aware.astimezone(eastern)
pytz
	import pytz
	*Common Properties*
		.timezone()
			pacific = pytz.timezone('US/Pacific')
			eastern = pytz.timezone('US/Eastern')
				imports the named time zone
			event_pacific = pacific.localize(event)
				adds the pacific timezone to tzinfo
			event_eastern = event.astimezone(eastern)
				returns the same event localized to the new TZ
			pytz.utc
				returns the utc time zone
			event_utc = event.astimezone(utc)
				returns the event in the utc TZ
		.all_timezones
			returns an array of all pytz timezones
		.country_timezones()
			given 2 digit country string, returns all country's TZs
		