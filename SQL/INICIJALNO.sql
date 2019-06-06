create table inicijalno (id number, kategorija varchar2(100), sifra_oglasa number, link varchar2(500), opis varchar2(4000), lokacija varchar2(500), cijena number, 
datum_oglasa date, broj_pregleda number, kreirao varchar2(3), datum_kreiranja timestamp, azurirao varchar2(3), datum_azuriranja timestamp);

create unique index inicijalno_ind on inicijalno (id);

create sequence inicijalno_seq
minvalue 1
maxvalue 999999
start with 1
increment by 1
cache 20;