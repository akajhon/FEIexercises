SELECT SUM(L.valor) as faturamento, E.entrega_tipo as tipo_de_entrega,
Case Extract(month from A.data) 
when 1 then 'Janeiro'
when 2 then 'Fevereiro'
when 3 then 'Março'
when 4 then 'Abril'
when 5 then 'Maio'
when 6 then 'Junho'
when 7 then 'Julho'
when 8 then 'Agosto'
when 9 then 'Setembro'
when 10 then 'Outubro'
when 11 then 'Novembro'
when 12 then 'Dezembro'
else NULL
end
as mes
FROM agendamento A
INNER JOIN entregador_lavagem E
ON A.id_lavagem = E.id_lavagem
INNER JOIN lavagem L
ON L.id_lavagem = E.id_lavagem
WHERE Extract(month from A.data) <= Extract(month from Now())
AND Extract(month from A.data) >= Extract(month from Now() - Interval '90 day')
GROUP BY E.entrega_tipo, Extract(month from A.data)
ORDER BY Extract(month from A.data) DESC
