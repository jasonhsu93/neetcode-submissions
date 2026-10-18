class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder newS = new StringBuilder("");
        String sLower = s.toLowerCase();

        for(int i = 0; i < s.length(); i++){
            if((sLower.charAt(i) >= 'a' && sLower.charAt(i) <= 'z') || (sLower.charAt(i) >= '0' && sLower.charAt(i) <= '9')){
                newS.append(sLower.charAt(i));
            }
        }
        String ss = newS.toString();
        System.out.println(newS.toString());
        newS.reverse();
        String sss= newS.toString();
        System.out.println(newS.toString());
        //System.out.println(reverseString);
        return ss.equals(sss);
    }
}
