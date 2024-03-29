"""
给定一个形如 “HH:MM” 表示的时刻，利用当前出现过的数字构造下一个距离当前时间最近的时刻。每个出现数字都可以被无限次使用。
你可以认为给定的字符串一定是合法的。例如，“01:34” 和 “12:09” 是合法的，“1:34” 和 “12:9” 是不合法的。

样例 1:
输入: "19:34"
输出: "19:39"
解释: 利用数字 1, 9, 3, 4 构造出来的最近时刻是 19:39，是 5 分钟之后。结果不是 19:33 因为这个时刻是 23 小时 59 分钟之后。
 
样例 2:
输入: "23:59"
输出: "22:22"
解释: 利用数字 2, 3, 5, 9 构造出来的最近时刻是 22:22。 答案一定是第二天的某一时刻，所以选择可构造的最小时刻。

"""

class Solution(object):
    def nextClosestTime(self, time):
        dict_number = [time[0], time[1], time[3], time[4]]
        dict_number.sort()
        # 比较当天
        # 最末位
        for n in dict_number:
            if int(time[4]) < int(n):
                return time[:4] + n
        # 第三位
        for n in dict_number:
            if int(time[3]) < int(n) and int(n) < 6:
                return time[:3] + n + dict_number[0]
        # 第二位
        for n in dict_number:
            if int(time[1]) < int(n) and (int(time[0]) < 2 or int(n) < 4):
                return time[:1] + n + ":" + dict_number[0] + dict_number[0]
        # 第一位
        for n in dict_number:
            if int(time[0]) < int(n) and int(n) < 3:
                return n + dict_number[0] + ":" + dict_number[0] + dict_number[0]
        # 第二天
        return dict_number[0] + dict_number[0] + ":" + dict_number[0] + dict_number[0]

s = Solution()
res = s.nextClosestTime("23:05")
print(res)