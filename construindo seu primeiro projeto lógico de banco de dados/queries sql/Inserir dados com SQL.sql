INSERT INTO Produto (nome, descricao) VALUES
('Camiseta', 'Camiseta de algodão'),
('Calça Jeans', 'Calça jeans slim fit'),
('Tênis', 'Tênis esportivo');
INSERT INTO Vendedor_has_Produto (Vendedor_idVendedor, Produto_idProduto, comissao) VALUES
(1, 1, 0.1),
(1, 2, 0.15),
(2, 3, 0.12);
INSERT INTO Vendedor (nome, email, telefone) VALUES
('Ana Santos', 'ana@example.com', '9876543210'),
('Carlos Oliveira', 'carlos@example.com', '1234567890');
INSERT INTO Produto_has_Fornecedor (Produto_idProduto, Fornecedor_idFornecedor, preco) VALUES
(1, 1, 30.00),
(1, 2, 25.00),
(2, 2, 80.00),
(3, 3, 120.00);
INSERT INTO Fornecedor (nome, endereco) VALUES
('Fornecedor A', 'Rua A, 123'),
('Fornecedor B', 'Rua B, 456'),
('Fornecedor C', 'Rua C, 789');
INSERT INTO Estoque_has_Produto (Estoque_idEstoque, Produto_idProduto, quantidade, data_entrada) VALUES
(1, 1, 10, '2023-07-14 10:00:00'),
(1, 2, 5, '2023-07-14 11:30:00'),
(2, 1, 8, '2023-07-13 09:45:00'),
(2, 3, 12, '2023-07-12 14:20:00');
INSERT INTO Estoque (local, nome) VALUES
('São Paulo', 'Estoque A'),
('Rio de Janeiro', 'Estoque B');
INSERT INTO Produto_has_Pedido (Produto_idProduto, Pedido_idPedido, quantidade) VALUES
(1, 1, 2),
(2, 1, 1),
(3, 2, 3),
(1, 3, 1);
INSERT INTO Pedido (status, Cliente_idCliente, data, total) VALUES
('Em andamento', 1, '2023-07-14', 50.00),
('Concluído', 2, '2023-07-12', 120.00),
('Em andamento', 3, '2023-07-10', 80.00);
clienteINSERT INTO Cliente (nome, email, telefone) VALUES
('João Silva', 'joao@example.com', '1234567890'),
('Maria Souza', 'maria@example.com', '9876543210'),
('Pedro Oliveira', 'pedro@example.com', '4567891230');

