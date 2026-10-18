class Solution {
    public void islandsAndTreasure(int[][] grid) {
        
        Queue<int[]> queue = new LinkedList<>();

        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 0){
                    queue.add(new int[]{i,j});
                }
            }
        }

        if(queue.isEmpty()){
            return;
        }

        while(queue.isEmpty() == false){
            int[] temp = queue.remove();

            int tempI = temp[0];
            int tempJ = temp[1];

            if(tempI + 1 < grid.length && grid[tempI + 1][tempJ] == 2147483647){
                queue.add(new int[]{tempI + 1, tempJ});
                grid[tempI + 1][tempJ] = grid[tempI][tempJ] + 1;
            }

            if(tempJ + 1 < grid[0].length && grid[tempI][tempJ + 1] == 2147483647){
                queue.add(new int[]{tempI, tempJ + 1});
                grid[tempI][tempJ + 1] = grid[tempI][tempJ] + 1;
            }

            if(tempI - 1 >= 0 && grid[tempI - 1][tempJ] == 2147483647){
                queue.add(new int[]{tempI - 1, tempJ});
                grid[tempI - 1][tempJ] = grid[tempI][tempJ] + 1;
            }

            if(tempJ - 1 >= 0 && grid[tempI][tempJ - 1] == 2147483647){
                queue.add(new int[]{tempI, tempJ - 1});
                grid[tempI][tempJ - 1] = grid[tempI][tempJ] + 1;
            }
        }
    }
}
  