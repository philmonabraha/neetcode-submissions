class Solution {
    public String mergeAlternately(String word1, String word2) {

        int l1 = word1.length();
        int l2 = word2.length();
        String s = "";

        int min;
        int max;

        if (l1 <= l2){
            min = l1;
            max = l2;
        }

        else{
            min = l2;
            max = l1;
        }

        int pointer = 0;
        char c;

        while (min > 0){
            min -= 1;

            c = word1.charAt(pointer);
            s += c;
            c = word2.charAt(pointer);
            s += c;

            pointer += 1;
        }

        for (int i = pointer; i < max; i ++){

            if (max == l1) {
                s += word1.charAt(i);
            }
            else {
                s += word1.charAt(i);
            } 
            
        }

        return s;



        
    }
}