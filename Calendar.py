import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    head_ru = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]
    month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mounth = 1
    week = []
    cal = []

    year = input("Введите год: ")

    for mounth in range(12):
        max_day = days_in_month[mounth]
        dat = datetime.date(int(year), mounth + 1, 1)
        week = feel_week(dat.weekday())
        cal.append([0,'\033[1m' + str(month_list[mounth]) + '\033[0m',0,0,0,0,0])
        cal.append(head_ru)
        for d in range(1, max_day + 1):
            if(len(week) > 6):
                cal.append(week)
                week = []
            if(len(week) <= 6):
                week.append(d)
            if((len(week) == 7) and (d == max_day)):
                cal.append(week)
        if((len(week) <= 6)):
                for i in range(len(week) - 1, 6):
                    week.append(0)
                cal.append(week)
        cal.append([0,0,0,0,0,0,0])
    print_cal(cal[:-1])

def print_cal(cal):
    for week in cal:
        print_week(week)

def print_week(week):
    colored_week = ["", "", "", "", "", "", ""]
    for i in range(0, 7):
        if((week[i] == 8) or (week[i] == 23)):
            if((i == 6) or (i == 5)):
                if(len(str(week[i])) == 2):
                    colored_week[4] = '\033[94m' + str(week[4]) + '\033[0m'
                else:
                    colored_week[4] = ' \033[94m' + str(week[4]) + '\033[0m'
                colored_week[i] = week[i]
            else:
                if(len(str(week[i])) == 2):
                    colored_week[i] =  '\033[94m' + str(week[i]) + '\033[0m'
                else:
                    colored_week[i] =  ' \033[94m' + str(week[i]) + '\033[0m'
        else:
            if(week[i] == 0):
                colored_week[i] = " "
            else:
                colored_week[i] = week[i]
        if((i == 6) or (i == 5)):
            if(week[i] == 0):
                colored_week[i] = " "
            else:
                if(len(str(week[i])) == 2):
                    colored_week[i] = '\033[92m' + str(week[i]) + '\033[0m'
                else:
                    colored_week[i] = ' \033[92m' + str(week[i]) + '\033[0m'
    print('{:2} {:2} {:2} {:2} {:2} {:2} {:2}'.format(colored_week[0], colored_week[1], colored_week[2], colored_week[3], colored_week[4], colored_week[5], colored_week[6]))


def feel_week2(x, cal):
    for i in range(x - 1, 6):
        cal[len[cal]].append(0)

def feel_week(f):
    week = []
    for i in range(0, int(f)):
        week.append(0)
    return week

if __name__=="__main__":
    main()