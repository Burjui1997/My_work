SELECT name, city
FROM "2gis_businesses"
WHERE name like "%котик%" and name not like "%наркотик%"
AND city == "Москва"