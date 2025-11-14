class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        int map_s_to_t[256] = {0};
        int map_t_to_s[256] = {0};
        for (int i = 0; i < s.length(); ++i) {
            char char_s = s[i];
            char char_t = t[i];
            if (map_s_to_t[char_s] == 0 && map_t_to_s[char_t] == 0) {
                map_s_to_t[char_s] = char_t;
                map_t_to_s[char_t] = char_s;
            }
            else if (map_s_to_t[char_s] == char_t && map_t_to_s[char_t] == char_s) {
                continue;
            }
            else {
                return false;
            }
        }
        return true;
    }
};