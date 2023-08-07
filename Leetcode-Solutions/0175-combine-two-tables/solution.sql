# Write your MySQL query statement below
SELECT firstname, lastname, city, state
FROM Person P left join
Address A on P.personId=A.personId
