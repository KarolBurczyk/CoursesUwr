--zad1
-- drop materialized view if exists skill_offer_mat_view;
-- create materialized view if not exists skill_offer_mat_view as
-- select 
--     s.name as skill, 
--     o.city as city,
--     (select count(distinct o2.id) from offer o2 join employment_details e on o2.id = e.offer_id join skill s2 on o2.id = s2.offer_id where e.type = 'permanent' and s2.name = s.name and o2.city = o.city) as permanent_count,
--     (select count(distinct o2.id) from offer o2 join employment_details e on o2.id = e.offer_id join skill s2 on o2.id = s2.offer_id where e.type = 'b2b' and s2.name = s.name and o2.city = o.city) as b2b_count
-- from offer o join skill s on o.id = s.offer_id join employment_details e on o.id = e.offer_id
-- group by s.name, o.city;
-- select * from skill_offer_mat_view where city = 'Wrocław' and skill = 'SQL' limit 100;
--zad2
drop table if exists skill_offer_table;
create table skill_offer_table (
    skill text,
    city text,
    permanent_count int,
    b2b_count int,
    primary key (skill, city)
);
insert into skill_offer_table (skill, city, permanent_count, b2b_count)
select skill, city, permanent_count, b2b_count from (
    select 
    s.name as skill, 
    o.city as city,
    (select count(distinct o2.id) from offer o2 join employment_details e on o2.id = e.offer_id join skill s2 on o2.id = s2.offer_id where e.type = 'permanent' and s2.name = s.name and o2.city = o.city) as permanent_count,
    (select count(distinct o2.id) from offer o2 join employment_details e on o2.id = e.offer_id join skill s2 on o2.id = s2.offer_id where e.type = 'b2b' and s2.name = s.name and o2.city = o.city) as b2b_count
    from offer o join skill s on o.id = s.offer_id join employment_details e on o.id = e.offer_id
    group by s.name, o.city
) where permanent_count > 0 or b2b_count > 0;
select * from skill_offer_table where city = 'Wrocław' and skill = 'SQL' limit 100;
--zad3
-- INSERT

CREATE OR REPLACE FUNCTION ins() RETURNS TRIGGER AS $O$
DECLARE
  thiscity TEXT;
  is_perm BOOL;
  is_b2b BOOL;
BEGIN
  SELECT city,
      BOOL_OR(type = 'permanent'),
      BOOL_OR(type = 'b2b')
    INTO thiscity, is_perm, is_b2b
    FROM offer JOIN employment_details ON id = offer_id
    WHERE id = NEW.offer_id
    GROUP BY city;
  IF NOT (is_perm OR is_b2b) THEN
    RETURN NEW;
  END IF;
  IF (NEW.name, thiscity) IN (
    SELECT skill, city FROM skill_offer_table
  ) THEN
    UPDATE skill_offer_table
      SET permanent_offers = permanent_offers + is_perm::INT,
        b2b_offers = b2b_offers + is_b2b::INT
      WHERE skill = NEW.name AND city = thiscity;
  ELSE
    INSERT INTO skill_offer_table VALUES
      (NEW.name, thiscity, is_perm::INT, is_b2b::INT);
  END IF;
  RETURN NEW;
END;
$O$ LANGUAGE plpgsql;

CREATE TRIGGER ins AFTER INSERT ON skill
FOR EACH ROW EXECUTE PROCEDURE ins();

-- DELETE

CREATE OR REPLACE FUNCTION del() RETURNS TRIGGER AS $O$
DECLARE
  thiscity TEXT;
  is_perm BOOL;
  is_b2b BOOL;
BEGIN
  SELECT city,
      BOOL_OR(type = 'permanent'),
      BOOL_OR(type = 'b2b')
    INTO thiscity, is_perm, is_b2b
    FROM offer JOIN employment_details ON id = offer_id
    WHERE id = OLD.offer_id
    GROUP BY city;
  IF NOT (is_perm OR is_b2b) THEN
    RETURN OLD;
  END IF;
  IF (is_perm::INT, is_b2b::INT) = (
    SELECT permanent_offers, b2b_offers
      FROM skill_offer_table
      WHERE skill = OLD.name AND city = thiscity
  ) THEN
    DELETE FROM skill_offer_table
      WHERE skill = OLD.name AND city = thiscity;
  ELSE
    UPDATE skill_offer_table
      SET permanent_offers = permanent_offers - is_perm::INT,
        b2b_offers = b2b_offers - is_b2b::INT
      WHERE skill = OLD.name AND city = thiscity;
  END IF;
  RETURN OLD;
END;
$O$ LANGUAGE plpgsql;

CREATE TRIGGER del AFTER DELETE ON skill
FOR EACH ROW EXECUTE PROCEDURE del();

-- UPDATE
-- zmianę name gwarantuje klauzula WHEN w CREATE TRIGGER
-- brak zmiany offer_id (a więc i miasta) gwarantuje treść zadania

CREATE OR REPLACE FUNCTION upd() RETURNS TRIGGER AS $O$
DECLARE
  thiscity TEXT;
  is_perm BOOL;
  is_b2b BOOL;
BEGIN
  SELECT city,
      BOOL_OR(type = 'permanent'),
      BOOL_OR(type = 'b2b')
    INTO thiscity, is_perm, is_b2b
    FROM offer JOIN employment_details ON id = offer_id
    WHERE id = OLD.offer_id
    GROUP BY city;
  IF NOT (is_perm OR is_b2b) THEN
    RETURN NEW;
  END IF;
  -- poniższy IF-ELSE skopiowany z ins()
  IF (NEW.name, thiscity) IN (
    SELECT skill, city FROM skill_offer_table
  ) THEN
    UPDATE skill_offer_table
      SET permanent_offers = permanent_offers + is_perm::INT,
        b2b_offers = b2b_offers + is_b2b::INT
      WHERE skill = NEW.name AND city = thiscity;
  ELSE
    INSERT INTO skill_offer_table VALUES
      (NEW.name, thiscity, is_perm::INT, is_b2b::INT);
  END IF;
  -- poniższy IF-ELSE skopiowany z del()
  IF (is_perm::INT, is_b2b::INT) = (
    SELECT permanent_offers, b2b_offers
      FROM skill_offer_table
      WHERE skill = OLD.name AND city = thiscity
  ) THEN
    DELETE FROM skill_offer_table
      WHERE skill = OLD.name AND city = thiscity;
  ELSE
    UPDATE skill_offer_table
      SET permanent_offers = permanent_offers - is_perm::INT,
        b2b_offers = b2b_offers - is_b2b::INT
      WHERE skill = OLD.name AND city = thiscity;
  END IF; 
  RETURN NEW;
END;
$O$ LANGUAGE plpgsql;

CREATE TRIGGER upd AFTER UPDATE ON skill
FOR EACH ROW
WHEN (OLD.name IS DISTINCT FROM NEW.name)
EXECUTE PROCEDURE upd();

-- testy

SELECT * FROM skill_offer_table
  WHERE city = 'Żyrardów' AND skill LIKE 'C%';

INSERT INTO skill VALUES ('C++', 31337, 3901), ('Caml', 161, 4774);

SELECT * FROM skill_offer_table
  WHERE city = 'Żyrardów' AND skill LIKE 'C%';

DELETE FROM skill
  WHERE (name, offer_id) = ('C++', 3901)
    OR (name, offer_id) = ('Caml', 4774);

SELECT * FROM skill_offer_table
  WHERE city = 'Żyrardów' AND skill LIKE 'C%';

UPDATE skill SET name = 'Caml'
  WHERE (name, offer_id) = ('C++', '4774');
UPDATE skill SET name = 'C#'
  WHERE (name, offer_id) = ('C', 9522);

SELECT * FROM skill_offer_table
  WHERE city = 'Żyrardów' AND skill LIKE 'C%';

ROLLBACK;
