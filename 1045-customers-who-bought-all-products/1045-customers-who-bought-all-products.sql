# Write your MySQL query statement below
SELECT C.customer_id
FROM Customer AS C
GROUP BY C.customer_id
HAVING count(DISTINCT C.product_key) = (
		SELECT count(*)
		FROM Product
		)