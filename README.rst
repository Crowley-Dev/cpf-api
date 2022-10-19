API Rest - Flask
================

- **próxima atualização**: *××/××/××××*
- **mudanças na próxima atualização**:
   - *cada token terá um tempo de uso (7d, 15d, 30d)*
   - *sistema de blacklist, caso o usuário faça muitas requisição em pouco tempo*

- **informo que**: *o banco de dados usado nesse projeto é totalmente fictício.*


tecnologias
-----------

- `flask`_
- `dynaconf`_
- `sqlalchemy`_

.. _flask: https://github.com/pallets/flask
.. _dynaconf: https://github.com/dynaconf/dynaconf
.. _sqlalchemy: https://github.com/zzzeek/sqlalchemy


instalação
----------

.. code-block:: powershell

	git clone https://github.com/Crowley-Dev/cpf-api


ambiente
--------

.. code-block:: powershell

	python3 -m pip install -r requirements.txt


execução
--------

.. code-block:: powershell

	flask run


rotas
-----

- API [POST]

  - **consultar o CPF cadastrado na base dados.**

    - http://0.0.0.0:5000/v1/cpf/


  - **consultar nomes cadastrados na base de dados.**

    - http://0.0.0.0:5000/v1/nome/


um exemplo simples de requisição
--------------------------------

.. code-block:: python

	import requests


	url = "http://0.0.0.0:5000/v1/cpf/"

	resp = requests.request(
	    method = "POST",
	    url = url,
	    headers = {
	        "Authorization": "clientes123token"
	    },
            data = {
                "cpf": "117.129.797-10"
            }

	); print(resp.text)


response
--------

.. code-block:: json

	{
	  "data": {
	    "cidade": "TEIXEIRA DE FREITAS",
	    "cpf": "11712979710",
	    "estado": "BA",
	    "nome": "BRUNA ALMEIDA LOVO"
	  },
	  "status": 200
	}
