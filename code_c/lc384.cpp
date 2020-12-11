/**
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
实现 Solution class:
Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果

示例：
输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]

提示：
1 <= nums.length <= 200
-106 <= nums[i] <= 106
nums 中的所有元素都是 唯一的
最多可以调用 5 * 104 次 reset 和 shuffle
*/

#include <iostream>
#include <vector>
#include <map>
#include <cstdlib>
#include<ctime>
using namespace std;

class Solution {

private:
    vector<int> ns;
public:
    Solution(vector<int>& nums) {
        ns = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return ns;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> res;
        int randoms[ns.size()];
        int n = 0;
        for(int* r = randoms; r <= &randoms[sizeof(randoms) / sizeof(randoms[0]) - 1]; r++) {
           *r = n;
           n++;
        }

        for(int i = 0; i < ns.size() - 1; i++) {
            int r = rand();
            int n = ns.size() - i;
            int number = r % n;
            // cout << r << "\n";
            res.push_back(ns[randoms[number]]);
            int tmp = randoms[number];
            randoms[number] = randoms[ns.size() - i - 1];
            randoms[ns.size() - i - 1] = tmp;
        }
        res.push_back(ns[randoms[0]]);
        return res;
    }
};

int main() {
    int nums[3] = {-6, 10, 184};
    vector<int> ins(nums, nums + 3);
    Solution* solution = new Solution(ins);
    
    for (size_t i = 0; i < 100; i++) {
        vector<int> res1 = solution -> shuffle();
        for(int i = 0; i < res1.size(); i++) {
            cout << res1[i] << "    ";
        }
        cout << "\n";
    }
    return 0;
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */