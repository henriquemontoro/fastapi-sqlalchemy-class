# Criacao de Livro

## Descricao
Cria um novo livro com os dados fornecidos no corpo da requisicao.

## Parametros
- **title** (str): Titulo do livro. Exemplo: "Clean Code"
- **isbn** (str): ISBN do livro no formato ISBN-10 ou ISBN-13. Exemplo: "978-0132350884"

## Resposta
- **200 OK**: Retorna o livro criado.
- **400 Bad Request**: Retorna um erro se os dados fornecidos forem invalidos.
