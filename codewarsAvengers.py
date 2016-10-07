'''The new "Avengers" movie has just been released!
    There are a lot of people at the cinema box office standing in a huge line.

    Each of them has a single 100, 50 or 25 dollars bill.
    A "Avengers" ticket costs 25 dollars.

    A clerk wants to sell a ticket to every single person in this line.

    Can he/she sell a ticket to each person and give the change if he/she initially has no money
    and sells the tickets strictly in the order people follow in the line?

    Return YES, if Vasya can sell a ticket to each person and give the change.
    Otherwise return NO.'''

def tickets(people):
    t = []                #store the bills in a register list
    flag = True
    for bill in people:
        if sum(t) == 0 and bill == 25:
            t.append(bill)
        elif sum(t) >= 25 and (bill == 50 or bill == 25):
            if bill == 25:
                t.append(bill)
            elif 25 in t:
                t.append(bill)
                t.remove(25)
            else:
                flag = False
                break
        elif sum(t) >= 75 and bill == 100:
            try:                                            #try catch block in case
                if set([25, 50]).issubset(set(t)):          #in case values not in register
                    t.append(bill)
                    t.remove(25)
                    t.remove(50)
            except:
                flag = False
                break
            try:
                if set([25, 25, 25]).issubset(set(t)):
                    t.append(bill)
                    t.remove(25)
                    t.remove(25)
                    t.remove(25)
            except:
                flag = False
                break
        else:
            flag = False
            break

    if flag:
        return "YES"
    else:
        return "NO"

array = [25,25,25,25,25,25,25,25,25,25,25,25,25,25,50,50,50,50,50,100,100,100,100,100]
print tickets(array)
