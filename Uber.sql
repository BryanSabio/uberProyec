CREATE DATABASE Microlocations;

USE Microlocations;

CREATE TABLE Locations (
id varchar(50) NOT NULL,
latitud varchar(20) NOT NULL,
longitud varchar(20) NOT NULL,
PRIMARY KEY (id) 
);

CREATE TABLE Trips (
id varchar(50) NOT NULL,
userId varchar(50) NOT NULL,
empieza datetime NOT NULL,
termina datetime NOT NULL,
PRIMARY KEY (id) 
);

insert into Locations (id, latitud, longitud)
values ("sd","juju","lala")


##para compartir el puerto de flas 

# empezar con micro en py.

