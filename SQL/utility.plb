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
    o_postoji out number) is
l_izv_id number;
begin
select id into l_izv_id from izvor
where izvor = i_izvor;
if not f_provjeri_sifru(l_izv_id, i_sifra) then
    insert into load_links values(
    load_links_seq.nextval,
    i_load_id,
    i_hyperlink,
    i_sifra,
    l_izv_id,
    systimestamp);
    o_postoji := 0;
else
    o_postoji := 1;
end if;
commit;
end p_insert_load_link;
end utility;