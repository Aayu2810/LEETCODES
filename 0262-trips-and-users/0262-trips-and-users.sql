# Write your MySQL query statement below
WITH trips_analysis
AS (
	SELECT t.request_at,
		t.STATUS,
		count(t.id) AS requests
	FROM Trips t
	INNER JOIN Users AS client ON t.client_id = client.users_id
		AND client.banned = 'No'
	INNER JOIN Users AS driver ON t.driver_id = driver.users_id
		AND driver.banned = 'No'
	WHERE t.request_at BETWEEN '2013-10-01'
			AND '2013-10-03'
	GROUP BY t.request_at,
		t.STATUS
	)
SELECT request_at AS Day,
	round(sum(CASE
				WHEN STATUS LIKE 'cancelled%'
					THEN requests
				ELSE 0
				END) / sum(requests), 2) AS "Cancellation Rate"
FROM trips_analysis
GROUP BY request_at;