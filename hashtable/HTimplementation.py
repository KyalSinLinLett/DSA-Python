class HashTable:

    def __init__(self):
        self.MAX_SIZE = 100
        self.arr = [None for i in range(self.MAX_SIZE)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)

        return h % self.MAX_SIZE

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == "__main__":

    t = HashTable()

    t['apple'] = 3
    t['banana'] = 5

    print(t['apple'])
    print(t['banana'])

    t['banana'] = 4

    print(t['banana'])
