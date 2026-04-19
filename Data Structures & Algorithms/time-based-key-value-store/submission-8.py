from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))
        print(self.dic[key])
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.dic[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        #error is if not found, you need to go for the timestamp just below
        #if timestamp is too low then you return ""

        return res