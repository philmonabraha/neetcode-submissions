class Solution {
    public void reverseString(char[] s) {

        pointer1 = 0;
        pointer2 = s.length - 1;

        while (pointer1 != pointer2){

            s[pointer1] = s[pointer2];
            pointer1 += 1;
            pointer2 -= 1;
        }

        return s;
        
    }
}