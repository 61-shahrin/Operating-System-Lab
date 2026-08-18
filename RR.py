from collections import deque

processes = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 15],
    ["P4", 3, 11],
    ["P5", 4, 20],
    ["P6", 4, 9]

]

quantum = 5

def round_robin(processes, quantum):
    time = 0
    queue = deque()
    remaining = {
        p[0]: p[2]
        for p in processes
    }
    completion = {}
    sequence = []
    for p in processes:
        if p[1] <= time:
            queue.append(p[0])

    while queue:

        current = queue.popleft()


        run_time = min(
            quantum,
            remaining[current]
        )

        sequence.append(current)
        time += run_time
        remaining[current] -= run_time

        for p in processes:

            if (
                p[1] <= time
                and remaining[p[0]] > 0
                and p[0] not in queue
                and p[0] not in completion
                and p[0] != current
            ):
                queue.append(p[0])
        if remaining[current] == 0:

            completion[current] = time


        else:

            queue.append(current)

    result = []
    for name, at, bt in processes:

        ct = completion[name]
        tat = ct - at
        wt = tat - bt

        result.append([
            name,
            at,
            bt,
            ct,
            tat,
            wt
        ])

    return sequence, result


def fcfs(processes):

    time = 0
    sequence = []
    result = []

    for name, at, bt in processes:

        if time < at:
            time = at

        sequence.append(name)

        time += bt

        ct = time
        tat = ct - at
        wt = tat - bt

        result.append([name, at, bt, ct, tat, wt])

    return sequence, result

def sjf(processes):
    time = 0
    remaining = processes.copy()
    sequence = []
    result = []
    while remaining:

        available = [
            p for p in remaining
            if p[1] <= time
        ]

        if not available:
            time = min(p[1] for p in remaining)
            continue
        current = min(available, key=lambda p: p[2])
        name, at, bt = current
        sequence.append(name)

        time += bt

        ct = time
        tat = ct - at
        wt = tat - bt

        result.append([name, at, bt, ct, tat, wt])

        remaining.remove(current)

    return sequence, result




def print_result(algorithm, sequence, result):

    print("\n---------------------------------------")
    print(algorithm)
    print("------------------------------------------")
    print("\nCPU Sequence:")
    print(" -> ".join(sequence))
    print("\nProcess\t\tAT\t\tBT\t\tCT\t\tTAT\t\tWT")
    print("------------------------------------------------------")

    total_ct = 0
    total_tat = 0
    total_wt = 0

    for row in result:

        process, at, bt, ct, tat, wt = row

        print(
            f"{process}\t\t\t{at}\t\t{bt}\t\t{ct}\t\t{tat}\t\t{wt}"
        )

        total_ct += ct
        total_tat += tat
        total_wt += wt

    n = len(result)

    avg_ct = total_ct / n
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    print("----------------------------------------")
    print("Average CT  =", round(avg_ct, 2))
    print("Average TAT =", round(avg_tat, 2))
    print("Average WT  =", round(avg_wt, 2))

    return avg_wt, avg_tat, avg_ct




fcfs_sequence, fcfs_result = fcfs(processes)

sjf_sequence, sjf_result = sjf(processes)

rr_sequence, rr_result = round_robin(
    processes,
    quantum
)

rr_avg_wt, rr_avg_tat, rr_avg_ct = print_result(
    "ROUND ROBIN",
    rr_sequence,
    rr_result
)



fcfs_avg_wt, fcfs_avg_tat, fcfs_avg_ct = print_result(
    "FCFS",
    fcfs_sequence,
    fcfs_result
)

sjf_avg_wt, sjf_avg_tat, sjf_avg_ct = print_result(
    "SJF",
    sjf_sequence,
    sjf_result
)

print("\n\n----------------------------------------")
print("FINAL COMPARISON")
print("--------------------------------------------")

print("\nAlgorithm\t\tAvg CT\t\tAvg TAT\t\tAvg WT")
print("---------------------------------------------")

print(
    f"RR\t\t\t\t{rr_avg_ct:.2f}\t"
    f"\t{rr_avg_tat:.2f}\t\t"
    f"{rr_avg_wt:.2f}"
)

print(
    f"FCFS\t\t\t{fcfs_avg_ct:.2f}"
    f"\t\t{fcfs_avg_tat:.2f}\t"
    f"\t{fcfs_avg_wt:.2f}"
)

print(
    f"SJF\t\t\t\t{sjf_avg_ct:.2f}\t"
    f"\t{sjf_avg_tat:.2f}\t"
    f"\t{sjf_avg_wt:.2f}"
)

algorithms = {
    "RR": rr_avg_wt,
    "FCFS": fcfs_avg_wt,
    "SJF": sjf_avg_wt

}

best = min(algorithms, key=algorithms.get)

print("\nBest Algorithm =", best)
