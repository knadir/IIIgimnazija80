--INSERT INTO dolaze(id,ime_i_prezime,razred_id)
select ROW_NUMBER() OVER () row_number,IME_I_PREZIME,r.id
from KO_DOLAZI k,razredi r
where substr(k.razred,3,2)=substr(r.razred,4,2)
order by r.id
