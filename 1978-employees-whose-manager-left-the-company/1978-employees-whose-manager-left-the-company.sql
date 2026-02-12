SELECT E.employee_id
FROM Employees AS E
LEFT JOIN Employees AS M ON E.manager_id = M.employee_id
WHERE E.salary < 30000
  AND E.manager_id IS NOT NULL
  AND M.employee_id IS NULL
ORDER BY E.employee_id;
