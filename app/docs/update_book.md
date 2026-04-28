# Atualizacao de Livro

## Descricao
Atualiza os dados de um livro existente com base no ID informado.

## Parametros
- **book_id** (int): ID unico do livro a ser atualizado. Exemplo: 1
- **title** (str): Novo titulo do livro. Exemplo: "Clean Code"
- **isbn** (str): Novo ISBN do livro no formato ISBN-10 ou ISBN-13. Exemplo: "978-0132350884"

## Resposta
- **200 OK**: Retorna o livro atualizado.
- **404 Not Found**: Retorna um erro se o livro nao for encontrado.
- **400 Bad Request**: Retorna um erro se os dados fornecidos forem invalidos.
