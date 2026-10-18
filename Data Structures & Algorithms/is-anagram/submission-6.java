class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character,Integer> map = new HashMap<>();
        HashMap<Character,Integer> map2 = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                int temp = map.get(s.charAt(i));
                map.put(s.charAt(i),temp + 1);
            }else{
                map.put(s.charAt(i),0);
            }

            if(map2.containsKey(t.charAt(i))){
                int temp = map2.get(t.charAt(i));
                map2.put(t.charAt(i),temp + 1);
            }else{
                map2.put(t.charAt(i),0);
            }
        }

        if(map.size() != map2.size()){
            return false;
        }

        for(char key : map.keySet()){
            if(!map2.containsKey(key)){
                return false;
            }
            
            if(map2.get(key) != map.get(key)){
                return false;
            }
        }

        return true;
    }
}
