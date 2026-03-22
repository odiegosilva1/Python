
import pytest
from app import app
from models import appointments, add_appointment, Appointment

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Limpar dados antes de cada teste
        appointments.clear()
        yield client

def test_create_appointment(client):
    data = {
        'patient_name': 'João',
        'patient_contact': 'joao@email.com',
        'professional_id': 1,
        'date': '2025-04-01',
        'time_slot': '09:00-10:00',
        'area': 'Psicologia'
    }
    response = client.post('/api/appointments', json=data)
    assert response.status_code == 201
    assert response.json['message'] == 'Agendamento criado com sucesso!'
    assert len(appointments) == 1

def test_conflict_appointment(client):
    # Primeiro agendamento
    client.post('/api/appointments', json={
        'patient_name': 'João', 'patient_contact': 'joao@email.com',
        'professional_id': 1, 'date': '2025-04-01', 'time_slot': '09:00-10:00',
        'area': 'Psicologia'
    })
    # Segundo agendamento mesmo profissional/horário
    response = client.post('/api/appointments', json={
        'patient_name': 'Maria', 'patient_contact': 'maria@email.com',
        'professional_id': 1, 'date': '2025-04-01', 'time_slot': '09:00-10:00',
        'area': 'Psicologia'
    })
    assert response.status_code == 409
    assert response.json['error'] == 'Horário já ocupado para este profissional'