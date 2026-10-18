class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        
        if(grid.length == 0){
            return 0;
        }

        int max = 0;
        
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 1){
                    int curr = BFS(i,j,grid);
                    if(curr > max){
                        max = curr;
                    }
                }
            }
        }

        return max;
    }

    private static int BFS(int i, int j, int[][] grid){
        int count = 1;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int []{i,j});
        grid[i][j] = 2;

        while(queue.isEmpty() == false){
            int[] newArr = queue.remove();
            int newI = newArr[0];
            int newJ = newArr[1];

            if(newI - 1 >= 0 && grid[newI - 1][newJ] == 1){
                queue.add(new int[]{newI - 1,newJ});
                grid[newI - 1][newJ] = 2;
                count++;
            }

            if(newJ - 1 >= 0 && grid[newI][newJ - 1] == 1){
                queue.add(new int[]{newI,newJ - 1});
                grid[newI][newJ - 1] = 2;
                count++;
            }

            if(newI + 1 < grid.length && grid[newI+1][newJ] == 1){
                queue.add(new int[]{newI+1,newJ});
                grid[newI+1][newJ] = 2;
                count++;
            }

            if(newJ + 1 < grid[0].length && grid[newI][newJ+1] == 1){
                queue.add(new int[]{newI,newJ+1});
                grid[newI][newJ+1] = 2;
                count++;
            }
        }

        return count;
    }
}
