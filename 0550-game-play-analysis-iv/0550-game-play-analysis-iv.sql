# Write your MySQL query statement below
WITH PlayerFirstLogin
AS (
	SELECT player_id
		,min(event_date) AS first_login_date
	FROM Activity
	GROUP BY player_id
	)
	,PlayerConsecutiveLogin
AS (
	SELECT A.player_id
	FROM Activity AS A
	INNER JOIN PlayerFirstLogin FL ON A.player_id = FL.player_id
		AND datediff(A.event_date, FL.first_login_date) = 1
	)
SELECT cast((
			SELECT count(DISTINCT player_id)
			FROM PlayerConsecutiveLogin
			) / cast((
				SELECT count(DISTINCT player_id)
				FROM Activity
				) AS FLOAT) AS DECIMAL(10, 2)) AS fraction