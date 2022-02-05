drop table if exists visitantes;
create table visitantes(
id_visita int auto_increment primary key,
nombre varchar(50) not null,
email varchar(50) not null,
celular varchar(20) not null
);