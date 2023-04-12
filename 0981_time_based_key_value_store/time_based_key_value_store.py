class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = {
                "values": [],
                "times": []
            }
        self.hashmap[key]["values"].append(value)
        self.hashmap[key]["times"].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        n = len(self.hashmap[key]["times"])
        for i in reversed(range(n)):
            if self.hashmap[key]["times"][i] <= timestamp:
                return self.hashmap[key]["values"][i]
        
        return ""
