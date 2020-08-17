def dfs(s, path, k, idx):

    if len(path) == k:
        result.append(path)
        return

    for i in range(idx, len(s)):
        dfs(s, path + s[i], k, i + 1)

result = []
char = 'abc'
combination_lenght = 2
dfs(char, '', combination_lenght, 0)
print(result)