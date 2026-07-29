class Solution:
    DIRECTIONS = ((1,0), (-1,0), (0,1), (0,-1))

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og_color = image[sr][sc]
        if og_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in self.DIRECTIONS:
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or image[nr][nc] != og_color:
                    continue
                q.append((nr, nc))
        return image
