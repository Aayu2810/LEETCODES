# Write your MySQL query statement below
SELECT
    C.Name AS Customers
FROM
    Customers AS C
LEFT JOIN
    Orders AS O ON C.Id = O.CustomerId
WHERE
    O.CustomerId IS NULL;