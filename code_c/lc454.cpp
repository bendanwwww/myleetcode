/**
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1 之间，最终结果不会超过 2^31 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
输出:
2
解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
*/

#include <iostream>
#include <vector>
#include <map>
using namespace std;


class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        int res = 0;
        map<int, int> addMapAB;
        map<int, int> addMapCD;
        int num = A.size();
        
        for (size_t i = 0; i < num; i++) {
            for (size_t x = 0; x < num; x++) {
                int addAB = A[i] + B[x];
                int addCD = C[i] + D[x];
                if(addMapAB.find(addAB) != addMapAB.end()) {
                    addMapAB[addAB] = addMapAB[addAB] + 1;
                }else {
                    addMapAB[addAB] = 1;
                }
                if(addMapCD.find(addCD) != addMapCD.end()) {
                    addMapCD[addCD] = addMapCD[addCD] + 1;
                }else {
                    addMapCD[addCD] = 1;
                }
            }
        }
        for (auto iter = addMapAB.begin(); iter != addMapAB.end(); iter++) {
            if(addMapCD.find(-(iter->first)) != addMapCD.end()) {
                res = res + iter->second * addMapCD[-(iter->first)];
            }
        }
        return res;
    }
};

int main() {
    Solution solution;
    int a[2] = {-1, -1};
    int b[2] = {-1, 1};
    int c[2] = {-1, 1};
    int d[2] = {1, -1};

    vector<int> A(a, a + 2);
    vector<int> B(b, b + 2);
    vector<int> C(c, c + 2);
    vector<int> D(d, d + 2);
    int res = solution.fourSumCount(A, B, C, D);
    cout << res;
    return 0;
}