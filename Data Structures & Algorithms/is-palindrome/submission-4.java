class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder newS = new StringBuilder("");
        String sLower = s.toLowerCase();

        for(int i = 0; i < s.length(); i++){
            if((sLower.charAt(i) >= 'a' && sLower.charAt(i) <= 'z') || (sLower.charAt(i) >= '0' && sLower.charAt(i) <= '9')){
                newS.append(sLower.charAt(i));
            }
        }

        String newString = newS.toString();

        int index = newString.length() - 1;
        System.out.println(newString);

        for(int i = 0; i < newString.length(); i++){
            System.out.println(newString.charAt(i));
            System.out.println(newString.charAt(index));
            if(newString.charAt(i) != newString.charAt(index)){
                return false;
            }
            index--;
        }

        return true;
    }
}
