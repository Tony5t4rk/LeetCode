"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_mp = {employee.id: employee for employee in employees}

        def dfs(employee_id: int):
            return employee_mp[employee_id].importance + sum(dfs(subordinate) for subordinate in employee_mp[employee_id].subordinates)

        return dfs(id)