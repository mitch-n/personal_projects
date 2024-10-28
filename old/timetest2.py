import datetime

time=datetime.datetime(2020, 12, 3, 13, 00)

print(time.astimezone(tz=datetime.timezone.utc))
