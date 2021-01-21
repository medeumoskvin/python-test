import datetime


def convert(time):
    return str(datetime.timedelta(seconds=time))

time = int(input('введите время в секундах !'))


print(convert(time))