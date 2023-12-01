class Solution(object):
    def average(self, salary):
        salary.sort()
        salary = salary[1:len(salary) - 1]
        total = 0
        for s in salary:
            total += s
        return float(total) / (len(salary))