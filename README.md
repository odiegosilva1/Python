## README.md (Versão Resumida)

```markdown
# Sistema de Agendamento de Acolhimento

Sistema web para agendamento de acolhimento com profissionais multidisciplinares.

## Funcionalidades

- Calendário interativo (semanal/diário)
- Agendamento rápido com validação de conflitos
- Cancelamento de atendimentos
- Interface responsiva e acessível
- Tratamento de erros

## Tecnologias

**Backend:** Python 3.11.2, Flask 2.3.3  
**Frontend:** HTML5, CSS3, JavaScript, FullCalendar 5.11.3  
**Testes:** pytest 7.4.0

## Configuração Rápida

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/agendamento-acolhimento.git
cd agendamento-acolhimento

# Crie e ative ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Instale dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py
```

Acesse: http://127.0.0.1:5000

## Dependências Principais

```
Flask==2.3.3
Werkzeug==2.3.7
pytest==7.4.0
python-dotenv==1.0.0
```

## Testes

```bash
# Executar testes
pytest tests/ -v

# Com cobertura
pip install pytest-cov
pytest tests/ --cov=.
```

## Estrutura do Projeto

```
agendamento-acolhimento/
├── app.py              # Aplicação principal
├── models.py           # Modelos de dados
├── tests/              # Testes unitários
├── static/             # CSS e JavaScript
└── templates/          # Templates HTML
```

## Próximas Melhorias

- Banco de dados (SQLAlchemy + PostgreSQL)
- Autenticação de usuários
- Notificações WhatsApp
- Otimização de rotas
- Relatórios e exportação

## Licença

MIT
```

---


