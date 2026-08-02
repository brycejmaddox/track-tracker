times = []
loop = True
event = input("Event:")
def find_fastest(times):
    fastest = times[0]
    for i in range(len(times)):
        if times[i] < fastest:
            fastest = times[i]
    return fastest
def find_slowest(times):
    slowest = times[0]
    for i in range(len(times)):
        if times[i] > slowest:
            slowest = times[i]
    return slowest
def average(times):
    avg = sum(times) / len(times)
    return avg
while loop:
    goal = input("What would you like to do (add/remove/replace time, find fastest/slowest time, average of times)? If you are done, type 'Done' or 'Thank you': ").lower()
    if goal == "add time":
        time = float(input("Time:"))
        times.append(time)
        print("New list of times:")
        for i in range(len(times)):
            print(1 + i, times[i])
    elif goal == "remove time":
        time = float(input("Time:"))
        times.remove(time)
        print("New list of times:")
        for i in range(len(times)):
            print(1 + i, times[i])
    elif goal == "replace time":
        time1 = float(input("Time to remove:"))
        times.remove(time1)
        time2 = float(input("Time to add:"))
        times.append(time2)
        print("New list of times:")
        for i in range(len(times)):
            print(1 + i, times[i])
    elif goal == "find fastest time":
        print(f"Fastest {event} time:", find_fastest(times))
    elif goal == "find slowest time":
        print(f"Slowest {event} time:", find_slowest(times))
    elif goal == "average of times":
        print(f"Your average 100m time this season is {average(times)}")
    elif goal == "thank you" or goal == "done":
        loop = False
print("Till next time!")



        
