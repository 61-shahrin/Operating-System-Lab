processes = [
    ["P1", 4, 2],
    ["P2", 2, 2],
    ["P3", 1, 3],
    ["P4", 0, 6],
    ["P5", 3, 1]
]

time_quantum = 2
n = len(processes)
remaining = {}

for p in processes:
    remaining[p[0]] = p[2]

CT = {}
sequence = []
time = 0

while len(CT) < n:
    available = []
    for p in processes:
        name = p[0]
        AT = p[1]
        if AT <= time and remaining[name] > 0:
            available.append(p)

    if len(available) == 0:
        time += 1
        continue

    current = min(
        available,
        key=lambda p: remaining[p[0]]
    )

    name = current[0]
    sequence.append(name)
    run_time = min(time_quantum, remaining[name])
    remaining[name] -= run_time
    time += run_time


    if remaining[name] == 0:
        CT[name] = time


TAT = {}
WT = {}

for p in processes:

    name = p[0]
    AT = p[1]
    BT = p[2]

    TAT[name] = CT[name] - AT
    WT[name] = TAT[name] - BT


print("Process Execution Sequence:")
print(" --> ".join(sequence))
print("\n")
print(f"{'P_ID':<8}{'AT':<8}{'BT':<8}{'CT':<8}{'TAT':<8}{'WT':<8}")
print("-" * 48)
total_tat = 0
total_wt = 0


for p in processes:

    name = p[0]
    AT = p[1]
    BT = p[2]

    print(
        f"{name:<8}"
        f"{AT:<8}"
        f"{BT:<8}"
        f"{CT[name]:<8}"
        f"{TAT[name]:<8}"
        f"{WT[name]:<8}"
    )

    total_tat += TAT[name]
    total_wt += WT[name]

avg_tat = total_tat / n
avg_wt = total_wt / n

print("-" * 48)
print(f"Average TAT = {avg_tat:.2f} sec")
print(f"Average WT  = {avg_wt:.2f} sec")
