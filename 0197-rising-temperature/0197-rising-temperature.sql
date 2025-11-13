# Write your MySQL query statement below
SELECT Today.id
FROM Weather AS Today
JOIN Weather AS Yesterday ON DATEDIFF(Today.recordDate, Yesterday.recordDate) = 1
WHERE Today.temperature > Yesterday.temperature;
