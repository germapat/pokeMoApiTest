# pokeMoApiTest
Test MO Tecnologias

1. clone repository: git clone https://github.com/germapat/pokeMoApiTest
2. cd pokeMoApiTest
3. install requirements: pip install -r requirements.txt
4. run command: python manage.py migrate
5. run command: python manage.py runserver
6. test api evolution: http://localhost:{portApp}/api/evolutions/{id}/ Example: http://localhost:8000/api/evolutions/10/
7. test pokemon api: http://localhost:{portApp}/api/evolutions/{name}/ Example: http://localhost:8000/api/evolutions/pichu/

The Test use https://pypi.org/project/fwbasemodel/ or https://github.com/germapat/fw let's do it !!

The Test is based on https://pokeapi.co/docs/v2#evolution-chains
