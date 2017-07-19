import random
class Class:
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday"]
    def __init__(self,classname):
        self.name = classname
        self.timetable = {"Sunday":{},"Monday":{},"Tuesday":{},"Wednesday":{},"Thursday":{}}
    def display(self):
        print self.name
        string = '+'
        for i in range(89):
            string += '-'
        print string + '+'
        print '|         |    1    |    2    |    3    |    4    |    5    |    6    |    7    |    8    |'
        string = '|'
        for i in range(89):
            string += '-'
        print string + '|'
        for d in self.days:
            string = '|' + d
            for e in range(10 - len(string)):
                string += " "
            string += '|'
            for b in range(1,9):
                if b in self.timetable[d]:
                    added = self.timetable[d][b]
                    string += added
                    for c in range(9 - len(added)):
                        string += " "
                else:
                    string += "         "
                string += "|"
            print string
        string = '+'
        for i in range(89):
            string += '-'
        print string + '+'
        print
    def labadd(self,detaillist,period):
        self.timetable[detaillist[0]][detaillist[1][0]] = period
        self.timetable[detaillist[0]][detaillist[1][1]] = period
    def coreadd(self,L,subject):
        for add in L:
            self.timetable[add[0]][add[1]] = subject
    def electivesadd(self,listtobeadded,elective):
        for a in listtobeadded:
            self.timetable[a[0]][a[1]] = elective
    
def randomize_labs():
    periods_to_select = [["Sunday",(5,6)],["Sunday",(7,8)],["Monday",(5,6)],["Monday",(7,8)],["Tuesday",(5,6)],["Tuesday",(7,8)],["Wednesday",(5,6)],
                         ["Wednesday",(7,8)],["Thursday",(5,6)],["Thursday",(7,8)],["Sunday",(5,6)],["Sunday",(7,8)],["Monday",(5,6)],["Monday",(7,8)],
                         ["Tuesday",(5,6)],["Tuesday",(7,8)],["Wednesday",(5,6)],["Wednesday",(7,8)],["Thursday",(5,6)],["Thursday",(7,8)]]
    chemtaken = []
    phytaken = []
    returnlist = ()
    for i in range(8):
        while True:
            phylab = random.choice(periods_to_select)
            if phylab not in phytaken:
                phytaken.append(phylab)
                break
        while True:
            chemlab = random.choice(periods_to_select)
            if chemlab != phylab and chemlab not in chemtaken:
                chemtaken.append(chemlab)
                break
        periods_to_select.remove(phylab)
        periods_to_select.remove(chemlab)
        returnlist += ([phylab , chemlab],)
    return returnlist

def randomize_electivelabs(obj,elective):
    electives_to_select = [["Sunday",(5,6)],["Sunday",(7,8)],["Monday",(5,6)],["Monday",(7,8)],["Tuesday",(5,6)],["Tuesday",(7,8)],["Wednesday",(5,6)],
                         ["Wednesday",(7,8)],["Thursday",(5,6)],["Thursday",(7,8)]]
    to_remove = []
    for i in obj.timetable:
        if 5 in obj.timetable[i]:
            if 7 not in obj.timetable[i]:
                for j in range(len(electives_to_select)):
                    if electives_to_select[j][0] == i and electives_to_select[j][1][0] == 5:
                        to_remove.append(j)
            else:
                for x in range(len(electives_to_select)):
                    if electives_to_select[x][0] == i:
                        to_remove.append(x)
        elif 7 in obj.timetable[i]:
            for k in range(len(electives_to_select)):
                if electives_to_select[k][0] == i and electives_to_select[k][1][0] == 7:
                    to_remove.append(k)
    count = 0
    for l in sorted(to_remove):
        item = electives_to_select.pop(l - count)
        count += 1
    sub = ''
    if elective == 'B':
        sub = 'Bio Lab'
    elif elective == 'C':
        sub = 'Comp Lab'
    elif elective == 'E':
        sub = 'EG Lab'
    subL = electivelabs_occupied[sub]
    to_remove = []
    for q in range(len(electives_to_select)):
        if electives_to_select[q] in subL:
            to_remove.append(q)
    count = 0
    for m in sorted(to_remove):
        item = electives_to_select.pop(m - count)
        count += 1
    ranchoice = random.choice(electives_to_select)
    electivelabs_occupied[sub].append(ranchoice)
    return ranchoice

def randomize_phy(obj,elective,option = False):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday"]
    table = obj.timetable
    if option != False:
        for i in phy_occupied[option]["days"]:
            days.remove(i)
    phyday1 = random.choice(days)
    days.remove(phyday1)
    phyday2 = random.choice(days)
    phyperiodsday1 = range(1,9)
    phyperiodsday2 = range(1,9)
    for x in table[phyday1]:
        phyperiodsday1.remove(x)
    for y in table[phyday2]:
        phyperiodsday2.remove(y)
    if option != False:
        for m in phy_occupied[option][phyday1]:
            if m in phyperiodsday1:
                phyperiodsday1.remove(m)
        for n in phy_occupied[option][phyday2]:
            if n in phyperiodsday2:
                phyperiodsday2.remove(n)
    phyday1period1 = random.choice(phyperiodsday1)
    phyperiodsday1.remove(phyday1period1)
    phyday1period2 = random.choice(phyperiodsday1)
    phyday2period1 = random.choice(phyperiodsday2)
    phyperiodsday2.remove(phyday2period1)
    phyday2period2 = random.choice(phyperiodsday2)
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday"]
    days.remove(phyday1)
    days.remove(phyday2)
    phyperiodsday3 = range(1,9)
    for a in table[days[0]]:
        phyperiodsday3.remove(a)
    if option != False:
        for o in phy_occupied[option][days[0]]:
            if o in phyperiodsday3:
                phyperiodsday3.remove(o)
    phyday3 = random.choice(phyperiodsday3)
    phyperiodsday4 = range(1,9)
    for b in table[days[1]]:
        phyperiodsday4.remove(b)
    if option != False:
        for p in phy_occupied[option][days[1]]:
            if p in phyperiodsday4:
                phyperiodsday4.remove(p)
    phyday4 = random.choice(phyperiodsday4)
    phyperiodsday5 = range(1,9)
    for c in table[days[2]]:
        phyperiodsday5.remove(c)
    if option != False:
        for r in phy_occupied[option][days[2]]:
            if r in phyperiodsday5:
                phyperiodsday5.remove(r)
    phyday5 = random.choice(phyperiodsday5)
    phy_occupied[elective] = {"days":[]}
    phy_occupied[elective]["days"].append(phyday1)
    phy_occupied[elective]["days"].append(phyday2)
    phy_occupied[elective][days[0]] = [phyday3]
    phy_occupied[elective][days[1]] = [phyday4]
    phy_occupied[elective][days[2]] = [phyday5]
    phy_occupied[elective][phyday1] = [phyday1period1]
    phy_occupied[elective][phyday1].append(phyday1period2)
    phy_occupied[elective][phyday2] = [phyday2period1]
    phy_occupied[elective][phyday2].append(phyday2period2)
    return [(phyday1,phyday1period1),(phyday1,phyday1period2),(phyday2,phyday2period1),(phyday2,phyday2period2),(days[0],phyday3),(days[1],phyday4),(days[2],phyday5)]

def randomize_chem(obj,elective,option = False):
    while True:
        br = True
        d = ["Sunday","Monday","Tuesday","Wednesday","Thursday"]
        table = obj.timetable
        if option != False:
            for i in chem_occupied[option]["days"]:
                d.remove(i)    
        while True:
            days = []
            for i in d:
                days.append(i)
            chemday1 = random.choice(days)
            days.remove(chemday1)
            chemday2 = random.choice(days)
            chemperiodsday1 = range(1,9)
            chemperiodsday2 = range(1,9)
            for x in table[chemday1]:
                chemperiodsday1.remove(x)
            for y in table[chemday2]:
                chemperiodsday2.remove(y)
            if option != False:
                for m in chem_occupied[option][chemday1]:
                    if m in chemperiodsday1:
                        chemperiodsday1.remove(m)
                for n in chem_occupied[option][chemday2]:
                    if n in chemperiodsday2:
                        chemperiodsday2.remove(n)
            if len(chemperiodsday1) >= 2 and len(chemperiodsday2) >= 2:
                break
        chemday1period1 = random.choice(chemperiodsday1)
        chemperiodsday1.remove(chemday1period1)
        chemday1period2 = random.choice(chemperiodsday1)
        chemday2period1 = random.choice(chemperiodsday2)
        chemperiodsday2.remove(chemday2period1)
        chemday2period2 = random.choice(chemperiodsday2)
        days = ["Sunday","Monday","Tuesday","Wednesday","Thursday"]
        days.remove(chemday1)
        days.remove(chemday2)
        chemperiodsday3 = range(1,9)
        for a in table[days[0]]:
            chemperiodsday3.remove(a)
        if option != False:
            for o in chem_occupied[option][days[0]]:
                if o in chemperiodsday3:
                    chemperiodsday3.remove(o)
        try:
            chemday3 = random.choice(chemperiodsday3)
        except:
            br = False
        chemperiodsday4 = range(1,9)
        for b in table[days[1]]:
            chemperiodsday4.remove(b)
        if option != False:
            for p in chem_occupied[option][days[1]]:
                if p in chemperiodsday4:
                    chemperiodsday4.remove(p)
        try:
            chemday4 = random.choice(chemperiodsday4)
        except:
            br = False
        chemperiodsday5 = range(1,9)
        for c in table[days[2]]:
            chemperiodsday5.remove(c)
        if option != False:
            for r in chem_occupied[option][days[2]]:
                if r in chemperiodsday5:
                    chemperiodsday5.remove(r)
        try:
            chemday5 = random.choice(chemperiodsday5)
        except:
            br = False
        if br:
            break
    chem_occupied[elective] = {"days":[]}
    chem_occupied[elective]["days"].append(chemday1)
    chem_occupied[elective]["days"].append(chemday2)
    chem_occupied[elective][days[0]] = [chemday3]
    chem_occupied[elective][days[1]] = [chemday4]
    chem_occupied[elective][days[2]] = [chemday5]
    chem_occupied[elective][chemday1] = [chemday1period1]
    chem_occupied[elective][chemday1].append(chemday1period2)
    chem_occupied[elective][chemday2] = [chemday2period1]
    chem_occupied[elective][chemday2].append(chemday2period2)
    return [(chemday1,chemday1period1),(chemday1,chemday1period2),(chemday2,chemday2period1),(chemday2,chemday2period2),(days[0],chemday3),(days[1],chemday4),
            (days[2],chemday5)]

def randomize_electives(obj,elective,occupied=False):
    table = obj.timetable
    possibilities = []
    for i in range(1,9):
        if i not in table["Sunday"]:
            possibilities.append(("Sunday",i))
    for j in range(1,9):
        if j not in table["Monday"]:
            possibilities.append(("Monday",j))
    for k in range(1,9):
        if k not in table["Tuesday"]:
            possibilities.append(("Tuesday",k))
    for l in range(1,9):
        if l not in table["Wednesday"]:
            possibilities.append(("Wednesday",l))
    for m in range(1,9):
        if m not in table["Thursday"]:
            possibilities.append(("Thursday",m))
    if occupied:
        if elective == 'B':
            for removeitem in electives_occupied['Biology']:
                if removeitem in possibilities:
                    possibilities.remove(removeitem)
        elif elective == 'C1':
            for removeitem in electives_occupied['Computer1']:
                if removeitem in possibilities:
                    possibilities.remove(removeitem)
        elif elective == 'C2':
            for removeitem in electives_occupied['Computer2']:
                if removeitem in possibilities:
                    possibilities.remove(removeitem)
        elif elective == 'EG':
            for removeitem in electives_occupied['EG']:
                if removeitem in possibilities:
                    possibilities.remove(removeitem)
    l = []
    for a in possibilities:
        if a[0] not in l:
            l.append(a[0])
    if len(l) == 5:
        select = []
        for x in possibilities:
            if x[0] == 'Sunday':
                select.append(x)
        first = random.choice(select)
        select = []
        for x in possibilities:
            if x[0] == 'Monday':
                select.append(x)
        second = random.choice(select)
        select = []
        for x in possibilities:
            if x[0] == 'Tuesday':
                select.append(x)
        third = random.choice(select)
        select = []
        for x in possibilities:
            if x[0] == 'Wednesday':
                select.append(x)
        fourth = random.choice(select)
        select = []
        for x in possibilities:
            if x[0] == 'Thursday':
                select.append(x)
        fifth = random.choice(select)
    elif len(l) == 4:
        select = []
        for x in possibilities:
            if x[0] == l[0]:
                select.append(x)
        first = random.choice(select)
        select = []
        for x in possibilities:
            if x[0] == l[1]:
                select.append(x)
        second = random.choice(select)
        select = []
        for x in possibilities:
            if x[0] == l[2]:
                select.append(x)
        third = random.choice(select)
        select = []
        for x in possibilities:
            if x[0] == l[3]:
                select.append(x)
        fourth = random.choice(select)
        fifth = random.choice(possibilities)
    elif len(l) == 3:
        select = []
        for x in possibilities:
            if x[0] == l[0]:
                select.append(x)
        first = random.choice(select)
        select = []
        for x in possibilities:
            if x[0] == l[1]:
                select.append(x)
        second = random.choice(select)
        select = []
        for x in possibilities:
            if x[0] == l[2]:
                select.append(x)
        third = random.choice(select)
        fourth = random.choice(possibilities)
        fifth = random.choice(possibilities)
    if elective == 'B':
        electives_occupied['Biology'].append(first)
        electives_occupied['Biology'].append(second)
        electives_occupied['Biology'].append(third)
        electives_occupied['Biology'].append(fourth)
        electives_occupied['Biology'].append(fifth)
    elif elective == 'C1':
        electives_occupied['Computer1'].append(first)
        electives_occupied['Computer1'].append(second)
        electives_occupied['Computer1'].append(third)
        electives_occupied['Computer1'].append(fourth)
        electives_occupied['Computer1'].append(fifth)
    elif elective == 'C2':
        electives_occupied['Computer2'].append(first)
        electives_occupied['Computer2'].append(second)
        electives_occupied['Computer2'].append(third)
        electives_occupied['Computer2'].append(fourth)
        electives_occupied['Computer2'].append(fifth)
    elif elective == 'EG':
        electives_occupied['EG'].append(first)
        electives_occupied['EG'].append(second)
        electives_occupied['EG'].append(third)
        electives_occupied['EG'].append(fourth)
        electives_occupied['EG'].append(fifth)
    return (first,second,third,fourth,fifth)

def randomize_math(obj):
    table = obj.timetable
    possibilities = []
    for i in range(1,9):
        if i not in table["Sunday"]:
            possibilities.append(("Sunday",i))
    for j in range(1,9):
        if j not in table["Monday"]:
            possibilities.append(("Monday",j))
    for k in range(1,9):
        if k not in table["Tuesday"]:
            possibilities.append(("Tuesday",k))
    for l in range(1,9):
        if l not in table["Wednesday"]:
            possibilities.append(("Wednesday",l))
    for m in range(1,9):
        if m not in table["Thursday"]:
            possibilities.append(("Thursday",m))
    first = random.choice(possibilities)
    possibilities.remove(first)
    second = random.choice(possibilities)
    possibilities.remove(second)
    third = random.choice(possibilities)
    possibilities.remove(third)
    fourth = random.choice(possibilities)
    possibilities.remove(fourth)
    fifth = random.choice(possibilities)
    possibilities.remove(fifth)
    sixth = random.choice(possibilities)
    possibilities.remove(sixth)
    seventh = random.choice(possibilities)
    return (first,second,third,fourth,fifth,sixth,seventh)

def randomize_eng(obj):
    table = obj.timetable
    possibilities = []
    for i in range(1,9):
        if i not in table["Sunday"]:
            possibilities.append(("Sunday",i))
    for j in range(1,9):
        if j not in table["Monday"]:
            possibilities.append(("Monday",j))
    for k in range(1,9):
        if k not in table["Tuesday"]:
            possibilities.append(("Tuesday",k))
    for l in range(1,9):
        if l not in table["Wednesday"]:
            possibilities.append(("Wednesday",l))
    for m in range(1,9):
        if m not in table["Thursday"]:
            possibilities.append(("Thursday",m))
    first = random.choice(possibilities)
    possibilities.remove(first)
    second = random.choice(possibilities)
    possibilities.remove(second)
    third = random.choice(possibilities)
    possibilities.remove(third)
    fourth = random.choice(possibilities)
    return (first,second,third,fourth)

def assign_freeperiods(obj):
    table = obj.timetable
    possibilities = []
    for i in range(1,9):
        if i not in table["Sunday"]:
            possibilities.append(("Sunday",i))
    for j in range(1,9):
        if j not in table["Monday"]:
            possibilities.append(("Monday",j))
    for k in range(1,9):
        if k not in table["Tuesday"]:
            possibilities.append(("Tuesday",k))
    for l in range(1,9):
        if l not in table["Wednesday"]:
            possibilities.append(("Wednesday",l))
    for m in range(1,9):
        if m not in table["Thursday"]:
            possibilities.append(("Thursday",m))
    return possibilities

class_11SciD = Class('11SciD')
class_11SciE = Class('11SciE')
class_11SciF = Class('11SciF')
class_11SciG = Class('11SciG')
class_12SciD = Class('12SciD')
class_12SciE = Class('12SciE')
class_12SciF = Class('12SciF')
class_12SciG = Class('12SciG')

labs_to_be_added = randomize_labs()
electivelabs_occupied = {'Bio Lab':[],'Comp Lab':[],'EG Lab':[]}
phy_occupied = {}
chem_occupied = {}
electives_occupied = {'Biology':[],'Computer1':[],'Computer2':[],'EG':[]}

class_11SciD.labadd(labs_to_be_added[0][0],'Phy Lab')
class_11SciD.labadd(labs_to_be_added[0][1],'Chem Lab')
class_11SciE.labadd(labs_to_be_added[1][0],'Phy Lab')
class_11SciE.labadd(labs_to_be_added[1][1],'Chem Lab')
class_11SciF.labadd(labs_to_be_added[2][0],'Phy Lab')
class_11SciF.labadd(labs_to_be_added[2][1],'Chem Lab')
class_11SciG.labadd(labs_to_be_added[3][0],'Phy Lab')
class_11SciG.labadd(labs_to_be_added[3][1],'Chem Lab')

class_12SciD.labadd(labs_to_be_added[4][0],'Phy Lab')
class_12SciD.labadd(labs_to_be_added[4][1],'Chem Lab')
class_12SciE.labadd(labs_to_be_added[5][0],'Phy Lab')
class_12SciE.labadd(labs_to_be_added[5][1],'Chem Lab')
class_12SciF.labadd(labs_to_be_added[6][0],'Phy Lab')
class_12SciF.labadd(labs_to_be_added[6][1],'Chem Lab')
class_12SciG.labadd(labs_to_be_added[7][0],'Phy Lab')
class_12SciG.labadd(labs_to_be_added[7][1],'Chem Lab')

class_11SciD.labadd(randomize_electivelabs(class_11SciD,'B'),'Bio Lab')
class_11SciE.labadd(randomize_electivelabs(class_11SciE,'C'),'Comp Lab')
class_11SciF.labadd(randomize_electivelabs(class_11SciF,'C'),'Comp Lab')
class_11SciG.labadd(randomize_electivelabs(class_11SciG,'E'),'EG Lab')
class_12SciD.labadd(randomize_electivelabs(class_12SciD,'B'),'Bio Lab')
class_12SciE.labadd(randomize_electivelabs(class_12SciE,'C'),'Comp Lab')
class_12SciF.labadd(randomize_electivelabs(class_12SciF,'C'),'Comp Lab')
class_12SciG.labadd(randomize_electivelabs(class_12SciG,'E'),'EG Lab')

class_11SciD.coreadd(randomize_phy(class_11SciD,'1B'),"Physics")
class_11SciE.coreadd(randomize_phy(class_11SciE,'1C1'),"Physics")
class_11SciF.coreadd(randomize_phy(class_11SciF,'1C2'),"Physics")
class_11SciG.coreadd(randomize_phy(class_11SciG,'1EG'),"Physics")
class_12SciD.coreadd(randomize_phy(class_12SciD,'2B','1B'),"Physics")
class_12SciE.coreadd(randomize_phy(class_12SciE,'2C1','1C1'),"Physics")
class_12SciF.coreadd(randomize_phy(class_12SciF,'2C2','1C2'),"Physics")
class_12SciG.coreadd(randomize_phy(class_12SciG,'2EG','1EG'),"Physics")

class_11SciD.coreadd(randomize_chem(class_11SciD,'1B'),"Chemistry")
class_11SciE.coreadd(randomize_chem(class_11SciE,'1C1'),"Chemistry")
class_11SciF.coreadd(randomize_chem(class_11SciF,'1C2'),"Chemistry")
class_11SciG.coreadd(randomize_chem(class_11SciG,'1EG'),"Chemistry")
class_12SciD.coreadd(randomize_chem(class_12SciD,'2B','1B'),"Chemistry")
class_12SciE.coreadd(randomize_chem(class_12SciE,'2C1','1C1'),"Chemistry")
class_12SciF.coreadd(randomize_chem(class_12SciF,'2C2','1C2'),"Chemistry")
class_12SciG.coreadd(randomize_chem(class_12SciG,'2EG','1EG'),"Chemistry")

class_11SciD.electivesadd(randomize_electives(class_11SciD,'B'),'Biology')
class_11SciE.electivesadd(randomize_electives(class_11SciE,'C1'),'Computer')
class_11SciF.electivesadd(randomize_electives(class_11SciF,'C2'),'Computer')
class_11SciG.electivesadd(randomize_electives(class_11SciG,'EG'),'EG')
class_12SciD.electivesadd(randomize_electives(class_12SciD,'B',True),'Biology')
class_12SciE.electivesadd(randomize_electives(class_12SciE,'B',True),'Computer')
class_12SciF.electivesadd(randomize_electives(class_12SciF,'B',True),'Computer')
class_12SciG.electivesadd(randomize_electives(class_12SciG,'B',True),'EG')

class_11SciD.electivesadd(randomize_math(class_11SciD),'Maths')
class_11SciE.electivesadd(randomize_math(class_11SciE),'Maths')
class_11SciF.electivesadd(randomize_math(class_11SciF),'Maths')
class_11SciG.electivesadd(randomize_math(class_11SciG),'Maths')
class_12SciD.electivesadd(randomize_math(class_12SciD),'Maths')
class_12SciE.electivesadd(randomize_math(class_12SciE),'Maths')
class_12SciF.electivesadd(randomize_math(class_12SciF),'Maths')
class_12SciG.electivesadd(randomize_math(class_12SciG),'Maths')

class_11SciD.electivesadd(randomize_eng(class_11SciD),'English')
class_11SciE.electivesadd(randomize_eng(class_11SciE),'English')
class_11SciF.electivesadd(randomize_eng(class_11SciF),'English')
class_11SciG.electivesadd(randomize_eng(class_11SciG),'English')
class_12SciD.electivesadd(randomize_eng(class_12SciD),'English')
class_12SciE.electivesadd(randomize_eng(class_12SciE),'English')
class_12SciF.electivesadd(randomize_eng(class_12SciF),'English')
class_12SciG.electivesadd(randomize_eng(class_12SciG),'English')

class_11SciD.electivesadd(assign_freeperiods(class_11SciD),'Work Exp')
class_11SciE.electivesadd(assign_freeperiods(class_11SciE),'Work Exp')
class_11SciF.electivesadd(assign_freeperiods(class_11SciF),'Work Exp')
class_11SciG.electivesadd(assign_freeperiods(class_11SciG),'Work Exp')
class_12SciD.electivesadd(assign_freeperiods(class_12SciD),'Work Exp')
class_12SciE.electivesadd(assign_freeperiods(class_12SciE),'Work Exp')
class_12SciF.electivesadd(assign_freeperiods(class_12SciF),'Work Exp')
class_12SciG.electivesadd(assign_freeperiods(class_12SciG),'Work Exp')

file_handle = open('Instructions.txt')
print file_handle.read()
file_handle.close()
print
class_11SciD.display()
class_11SciE.display()
class_11SciF.display()
class_11SciG.display()
class_12SciD.display()
class_12SciE.display()
class_12SciF.display()
class_12SciG.display()
