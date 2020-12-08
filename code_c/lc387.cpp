/**
 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

提示：你可以假定该字符串只包含小写字母。
*/

#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> charMap;
        for (size_t i = 0; i < s.length(); i++) {
            char c = s[i];
            if(charMap.find(c) != charMap.end()) {
                charMap[c]++;
            }else {
                charMap[c] = 1;
            }
        }
        for (size_t i = 0; i < s.length(); i++) {
            if(charMap[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};

int main() {
    Solution solution;
    int res = solution.firstUniqChar("yekbsxznylrwamcaugrqrurvpqybkpfzwbqiysrdnrsnbftvrnszfjbkbmrctjizkjqoxqzddyfnavnhqeblfmzqgsjflghaulbadwqsyuetdelujphmlgtmkoaoijypvcajctbaumeromgejtewbwqptotrorephegyobbstvywljboeihdliknluqdpgampjyjpinxhhqexoctysfdciqjbzilnodzoihihusxluqoayenluziobxiodrfdkinkzzozmxfezfvllpdvogqqtquwcsijwachefspywdgsohqtlquhnoecccgbkrzqcprzmwvygqwddnehhi");
    cout << res;
    return 0;
}