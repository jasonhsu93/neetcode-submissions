class Solution {
    public int[] twoSum(int[] nums, int target) {

        if(nums.length == 0){
            //throw new Exception("should not have a length of 0");
            return new int[]{};
        }
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            if(map.get(target-nums[i]) != null){
                return new int[]{map.get(target-nums[i]),i};
            }

            map.put(nums[i],i);
        }  

        return new int[]{};
    }
}
