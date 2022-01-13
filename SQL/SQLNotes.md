

using where

```sql
SELECT 
  player_name as Name, birthday as "Player Birthday"
FROM
  player 
  where weight > 190 and height > 190 --both must be met
SELECT 
  player_name as Name, birthday as "Player Birthday"
FROM
  where Name = 'Aaron galindo'
  --where Name like Aaron
  where Name = 'Aaron%' -- all names that begin with Aaron
  where Name = '%Aaron' -- all names that end with Aaron
  where Name = 'A%n' -- all names that start with A and ends with n
  where Name = 'T_m%' -- needs the initial T, to start with, then any single character then has to have m, then can have anything else in the sequence. e.g. Tamas Hajnal, Tim Cahall, Tom Sebastian and so on

-- % can be an number of characters 
-- _ is one character
  where Name in ('Cristiano Ronaldo', 'Lionel Messi') 
```


the between keyword
```sql
SELECT 
  player_name as Name, birthday as "Player Birthday"
FROM
  where weight between 180 and 190
```
```sql
SELECT 
  *
FROM
  match -- different table this time
  where home_player is not null -- finding all the non null values, the ones that are actually filled out
```

```sql
SELECT *
FROM 
  player
ORDER BY weight desc --gets the weight and descending
```

to join two tables together
```sql
SELECT 
   player_attributes.player_api_id,
   player.player_name
   player_attributes.date,
   player_attributes.overall_rating 
FROM
   Player_Attributes
    inner join player b on Player_Attributes.player_api_id = player.player_api_id -- player_api_id is the same on both fields, this will mean it is able to access the fields that are in player, but are not in player_attributes
```

you can give the tables aliases, i.e. shorter names so that you can make the SQL code much cleaner

```sql
SELECT 
   a.player_api_id,
   b.player_name
   sum(a.overall_rating) as rating --adds all of the ratings from the different dates together
    count(a.player_name) as frequency --shows how many times the player appears in the table
    avg(a.overall_rating) as average_rating 
FROM
   Player_Attributes a
    inner join player b on a.player_api_id = player.b
    group by a.player_api_id, player_name -- want to remove the date field otherwise it will add all of them together
    order by rating desc -- orders it by decending rate
```

creating new tables

```sql
CREATE TABLE bond(
id INT PRIMARY KEY, --the key needed to identify the record, has to be unique no duplicate values and cannot be null
title VARCHAR(50) UNIQUE, --character array/string need to specify how many characters, also no duplicate values
released INT NOT NULL,  
actor VARCHAR(30),
director VARCHAR(30),
box_office DECIMAL(5,1) DEFAULT '0.0' -- must match the data type
);

DROP TABLE bond --will delete the table
```

```sql
INSERT INTO bond VALUES
(1, 'DR.NO', 1962, 'SEAN CONNERY', 'Terence Young', 59.5)
```

```sql
INSERT INTO bond(id, title, released) VALUES
(2, 'FROM RUSSIA WITH LOVE', 1962)
```

```sql
ALTER TABLE bond ADD studio VARCHAR(30) -- to add a new field
ALTER TABLE bond DROP studio -- to delete

describe bond -- to see what are the data types and the names of the fields
```

```sql
UPDATE bond
SET actor = 'Connery'
where actor = 'SEAN CONNERY'
```

```sql
SELECT *
FROM Customers
WHERE state IN ('VA', 'FL', 'GA')
-- WHERE state = 'VA' OR state = 'FL' OR state = 'GA'

WHERE state NOT IN ('VA', 'FL', 'GA')
```

```sql

SELECT *
FROM Orders
WHERE stock IN (49, 39, 72)
```

```sql
SELECT * 
FROM Customers
WHERE points BETWEEN 1000 AND 3000
--WHERE points >= 1000 AND points <= 3000
```