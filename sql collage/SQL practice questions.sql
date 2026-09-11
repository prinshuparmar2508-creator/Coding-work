insert into EMPLOYEE(EmpID,EmpName,Email,Department,Salary,Age,city)
	values(01,"Emp1","yegneshsharma1@gmail.com","Dep1",55000,21,"bhiwani"),
		  (02,"Emp2","yegneshsharma2@gmail.com","Dep1",54000,20,"rohtak"),
          (03,"Emp3","yegneshsharma3@gmail.com","Dep2",70000,24,"bhiwani"),
          (04,"Emp4","yegneshsharma4@gmail.com","Dep1",55000,21,"bhiwani"),
          (05,"Emp5","yegneshsharma5@gmail.com","Dep3",65000,23,"jind");
select * from EMPLOYEE;
select EmpName,Salary 
from EMPLOYEE;
select EmpName,EmpID 
from EMPLOYEE where (Salary>40000);
select EmpID,EmpName
from EMPLOYEE where (Department = "Dep1");
select EmpID,EmpName
from EMPLOYEE where (25<age and age<35);
select * from EMPLOYEE order by Salary desc;
alter table EMPLOYEE add Experience numeric(2);
alter table EMPLOYEE modify EmpName varchar(50);
alter table EMPLOYEE rename column city to Adress;
alter table EMPLOYEE drop column Experience;
update EMPLOYEE set Salary=60000 where EmpID=04;
delete from EMPLOYEE where EmpID=02;