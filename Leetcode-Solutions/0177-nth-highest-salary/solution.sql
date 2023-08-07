CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
count_s NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    select count(distinct salary) into count_s from Employee;
    IF count_s < N
    THEN
      RETURN NULL;
    END IF;
    select salary into result from (   
    with T1 as (
    select distinct salary from employee order by salary desc)
    select T1.salary  , rownum as rn from T1 ) where RN=N;
    RETURN result;
END;
