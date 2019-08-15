# -*- coding: utf-8 -*-

'''Hash Table'''
class hash_table:
    def __init__(self, num):
        self.__solts__ = []
        self.num = num
        for _ in range(num):
            self.__solts__.append([])
    def hash_fun(self,key,num):
        hashval = 0
        x = key
        if x < 0:
                print("the key is low")
                return
        while x != 0:
                hashval = (int(hashval)<<3) + x%10
                x /=10
        return hashval % num
    def put(self, key, value):
        i = self.hash_fun(key,self.num) % self.num
        for p, (k, v) in enumerate(self.__solts__[i]):
            if k == key:
                break
        else:
            self.__solts__[i].append((key, value))
            return
        self.__solts__[i][p] = (key, value)
    def get(self, key):
        i = self.hash_fun(key,self.num) % self.num
        for k, v in self.__solts__[i]:
            if k == key:
                return v
        raise KeyError(key)
    # keys函数
    def keys(self):
        ret = []
        for solt in self.__solts__:
            for k, _ in solt:
                ret.append(k)
        return ret
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


'''String(Tree)'''



if __name__ == '__main__':
    H = hash_table(13)
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.get(54))
    H.put(13,"duck")
    print(H.__solts__)
    print(H.keys())