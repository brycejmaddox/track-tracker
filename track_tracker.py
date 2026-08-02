times = []
loop = True
event = input("Event:")
def find_fastest(times):
    try:
        fastest = times[0]
        for i,value in enumerate(times):
            if value < fastest:
                fastest = value
        return fastest
    except IndexError:
        return "No times recorded yet"
def find_slowest(times):
    try:
        slowest = times[0]
        for i,value in enumerate(times):
            if value > slowest:
                slowest = value
        return slowest
    except IndexError:
        return "No times recorded yet"
def average(times):
    try:
        avg = sum(times) / len(times)
        return avg
    except ZeroDivisionError:
        return "No times recorded yet"
while loop:
    goal = input("What would you like to do (add/remove/replace time, find fastest/slowest time, average of times)? If you are done, type 'Done' or 'Thank you': ").lower()
    if goal == "add time":
        time = float(input("Time:"))
        times.append(time)
        print("New list of times:")
        for i,value in enumerate(times):
            print(1 + i, value)
    elif goal == "remove time":
        time = float(input("Time:"))
        times.remove(time)
        print("New list of times:")
        for i,value in enumerate(times):
            print(1 + i, value)
    elif goal == "replace time":
        time1 = float(input("Time to remove:"))
        times.remove(time1)
        time2 = float(input("Time to add:"))
        times.append(time2)
        print("New list of times:")
        for i,value in enumerate(times):
            print(1 + i, value)
    elif goal == "find fastest time":
        print(f"Fastest {event} time:", find_fastest(times))
    elif goal == "find slowest time":
        print(f"Slowest {event} time:", find_slowest(times))
    elif goal == "average of times":
        print(f"Your average 100m time this season is {average(times)}")
    elif goal == "thank you" or goal == "done":
        loop = False
print("Till next time!")



        
