import os, json, time, requests, clear
clear.c()
deletedevs = []
evdict = {}
mnp = []
evlist = []
url = ''
def main():
    global url
    global evdict
    global evlist
    global deletedevs
    global mnp
    clear.c()
    direc = input('Pick what number you would like to do, type the number and press enter\n----------------------------------------------------------------------\n1. Enter event url\n2. View events\n----------------------------------------------------------------------\n')
    if direc.isdigit() == False:
        clear.c()
        print('What you entered was not just a number, please try again in 5 seconds')
        time.sleep(5)
        main()
    if direc.isdigit() == True:
        if (int(direc) < 1) or (int(direc) > 2):
            clear.c()
            print('What you entered was not a valid number, please try again in 5 seconds')
            time.sleep(5)
            main()
        if 0 < int(direc) < 3:
            clear.c()
            regionlist = ['NAE', 'NAW', 'EU', 'ASIA', 'ME', 'OCE', 'BR']
            regionlistinput = ['1. NAE', '2. NAW', '3. EU', '4. ASIA', '5. ME', '6. OCE', '7. BR']
            region = input('What region would you like to look at, type the number and press enter\n----------------------------------------------------------------------\n' + '\n'.join(regionlistinput) + '\n----------------------------------------------------------------------\n')
            if region.isdigit() == False:
                clear.c()
                print('What you entered was not just a number, please try again in 5 seconds')
                time.sleep(5)
                main()
            if region.isdigit() == True:
                if (int(region) < 1) or (int(region) > 7):
                    clear.c()
                    print('What you entered was not a valid number, please try again in 5 seconds')
                    time.sleep(5)
                    main()
                if 0 < int(region) < 8:
                    region = regionlist[int(region) - 1]
                    url = 'https://fortnitetracker.com/events?region=' + region
                    r = requests.get(url)
                    htmlcode = r.text
                    obj = htmlcode.split('var imp_calendar =')[1].split(';')[0]
                    evobj = json.loads(obj)
                    a = 0
                    while a < len(evobj):
                        exec('ev' + str(a + 1) + ' = evobj[a]')
                        if eval('\"Bugha\" in ev' + str(a + 1) + '[\'customData\'][\'title\']') == True:
                            exec('deletedevs.append(ev' + str(a + 1) + ')')
                        if eval('\"Bugha\" in ev' + str(a + 1) + '[\'customData\'][\'title\']') == False:
                            exec('mnp.append(ev' + str(a + 1) + ')')
                        a = a + 1
                    a = 0
                    while a < len(mnp):
                        exec('ev' + str(a + 1) + ' = mnp[a]')
                        exec('ev' + str(a + 1) + 'cd = ev' + str(a + 1) + '[\'customData\']')
                        exec('ev' + str(a + 1) + 'nm = ev' + str(a + 1) + 'cd[\'title\']')
                        exec('ev' + str(a + 1) + 'wdtest = ev' + str(a + 1) + 'cd[\'windows\']')
                        if eval('len(ev' + str(a + 1) + 'wdtest) == 1') == True:
                            exec('ev' + str(a + 1) + 'wd = ev' + str(a + 1) + 'wdtest[0]')
                            exec('ev' + str(a + 1) + 'snm = ev' + str(a + 1) + 'wd[\'name\']')
                            exec('ev' + str(a + 1) + 'spath = ev' + str(a + 1) + 'wd[\'eventId\'] + \'/\' + ev' + str(a + 1) + 'wd[\'eventWindowId\']')
                            if eval('ev' + str(a + 1) + 'nm in evdict') == False:
                                exec('evdict[ev' + str(a + 1) + 'nm] = {ev' + str(a + 1) + 'snm: ev' + str(a + 1) + 'spath}')
                            if eval('ev' + str(a + 1) + 'nm in evdict') == True:
                                exec('evdict[ev' + str(a + 1) + 'nm][ev' + str(a + 1) + 'snm] = ev' + str(a + 1) + 'spath')
                        if eval('len(ev' + str(a + 1) + 'wdtest) == 1') == False:
                            b = 0
                            while eval('b < len(ev' + str(a + 1) + 'wdtest)'):
                                exec('ev' + str(a + 1) + 'wd' + str(b + 1) + ' = ev' + str(a + 1) + 'wdtest[b]')
                                exec('ev' + str(a + 1) + 'wd' + str(b + 1) + 'snm = ev' + str(a + 1) + 'wd' + str(b + 1) + '[\'name\']')
                                exec('ev' + str(a + 1) + 'wd' + str(b + 1) + 'spath = ev' + str(a + 1) + 'wd' + str(b + 1) + '[\'eventId\'] + \'/\' + ev' + str(a + 1) + 'wd' + str(b + 1) + '[\'eventWindowId\']')
                                if eval('ev' + str(a + 1) + 'nm in evdict') == False:
                                    exec('evdict[ev' + str(a + 1) + 'nm] = {ev' + str(a + 1) + 'wd' + str(b + 1) + 'snm: ev' + str(a + 1) + 'wd' + str(b + 1) + 'spath}')
                                if eval('ev' + str(a + 1) + 'nm in evdict') == True:
                                    exec('evdict[ev' + str(a + 1) + 'nm][ev' + str(a + 1) + 'wd' + str(b + 1) + 'snm] = ev' + str(a + 1) + 'wd' + str(b + 1) + 'spath')
                                b = b + 1
                        a = a + 1
                    events = eval(str(evdict.keys()).split('(')[1].split(')')[0])
                    a = 0
                    prevents = []
                    while a < len(evdict):
                        exec('prevents.append(\'' + str(a + 1) + '. \' + events[a] + \': \' + str(len(evdict[events[a]])) + \' SESSIONS\')')
                        a = a + 1
                    clear.c()
                    print('\n'.join(prevents) + '\n-----------------------------------------------------\nType the number event you would like to look at\n')
                    direc = input('')
                    if direc.isdigit() == False:
                        clear.c()
                        print('This is not a number, try again in 5 seconds')
                        time.sleep(5)
                        main()
                    if direc.isdigit() == True:
                        selev = evdict[prevents[int(direc) - 1].split(':')[0].split('. ')[1]]
                        a = 0
                        selevses = eval(str(selev.keys()).split('(')[1].split(')')[0])
                        prselevses = []
                        while a < len(selevses):
                            prselevses.append(str(a + 1) + '. ' + selevses[a])
                            a = a + 1
                        clear.c()
                        print('\n'.join(prselevses) + '\n-------------\nWhich session would you like to look at? Please pick the number\n')
                        direc = input('')
                        selevsesstr = selevses[int(direc) - 1]
                        evpath = selev[selevsesstr]
main()
