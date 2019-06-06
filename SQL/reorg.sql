create table loads (id number primary key, datum_loada date, vrijeme_loada varchar2(100), kreirano timestamp);
CREATE SEQUENCE loads_seq
  MINVALUE 1
  MAXVALUE 999999
  START WITH 1
  INCREMENT BY 1
  CACHE 20;

create table load_links (id number primary key, 
load_id number, constraint links_load_fk foreign key(load_id) references loads(id),
hyperlink varchar2(1000),
sifra number,
izv_id number, constraint links_izvor_fk foreign key(izv_id) references izvor(id),
kreirano timestamp);

CREATE INDEX load_links_sifra_ind
  ON load_links (sifra)
  COMPUTE STATISTICS;

CREATE SEQUENCE load_links_seq
  MINVALUE 1
  MAXVALUE 999999
  START WITH 1
  INCREMENT BY 1
  CACHE 20;
  
  create table izvor (id number primary key, izvor varchar2(100));
  insert into izvor values (1, 'PLAVI OGLASNIK');
  insert into izvor values (2, 'NJUSKALO');
  insert into izvor values (3, 'INDEX OGLASI');
  commit;