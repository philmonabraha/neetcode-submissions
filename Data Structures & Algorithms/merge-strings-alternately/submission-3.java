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

        pointer = 0;
        char c;

        while (min > 0){
            min -= 1;

            c = word1.getChar(pointer);
            s.append(c);
            c = word2.getChar(pointer);
            s.append(c);

            pointer += 1;
        }

        for (int i = pointer; i < max; i ++){

            if (max == l1) {
                s.append(word1.getChar(i));
            }
            else {
                s.append(word2.getChar(i));
            } 
            
        }

        return s;



        
    }
}