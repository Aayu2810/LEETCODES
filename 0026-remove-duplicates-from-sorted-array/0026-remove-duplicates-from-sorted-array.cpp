class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
    if (nums.empty()) {
            return 0;
        }
        int write_pointer = 1; 
        for (int read_pointer = 1; read_pointer < nums.size(); ++read_pointer) {
            if (nums[read_pointer] != nums[write_pointer - 1]) {
                nums[write_pointer] = nums[read_pointer]; 
                write_pointer++; 
            }
        }
        return write_pointer; 
    }
};
