-- Retorna os pedidos com valor total maior que 100
SELECT idPedido, SUM(total) AS total_pedido
FROM Pedido
GROUP BY idPedido
HAVING total_pedido > 100;

-- Retorna os produtos com quantidade total em estoque menor que 50
SELECT p.idProduto, p.nome, SUM(e.quantidade) AS total_estoque
FROM Produto p
JOIN Estoque_has_Produto e ON p.idProduto = e.Produto_idProduto
GROUP BY p.idProduto
HAVING total_estoque < 50;
