# 1
select Name from Employee where Department='Software';

# 2
select Name from Employee inner join (select Name as manager_name, Salary as manager_salary from Employee)as temp on Employee.Manager=temp.manager_name where Salary>manager_salary+5000;

# 3
select distinct Name from (Employee inner join Course on Employee.Name=Course.Student) inner join (select Student as manager_name, Subj as manager_subj, grade as manager_grade from Course where Student in (select Manager from Employee)) as temp on temp.manager_name=Employee.Manager and temp.manager_subj=Course.Subj where Grade>manager_grade;

# 4
select Name from Employee where Name not in (select Student from Course);

# 5
select distinct Department from Employee where Department not in (Select distinct Department from Employee where Name not in (select Student from Course));

# 6
create temporary table temp select Student, count(Student) as name_num from Course group by Student;
select distinct Department from Employee where Department not in (select distinct Department from Employee left join temp on Employee.Name=temp.Student where temp.name_num<2 or temp.name_num is NULL);
drop temporary table if exists temp;

# 7
select avg(salary) as Average_Salary from Employee;

# 8
select min(salary) as Min_Salary from Employee inner join Course on Employee.Name=Course.Student where Course.Prof='Roe';

# 9
create temporary table temp select Department,count(Name)as num from Employee inner join Course on Employee.Name=Course.Student group by Department;
select Department, avg(Salary) as Average_Salary from Employee where Department in (select Department from temp where num>3) group by Department;
drop temporary table if exists temp;

# 10
create temporary table temp1 select Department, count(Name) as total_num from Employee group by Department;
create temporary table temp2 select Department, count(Name) as no_course_num from Employee where Name not in (select Student from Course) group by Department;
select temp1.Department,  ifnull(no_course_num,0)/total_num*100 as percentage from temp1 left join temp2 on temp1.Department=temp2.Department;
drop temporary table if exists temp1;
drop temporary table if exists temp2;
