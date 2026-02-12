# Write your MySQL query statement below
SELECT E.employee_id AS employee_id
FROM Employees AS E
LEFT JOIN Salaries AS S ON E.employee_id = S.employee_id
WHERE S.employee_id IS NULL

UNION

SELECT S.employee_id
FROM Employees AS E
RIGHT JOIN Salaries AS S ON E.employee_id = S.employee_id
WHERE E.employee_id IS NULL
ORDER BY employee_id