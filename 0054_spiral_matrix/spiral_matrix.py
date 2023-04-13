class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        if m == 2:
            out = []
            out.extend(matrix[0])
            out.extend(reversed(matrix[1]))
            return out
        
        if n == 2:
            out = [matrix[0][0]]
            out.extend([matrix[i][1] for i in range(m)])
            out.extend([matrix[i][0] for i in reversed(range(1, m))])
            return out

        # Borders
        l = 0  # left
        r = n-1  # right
        b = 0  # bottom
        t = m-1  # top

        # Current position
        # i should stay within [l, r]
        # j should stay within [b, t]
        i = j = 0

        spiral = [0] * n * m

        count = 0
        spiral[count] = matrix[j][i]

        while l <= r and b <= t:
            moved = False
            if i < r and j == b:
                i += 1
                moved = True
            elif i == r and j < t:
                j += 1
                moved = True
            elif i > l and j == t:
                i -= 1
                moved = True
            elif i == l and j > b:
                j -= 1
                moved = True

            if count == n*m - 1:
                break

            if moved:
                print(f"i={i}, j={j}, l={l}, r={r}, b={b}, t={t}")
                count += 1
                spiral[count] = matrix[j][i]
                print(f"spiral={spiral}")

            turned = False
            if i == r and j == b:
                j += 1
                b += 1
                turned = True
            elif i == r and j == t:
                i -= 1
                r -= 1
                turned = True
            elif i == l and j == t:
                j -= 1
                t -= 1
                turned = True
            elif i == l and j == b:
                i += 1
                l += 1
                turned = True

            if count == n*m - 1:
                break

            if turned:
                print(f"i={i}, j={j}, l={l}, r={r}, b={b}, t={t}")
                count += 1
                spiral[count] = matrix[j][i]
                print(f"spiral={spiral}")

            if count == n*m - 1:
                break
        
        return spiral

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        row_begin = 0
        col_begin = 0
        row_end = len(matrix)-1 
        col_end = len(matrix[0])-1
        while (row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])
            row_begin += 1
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            if (row_begin <= row_end):
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])
                row_end -= 1
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin])
                col_begin += 1
        return res
