class HashTable:
    def __init__(self, n):
        self.size      = n
        self.hashtable = [[] for _ in range(self.size)]

    def hash(self,item):
        ''' Compute a hash code for item '''

        res = 0
        for ch in item:
            res += ord(ch)

        return res % self.size
    
    def add(self, item):

        code = self.hash(item)

        if item not in self.hashtable[code]:
            self.hashtable[code].append(item)

    def contains(self, item):
        code   = self.hash(item)
        bucket = self.hashtable[code]

        return item in bucket
    
    def remove(self, item):
        code = self.hash(item)
        bucket = self.hashtable[code]

        if item in bucket:
            bucket.remove(item)

    def print_hashset(self):
        print('Hash set contents')

        for idx, container in enumerate(self.hashtable):
            print(f"Bucket {idx} Contents: {container}")


hash_table = HashTable(10)
hash_table.add("Felix")
hash_table.add("Alex")
hash_table.print_hashset()


