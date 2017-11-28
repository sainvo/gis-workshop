begin;

create table if not exists street (id serial not null primary key, street_name text not null);
-- Add geometry column with type LINESTRING, SRID 4362 and dimension 2
select AddGeometryColumn('public', 'street', 'geometry', 3067, 'LINESTRING', 2);

commit;
