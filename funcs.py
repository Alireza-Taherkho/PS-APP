
import jdatetime


def fix_calcute(val):
    l_operation = []
    l_val = []
    val = val.replace(' ', '')
    for i in val:
        if i == '+' or i == '-' or i == '*' or i == '/':
            l_operation.append(i)


    val = val.replace('+', ' ')
    val = val.replace('-', ' ')
    val = val.replace('/', ' ')
    val = val.replace('*', ' ')
    l = val.split(' ')
    for i in range(len(l)):
        if i + 1 == len(l):
            l_val.append(l[i])
            break

        l_val.append(l[i])
        l_val.append(' ')

    t = 0
    for i in range(len(l_val)):
        if l_val[i] == ' ':
            l_val[i] = l_operation[t]
            t += 1
    return l_val



def calcute_u_n(users, hour, minute, userlist, per_minute):
    #until_now
    userlist[0] , userlist[1]= userlist[0] // per_minute, userlist[1] // per_minute
    userlist[2] , userlist[3]= userlist[2] // per_minute, userlist[3] // per_minute

    hour2 = jdatetime.datetime.now().hour
    minute2 = jdatetime.datetime.now().minute


    if hour2 - hour < 0:
        h = (24 + (hour2 - hour))
    else:
        h = (hour2 - hour)

    if minute2 - minute < 0:
        m = 60 + (minute2 - minute)
        h -= 1
    else:
        m = (minute2 - minute)

    time = (h * 60) + m


    if users == 1:
        return round(userlist[0] * time), h, m
    elif users == 2:
        return round(userlist[1] * time), h, m
    elif users == 3:
        return round(userlist[2] * time), h, m
    elif users == 4:
        return round(userlist[3] * time), h, m




def show(val):
    for main in [val]:
        i = main['text']
        n = 0
        st = ''
        i = str(i)
        if len(i) > 3:
            for j in range(len(i)-1,-1,-1):
                if n == 3:
                    st += ','
                    n = 0
                st += i[j]
                n += 1
            i = ''
            for j in st[::-1]:
                i += j
            main['text'] = i



def show_entry(val):
    for main in val:
        i = main.get()
        n = 0
        st = ''
        i = str(i)
        if len(i) > 3:
            for j in range(len(i)-1,-1,-1):
                if n == 3:
                    st += ','
                    n = 0
                st += i[j]
                n += 1
            i = ''
            for j in st[::-1]:
                i += j
            main.set(i)

