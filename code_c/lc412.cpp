/**
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：
n = 15,
返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
*/

#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> resList;
        for (size_t i = 1; i <= n; i++) {
            if(i % 3 == 0 && i % 5 == 0) {
                resList.push_back("FizzBuzz");
                continue;
            }
            if(i % 3 == 0) {
                resList.push_back("Fizz");
                continue;
            }
            if(i % 5 == 0) {
                resList.push_back("Buzz");
                continue;
            }
            resList.push_back(std::to_string(i));
        }
        
        return resList;
    }
};

int main() {
    Solution solution;
    vector<string> resList = solution.fizzBuzz(15);
    for(int i = 0; i < resList.size(); i++){
        cout << resList[i] << ",";
    }
    return 0;
}