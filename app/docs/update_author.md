# Atualizacao de Autor

## Descricao
Atualiza os dados de um autor existente com base no ID informado.

## Parametros
- **author_id** (int): ID unico do autor a ser atualizado. Exemplo: 1
- **name** (str): Novo nome completo do autor. Exemplo: "Joao Silva"
- **email** (str): Novo email valido do autor. Exemplo: "joao.silva@example.com"

## Resposta
- **200 OK**: Retorna o autor atualizado.
- **404 Not Found**: Retorna um erro se o autor nao for encontrado.
- **400 Bad Request**: Retorna um erro se os dados fornecidos forem invalidos.
