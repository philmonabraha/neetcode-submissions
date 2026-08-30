class Solution {
    public int removeDuplicates(int[] nums) {

        int sizeofnums = nums.length;
        int pointer1 = 0;
        int pointer2 = 1;
        int unique = 0;

        while (pointer2 < sizeofnums){

            if (nums.[pointer1] == nums.get[pointer2]){
                pointer1 += 1;
                }

            else{

                unique += 1;

                nums[pointer1] = nums[pointer2];
                pointer2 += 1;
            }
            

        }

        return unique;
    }
}