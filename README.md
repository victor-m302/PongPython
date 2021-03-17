# PongPython
#### (PT-BR)
## Pong em Python
### Poetry
`poetry` é uma ferramenta para lidar com a instalação de dependências, bem como com a construção e empacotamento de pacotes Python. Ele só precisa de um arquivo para fazer tudo isso: o novo e padronizado `pyproject.toml`.

Em outras palavras, o `poetry` usa `pyproject.toml` para substituir `setup.py`,	`requirements.txt`, `setup.cfg`, `MANIFEST.in` e o recém-adicionado `Pipfile`.
#### Instalação
Usando `pip` para instalar `poetry`.

	pip install --user poetry
#### Comandos

##### install
O `install` o comando lê o `pyproject.toml` arquivo do projeto atual, resolve as dependências e as instala.

	poetry install

Se houver um arquivo `poetry.lock` no diretório atual, ele usará as versões exatas de lá em vez de resolvê-los. Isso garante que todos os usuários da biblioteca obtenham as mesmas versões das dependências.

Se não há `poetry.lock` arquivo, Poetry criará um após a resolução de dependência.

##### add
O `add` comando adiciona os pacotes necessários ao seu	`pyproject.toml` e os instala.

Se você não especificar uma restrição de versão, o `poetry` escolherá uma adequada com base nas versões de pacote disponíveis. 

	poetry add requests pendulum 


Você também pode especificar uma restrição ao adicionar um pacote, da seguinte forma:


	poetry add pendulum@^2.0.5
	poetry add "pendulum>=2.0.5"

###### Opções
	--dev (-D): Adicionar pacote como dependência de desenvolvimento.
    --path: O caminho para uma dependência.
    --optional : Adicione como uma dependência opcional.
    --dry-run : Exibe as operações, mas não executa nada (habilita implicitamente --verbose).
    --lock : Não execute a instalação (apenas atualize o arquivo de bloqueio).

##### remove
O `remove` comando remove um pacote da lista atual de pacotes instalados.


	poetry remove pendulum


##### show
Para listar todos os pacotes disponíveis, você pode usar o `show` comando.


	poetry show


Se quiser ver os detalhes de um determinado pacote, pode passar o nome do pacote.


	poetry show pendulum

	name        : pendulum
	version     : 1.4.2
	description : Python datetimes made easy

	dependencies:
	 - python-dateutil >=2.6.1
	 - tzlocal >=1.4
	 - pytzdata >=2017.2.2


##### shell
O `shell` comando gera um shell, de acordo com o `$SHELL` variável de ambiente, dentro do ambiente virtual. Se ainda não houver um, ele será criado.


	poetry shell

### Recursos
 - [Website oficial do Poetry](https://python-poetry.org/)
