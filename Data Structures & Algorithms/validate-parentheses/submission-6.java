class Solution {
    public boolean isValid(String s) {
        if(s.length() % 2 != 0){
            return false;
        }

        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < s.length(); i++){

            if(s.charAt(i) == '{'){
                stack.push(s.charAt(i));
            }else if(s.charAt(i) == '['){
                stack.push(s.charAt(i));
            }else if(s.charAt(i) == '('){
                stack.push(s.charAt(i));
            }else{
                if(stack.isEmpty()){
                    return false;
                }
                char check = stack.pop();

                if(check == '{'){
                    if(s.charAt(i) != '}'){
                        return false;
                    }
                }else if(check == '['){
                    if(s.charAt(i) != ']'){
                        return false;
                    }
                }else if(check == '('){
                    if(s.charAt(i) != ')'){
                        return false;
                    }
                }
            }

        }

        if(!stack.isEmpty()){
            return false;
        }
        return true;
    }
}
