# Write your MySQL query statement below
SELECT id
	,'Root' AS Type
FROM tree
WHERE p_id IS NULL
UNION
SELECT N.id
	,'Inner'
FROM tree AS N
INNER JOIN tree AS P ON N.p_id = P.id
INNER JOIN tree AS C ON N.id = C.p_id
UNION
SELECT N.id
	,'Leaf'
FROM tree AS N
INNER JOIN tree AS P ON N.p_id = P.id
LEFT JOIN tree AS C ON N.id = C.p_id
WHERE C.p_id IS NULL
ORDER BY id ASC -- Sort your output by the node id.