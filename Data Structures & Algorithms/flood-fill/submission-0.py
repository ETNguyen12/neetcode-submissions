class Solution:
    DIRECTIONS = ((1,0), (-1,0), (0,1), (0,-1))

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])

        og_color = image[sr][sc]
        q = deque([(sr, sc)])
        seen = set()

        while q:
            r, c = q.popleft()
            seen.add((r, c))
            image[r][c] = color
            for dr, dc in self.DIRECTIONS:
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or image[nr][nc] != og_color or (nr, nc) in seen:
                    continue
                q.append((nr, nc))
        return image
