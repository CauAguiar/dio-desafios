-- Retorna os produtos com preço maior que 50
SELECT * FROM Produto WHERE preco > 50;

-- Retorna os clientes com nome começando com "A"
SELECT * FROM Cliente WHERE nome LIKE 'A%';

-- Retorna os pedidos com status "Em andamento"
SELECT * FROM Pedido WHERE status = 'Em andamento';
