
processes = [
    ["P1", 0, 3, 3],
    ["P2", 1, 4, 2],
    ["P3", 2, 6, 4],
    ["P4", 3, 4, 6],
    ["P5", 5, 2, 10]
]


print("\n========== PREEMPTIVE PRIORITY SCHEDULING ==========\n")

n = len(processes)

remaining_bt = []
ct = [0] * n


for p in processes:
    remaining_bt.append(p[2])

time = 0
completed = 0

execution = []

while completed < n:

    selected = -1
    highest_priority = 999

    for i in range(n):

        if processes[i][1] <= time and remaining_bt[i] > 0:

            if processes[i][3] < highest_priority:
                highest_priority = processes[i][3]
                selected = i

    if selected == -1:
        execution.append("Idle")
        time += 1
        continue


    execution.append(processes[selected][0])

    remaining_bt[selected] -= 1
    time += 1

    # Check if process is completed
    if remaining_bt[selected] == 0:
        ct[selected] = time
        completed += 1


print("Execution Sequence:")

previous = ""

for process in execution:

    if process != previous:

        if previous != "":
            print(" > ", end="")

        print(process, end="")
        previous = process

print("\n")


total_wt = 0
total_tat = 0

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'PR':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")

for i in range(n):

    pid = processes[i][0]
    at = processes[i][1]
    bt = processes[i][2]
    priority = processes[i][3]

    tat = ct[i] - at
    wt = tat - bt

    print(f"{pid:<5}{at:<5}{bt:<5}{priority:<5}{ct[i]:<5}{tat:<5}{wt:<5}")

    total_wt += wt
    total_tat += tat


print()

preemptive_avg_tat = total_tat / n
preemptive_avg_wt = total_wt / n

print(f"Average TAT = {preemptive_avg_tat:.2f}")
print(f"Average WT  = {preemptive_avg_wt:.2f}")



# NON-PREEMPTIVE PRIORITY SCHEDULING

print("\n\n========== NON-PREEMPTIVE PRIORITY SCHEDULING ==========\n")


processes = [
    ["P1", 0, 3, 3],
    ["P2", 1, 4, 2],
    ["P3", 2, 6, 4],
    ["P4", 3, 4, 6],
    ["P5", 5, 2, 10]
]

time = 0

total_wt = 0
total_tat = 0

completed = []

schedule = []


while len(completed) < len(processes):

    ready = []

    for p in processes:

        if p[1] <= time and p not in completed:
            ready.append(p)

    if len(ready) == 0:
        time += 1
        continue

    ready.sort(key=lambda x: x[3])

    p = ready[0]

    pid = p[0]
    at = p[1]
    bt = p[2]
    priority = p[3]

    start_time = time
    ct = time + bt

    tat = ct - at
    wt = tat - bt

    schedule.append([pid, start_time, ct])

    time = ct

    total_wt += wt
    total_tat += tat

    completed.append(p)


print("Execution Sequence:")

for i, item in enumerate(schedule):

    if i != 0:
        print(" > ", end="")

    print(item[0], end="")

print("\n")

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'PR':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")

for item in schedule:

    pid = item[0]
    ct = item[2]

    for p in processes:

        if p[0] == pid:

            at = p[1]
            bt = p[2]
            priority = p[3]

            break

    tat = ct - at
    wt = tat - bt

    print(f"{pid:<5}{at:<5}{bt:<5}{priority:<5}{ct:<5}{tat:<5}{wt:<5}")


nonpreemptive_avg_tat = total_tat / len(processes)
nonpreemptive_avg_wt = total_wt / len(processes)

print()

print(f"Average TAT = {nonpreemptive_avg_tat:.2f}")
print(f"Average WT  = {nonpreemptive_avg_wt:.2f}")

