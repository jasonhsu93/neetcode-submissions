class Solution {
    public int numIslands(char[][] grid) {
        
        if(grid.length == 0){
            return 0;
        }

        int count = 0;

        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == '1'){
                    BFS(i,j, grid);
                    count++;
                }
            }
        }

        return count;
    }

    private static void BFS(int i, int j, char[][] grid){
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{i,j});

        while(!queue.isEmpty()){
            int[] temp = queue.remove();

            i = temp[0];
            j = temp[1];

            if(i + 1 < grid.length && grid[i+1][j] == '1'){
                queue.add(new int[]{i+1,j});
                grid[i+1][j] = 2;
            }

            if(i - 1 >= 0 && grid[i-1][j] == '1'){
                queue.add(new int[]{i-1,j});
                grid[i-1][j] = 2;
            }

            if(j + 1 < grid[0].length && grid[i][j+1] == '1'){
                queue.add(new int[]{i,j+1});
                grid[i][j+1] = 2;
            }

            if(j - 1 >= 0 && grid[i][j-1] == '1'){
                queue.add(new int[]{i,j-1});
                grid[i][j-1] = 2;
            }
        }
    }
}
