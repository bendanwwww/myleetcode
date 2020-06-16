"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

"""

class Solution(object):
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        # sort
        # for i in range(len(intervals)):
        #     for x in range(i, len(intervals)):
        #         if intervals[i][0] > intervals[x][0]:
        #             tmp = intervals[i]
        #             intervals[i] = intervals[x]
        #             intervals[x] = tmp
        intervals.sort(key=lambda x: x[0])
        index = 0
        while index < len(intervals) - 1:
            if intervals[index][1] >= intervals[index + 1][0]:
                if intervals[index][1] < intervals[index + 1][1]:
                    intervals[index] = [intervals[index][0], intervals[index + 1][1]]
                else:
                    intervals[index] = [intervals[index][0], intervals[index][1]]
                del intervals[index + 1]
            else:
                index+= 1
        return intervals

s = Solution()
res = s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
print(res)