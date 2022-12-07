select current_timestamp;

create table produkty(
id_produktu serial primary key,
	nazwa text not null,
	cena numeric not null,
	opis text,
	stan integer
);

insert into produkty(nazwa,cena,opis,stan) values ('Bulbulator',69,'Urządzenie robiące bul bul',10);
insert into produkty(nazwa,cena,opis,stan) values ('Półoś do Jelcza',500,'Wiadomo, niezbednik',3);
insert into produkty(nazwa,cena,opis,stan) values ('Wihajster',20,'Takie coś z takim czymś bez takiego czegoś',5);

select * from produkty;

create table pracownicy(
	id_pracownika serial primary key,
	imie text not null,
	nazwisko text not null,
	zarobki numeric,
	komentarz text
);

insert into pracownicy(imie,nazwisko,zarobki,komentarz) values ('Stefan','Burczymucha',6000,'fajny kolega');
insert into pracownicy(imie,nazwisko,zarobki,komentarz) values ('Czesław','Informator',10000,'kabluje do szefa');
insert into pracownicy(imie,nazwisko,zarobki,komentarz) values ('Arnold','Boczek',7000,'lubi golonkę i piwo');

select * from pracownicy;
--DBEAVER


create table zawodnicy(
id_zawodnika integer primary key,
imie text,
nazwisko text,
wzrost numeric,
masa numeric
);

select  * from zawodnicy;