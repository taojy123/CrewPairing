import csv               
import calendar

class Virgin:
    @staticmethod
    def reader (a) :
        jancok = []
        read = []
        locked = []
        
        for i in a:
            read.append(i)

        for i in range(len(read)) :
           read[i]= read[i][0].split()

        for i in read :
            if  i[0] == "F" or i[0] == "U" :
                blocknumber = int(i[-1][1:])
                if i[0] == "F" :
                    status = "Locked"
                else :
                    status = "Unlocked"
                locked.append(status)
                base = i[1]
                daytodate = { 1 : [], 2 : [], 3 : [], 4:  [], 5 : [], 6 : [], 7 : []}
                daydic = { 1 : 'N', 2 : 'N', 3 : 'N', 4:  'N', 5 : 'N', 6 : 'N', 7 : 'N'}
                for j in i[2] :
                    if j == "1":
                        daydic[1] = "Y"
                    elif j == "2":
                        daydic[2] = "Y"
                    elif j == "3":
                        daydic[3] = "Y"
                    elif j == "4":
                        daydic[4] = "Y"
                    elif j == "5":
                        daydic[5] = "Y"
                    elif j == "6":
                        daydic[6] = "Y"
                    elif j == "7":
                        daydic[7] = "Y"

                firstyear = int(i[3][4:])
                firstmonth = int(i[3][0:2])
                firstdate = int(i[3][2:4])
                
                lastyear = int(i[4][4:])
                lastmonth = int(i[4][0:2])
                lastdate = int(i[4][2:4])

                firstday = (calendar.weekday(firstyear, firstmonth, firstdate))+1
                
                ## inserting dates to daytodate
                daytodate[firstday].append(firstdate)
                if firstday+1 > 7 :            
                    if daydic[firstday+1-7] == "Y" :
                        daytodate[firstday+1-7].append(firstdate+1)
                else :
                    if daydic[firstday+1] == "Y" :
                        daytodate[firstday+1].append(firstdate+1)
                if firstday+2 > 7 : 
                    if daydic[firstday+2-7] == "Y" :
                        daytodate[firstday+2-7].append(firstdate+2)
                else :
                    if daydic[firstday+2] == "Y" :
                        daytodate[firstday+2].append(firstdate+2)
                if firstday+3 > 7 : 
                    if daydic[firstday+3-7] == "Y" :
                        daytodate[firstday+3-7].append(firstdate+3)
                else :
                    if daydic[firstday+3] == "Y" :
                        daytodate[firstday+3].append(firstdate+3)
                if firstday+4 > 7 : 
                    if daydic[firstday+4-7] == "Y" :
                        daytodate[firstday+4-7].append(firstdate+4)
                else :
                    if daydic[firstday+4] == "Y" :
                        daytodate[firstday+4].append(firstdate+4)
                if firstday+5 > 7 : 
                    if daydic[firstday+5-7] == "Y" :
                        daytodate[firstday+5-7].append(firstdate+5)
                else :
                    if daydic[firstday+5] == "Y" :
                        daytodate[firstday+5].append(firstdate+5)
                if firstday+6 > 7 : 
                    if daydic[firstday+6-7] == "Y" :
                        daytodate[firstday+6-7].append(firstdate+6)
                else :
                    if daydic[firstday+6] == "Y" :
                        daytodate[firstday+6].append(firstdate+6)


                ## if range is between 7 and 13 days
                if 7 <= lastdate - firstdate :
                    daytodate[firstday].append(firstdate+7)           
                    if firstday+1 > 7 :            
                        if daydic[firstday+1-7] == "Y" :
                            daytodate[firstday+1-7].append(firstdate+8)
                    else :
                        if daydic[firstday+1] == "Y" :
                            daytodate[firstday+1].append(firstdate+8)
                    if firstday+2 > 7 : 
                        if daydic[firstday+2-7] == "Y" :
                            daytodate[firstday+2-7].append(firstdate+9)
                    else :
                        if daydic[firstday+2] == "Y" :
                            daytodate[firstday+2].append(firstdate+9)
                    if firstday+3 > 7 : 
                        if daydic[firstday+3-7] == "Y" :
                            daytodate[firstday+3-7].append(firstdate+10)
                    else :
                        if daydic[firstday+3] == "Y" :
                            daytodate[firstday+3].append(firstdate+10)
                    if firstday+4 > 7 : 
                        if daydic[firstday+4-7] == "Y" :
                            daytodate[firstday+4-7].append(firstdate+11)
                    else :
                        if daydic[firstday+4] == "Y" :
                            daytodate[firstday+4].append(firstdate+11)
                    if firstday+5 > 7 : 
                        if daydic[firstday+5-7] == "Y" :
                            daytodate[firstday+5-7].append(firstdate+12)
                    else :
                        if daydic[firstday+5] == "Y" :
                            daytodate[firstday+5].append(firstdate+12)
                    if firstday+6 > 7 : 
                        if daydic[firstday+6-7] == "Y" :
                            daytodate[firstday+6-7].append(firstdate+13)
                    else :
                        if daydic[firstday+6] == "Y" :
                            daytodate[firstday+6].append(firstdate+13)

                    
                ## if range is more than 2 weeks
                if 14 <= lastdate - firstdate :
                    daytodate[firstday].append(firstdate+14)           
                    if firstday+1 > 7 :            
                        if daydic[firstday+1-7] == "Y" :
                            daytodate[firstday+1-7].append(firstdate+15)
                    else :
                        if daydic[firstday+1] == "Y" :
                            daytodate[firstday+1].append(firstdate+15)
                    if firstday+2 > 7 : 
                        if daydic[firstday+2-7] == "Y" :
                            daytodate[firstday+2-7].append(firstdate+16)
                    else :
                        if daydic[firstday+2] == "Y" :
                            daytodate[firstday+2].append(firstdate+16)
                    if firstday+3 > 7 : 
                        if daydic[firstday+3-7] == "Y" :
                            daytodate[firstday+3-7].append(firstdate+17)
                    else :
                        if daydic[firstday+3] == "Y" :
                            daytodate[firstday+3].append(firstdate+17)
                    if firstday+4 > 7 : 
                        if daydic[firstday+4-7] == "Y" :
                            daytodate[firstday+4-7].append(firstdate+18)
                    else :
                        if daydic[firstday+4] == "Y" :
                            daytodate[firstday+4].append(firstdate+18)
                    if firstday+5 > 7 : 
                        if daydic[firstday+5-7] == "Y" :
                            daytodate[firstday+5-7].append(firstdate+19)
                    else :
                        if daydic[firstday+5] == "Y" :
                            daytodate[firstday+5].append(firstdate+19)
                    if firstday+6 > 7 : 
                        if daydic[firstday+6-7] == "Y" :
                            daytodate[firstday+6-7].append(firstdate+20)
                    else :
                        if daydic[firstday+6] == "Y" :
                            daytodate[firstday+6].append(firstdate+20)

                ## if range is more than 3 weeks
                if 21 <= lastdate - firstdate  :
                    daytodate[firstday].append(firstdate+21)           
                    if firstday+1 > 7 :            
                        if daydic[firstday+1-7] == "Y" :
                            daytodate[firstday+1-7].append(firstdate+22)
                    else :
                        if daydic[firstday+1] == "Y" :
                            daytodate[firstday+1].append(firstdate+22)
                    if firstday+2 > 7 : 
                        if daydic[firstday+2-7] == "Y" :
                            daytodate[firstday+2-7].append(firstdate+23)
                    else :
                        if daydic[firstday+2] == "Y" :
                            daytodate[firstday+2].append(firstdate+23)
                    if firstday+3 > 7 : 
                        if daydic[firstday+3-7] == "Y" :
                            daytodate[firstday+3-7].append(firstdate+24)
                    else :
                        if daydic[firstday+3] == "Y" :
                            daytodate[firstday+3].append(firstdate+24)
                    if firstday+4 > 7 : 
                        if daydic[firstday+4-7] == "Y" :
                            daytodate[firstday+4-7].append(firstdate+25)
                    else :
                        if daydic[firstday+4] == "Y" :
                            daytodate[firstday+4].append(firstdate+25)
                    if firstday+5 > 7 : 
                        if daydic[firstday+5-7] == "Y" :
                            daytodate[firstday+5-7].append(firstdate+26)
                    else :
                        if daydic[firstday+5] == "Y" :
                            daytodate[firstday+5].append(firstdate+26)
                    if firstday+6 > 7 : 
                        if daydic[firstday+6-7] == "Y" :
                            daytodate[firstday+6-7].append(firstdate+27)
                    else :
                        if daydic[firstday+6] == "Y" :
                            daytodate[firstday+6].append(firstdate+27)
                    
                ## if range is more than 4 weeks
                if 28 <= lastdate - firstdate :
                    daytodate[firstday].append(firstdate+28)           
                    if firstday+1 >28 :            
                        if daydic[firstday+1-7] == "Y" :
                            daytodate[firstday+1-7].append(firstdate+29)
                    else :
                        if daydic[firstday+1] == "Y" :
                            daytodate[firstday+1].append(firstdate+29)
                    if firstday+2 > 7 : 
                        if daydic[firstday+2-7] == "Y" :
                            daytodate[firstday+2-7].append(firstdate+30)
                    else :
                        if daydic[firstday+2] == "Y" :
                            daytodate[firstday+2].append(firstdate+30)
                   
            if i[0] == 'O' or i[0] == "D" :
                for j in daytodate :
                    for k in daytodate[j] :
                        jancok.append([status, blocknumber, base, k + int(i[1]) -1, i[2], i[3], i[4], i[5], i[6], i[7]])

        jancok.sort(key = lambda x: (int(x[1]), int(x[3])))
        jancok.insert(0,["Status", "Block Number", "Base", "Date", "Plane Type","Stays With Plane", "Flight Number", "Departure City", "Departure Time", "Arrival City", "Arrival Time"])

        return (jancok,locked)

    @staticmethod
    def aospreader(aosp_file="JanuaryAOSPgs0002.rpt"):
        #fh = open("JanuaryAOSPgs0002.rpt", "r")
        fh = open(aosp_file, "r")
        line = "line"
        lines = []
        final = []
        while line:
            stuff = []
            #print(line.replace("\n", "\\n"))
            if line == "***********************************************\n":
                # print(line.replace("\n", "\\n")) 
                while line[0:9] != "THE BLOCK":
                    line = fh.readline()
                    stuff.append(line)
                lines.append(stuff)
                line = fh.readline()
            line = fh.readline()
            # print(line.replace("\n", "\\n")) 
        for x in lines:
            new = []
            legs = []
            paths = []
            new_line = x.pop(0)
            new.append(Virgin.numGet(new_line[30:-1])) # TRIP NUMBER
            new_line = x.pop(0)
            new.append(new_line[34:-1]) # OPERATION RANGE
            new_line = x.pop(0)
            new.append(new_line[34:-1]) # TRIP DAYS
            new_line = x.pop(0)
            new.append(new_line[34:-1]) # CREW POSITIONS
            x.pop(0) # GETTING RID OF BLANK LINE
            new_line = x.pop()
            new.append((new_line[20:-1].strip())) # BLOCK TIME
            new_line = x.pop()
            new.append((new_line[20:-1].strip())) # Artificial Cost
            new_line = x.pop()
            new.append(new_line[30:-1].strip()) # SOFT PERCsENT
            new_line = x.pop()
            new.append(new_line[25:-1].strip()) # SOFT HOURS
            new_line = x.pop()
            new.append(new_line[30:-1].strip()) # PRODUCTION DAYS
            new_line = x.pop()
            new.append(new_line[30:-1].strip()) # DUTY PERIODS
            new_line = x.pop()
            new.append((new_line[30:-1].strip())) # CREW COST
            totals = x.pop()
            new.append(totals.strip())
            for y in x:
                leg = []
                flight_num = y[3:7]
                if flight_num == "----":
                    continue
                flight_num = int(flight_num)
                departureCity = y[8:11]
                flight_time = y[30:35]
                ground_time = y[36:44].strip()
                if y[44:45] == "*":
                    stay_with_plane = True
                else:
                    stay_with_plane = False
                leg.append(flight_num)
                leg.append(flight_time)
                leg.append(ground_time)
                leg.append(stay_with_plane)
                leg.append(departureCity)
                paths.append(leg)
            new.append(paths)
            final.append(new)
        return final

    @staticmethod
    def numGet(number):
        number = number.strip()
        if len(number) > 1 and number[0] == '0':
            num = number[1:]
        else:
            num = number
            if num == '':
                num = '0'
        return int(num)
    @staticmethod
    def timeGet(time):
        hours = Virgin.numGet(time[:-3])
        mins = Virgin.numGet(time[-2:])
        totalmins = hours+mins
        return totalmins
    @staticmethod
    def timeChanger(time, airport):
        PST = ["SEA", "PDX","SFO","LAS","SJC","LAX","PSP","SAN"]
        MST = ["SJD"]
        CST = ["PVR", "DFW", "AUS", "ORD", "CUN"]
        EST = ["BOS", "JFK", "EWR", "PHL", "IAD", "DCA", "MCO", "FLL"]
        if airport in PST:
            newtime = Virgin.timeChangerHelper(time,-800)
        elif airport in MST:
            newtime = Virgin.timeChangerHelper(time,-700)
        elif airport in CST:
            newtime = Virgin.timeChangerHelper(time,-600)
        else:
            newtime = Virgin.timeChangerHelper(time,-500)
        return newtime
    @staticmethod
    def timeChangerHelper(time, val):
        newtime = time + val
        if newtime < 0:
            newtime = 2400 + newtime
        return newtime
    @staticmethod
    def summer(lists):
        sum = 0
        for x in lists:
            sum+= Virgin.timeGet(x[10])
        return sum
    @staticmethod
    def locker(collin_legs, locked):
        i = 0
        while i<len(locked):
            collin_legs[i].insert(1,locked[i])
            i+=1
        return collin_legs
    @staticmethod
    def combiner(prg_file="january.prg.txt", aosp_file="JanuaryAOSPgs0002.rpt"):
        collin_legs = Virgin.aospreader(aosp_file)
        #file=open("january.prg.txt",'r')
        file=open(prg_file,'r')
        csvreader=csv.reader(file,dialect="excel")
        jancok = Virgin.reader(csvreader)
        kenzie = jancok[0]
        collin = Virgin.locker(collin_legs,jancok[1])
        file.close()
        return collin, kenzie
    @staticmethod
    def astrixAdder(pairings): #Adds the astrix to kenzie's code
        # takes in a tuple with collin's pairings in 0 and kenzie's in 1
        new_pairings = []
        collin = pairings[0]
        kenzie = pairings[1]

        for x in kenzie[1:]:
            # print(x)
            for y in collin:
                for z in y[13]:
                    # print(z)
                    if z[0] == int(x[5]) and y[0] == x[1] and z[4] == x[6]:
                        # print(z[0],int(x[5]),y[0],x[1])
                        # print(x,z[3])
                        x.insert(5,z[3])
        countCollin = 0
        adjCollin = []
        for x in collin:
            number_of_reps = len(x[3])
            number_of_legs = len(x[13])
            countCollin += number_of_legs*number_of_reps
            for y in x[13]:
                # print(y)
                pass
        return kenzie
    @staticmethod
    def csvWriter(pairings, output_file="january.prg.csv"):
        new_csv = open(output_file,'w')
        csvwriter = csv.writer(new_csv)
        csvwriter.writerows(pairings)
        new_csv.close()
    @staticmethod
    def swapper(pairings):
        pass
        #code

if __name__ == "__main__":
    pairings = Virgin.combiner("january.prg.txt", "JanuaryAOSPgs0002.rpt");
    pairings = Virgin.astrixAdder(pairings) # put the astrix in kenzie's code
    Virgin.csvWriter(pairings, "january.prg.csv")
    for x in pairings:
        print(x)
    print("done")
    Virgin.swapper(pairings)
