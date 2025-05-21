# 📊 Integração entre ServiceDesk Plus Cloud e Analytics Plus

Este projeto realiza a integração entre o **ServiceDesk Plus Cloud** e o **Zoho Analytics (Analytics Plus)**, utilizando a API REST do ServiceDesk para exportar dados de chamados e permitir a criação de dashboards de análise.

---

## 🚀 Objetivo

Automatizar a extração de chamados recentes do ServiceDesk Plus Cloud, salvando os dados em arquivos `.json`, prontos para importação no Zoho Analytics.

---

## 🧰 Tecnologias e Bibliotecas

- Python 3.x
- `requests`
- `python-dotenv`
- API REST ManageEngine ServiceDesk Plus Cloud
- Zoho OAuth2

---

## 📂 Estrutura do Projeto

```
.
├── .env                    # Variáveis de ambiente (não versionar)
├── .gitignore              # Exclusões para versionamento
├── tickets.json           # Exportação em JSON
├── main.py                 # Script principal
├── README.md               # Documentação do projeto
├── requirements.txt        # Dependências do projeto
├── servicedesk_api.py      # Lógica de API
└── .venv/                  # Ambiente virtual (não versionar)
```

---

## ⚙️ Configuração do Ambiente

Siga os passos abaixo para configurar e executar o projeto corretamente:

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/selecao-acs.git
cd selecao-acs
```

### 2. Crie um ambiente virtual

- **Windows**:
  ```bash
  python -m venv .venv
  .\.venv\Scripts\activate
  ```

- **Linux/Mac**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

> O ambiente virtual é importante para isolar as dependências do projeto.

### 3. Instale as dependências do projeto

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

Isso instalará automaticamente bibliotecas como `requests` e `python-dotenv`.

### 4. Configure o arquivo `.env`

Crie um arquivo tickets `.env` na raiz do projeto com o seguinte conteúdo:

```env
CLIENT_ID=seu_client_id
CLIENT_SECRET=seu_client_secret
REFRESH_TOKEN=seu_refresh_token
```

Esses dados são obtidos ao registrar sua aplicação no Zoho Developer Console.

### 5. Execute o script principal

```bash
python main.py
```

Ao final, os dados dos chamados serão exportados em `tickets.json`prontos para importação manual no Zoho Analytics.

---

## 🔐 Autenticação

A autenticação é feita via **OAuth2 com Refresh Token** (Zoho Accounts). Certifique-se de gerar corretamente os dados no portal de desenvolvedor da Zoho.

---

## 📈 Dashboards sugeridos no Analytics Plus

- Tickets por Grupo
- Distribuição por Status
- Chamados por Técnico
- Linha do tempo de criação de chamados
- Análise de backlog

---

## 📊 Exemplo de visualização

Os dados exportados podem ser utilizados para criar gráficos como:

- 📍 Gráfico de dispersão por **grupo de atendimento**
- 📍 Barras por **status dos tickets**
- 📍 Gráfico de pizza por **técnico responsável**

Esses dashboards ajudam a monitorar a produtividade da equipe, distribuição de carga de trabalho e status atual dos atendimentos.

---

## 🔄 Melhorias futuras

- Integração direta com a API do Zoho Analytics para envio automático.
- Agendamento da execução via `cron` ou Agendador de Tarefas.
- Inclusão de filtros adicionais (categoria, prioridade, solicitante etc.).
- Cálculo de SLA e tempo médio de resolução.

---

## 🧾 Exemplo de `.gitignore`

Certifique-se de ignorar os arquivos sensíveis e temporários:

```gitignore
.venv/
.env
__pycache__/
*.pyc
tickets.json
```

---

## 👨‍💻 Autor

Desenvolvido por Gustavo Gracio Sbrana Martins, como parte do processo seletivo para a **ACS Pro**.

---