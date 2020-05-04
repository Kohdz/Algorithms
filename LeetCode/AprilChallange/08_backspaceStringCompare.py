



def build(X):
    ans = []
    for c in X:
        if c != '#':
            ans.append(c)
        elif ans:
            ans.pop()
    return "".join(ans)


def backspaceCompare(S, T):
    return build(S) == build(T)


S = "ab#c"
T = "ad#c"

S2 = "ab##"
T2 = "c#d#"
print(backspaceCompare(S, T))
print(backspaceCompare(S2, T2))
