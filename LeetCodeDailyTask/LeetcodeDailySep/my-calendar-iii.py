"""
my-calendar-iii

A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.


Example 1:

Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3


Constraints:

0 <= start < end <= 109
At most 400 calls will be made to book.

Question list https://leetcode.com/problems/my-calendar-iii/
"""
from sortedcontainers import SortedDict

# Time Complexity: O(N ^ 2)
# Space Complexity: O(N)
class MyCalendarThree:

    def __init__(self):
        # in line sweeping, we need to ensure the keys are sorted
        # in python, we can use SortedDict which fulfils the above requirement
        # lines[i] = j means we have j overlapping elements at time point i
        self.lines = SortedDict()


    # finding number of overlapping elements at time points -> line sweeping
    def book(self, start: int, end: int) -> int:
        # new event starts here -> increase by 1
        self.lines[start] = self.lines.get(start, 0) + 1
        # the event ends here -> decrease by 1
        # p.s. sometimes you may see `lines.get(end + 1, 0) - 1;`. e.g. 2406. Divide Intervals Into Minimum Number of Groups
        #      you may search `leetcode-the-hard-way` on Discussion to see my solution explanation on that problem
        #      this is because the interval is inclusive, i.e [start, end]
        #      however, the interval in this problem is [start, end), so we don't need to add 1 here.
        self.lines[end] = self.lines.get(end, 0) - 1
        # here we calculate the prefix sum using `accumulate`
        # and get the maximum overlapping intervals using `max`
        return max(accumulate(self.lines.values()))


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)from sortedcontainers import SortedDict
#
# # Time Complexity: O(N ^ 2)
# # Space Complexity: O(N)
# class MyCalendarThree:
#
#     def __init__(self):
#         # in line sweeping, we need to ensure the keys are sorted
#         # in python, we can use SortedDict which fulfils the above requirement
#         # lines[i] = j means we have j overlapping elements at time point i
#         self.lines = SortedDict()
#
#
#     # finding number of overlapping elements at time points -> line sweeping
#     def book(self, start: int, end: int) -> int:
#         # new event starts here -> increase by 1
#         self.lines[start] = self.lines.get(start, 0) + 1
#         # the event ends here -> decrease by 1
#         # p.s. sometimes you may see `lines.get(end + 1, 0) - 1;`. e.g. 2406. Divide Intervals Into Minimum Number of Groups
#         #      you may search `leetcode-the-hard-way` on Discussion to see my solution explanation on that problem
#         #      this is because the interval is inclusive, i.e [start, end]
#         #      however, the interval in this problem is [start, end), so we don't need to add 1 here.
#         self.lines[end] = self.lines.get(end, 0) - 1
#         # here we calculate the prefix sum using `accumulate`
#         # and get the maximum overlapping intervals using `max`
#         return max(accumulate(self.lines.values()))
#
#
# # Your MyCalendarThree object will be instantiated and called as such:
# # obj = MyCalendarThree()
# # param_1 = obj.book(start,end)