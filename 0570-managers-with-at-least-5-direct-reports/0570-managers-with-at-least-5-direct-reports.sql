# Write your MySQL query statement below
WITH MgrWithAtLeastFiveDirectReport
AS (
	SELECT M.ManagerId
	FROM Employee AS M
	GROUP BY M.ManagerId
	HAVING count(M.Id) >= 5
	)
SELECT E.Name
FROM MgrWithAtLeastFiveDirectReport AS M
INNER JOIN Employee AS E ON M.ManagerId = E.Id