# 一文讲解区间问题

区间问题也是 neetcode150 里面的经典，几道代表性的题目

- 56. Merge Intervals
- 57. Insert Interval
- 435. Non-overlapping Intervals

区间问题一般涉及到的算法是

- greedy

其实我们把 interval 抽象出来，一个个区间就是会议室，或者 timestamp，那总共就这几类问题了

- 1 个会议室能不能开所有会议
  - 252 https://leetcode.com/problems/meeting-rooms/description/
- 所有这些会议都不能删，要几个会议室
  - 253 https://leetcode.com/problems/meeting-rooms-ii/description/
- 1 个会议室怎么开最多的会议
  - 435 https://leetcode.com/problems/non-overlapping-intervals/description/
- 将新增的会议与已有的会议合并，确保每个人都能参加所有的会议
  - 57 [insert interval](https://leetcode.com/problems/insert-interval/description/)
- 现有的会议合并，确保每个人都能参加所有的会议
  - 56 [merge interval](https://leetcode.com/problems/merge-intervals/)
