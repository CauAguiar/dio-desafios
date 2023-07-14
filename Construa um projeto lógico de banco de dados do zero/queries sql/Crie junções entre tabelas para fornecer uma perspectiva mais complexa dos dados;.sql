-- Recuperar informações de um serviço, incluindo cliente e peças utilizadas
SELECT servico.servico_id, cliente.nome AS cliente, peca.nome AS peca, utiliza.quantidade_utilizada
FROM servico
JOIN cliente ON servico.cliente_id = cliente.cliente_id
JOIN utiliza ON servico.servico_id = utiliza.servico_id
JOIN peca ON utiliza.peca_id = peca.peca_id
WHERE servico.servico_id = 1;
