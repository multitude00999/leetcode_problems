class Solution1:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # maintain counter hashmaps where keys are rows and columns represented as space separated strings
        # e.g [1, 2, 3] --> "1 2 3" 
        n = len(grid)
        hashmap_rows = {}
        hashmap_cols = {}
        for i in range(n):
            row =  " ".join(map(str, grid[i]))
            col =  " ".join(map(str, [j[i] for j in grid]))
            if row not in hashmap_rows:
                hashmap_rows[row] = 1
            else:
                hashmap_rows[row] += 1

            if col not in hashmap_cols:
                hashmap_cols[col] = 1
            else:
                hashmap_cols[col] += 1

        # count number of matching row and column pairs
        count = 0
        for i in hashmap_rows:
            if i in hashmap_cols:
                n = hashmap_cols[i]*hashmap_rows[i]
                count += n
                hashmap_cols.pop(i)

        return count


class Solution2:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # brute force solution, separate columns and rows
        n = len(grid)
        rows, columns = [""]*n, [""]*n
        for i in range(n):
            rows[i] =  grid[i]
            col = [j[i] for j in grid]
            columns[i] =  col
        
        # search each row in the columns list
        count = 0
        for i in range(n):
            for j in range(n):
                if grid[i] == columns[j]:
                    count += 1
        return count