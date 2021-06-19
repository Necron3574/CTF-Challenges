from pwn import *

def solve(start_date,end_date,p1_schedule,p2_schedule):
    startmonth,startday = start_date.split()
    startmonth = int(startmonth[1:])
    startday = int(startday[1:])
    endmonth,endday = end_date.split()
    endmonth = int(endmonth[1:])
    endday = int(endday[1:])
    start_time = 30*startmonth + startday
    end_time = 30*endmonth + endday
    p1_inPerson,p1_virtual = p1_schedule.split()
    p1_inPerson = int(p1_inPerson[1:])
    p1_virtual = int(p1_virtual[1:])
    p2_inPerson,p2_virtual = p2_schedule.split()
    p2_inPerson = int(p2_inPerson[1:])
    p2_virtual = int(p2_virtual[1:])
    p1_state = "I"
    p2_state = "I"
    p1_count = 0
    p2_count = 0
    ans = 0
    weekend_list = []
    wknd_count = 0
    count = 0
    while count <361:
        if wknd_count ==5:
            weekend_list.append(count)
            weekend_list.append(count+1)
            wknd_count = 0
            count += 2
            pass
        wknd_count +=1
        count += 1
    for i in range(0,end_time+1):
        if i in weekend_list:
            continue
        if p1_state == p2_state and i>= start_time:
            ans += 1
        p1_count += 1
        p2_count += 1
        if p1_state == "I" and p1_count == p1_inPerson:
            p1_count = 0
            p1_state = "V"
        elif p1_state == "V" and p1_count == p1_virtual:
            p1_count = 0
            p1_state = "I"
        if p2_state == "I" and p2_count == p2_inPerson:
            p2_count = 0
            p2_state = "V"
        elif p2_state == "V" and p2_count == p2_virtual:
            p2_count = 0
            p2_state = "I"
    return ans
r = remote("class-meets.hsc.tf",1337)
print(r.recvline())
check = 0
for _ in range(15):
    print(r.recvline())
    print(r.recvline())
    start_date = r.recvline().decode().strip()
    end_date = r.recvline().decode().strip()
    p1_schedule = r.recvline().decode().strip()
    p2_schedule = r.recvline().decode().strip()
    r.sendline(str(solve(start_date,end_date,p1_schedule,p2_schedule)))
    print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
