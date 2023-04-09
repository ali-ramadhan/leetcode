class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        old_color = image[sr][sc]
        image[sr][sc] = color
        
        m = len(image)
        n = len(image[0])

        if sr-1 >= 0 and image[sr-1][sc] == old_color:
            self.floodFill(image, sr-1, sc, color)
        if sr+1 < m and image[sr+1][sc] == old_color:
            self.floodFill(image, sr+1, sc, color)
        if sc-1 >= 0 and image[sr][sc-1] == old_color:
            self.floodFill(image, sr, sc-1, color)
        if sc+1 < n and image[sr][sc+1] == old_color:
            self.floodFill(image, sr, sc+1, color)
        
        return image
