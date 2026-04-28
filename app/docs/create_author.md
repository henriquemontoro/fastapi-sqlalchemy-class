# Criacao de Autor

## Descricao
Cria um novo autor com os dados fornecidos no corpo da requisicao.

## Parametros
- **name** (str): Nome completo do autor. Exemplo: "Joao Silva"
- **email** (str): Email valido do autor. Exemplo: "joao.silva@example.com"

## Resposta
- **200 OK**: Retorna o autor criado.
- **400 Bad Request**: Retorna um erro se os dados fornecidos forem invalidos.
