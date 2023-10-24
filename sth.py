def min_total_waiting_time(arr):
    arr.sort()  # Sort the list of session durations in ascending order
    total_waiting_time = 0

    for i in range(len(arr)):
        total_waiting_time += arr[i] * (len(arr) - 1 - i)

    return total_waiting_time

print(min_total_waiting_time([3,2,2,1,6]))

[1, 2, 2, 3, 6]
1-> 1 * 4 -> 4
2-> 2 * 3 -> 6
2-> 2 * 2 -> 4
3-> 3 * 1 -> 3
6-> 6 * 0 -> 0
