# https://leetcode.com/problems/search-suggestions-system/


def suggestedProducts(products, searchWord):
    trie = {
        'words': []
    }

    def helper(t, word, deep):
        if word[deep:] == '':
            return
        idx = word[deep]
        if idx not in t:
            t[idx] = {
                'words': []
            }
        t[idx]['words'].append(word)
        helper(t[idx], word, deep + 1)

    for word in products:
        helper(trie, word, 0)

    res = []
    for i, w in enumerate(searchWord):

        if not trie or w not in trie:
            res += [[]] * (len(searchWord) - i)
            break

        res.append(sorted(trie[w]['words'])[:3])
        trie = trie[w]

    return res


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"

print(suggestedProducts(products, searchWord))
