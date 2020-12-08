# Most Common Word

# https://leetcode.com/problems/most-common-word/

import collections, re

def mostCommonWordI(paragraph, banned):
    remove_chars = "[!?',;.']"
    paragraph = re.sub(remove_chars, ' ', paragraph)

    words = paragraph.split()
    dic = {}
    max_v = 0
    for word in words:
        word = word.lower()
        if word not in banned:
            dic[word] = dic.get(word, 0)+1
            if dic[word] > max_v:
                max_v = dic[word]
                res = word
    return res


def mostCommonWordII(paragraph, banned):

    clean_paragraph = ""
    for c in paragraph:
        if c in {',', '.', '!', ' '}:
            clean_paragraph += " "
        elif c.isalpha():
            clean_paragraph += c.lower()

    banned = set([x.lower().strip() for x in banned])

    words = [x for x in clean_paragraph.split() if x not in banned]

    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]
