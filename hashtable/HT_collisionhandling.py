class HashTable:
    '''
    Hash table implementation with chaining as collision handling
    '''

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)

        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        found = False
        # case where there is a same key - then it is an update situation
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


if __name__ == "__main__":

    t = HashTable()

    t['apple'] = 3
    t['banana'] = 5

    print(t['apple'])
    print(t['banana'])

    t['banana'] = 4

    print(t['banana'])

    t['march 6'] = 10
    t['march 17'] = 45

    print(t.arr)

    t['march 17'] = 400

    print(t.arr)
