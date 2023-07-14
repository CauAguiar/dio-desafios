-- Retorna o total de cada pedido
SELECT idPedido, SUM(total) AS total_pedido FROM Pedido GROUP BY idPedido;

-- Retorna o valor total de cada produto em estoque
SELECT p.idProduto, p.nome, SUM(e.quantidade) AS total_estoque
FROM Produto p
JOIN Estoque_has_Produto e ON p.idProduto = e.Produto_idProduto
GROUP BY p.idProduto;
