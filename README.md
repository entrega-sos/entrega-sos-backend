# Entrega SOS - Back-end

API REST desenvolvida com Python/Flask, Postgres e Docker.


## Configuração do Ambiente

Os serviços Flask e Postgres rodam na porta 5000 e 5432, respectivamente.

1. Instale o Docker: https://docs.docker.com/install/linux/docker-ce/ubuntu/

2. Instale o Docker Compose: https://docs.docker.com/compose/install/

2. Instale o Git: ```sudo apt install git```

3. Clone este repositório: ```git clone ```

4. Entre no diretório: ```cd entrega-sos-backend/```

5. Crie os containers (1x apenas): ```export ENV_APP=development ; docker-compose build```

6. Execute (CTRL+C para exit): ```export ENV_APP=development ; docker-compose up```


## Executando a Aplicação

Instale o Insomnia ou equivalente: https://insomnia.rest/download/

### 1. Criar empresa
- Endpoint (POST): http://localhost:5000/v1/empresas
- Request:
    ```JSON
    {
        "id": "99602837a596498c85e214afb3a6f484",
        "descricao": "Mercadinho Espaço da Carne",
        "usuario": "msc",
        "email": "msg@gmail.com",
        "telefone": "7522220000",
        "whatsapp": "7599991111",
        "cep": "4444000",
        "endereco": "Rua São Jorge, n 80",
        "bairro": "George Américo",
        "cidade": "Feira de Santana",
        "uf": "BA",
        "tipo_negocio": "Mercado",
        "meio_pagamento": [
            "Dinheiro",
            "Crédito",
            "Débito"
        ],
        "dias_horarios": "Seg a Sex 8 as 18, Sab e Dom 8 as 12",
        "delivery": true,
        "instagram": "www.instagram.com/espaco_da_carne",
        "facebook": "www.facebook.com/espaco_da_carne",
        "site": "",
        "obs": "Fazemos entrega somente no bairro George Americo"
    }
    ```

### 2. Obter token
- Endpoint (POST): http://localhost:5000/v1/empresas/auth/token
- Response:
    ```JSON
    {
        "token": "seYladgufOiX8EsfKEK5b6vt7CPojv0h"
    }
    ```

### 3. Revogar token
- Endpoint (DELETE): http://localhost:5000/v1/empresas/auth/token
- Configurar autenticação para **Bearer Token** e informar o respectivo token


### 4. Consultar empresa pelo usuário
- Endpoint (GET): http://localhost:5000/v1/empresas/msc
    - Troque "msc" pelo respectivo usuário
- Configurar autenticação para **Bearer Token** e informar o respectivo token
- Response:
    ```JSON
    {
        "id": "99602837a596498c85e214afb3a6f484",
        "descricao": "Mercadinho Espaço da Carne",
        "usuario": "msc",
        "email": "msg@gmail.com",
        "telefone": "7522220000",
        "whatsapp": "7599991111",
        "cep": "4444000",
        "endereco": "Rua São Jorge, n 80",
        "bairro": "George Américo",
        "cidade": "Feira de Santana",
        "uf": "BA",
        "tipo_negocio": "Mercado",
        "meio_pagamento": [
            "Dinheiro",
            "Crédito",
            "Débito"
        ],
        "dias_horarios": "Seg a Sex 8 as 18, Sab e Dom 8 as 12",
        "delivery": true,
        "instagram": "www.instagram.com/espaco_da_carne",
        "facebook": "www.facebook.com/espaco_da_carne",
        "site": "",
        "obs": "Fazemos entrega somente no bairro George Americo"
    }
    ```

### 5. Consultar todas as empresas
- Endpoint (GET): http://localhost:5000/v1/empresas
- Configurar autenticação para **Bearer Token** e informar o respectivo token
- Response:
    ```JSON
    {
        "_meta": {
            "page": 1,
            "per_page": 10,
            "total_pages": 1,
            "total_items": 1
        },
        "_links": {
            "self": "/v1/empresas?page=1&per_page=10",
            "next": null,
            "prev": null
        },
        "items": [
            {
                "id": "0ae7eaa6d63c4a2ea76ab1bb4a2455f6",
                "descricao": "Mercadinho Espaço da Carne",
                "usuario": "msc",
                "email": "msg@gmail.com",
                "telefone": "7522220000",
                "whatsapp": "7599991111",
                "cep": "4444000",
                "endereco": "Rua São Jorge, n 80",
                "bairro": "George Américo",
                "cidade": "Feira de Santana",
                "uf": "BA",
                "tipo_negocio": "Mercado",
                "meio_pagamento": [
                    "Dinheiro",
                    "Crédito",
                    "Débito"
                ],
                "dias_horarios": "Seg a Sex 8 as 18, Sab e Dom 8 as 12",
                "delivery": true,
                "instagram": "www.instagram.com/espaco_da_carne",
                "facebook": "www.facebook.com/espaco_da_carne",
                "site": "",
                "obs": "Fazemos entrega somente no bairro George Americo"
            }
        ]
    }
    ```

### 6. Alterar dados de uma empresa
- Endpoint (PUT): http://localhost:5000/v1/empresas/msc
    - Troque "msc" pelo respectivo usuário
- Configurar autenticação para **Bearer Token** e informar o respectivo token
- Request:
    ```JSON
    {
        "email": "msc@hotmail.com",
        "cep": "4444111"
    }
    ```
- Response:
    ```JSON
    {
        "id": "99602837a596498c85e214afb3a6f484",
        "descricao": "Mercadinho Espaço da Carne",
        "usuario": "msc",
        "email": "msc@hotmail.com",
        "telefone": "7522220000",
        "whatsapp": "7599991111",
        "cep": "4444111",
        "endereco": "Rua São Jorge, n 80",
        "bairro": "George Américo",
        "cidade": "Feira de Santana",
        "uf": "BA",
        "tipo_negocio": "Mercado",
        "meio_pagamento": [
            "Dinheiro",
            "Crédito",
            "Débito"
        ],
        "dias_horarios": "Seg a Sex 8 as 18, Sab e Dom 8 as 12",
        "delivery": true,
        "instagram": "www.instagram.com/espaco_da_carne",
        "facebook": "www.facebook.com/espaco_da_carne",
        "site": "",
        "obs": "Fazemos entrega somente no bairro George Americo"
    }
    ```

### 7. Deletar uma empresa
- Endpoint (DELETE): http://localhost:5000/v1/empresas/msc
    - Troque "msc" pelo respectivo usuário
- Configurar autenticação para **Bearer Token** e informar o respectivo token