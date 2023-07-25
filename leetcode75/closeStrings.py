class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # initialize hashmap for storing count of each character in each of the strings
        hashmap_str1 = {}
        hashmap_str2 = {}
        n, m = len(word1), len(word2)
        
        # count characters in both of the string
        for i in range(n):
            if word1[i] not in hashmap_str1:
                hashmap_str1[word1[i]] = 1
            
            else:
                hashmap_str1[word1[i]] += 1

        for i in range(m):
            # check if there are different characters in both strings
            if word2[i] not in hashmap_str1:
                return False

            elif word2[i] not in hashmap_str2:
                hashmap_str2[word2[i]] = 1
            
            else:
                hashmap_str2[word2[i]] += 1
        
        # join keys and values so that both of the hashmaps can be compared
        str1 = "".join(list(hashmap_str1.keys())) + "".join(map(str, list(hashmap_str1.values())))
        str2 = "".join(list(hashmap_str2.keys())) + "".join(map(str, list(hashmap_str2.values())))

        # hashmaps for comparing hashmap_str1, hashmap_str2
        hashmap_3 = {}
        hashmap_4 = {}
        for i in str1:
            if i not in hashmap_3:
                hashmap_3[i] = 1
            
            else:
                hashmap_3[i] += 1

        for i in str2:
            if i not in hashmap_3:
                return False

            elif i not in hashmap_4:
                hashmap_4[i] = 1

            else:
                hashmap_4[i] += 1
        
        # check if the values of each of the keys is also the same
        for i in hashmap_4:
            if hashmap_3[i] != hashmap_4[i]:
                return False
        
        return True
