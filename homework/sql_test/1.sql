SELECT category, city , website
FROM "2gis_businesses"
WHERE category like "кафе%" or category like "%магазин%"
and city == "Москва" and email IS NOT NULL