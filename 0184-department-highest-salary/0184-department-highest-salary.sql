# Write your MySQL query statement below
-- Rank salary in each department. Highest salary is ranked as 1.
WITH SalaryRankedByDept
AS (
	SELECT D.Name AS Department
		,E.Name AS Employee
		,E.Salary
		,rank() OVER (
			PARTITION BY D.Id ORDER BY E.Salary DESC
			) AS RankNum
	FROM Department AS D
	INNER JOIN Employee AS E ON D.Id = E.DepartmentId
	)
-- Output highest ranked salary in each department
SELECT Department
	,Employee
	,Salary
FROM SalaryRankedByDept
WHERE RankNum = 1