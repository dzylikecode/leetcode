"""
https://leetcode.cn/problems/group-anagrams/?envType=study-plan-v2&envId=top-100-liked

## summary

考验的是如何设计哈希映射

"""
from collections import Counter


class Solution:
    """
    和上一题一样, 不过考验的就是 hash 编码了
    """
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res: dict[str, list[str]] = {}
        for s in strs:
            id = self.hashId(s)
            if id not in res:
                res[id] = []
            res[id].append(s)
        return list(res.values())

    def hashId(self, word: str):
        id = [0] * 26
        for ch in word:
            num = self.char_to_num(ch)
            id[num] += 1
        return tuple(id)

    _start = ord('a')
    def char_to_num(self, char):
        return ord(char) - Solution._start
