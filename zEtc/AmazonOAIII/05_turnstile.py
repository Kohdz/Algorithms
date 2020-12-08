# Turnstile


from collections import deque

# time O(n) and space O(n)
# n = size(time)

def turnstile(numCust, arrT, directions):
    i = 0
    enter = deque()
    exit = deque()
    res = [-1] * numCust
    time = 0
    status = True  # True == exit / False == enter

    while i < numCust or enter or exit:
        while i < numCust and arrT[i] <= time:
            if directions[i] == 1:
                exit.append(i)
            else:
                enter.append(i)
            i += 1

        if enter or exit:
            # if previous sec is exit/not used and exit queue is not empty
            if exit and status:
                res[exit.popleft()] = time
            # if previous sec is enter and enter queue is not empty
            elif enter and not status:  #
                res[enter.popleft()] = time
            # enter queue is empty and exit is not
            elif exit:
                res[exit.popleft()] = time
                status = True
            # exit queue is empty and enter is not
            elif enter:
                res[enter.popleft()] = time
                status = False
        else:
            status = True
            # skip time if next arrival time is longer than 1 sec
            time = arrT[i] - 1

        time += 1

    return res


customers = [16, 5, 20, 1, 4, 5]
arrTime = [
    [0, 0, 1, 2, 6, 6, 7, 7, 7, 10, 11, 12, 12, 12, 12, 14],
    [0, 1, 1, 3, 3],
    [0, 1, 3, 4, 4, 4, 10, 11, 15, 17, 21, 21, 23, 24, 24, 25, 27, 28, 29, 29],
    [10],
    [0, 0, 1, 5],
    [0, 1, 1, 5, 5]
]
direction = [
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0],
    [0, 1, 1, 0],
    [0, 1, 0, 0, 1]
]
expected = [
    [0, 1, 2, 3, 13, 6, 7, 8, 9, 10, 11, 14, 12, 15, 16, 17],
    [0, 2, 1, 4, 3],
    [0, 1, 3, 4, 5, 6, 10, 11, 15, 17, 22, 21, 23, 24, 25, 26, 27, 28, 29, 30],
    [10],
    [2, 0, 1, 5],
    [0, 2, 1, 6, 5]
]


for i in range(0, len(customers)):
    assert (turnstile(customers[i], arrTime[i], direction[i]) == expected[i])
