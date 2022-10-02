create database attendance_db
use attendance_db

create table mark_attendance(rollno int not null primary key,current_day varchar(100),InTime varchar(100),InDate date);
drop table mark_attendance
drop table personal_details

select * from mark_attendance

create table personal_details(rollno int not null primary key ,stud_name varchar(100) , department varchar(100),stud_year varchar(100));
insert into personal_details values (20239,'Badri Narayanan', 'Computer Science' , 'III'),
(20240,'Rosan', 'Computer Science' , 'III'),
(20241,'Virat', 'Computer Science' , 'III'),
(20242,'Rohit', 'Computer Science' , 'III'),
(20243,'Kofi Kingston', 'Computer Science' , 'III')

insert into personal_details values (20219,'AJAY', 'Computer Science' , 'III')

create view view1 as
select mark_attendance.rollno , personal_details.stud_name , personal_details.department, personal_details.stud_year , mark_attendance.InDate , mark_attendance.InTime , mark_attendance.current_day
from personal_details 
full outer join mark_attendance
on personal_details.rollno = mark_attendance.rollno 
where mark_attendance.InDate = CAST( GETDATE() AS Date )
drop view view1
select * from view1
drop table mark_attendance
drop table personal_details
select * from personal_details


create view view2 as
select mark_attendance2.rollno , personal_details.stud_name , personal_details.department, personal_details.stud_year , mark_attendance2.OutDate , mark_attendance2.OutTime , mark_attendance2.current_day
from personal_details 
full outer join mark_attendance2
on personal_details.rollno = mark_attendance2.rollno 
where mark_attendance2.OutDate = CAST( GETDATE() AS Date


create table mark_attendance2(rollno int not null primary key,current_day varchar(100),OutTime varchar(100),OutDate date);
select * from mark_attendance2

select * from view2
select * from personal_details
drop table mark_attendance2