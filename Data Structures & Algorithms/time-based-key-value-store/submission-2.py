class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        vals = self.cache.get(key, [])
        vals.append((timestamp, value))
        self.cache[key] = vals

    def get(self, key: str, timestamp: int) -> str:
        vals = self.cache.get(key, [])
        if not vals: return ""
        
        #find greatest timestamp in vals that is <= timestamp
        l, r = 0, len(vals)-1
        res = ""
        while l<=r:
            m = (l+r)//2
            if vals[m][0] <= timestamp:
                res = vals[m][1] #potential answer
                l = m+1
            else:
                r = m-1

        return res