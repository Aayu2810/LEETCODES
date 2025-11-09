class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) {
            return 0; 
        }
        if (haystack.length() < needle.length()) {
            return -1; 
        }
        int hayLen = haystack.length();
        int needleLen = needle.length();
        for (int i = 0; i <= hayLen - needleLen; ++i) {
            if (haystack.substr(i, needleLen) == needle) {
                return i; 
            }
        }

        // If no match is found after checking all possible positions
        return -1;
    }
};