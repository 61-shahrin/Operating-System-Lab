processes = [
    ["P0", 3, 1],
    ["P1", 5, 3],
    ["P2", 2, 2],
    ["P3", 1, 2],
    ["P4", 6, 3]
]


processes.sort(key=lambda x: x[1])

time = 0
total_tat = 0
total_wt = 0

print("ID\tAT\tBT\tCT\tTAT\tWT")

for p in processes:
    p_id, at, bt = p


    if time < at:
        time = at

    ct = time + bt
    tat = ct - at
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    print(f"{p_id}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    time = ct

n = len(processes)

print("\nAvg TAT =", total_tat / n)
print("Avg WT =", total_wt / n)

print("\nExecution Sequence:")
for p in processes:
    print(p[0], end=" -> ")
print("End")
