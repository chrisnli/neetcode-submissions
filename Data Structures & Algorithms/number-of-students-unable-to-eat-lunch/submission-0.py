from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student = deque(students)
        sandwhich = deque(sandwiches)
        count = 0
        while len(sandwhich) > 0:
            if count >= len(sandwhich): break
            stu = student.popleft()
            sand = sandwhich[0]
            if stu != sand: 
                student.append(stu)
                count += 1

            else: 
                sandwhich.popleft()
                count = 0


        return len(sandwhich)
