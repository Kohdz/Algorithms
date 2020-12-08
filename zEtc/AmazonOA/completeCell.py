def cellCompete(states, days):

    new = states[:]  # get a copy of the array
    n = len(states)

    if n == 1:
        print(0)  # when only 1 node, return [0]

    for _ in range(days):
        new[0] = states[1]  # determine the edge nodes first
        new[n - 1] = states[n - 2]

        for i in range(1, n-1):
            # logic for the rest nodes
            new[i] = 1 - (states[i-1] == states[i+1])
        states = new[:]  # update the list for the next day

    return new
