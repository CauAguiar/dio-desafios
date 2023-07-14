-- Calcular o salário líquido dos funcionários (salário - 10%)
SELECT nome, salario, salario * 0.9 AS salario_liquido FROM funcionario;

-- Concatenar nome e telefone dos clientes
SELECT CONCAT(nome, ' - ', telefone) AS nome_telefone FROM cliente;
