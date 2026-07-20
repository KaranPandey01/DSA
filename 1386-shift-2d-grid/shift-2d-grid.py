class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # Optimize k if it is larger than the total number of elements
        k = k % total_elements
        
        # Initialize a new grid filled with placeholder zeros
        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # Calculate the unique 1D index and apply shift
                new_1D_index = (i * n + j + k) % total_elements
                
                # Convert the 1D index back to 2D coordinates
                new_row = new_1D_index // n
                new_col = new_1D_index % n
                
                # Place the element into its new position
                ans[new_row][new_col] = grid[i][j]
                
        return ans
