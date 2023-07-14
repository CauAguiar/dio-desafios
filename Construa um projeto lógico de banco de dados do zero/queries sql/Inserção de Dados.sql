-- Inserir um novo cliente
INSERT INTO cliente (nome, telefone, endereco)
VALUES ('João Silva', '123456789', 'Rua A, 123');

-- Inserir um novo funcionário
INSERT INTO funcionario (nome, cargo, salario, endereco, telefone)
VALUES ('Maria Souza', 'Gerente', 5000.00, 'Avenida B, 456', '987654321');

-- Inserir uma nova peça
INSERT INTO peca (nome, descricao, preco)
VALUES ('Bateria', 'Bateria de carro 12V', 150.00);

-- Inserir um novo serviço
INSERT INTO servico (cliente_id, data, descricao, valor_total)
VALUES (1, '2023-07-14', 'Troca de óleo', 100.00);

-- Inserir um funcionário associado a um serviço
INSERT INTO servico_funcionario (servico_id, funcionario_id)
VALUES (1, 1);

-- Inserir uma peça utilizada em um serviço
INSERT INTO utiliza (servico_id, peca_id, quantidade_utilizada)
VALUES (1, 1, 2);

-- Inserir um novo veículo
INSERT INTO veiculo (cliente_id, marca, modelo, ano)
VALUES (1, 'Ford', 'Fiesta', 2018);
