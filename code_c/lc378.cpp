/**
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。
 
提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n^2 
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int kthSmallest(vector< vector<int> >& matrix, int k) {
        int left = matrix[0][0];
        int right = matrix[matrix.size() - 1][matrix.size() - 1];
        while(left < right) { 
            int mid = (left + right) / 2;
            if(checkNumber(matrix, mid) < k) {
                left = mid + 1;
            }else {
                right = mid;
            }
        }
        return left;
    }

    int checkNumber(vector< vector<int> >& matrix, int n) {
        int res = 0;
        int rowIndex = 0;
        for(int i = matrix.size() - 1; i >= 0; i--) {
            while(rowIndex < matrix[i].size() && matrix[i][rowIndex] <= n) {
                rowIndex++;
            }
            res+= rowIndex;
        }
        return res;
    }
};

int main() {
    Solution* solution = new Solution();
    vector< vector<int> > matrix;
    vector<int> tmps1;
    tmps1.push_back(1);
    tmps1.push_back(5);
    tmps1.push_back(9);
    vector<int> tmps2;
    tmps2.push_back(10);
    tmps2.push_back(11);
    tmps2.push_back(13);
    vector<int> tmps3;
    tmps3.push_back(12);
    tmps3.push_back(13);
    tmps3.push_back(15);
    matrix.push_back(tmps1);
    matrix.push_back(tmps2);
    matrix.push_back(tmps3);
    cout << solution -> kthSmallest(matrix, 8);
    return 0;
}