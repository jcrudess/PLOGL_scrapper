create or replace package utility as
procedure p_start_load(o_id out number);
procedure p_insert_load_link(
    i_hyperlink in varchar2, 
    i_load_id in number, 
    i_izvor in varchar2, 
    i_sifra in number, 
    o_postoji out number);
end utility;

