class Solution {
    public int numIslands(char[][] grid) {
        
        if(grid.length == 0){
            return 0;
        }

        int count = 0;

        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == '1'){
                    count++;
                    BFS(i,j,grid);
                }
            }
        }

        return count;
    }

    private static void BFS(int i, int j, char[][] grid){

        Queue<int[]> queue = new LinkedList<>();

        queue.add(new int[]{i,j});
        grid[i][j] = '2';

        while(queue.isEmpty() == false){
            int[] temp = queue.remove();

            int tempI = temp[0];
            int tempJ = temp[1];

            if(tempI + 1 < grid.length && grid[tempI + 1][tempJ] == '1'){
                queue.add(new int[]{tempI + 1, tempJ});
                grid[tempI + 1][tempJ] = '2';
            }

            if(tempJ + 1 < grid[0].length && grid[tempI][tempJ + 1] == '1'){
                queue.add(new int[]{tempI, tempJ + 1});
                grid[tempI][tempJ + 1] = '2';
            }

            if(tempI - 1 >= 0 && grid[tempI - 1][tempJ] == '1'){
                queue.add(new int[]{tempI - 1, tempJ});
                grid[tempI - 1][tempJ] = '2';
            }

            if(tempJ - 1 >= 0 && grid[tempI][tempJ - 1] == '1'){
                queue.add(new int[]{tempI, tempJ - 1});
                grid[tempI][tempJ - 1] = '2';
            }
        }
    }
}
