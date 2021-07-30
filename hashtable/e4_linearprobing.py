class HashTable:
    '''
    Hash table implementation with linear probing as collision handling
    '''

    def __init__(self):
        self.MAX_SIZE = 10
        self.arr = [None for i in range(self.MAX_SIZE)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX_SIZE

    def linear_probe_set(self, index, key, val):
        if None not in self.arr:
            raise Exception('Table is full')

        # if there is already a value at the index
        if self.arr[index] is not None and self.arr[index][0] == key:
            self.arr[index] = (key, val)
            return

        if self.arr[index] is None:
            self.arr[index] = (key, val)
            return

        index = (index + 1) if index != self.MAX_SIZE-1 else 0
        self.linear_probe_set(index, key, val)

    def __setitem__(self, key, val):
        index = self.get_hash(key)

        self.linear_probe_set(index, key, val)

    def linear_probe_get(self, index, key):
        if self.arr[index][0] == key:
            return self.arr[index][1]

        index = (index + 1) if index != self.MAX_SIZE-1 else 0
        return self.linear_probe_get(index, key)

    def __getitem__(self, key):
        index = self.get_hash(key)

        if key not in [k for k, v in list(filter(lambda x: x is not None, self.arr))]:
            raise Exception('Invalid key!')

        return self.linear_probe_get(index, key)

    def linear_probe_del(self, index, key):
        if self.arr[index] is not None:
            if self.arr[index][0] == key:
                self.arr[index] = None
                return

        index = (index + 1) if index != self.MAX_SIZE-1 else 0
        return self.linear_probe_del(index, key)

    def __delitem__(self, key):
        index = self.get_hash(key)

        if key not in [k for k, v in list(filter(lambda x: x is not None, self.arr))]:
            raise Exception('Invalid key!')

        self.linear_probe_del(index, key)


if __name__ == "__main__":

    t = HashTable()

    t["march 6"] = 20
    t["march 17"] = 88

    # with open('./datasets/nyc_weather.csv', 'r') as f:
    #     for row in f:
    #         token = row.split(",")
    #         date = token[0]
    #         if date == 'date':
    #             continue
    #         t[date] = int(token[1])

    # print(t.arr)

    # print(t['Jan 9'])

