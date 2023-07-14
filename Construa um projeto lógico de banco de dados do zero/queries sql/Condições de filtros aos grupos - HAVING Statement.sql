-- Recuperar funcionários que possuem salário médio acima de 4000
SELECT funcionario_id, AVG(salario) AS salario_medio
FROM servico_funcionario
JOIN funcionario ON servico_funcionario.funcionario_id = funcionario.funcionario_id
GROUP BY funcionario_id
HAVING salario_medio > 4000;
