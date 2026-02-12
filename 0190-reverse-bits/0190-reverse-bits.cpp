class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t reversed_n = 0; 
        for (int i = 0; i < 32; ++i) {
            reversed_n <<= 1; 
            if (n & 1) {
                reversed_n |= 1;
            }
            n >>= 1; 
        }
        return reversed_n; 
    }
};