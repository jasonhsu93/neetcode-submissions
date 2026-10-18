class Solution {
    public int numIslands(char[][] grid) {
        
        if(grid.length == 0){
            return 0;
        }
        
        boolean[][] visited = new boolean[grid.length][grid[0].length]; 
        int count = 0;

        for(int y = 0; y < grid.length; y++){
            for(int x = 0; x < grid[0].length; x++){
                if(visited[y][x] == false && grid[y][x] == '1'){
                    BFS(x,y,visited,grid);
                    count++;
                }
            }
        }

        return count;
    }

    private static void BFS(int x, int y, boolean[][] visited, char[][] grid){

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{y,x});
        visited[y][x] = true; 

        while(queue.isEmpty() == false){
            int[] arr = queue.remove();
            int hori = arr[1];
            int vert = arr[0];

            if(hori - 1 >= 0 && !visited[vert][hori - 1] && grid[vert][hori - 1] == '1'){
                queue.add(new int[]{vert, hori - 1});
                visited[vert][hori-1] = true;
            }

            if(vert - 1 >= 0 && !visited[vert - 1][hori] && grid[vert-1][hori] == '1'){
                queue.add(new int[]{vert - 1, hori});
                visited[vert-1][hori] = true;
            }

            if(hori + 1 < visited[0].length && !visited[vert][hori + 1] && grid[vert][hori + 1] == '1'){
                queue.add(new int[]{vert, hori + 1});
                visited[vert][hori+1] = true;
            }

            if(vert + 1 < visited.length && !visited[vert + 1][hori] && grid[vert+1][hori] == '1'){
                queue.add(new int[]{vert + 1, hori});
                visited[vert+1][hori] = true;
            }
        }
    }
}
