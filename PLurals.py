import datetime
# 16.07.2021 20:30
def choose_plural(num, word):
    if num != 0 and num % 100 != 11 and num % 10 == 1:
        cho = word[0]  # копейка
    elif num <= 20 and num >= 10 or num % 10 == 0:
        cho = word[2]  # копеек
    elif num % 100 <= 20 and num % 100 >= 10:
        cho = word[2]  # копеек
    elif num % 10 in [5, 6, 7, 8, 9]:
        cho = word[2]  # копеек
    else:
        cho = word[1]  # копейки
    return '{} {}'.format(num, cho)
try:
    in_d = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ')
    date_x = datetime.datetime.strptime(in_d, '%d.%m.%Y %H:%M')
    now_time = datetime.datetime.now().replace(second=0, microsecond=0)
    if date_x < now_time:
        print('Ошибка')
    delta_time = date_x - now_time
    days = delta_time.days
    secs = delta_time.seconds
    mins_total = secs // 60
    hrs = mins_total // 60
    mins = mins_total - hrs * 60
    if days >= 1:  # 'До часа "Икс" ' + choose_plural(days, ["день", "дня", "дней"]) + " " + choose_plural(hrs, ["час", "часа", "часов"]) + " " +
        days_res = choose_plural(days, ["день", "дня", "дней"] + ' ')
    else:
        days_res = ""
    if hrs != 0:
        hrs_res = choose_plural(hrs, ["час", "часа", "часов"] + ' ')
    else:
        hrs_res = ""
    if mins != 0:
        mins_res = choose_plural(mins, ["минута", "минуты ", "минут"])
    else:
        mins_res = ""
    print('До часа "Икс" ' + days_res + hrs_res + mins_res)
except:
    print('Ошибка')
