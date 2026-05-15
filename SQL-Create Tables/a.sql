-- create table if not exists
create table if not exists empl(
    Eno char(3),
    Ename varchar(15),
    age int(2),
    gen char(1),
    sal int(7),
    exp int(2),
    loc varchar(15),
    dno char(3)
);

-- insert values
insert into empl values
('E01','Tenzin',32,'M',50000,2,'Delhi','D03'),
('E02','San',39,'M',40000,8,NULL,'D02'),
('E03','Mady',27,'F',30000,4,'Mumbai','D01'),
('E04','Arnold',NULL,'M',50000,9,'Delhi','D02'),
('E05','Prag',43,'M',50000,3,'Mumbai','D04'),
('E06','Sana',38,'F',37000,0,'Pune','D03'),
('E07','Aari',27,'F',48000,1,NULL,'D04'),
('E08','Prabh',NULL,'M',72000,6,'Pune','D01'),
('E09','Mahi',21,'F',54000,5,'Mumbai','D03');

-- view all records
select * from empl;

-- display the names of employees
select ename from empl;

-- display the names and age of employees whose age is more than 30
select ename, age from empl where age > 30;

-- display names of female employees
select ename from empl where gen = 'F';

-- display the names of employees which are starting with either A or S
select ename from empl where ename like 'A%' or ename like 'S%';

/*
Wildcards:
% : any number of characters
_ : exactly 1 character

Examples:
J%   → names starting with J
%a   → names ending with a
J_   → J followed by exactly one character
J_e% → J, then any one character, then 'e', followed by anything
*/


-- display maximum age and minimum experience of the employees whose names end with 'i' or 'a'
select max(Age), min(Exp)
from emp1
where ename like '%a' or ename like '%i';

-- display maximum age for male employees whose names are more than 3 characters long
select max(age)
from emp1
where gen = 'M' and ename like '___%';

-- display names of female employees whose names contain 'i' anywhere
-- and either experience is more than 1 year or age is less than 40
select Ename
from emp1
where gen = 'F' and ename like '%i%' and (exp > 1 or age < 40);
#display total number of female employees
select count(*)
from empl
where gen='F';

#display total salary paid to male employees whose experience is more than 3 years and names are more than 3 characters long
select sum(sal)
from empl
where exp>3
and gen='M'
and ename like '____%';

#display average age for female employees
select avg(age)
from empl
where gen='F';

#display unique department numbers in which the employees are working
select DISTINCT(dno)
from empl;

select dno
from empl;
















-- create table if not exists
create table if not exists empl(
    Eno char(3),
    Ename varchar(15),
    age int(2),
    gen char(1),
    sal int(7),
    exp int(2),
    loc varchar(15),
    dno char(3)
);

-- insert values
insert into empl values
('E01','Tenzin',32,'M',50000,2,'Delhi','D03'),
('E02','San',39,'M',40000,8,NULL,'D02'),
('E03','Mady',27,'F',30000,4,'Mumbai','D01'),
('E04','Arnold',NULL,'M',50000,9,'Delhi','D02'),
('E05','Prag',43,'M',50000,3,'Mumbai','D04'),
('E06','Sana',38,'F',37000,0,'Pune','D03'),
('E07','Aari',27,'F',48000,1,NULL,'D04'),
('E08','Prabh',NULL,'M',72000,6,'Pune','D01'),
('E09','Mahi',21,'F',54000,5,'Mumbai','D03');

-- view all records
select * from empl;

-- display the names of employees
select ename from empl;

-- display the names and age of employees whose age is more than 30
select ename, age from empl where age > 30;

-- display names of female employees
select ename from empl where gen = 'F';

-- display the names of employees which are starting with either A or S
select ename from empl where ename like 'A%' or ename like 'S%';

-- display maximum age and minimum experience of the employees whose names end with 'i' or 'a'
select max(age), min(exp)
from empl
where ename like '%a' or ename like '%i';

-- display maximum age for male employees whose names are more than 3 characters long
select max(age)
from empl
where gen = 'M' and ename like '___%';

-- display names of female employees whose names contain 'i' anywhere
-- and either experience is more than 1 year or age is less than 40
select ename
from empl
where gen = 'F' and ename like '%i%' and (exp > 1 or age < 40);

-- display total number of female employees
select count(*)
from empl
where gen='F';

-- display total salary paid to male employees whose experience is more than 3 years and names are more than 3 characters long
select sum(sal)
from empl
where exp>3
and gen='M'
and ename like '____%';

-- display average age for female employees
select avg(age)
from empl
where gen='F';

-- display unique department numbers in which the employees are working
select distinct(dno)
from empl;

-- display employee names starting with 'A' or 'S'
select ename
from empl
where ename like 'A%' or ename like 'S%';

-- display total number of employees working in department 'D01' or 'D03'
select count(*)
from empl
where dno in ('D01','D03');

-- display average salary and maximum age of male employees
select avg(sal), max(age)
from empl
where gen = 'M';

-- display total number of employees whose age is more than 30
select count(*)
from empl
where age > 30;

-- display unique age of employees
select distinct age
from empl;
