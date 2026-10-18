class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] arr = new int[2];
        for(int i = 0; i < nums.length; i++){
            for(int k = i + 1; k < nums.length; k++){
                if(nums[i] + nums[k] == target && i != k){
                    arr[0] = i;
                    arr[1] = k;
                    break;
                }
            }
        }
        return arr;
    }
}
