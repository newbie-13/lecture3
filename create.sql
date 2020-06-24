create table flights(
  id serial primary key,
  origin varchar not null,
  destination varchar not null,
  duration integer not null
);

insert into flights (origin, destination, duration) values ('New York', 'London', 415);
insert into flights (origin, destination, duration) values ('Shanghai', 'Paris', 760);
insert into flights (origin, destination, duration) values ('Istanbul', 'Tokyo', 700);
insert into flights (origin, destination, duration) values ('New York', 'Paris', 435);
insert into flights (origin, destination, duration) values ('Moscow', 'Paris', 245);
insert into flights (origin, destination, duration) values ('Lima', 'New York', 455);
/*write*/

select * from flights;
select * from flights limit 2;
select * from flights order by duration asc limit 3;
select * from flights order by duration desc limit 3;
select orgin, destination from flights;
select * from flights where id=3;
select * from flights where destination='Paris' and duration>500;
select avg(duration) from flights where origin='New York';
select count(*) from flights where origin='New York';
select min(duration) from flights where origin in ('New York', 'Lima');
select * from flights where origin like '%York%';
select origin, count(*) from flights group by origin having count(*)>1;
/*read*/

update flights
  set duration=430  /*modify*/
  where origin='New York' and destination='London'; /*scope of modification*/

delete from flights where destination='Tokyo';
/*delete*/

create table passengers(
  id serial primary key,
  name varchar not null,
  flight_id integer references flights
);

insert into passengers (name, flight_id) values ('Alice',1);
insert into passengers (name, flight_id) values ('Bob',1);
insert into passengers (name, flight_id) values ('Charlie',2);
insert into passengers (name, flight_id) values ('Don',2);
insert into passengers (name, flight_id) values ('Eason',4);
insert into passengers (name, flight_id) values ('Fan',6);
insert into passengers (name, flight_id) values ('Grace',6);

select origin, destination, name from flights join passengers on passengers.flight_id=flights.id;
/*inner join*/

select origin, destination, name from flights left join passengers on passengers.flight_id=flights.id;
/*left join*/

select origin, destination, name from flights right join passengers on passengers.flight_id=flights.id;
/*right join*/

select * from flights where id in(
  select flight_id from passengers group by flight_id having count(*)>1
);

begin;
commit;
