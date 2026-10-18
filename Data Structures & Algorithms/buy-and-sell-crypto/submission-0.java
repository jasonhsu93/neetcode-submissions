class Solution {
    public int maxProfit(int[] prices) {
        
        if(prices.length < 2){
            return 0;
        }

        int maxDiff = 0;

        for(int i = 0; i < prices.length; i++){
            int smallVal = prices[i];
            int maxVal = smallVal;
            int diff = 0;

            for(int j = i + 1; j < prices.length; j++){
                if(prices[j] > maxVal){
                    maxVal = prices[j];
                    diff = maxVal - smallVal;
                }
            }

            if(maxDiff < diff){
                maxDiff = diff;
            }
        }

        return maxDiff;
    }
}
