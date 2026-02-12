#include <string>
#include <unordered_map>
class Solution {
public:
    int romanToInt(std::string s) {
        std::unordered_map<char, int> romanValues = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int total = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (i + 1 < s.length() && romanValues[s[i]] < romanValues[s[i+1]]) {
                total -= romanValues[s[i]];
            } else {
                total += romanValues[s[i]];
            }
        }
        return total;
    }
};