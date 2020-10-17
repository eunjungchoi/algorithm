# Table: Project
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | project_id  | int     |
# | employee_id | int     |
# +-------------+---------+
# (project_id, employee_id) is the primary key of this table.
# employee_id is a foreign key to Employee table.
# Table: Employee
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | employee_id      | int     |
# | name             | varchar |
# | experience_years | int     |
# +------------------+---------+
# employee_id is the primary key of this table.
#
#
# Write an SQL query that reports the most experienced employees in each project.
# In case of a tie, report all employees with the maximum number of experience years.
#
# The query result format is in the following example:
#
# Project table:
# +-------------+-------------+
# | project_id  | employee_id |
# +-------------+-------------+
# | 1           | 1           |
# | 1           | 2           |
# | 1           | 3           |
# | 2           | 1           |
# | 2           | 4           |
# +-------------+-------------+
#
# Employee table:
# +-------------+--------+------------------+
# | employee_id | name   | experience_years |
# +-------------+--------+------------------+
# | 1           | Khaled | 3                |
# | 2           | Ali    | 2                |
# | 3           | John   | 3                |
# | 4           | Doe    | 2                |
# +-------------+--------+------------------+
#
# Result table:
# +-------------+---------------+
# | project_id  | employee_id   |
# +-------------+---------------+
# | 1           | 1             |
# | 1           | 3             |
# | 2           | 1             |
# +-------------+---------------+
# Both employees with id 1 and 3 have the most experience among the employees of the first project.
# For the second project, the employee with id 1 has the most experience.

# Write your MySQL query statement below


# select p.project_id, p.employee_id
# from project p
# left join employee e
# using (employee_id)
# where (p.project_id, e.experience_years) in
# (
#     select project_id, max(experience_years)
#     from project
#     left join employee
#     using (employee_id)
#     group by project_id
# )
