# Products FastAPI

API REST para gerenciamento de produtos com arquitetura em camadas.

## 📋 Sobre o Projeto

API completa para CRUD de produtos, implementando boas práticas de arquitetura com separação de responsabilidades em camadas (Controllers, Services, Repositories).

### Funcionalidades

- ✅ CRUD completo de produtos
- ✅ Validação de dados com Pydantic
- ✅ Tratamento de exceções customizado
- ✅ Migrações automáticas de banco de dados
- ✅ Documentação interativa com Swagger
- ✅ Arquitetura em camadas

## 🚀 Tecnologias

- **Python 3.13+**
- **FastAPI** - Framework web moderno e de alta performance
- **SQLAlchemy** - ORM para Python
- **Alembic** - Gerenciamento de migrações
- **PostgreSQL** - Banco de dados relacional
- **Pydantic** - Validação de dados
- **UV** - Gerenciador de pacotes rápido

## 📦 Pré-requisitos

- Python 3.13+
- PostgreSQL
- UV (gerenciador de pacotes)

## 🔧 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/yurictorquato/products-fastapi.git
cd products-fastapi
```

### 2. Instale as dependências

```bash
# Instalar UV (se ainda não tiver)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependências do projeto
uv sync
```

### 3. Configure o banco de dados

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/products_db
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
```

### 4. Execute as migrações

```bash
# Ativar ambiente virtual
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Rodar migrações
alembic upgrade head
```

### 5. Inicie o servidor

```bash
# Desenvolvimento (com reload automático)
uv run uvicorn src.app.main:app --reload

# Produção
uv run uvicorn src.app.main:app --host 0.0.0.0 --port 8000
```

## 🎯 Uso da API

### Acessar a aplicação

- **API**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Exemplos de Requisições

#### Criar um Produto

```bash
curl -X POST "http://localhost:8000/products" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Notebook Dell",
    "description": "Notebook para desenvolvimento",
    "price": 3500.00,
    "stock": 10
  }'
```

#### Listar Produtos

```bash
curl -X GET "http://localhost:8000/products"
```

#### Buscar Produto por ID

```bash
curl -X GET "http://localhost:8000/products/1"
```

#### Atualizar Produto

```bash
curl -X PUT "http://localhost:8000/products/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Notebook Dell XPS",
    "price": 4000.00
  }'
```

#### Deletar Produto

```bash
curl -X DELETE "http://localhost:8000/products/1"
```

## 📊 Arquitetura do Projeto

```
products-fastapi/
├── migrations/              # Migrações Alembic
├── src/
│   └── app/
│       ├── controllers/    # Endpoints e lógica de controle
│       ├── core/           # Configurações centrais
│       ├── exceptions/     # Exceções customizadas
│       ├── handlers/       # Handlers de exceção
│       ├── models/         # Modelos SQLAlchemy (Entities)
│       ├── repositories/   # Camada de acesso a dados
│       ├── routers/        # Rotas da API
│       ├── schemas/        # Schemas Pydantic (DTOs)
│       ├── services/       # Lógica de negócio
│       └── main.py         # Aplicação FastAPI
├── .env                    # Variáveis de ambiente
├── alembic.ini            # Configuração Alembic
├── pyproject.toml         # Dependências e configs
├── tasks.py               # Scripts auxiliares
└── uv.lock                # Lock de dependências
```

### Camadas da Arquitetura

1. **Controllers**: Recebem requisições HTTP e delegam para os services
2. **Services**: Contêm a lógica de negócio
3. **Repositories**: Abstraem o acesso ao banco de dados
4. **Models**: Definem a estrutura das tabelas
5. **Schemas**: Validam entrada/saída de dados

## 🗄️ Migrações de Banco de Dados

```bash
# Criar nova migração automaticamente
alembic revision --autogenerate -m "Adiciona campo X na tabela Y"

# Aplicar todas as migrações pendentes
alembic upgrade head

# Reverter última migração
alembic downgrade -1

# Ver histórico de migrações
alembic history

# Ver migração atual
alembic current
```

## 🛠️ Tasks Úteis

O projeto inclui um arquivo `tasks.py` com comandos úteis:

```bash
# Executar tasks disponíveis
uv run python tasks.py
```

## 🧪 Testes (Planejado)

```bash
# Estrutura de testes a ser implementada
pytest
pytest --cov=src tests/
```

## 📝 Variáveis de Ambiente

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `DATABASE_URL` | URL de conexão com PostgreSQL | `postgresql://user:pass@localhost:5432/db` |
| `SECRET_KEY` | Chave secreta para JWT | `sua-chave-super-secreta` |
| `DEBUG` | Modo debug | `True` ou `False` |

## 👤 Autor

**Yuri Torquato**

- GitHub: [@yurictorquato](https://github.com/yurictorquato)
- LinkedIn: www.linkedin.com/in/yuri-torquato-b824b0283

---

⭐ Se este projeto foi útil, considere dar uma estrela!
