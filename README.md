# School CRUD

* Um simples CRUD de Escola. Feito com Flask + SQLALCHEMY + MySQL
<hr>

## Requisitos
- Python 3.7 +
- Flask
- MySql 8

## Como executar

- Para executarmos este projeto devemos clonar primeiro em nossa maquina. basta irmos no GIT Bash e digitar o seguinte comando:
<code>git clone https://github.com/coffeblackpremium/school_crud.git </code>
- Inicie com a sua IDE de preferência
- Através do Terminal, devemos navegar até a pasta destino onde você clonou o repositório e instalarmos todas as bibliotecas utilizado no projeto através do comando:
<code> pip install -r requirements.txt</code>
- Configuremos no arquivo .env o nome do seu banco de dados, senha e o servidor. **Sem alterar o nome do banco de dados que se chama school_crud**
- No terminal, damos <code>flask init</code> para iniciar as migrações no banco de Dados
