create or replace package body utility as
procedure p_start_load(o_id out number) is
l_id number;
begin
l_id := loads_seq.nextval;
insert into loads values (
l_id,
trunc(sysdate),
to_char(sysdate, 'HH24:MI:SS'),
systimestamp
);
commit;
o_id := l_id;
end p_start_load;

function f_provjeri_sifru(i_izv_id in number, i_sifra in number) return boolean is
l_sifra number;
begin
select sifra into l_sifra from load_links
where izv_id = i_izv_id
and sifra = i_sifra;

return true;
exception
when no_data_found then
return false;
end f_provjeri_sifru;

procedure p_insert_load_link(
    i_hyperlink varchar2, 
    i_load_id in number, 
    i_izvor in varchar2, 
    i_sifra in number, 
    o_id out number) is
l_izv_id number;
l_id number;
begin
select id into l_izv_id from izvor
where izvor = i_izvor;
if not f_provjeri_sifru(l_izv_id, i_sifra) then
    l_id := load_links_seq.nextval;
    insert into load_links values(
    l_id,
    i_load_id,
    i_hyperlink,
    i_sifra,
    l_izv_id,
    systimestamp);
    o_id := l_id;
else
    o_id := 1;
end if;
commit;
end p_insert_load_link;

procedure p_insert_oglas(
    i_lol_id in number,
    i_cijena in number,
    i_datum in varchar2,
    i_slike in tt_varchar2,
    o_id out number) is
l_id number;
begin
l_id := oglasi_seq.nextval;
insert into oglasi values(
    l_id,
    i_lol_id,
    i_cijena,
    to_date(i_datum, 'DD.MM.YYYY.'));
for i in 1..i_slike.count loop
insert into oglasi_slike values(
    oglasi_slike_seq.nextval,
    l_id,
    i_slike(i));
end loop;
commit;
o_id := l_id;
end p_insert_oglas;
end utility;