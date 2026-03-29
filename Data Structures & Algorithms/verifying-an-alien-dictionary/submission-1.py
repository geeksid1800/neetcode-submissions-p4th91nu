class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        priority = dict()
        for ix, ch in enumerate(order): priority[ch] = ix

        if len(words)<2: return True #0 or 1 words are always sorted
        for i in range(len(words)-1): #compare i and i+1
            first, second = words[i], words[i+1]
            for ix in range(max(len(first), len(second))):
                if ix >= len(second): #second word is over but first isn't
                    print(f"Compared {first=} and {second=} at {ix=}. Second is shorter")
                    return False
                if ix < len(first) and priority[first[ix]] > priority[second[ix]]:
                    print(f"Compared {first=} and {second=} at {ix=}, {first[ix]=} and {second[ix]=}. Second is smaller lexic")
                    print(f"{priority=}")
                    return False
                if ix < len(first) and priority[first[ix]] < priority[second[ix]]:
                    break
        
        return True