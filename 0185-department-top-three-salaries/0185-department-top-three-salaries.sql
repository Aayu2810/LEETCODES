# Write your MySQL query statement below
WITH salary_analysis
AS (
	SELECT d.Name AS Department,
		e.Name AS Employee,
		e.Salary,
		dense_rank() OVER (
			PARTITION BY d.Id ORDER BY e.Salary DESC
			) AS salary_rank_num
	FROM Department d
	INNER JOIN Employee e ON d.Id = e.DepartmentId
	)
SELECT Department,
	Employee,
	Salary
FROM salary_analysis
WHERE salary_rank_num <= 3
ORDER BY Department,
	Salary DESC;