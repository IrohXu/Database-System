# (a)
Select @t1:=now(6);
create index temp_index on EMPLOYEE(ID, Salary);
create temporary table temp select distinct Manager from EMPLOYEE;
create temporary table temp2 select ID as Manager_ID, Salary as Manager_Salary from EMPLOYEE right join temp on EMPLOYEE.ID=temp.Manager;
create index temp_index2 on temp2(Manager_ID, Manager_Salary);
select count(ID) as Employee_Number from EMPLOYEE inner join temp2 on EMPLOYEE.Manager=temp2.Manager_ID where Salary > Manager_Salary + 50;
Select TimeDiff(now(6), @t1);
drop index temp_index on EMPLOYEE;
drop index temp_index2 on temp;
drop temporary table if exists temp2;
drop temporary table if exists temp;

# (b)
create temporary table temp select distinct(EmpID) from COURSE;
create temporary table temp2 select Department, count(Name) as num from EMPLOYEE inner join temp on EMPLOYEE.ID=temp.EmpID group by Department;
select EMPLOYEE.Department, avg(Salary) as Average_Salary from EMPLOYEE inner join temp2 on EMPLOYEE.Department=temp2.Department where temp2.num>1 group by temp2.Department;
drop temporary table if exists temp2;
drop temporary table if exists temp;


# (c)
create temporary table temp select distinct EmpID from COURSE where Prof='prof1038';
select avg(Salary) as Average_Salary from EMPLOYEE right join temp on EMPLOYEE.ID=temp.EmpID;
drop temporary table if exists temp;

