class Solution {
    public boolean isHappy(int n) {
        
        HashSet<Integer> set = new HashSet<>();

        while(true){
            int temp = 0;

            while(n != 0){
                temp += (n % 10) * (n % 10);
                n = n/10;
            }

            if(set.contains(temp)){
                return false;
            }else if(temp == 1){
                return true;
            }else{
                set.add(temp);
                n = temp;
            }
        }
    }
}
