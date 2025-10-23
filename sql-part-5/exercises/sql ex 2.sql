/*
select base_name,
RIGHT(base_name,3) as last_3_characters
from RideShareDb.dbo.other_FHV_services_jan_aug_2015
*/

/*
select Base_Name,
       CHARINDEX(' ',Number_of_Trips)as space_location_of_trips,
       CHARINDEX(' ',Number_of_pickups) as space_location_of_pickups
from RideShareDB.dbo.other_FHV_services_jan_aug_2015
*/

/*
SELECT Base_Name,
       DATENAME(MONTH,Pick_Up_Date) as Month_Name
from RideShareDB.dbo.other_FHV_services_jan_aug_2015
ORDER BY MONTH(Pick_Up_Date) DESC;   
*/


/*
SELECT Base_Name,
       DAY(Pick_Up_Date) as Day_Number,
       DATENAME(MONTH,Pick_Up_Date) as Month_Name
FROM RideShareDB.dbo.other_FHV_services_jan_aug_2015
ORDER BY Day_Number;
*/


