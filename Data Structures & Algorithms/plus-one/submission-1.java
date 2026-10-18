
class Solution {
    public int[] plusOne(int[] digits) {
        
        if(digits[digits.length-1] == 9){
            for(int i = digits.length-1; i >= 0; i--){
                if(digits[i] == 9){
                    digits[i] = 0;
                }else{
                    digits[i] = digits[i] + 1;
                    return digits;
                }
            }
            
            ArrayList<Integer> newList = new ArrayList<>();
            newList.add(1);
            System.out.println(digits.length);

            for(int i = 0; i < digits.length; i++){
                newList.add(digits[i]);
            }

            int[] newArray = new int[digits.length+1];

            for(int i = 0; i < digits.length+1; i++){
                newArray[i] = newList.get(i);
            }

            return newArray;
        }else{
            digits[digits.length-1] = digits[digits.length-1] + 1;
            
            return digits;
        }
    }

    // Helper method to convert ArrayList<Integer> to int[]
    private int[] convertToIntArray(ArrayList<Integer> list) {
        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i); // Unboxing Integer to int
        }
        return result;
    }
}
