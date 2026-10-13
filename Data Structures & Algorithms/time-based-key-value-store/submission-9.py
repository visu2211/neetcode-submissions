class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        arr = self.cache[key]
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            ts, val = arr[mid]

            if ts <= timestamp:
                res = val
                l = mid + 1
            else:
                r = mid - 1
        return res