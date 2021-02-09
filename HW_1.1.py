duration = int(input("Введите промежуток времени в секундах: "))

result = ''

if duration > 86400:
    days = duration // 86400
    duration = duration-(days*86400)
    days = str(days) + " days "
    result = days

if duration > 3600:
    hours = duration // 3600
    duration = duration - (hours*3600)
    hours = str(hours) + " hours "
    result = result + hours

if duration > 60:
    minute = duration // 60
    duration = duration - (minute*60)
    minute = str(minute) + " minutes "
    result = result + minute

sec = duration % 60
sec = str(sec) + " seconds "
result = result + sec

print(result)