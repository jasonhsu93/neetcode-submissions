class Solution {
    public boolean isValid(String s) {

        if(s.length() == 0 ){
            return true;
        }
        
        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < s.length(); i++){
            
            if(s.charAt(i) == '{'){
                stack.add('{');
            }else if(s.charAt(i) == '['){
                stack.add('[');
            }else if(s.charAt(i) == '('){
                stack.add('(');
            }else{
                if(stack.isEmpty()){
                    return false;
                }

                char temp = stack.pop();

                if(s.charAt(i) == ']'){
                    if(temp != '['){
                        return false;
                    }
                }else if(s.charAt(i) == '}'){
                    if(temp != '{'){
                        return false;
                    }
                }else if(s.charAt(i) == ')'){
                    if(temp != '('){
                        return false;
                    }
                }
            }
        }

        if(stack.isEmpty() == false){
            return false;
        }

        return true;
    }
}
