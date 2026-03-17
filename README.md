amo_system/
├── .env
├── .gitignore
├── requirements.txt
├── run.py
├── config.py
├── scripts/
│   ├── import_appointments.py
│   ├── import_transport.py
│   └── import_snack_purchases.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_routes.py
│   └── test_transport.py
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── utils.py
│   ├── decorators.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── patient/
│   │   │   ├── list.html
│   │   │   └── form.html
│   │   ├── professional/
│   │   │   ├── list.html
│   │   │   └── form.html
│   │   ├── vehicle/
│   │   │   ├── list.html
│   │   │   └── form.html
│   │   ├── appointment/
│   │   │   ├── calendar.html
│   │   │   ├── weekly.html        # grade semanal estilo PDF
│   │   │   └── form.html
│   │   ├── transport/
│   │   │   ├── list.html
│   │   │   ├── daily.html          # visão do motorista
│   │   │   └── form.html
│   │   ├── snack/
│   │   │   ├── daily.html
│   │   │   └── report.html
│   │   ├── stock/
│   │   │   ├── items.html
│   │   │   └── purchases.html
│   │   └── reports/
│   │       └── weekly_list.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   └── blueprints/
│       ├── auth.py
│       ├── patient.py
│       ├── professional.py
│       ├── vehicle.py
│       ├── appointment.py
│       ├── transport.py
│       ├── snack.py
│       ├── stock.py
│       └── reports.py