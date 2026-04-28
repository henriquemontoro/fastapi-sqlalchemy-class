# Adicionar Livro a Autor

## Descricao
Associa um livro existente a um autor existente na base de dados.

## Parametros
- **author_id** (int): ID unico do autor. Exemplo: 1
- **book_id** (int): ID unico do livro a ser associado. Exemplo: 2

## Resposta
- **200 OK**: Retorna o autor com o livro associado.
- **404 Not Found**: Retorna um erro se o autor ou o livro nao forem encontrados.
