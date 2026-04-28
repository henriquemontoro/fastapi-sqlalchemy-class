# Remover Livro de Autor

## Descricao
Remove a associacao entre um livro e um autor. O livro e o autor continuam existindo na base de dados.

## Parametros
- **author_id** (int): ID unico do autor. Exemplo: 1
- **book_id** (int): ID unico do livro a ser desassociado. Exemplo: 2

## Resposta
- **200 OK**: Retorna o autor sem o livro removido.
- **404 Not Found**: Retorna um erro se o autor ou o livro nao forem encontrados.
