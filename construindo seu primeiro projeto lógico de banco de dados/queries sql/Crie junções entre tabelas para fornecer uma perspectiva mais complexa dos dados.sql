-- Retorna todos os pedidos juntamente com as informações do cliente associado
SELECT p.idPedido, p.status, c.nome AS nome_cliente
FROM Pedido p
JOIN Cliente c ON p.Cliente_idCliente = c.idCliente;

-- Retorna todos os produtos juntamente com as informações dos fornecedores associados
SELECT p.idProduto, p.nome AS nome_produto, f.nome AS nome_fornecedor
FROM Produto p
JOIN Produto_has_Fornecedor pf ON p.idProduto = pf.Produto_idProduto
JOIN Fornecedor f ON pf.Fornecedor_idFornecedor = f.idFornecedor;
