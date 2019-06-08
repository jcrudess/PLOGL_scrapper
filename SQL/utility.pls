create or replace package utility as
type tt_varchar2 is table of varchar2(1000) index by binary_integer;
procedure p_start_load(o_id out number);
procedure p_insert_load_link(
    i_hyperlink in varchar2, 
    i_load_id in number, 
    i_izvor in varchar2, 
    i_sifra in number, 
    o_id out number);
procedure p_insert_oglas(
    i_lol_id in number,
    i_cijena in number,
    i_datum in varchar2,
    i_slike in tt_varchar2,
    o_id out number);

end utility;

