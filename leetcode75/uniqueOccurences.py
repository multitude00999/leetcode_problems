class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n = len(arr)

        # count number of occurences of each element in arr
        count_dict = {}

        for i in range(n):
            if arr[i] not in count_dict:
                count_dict[arr[i]] = 1
            
            else:
                count_dict[arr[i]] += 1
        
        # check whether two element have same number of occurences
        hashmap_values = {}
        for i in count_dict.values():
            if i not in hashmap_values:
                hashmap_values[i] = 1
            
            else:
                return False

        return True
