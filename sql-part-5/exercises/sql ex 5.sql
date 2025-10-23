
create table Sep2025JunkDB.jayanthi_kotturi.planned_makes(
make_id int primary key identity(1,1),
project_name  VARCHAR (150),
category VARCHAR (200),
planned_date DATE
);


---Adding  3 rows to table
INSERT into Sep2025JunkDB.jayanthi_kotturi.planned_makes(project_name,category,planned_date)
values ('Chocolate_cake','dessert','10-24-2025' ),
('Biryani','main_course','10-30-2025'),
('Candy','snack','10-31-2025');

--update a row
UPDATE  Sep2025JunkDB.jayanthi_kotturi.planned_makes
set project_name = 'Pizza'
where category ='snack'

---Delete a row
DELETE from Sep2025JunkDB.jayanthi_kotturi.planned_makes
where category = 'snack'

---Drop a TABLE
DROP table Sep2025JunkDB.jayanthi_kotturi.planned_makes

