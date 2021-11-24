<h1>Challenge Cross Commerce</h1>

<h4 align="center">
  Projeto desenvolvido como resposta ao Challenge ETL(Extract, Transform and Load)
</h4>
 
## Tecnologias adotadas


#### API
-  [Flask 2.0.x][flash]
-  [Python 3.8.x][python]
-  [pip3][pip3]

## Como utilizar

Primeiro você vai precisar de [Git](https://git-scm.com), [Python 3.8.x][python], [pip3][pip3] ou pip instalados na sua máquina.

No seu Terminal ou Console, siga os passos:

```bash
# Clone este repositório
$ git clone https://github.com/roberto5g/challengecrosscommerce.git

# Entre no repositório
$ cd challengecrosscommerce

# Instale as dependências da api com o pip3
$ pip3 install -r requirements.txt
```

#### A aplicação já possui os dados extraídos e ordenados
##### Para extrair novamente os dados é necessário executar o arquivo test.py 
```
$ python3 test.py
```
##### Para ordernar novamente os dados é necessário executar o arquivo test.py descomentando a função ordering()
```
...
  '''
    1 - Extract data
    2 - Execute orderind
  '''
  # extract_data()
  ordering()
...
$ python3 test.py
```

```
# Para executar a API e acessar os dados já extreidos e ordenados acesso api_cross
$ cd api_cross

# Agora execute o servidor para iniciar a API
$ python3 app.py

# A seguinte mensagem será mostrada
...
  * Serving Flask app 'app' (lazy loading)
  * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
  * Debug mode: off
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ...
 
# Agora abra seu navegador ou outra ferramenta com suporte a requisição HTTP
# Acesse a seguite URL http://127.0.0.1:5000/api/numbers
# Retorno esperado
{ "numbers": [6.649677943594556e-07, 1.9774114394001396e-06, 4.636210512744959e-06,...]}

# Também é possível navegar entre as páginas, por padrão a API retorna 100 resultatos por página. 
# Para acessar uma outra página, será necessário informar o parametro "page" na URL
ex: http://127.0.0.1:5000/api/numbers?page=2
```

---

[pip3]: https://pip.pypa.io/en/stable/user_guide/
[flash]: https://flask.palletsprojects.com/en/2.0.x/changes/
[python]: https://www.python.org/

