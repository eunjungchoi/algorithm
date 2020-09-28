# SQL Schema
# Write a SQL query to get the second highest salary from the Employee table.
#
# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.
#
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+


# Write your MySQL query statement below

# 1)
# SELECT
#     (SELECT DISTINCT
#             Salary
#         FROM
#             Employee
#         ORDER BY Salary DESC
#         LIMIT 1 OFFSET 1) AS SecondHighestSalary
# ;

# 2)
select max(Salary) as SecondHighestSalary
from Employee
where Salary not in (select max(Salary) from Employee)


# 7 / 7 test cases passed.
# Status: Accepted
# Runtime: 190 ms
# Memory Usage: 0B
#
# Your runtime beats 94.15 % of mysql submissions.
#
