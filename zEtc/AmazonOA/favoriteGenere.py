# https://leetcode.com/discuss/interview-question/373006

import collections


def favor(userSongs, songGenres):
    res = {}
    d = {s: g for g in songGenres for s in songGenres[g]}
    for name, songs in userSongs.items():
        c = collections.Counter(d[s] for s in songs if s in d)
        mxcnt = max(c.values() or [0])
        res[name] = [g for g in c if c[g] == mxcnt]
    return res


userSongs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma":  ["song5", "song6", "song7"]
}
songGenres = {
    "Rock":    ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno":  ["song2", "song4"],
    "Pop":     ["song5", "song6"],
    "Jazz":    ["song8", "song9"]
}

print(favor(userSongs, songGenres))
