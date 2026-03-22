# app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import (professionals, appointments, add_appointment, delete_appointment,
                    find_appointment_by_id, is_time_slot_available, get_appointments_for_date,
                    Appointment)
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-temporaria-para-flash-messages'  # Usar variável de ambiente depois

# Rota principal - exibe o calendário
@app.route('/')
def index():
    return render_template('index.html', professionals=professionals)

# API: listar agendamentos de um dia (para preencher o calendário)
@app.route('/api/appointments/<date>')
def get_appointments(date):
    appointments_day = get_appointments_for_date(date)
    # Transformar em formato que FullCalendar entende (eventos)
    events = []
    for apt in appointments_day:
        start_time = apt.time_slot.split('-')[0]
        end_time = apt.time_slot.split('-')[1]
        start_datetime = f"{apt.date}T{start_time}:00"
        end_datetime = f"{apt.date}T{end_time}:00"
        events.append({
            'id': apt.id,
            'title': f"{apt.patient_name} - {apt.area}",
            'start': start_datetime,
            'end': end_datetime,
            'extendedProps': {
                'professional_name': next((p.name for p in professionals if p.id == apt.professional_id), ''),
                'patient_contact': apt.patient_contact,
                'area': apt.area
            }
        })
    return jsonify(events)

# API: criar novo agendamento
@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    patient_name = data.get('patient_name')
    patient_contact = data.get('patient_contact')
    professional_id = data.get('professional_id')
    date = data.get('date')
    time_slot = data.get('time_slot')
    area = data.get('area')

    # Validação simples
    if not all([patient_name, patient_contact, professional_id, date, time_slot, area]):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400

    # Verificar disponibilidade
    if not is_time_slot_available(date, time_slot, professional_id):
        return jsonify({'error': 'Horário já ocupado para este profissional'}), 409

    # Criar agendamento
    new_appt = Appointment(
        id=None,
        patient_name=patient_name,
        patient_contact=patient_contact,
        professional_id=professional_id,
        date=date,
        time_slot=time_slot,
        area=area
    )
    add_appointment(new_appt)
    return jsonify({'message': 'Agendamento criado com sucesso!', 'id': new_appt.id}), 201

# API: cancelar agendamento
@app.route('/api/appointments/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    apt = find_appointment_by_id(appointment_id)
    if not apt:
        return jsonify({'error': 'Agendamento não encontrado'}), 404

    if delete_appointment(appointment_id):
        return jsonify({'message': 'Agendamento cancelado com sucesso'}), 200
    else:
        return jsonify({'error': 'Falha ao cancelar'}), 500

# Tratamento de erro 404 personalizado
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="Página não encontrada"), 404

# Tratamento de erro 500
@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html', error="Erro interno no servidor"), 500

if __name__ == '__main__':
    app.run(debug=True)