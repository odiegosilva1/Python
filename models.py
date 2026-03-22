# models.py
from datetime import datetime, time
from typing import List, Optional

class Professional:
    """Representa um profissional multidisciplinar."""
    def __init__(self, id: int, name: str, area: str):
        self.id = id
        self.name = name
        self.area = area

class Appointment:
    """Representa um agendamento de acolhimento."""
    def __init__(self, id: int, patient_name: str, patient_contact: str,
                 professional_id: int, date: str, time_slot: str, area: str):
        self.id = id
        self.patient_name = patient_name
        self.patient_contact = patient_contact
        self.professional_id = professional_id
        self.date = date          # formato YYYY-MM-DD
        self.time_slot = time_slot # ex: "09:00-10:00"
        self.area = area
        self.created_at = datetime.now()

# Dados iniciais (simulação)
professionals = [
    Professional(1, "Dr. Ana", "Psicologia"),
    Professional(2, "Dr. Carlos", "Nutrição"),
    Professional(3, "Dra. Beatriz", "Fisioterapia")
]

appointments = []
next_appointment_id = 1

def add_appointment(appointment: Appointment) -> int:
    global next_appointment_id
    appointment.id = next_appointment_id
    appointments.append(appointment)
    next_appointment_id += 1
    return appointment.id

def find_appointment_by_id(appointment_id: int) -> Optional[Appointment]:
    return next((a for a in appointments if a.id == appointment_id), None)

def delete_appointment(appointment_id: int) -> bool:
    global appointments
    initial_len = len(appointments)
    appointments = [a for a in appointments if a.id != appointment_id]
    return len(appointments) < initial_len

def get_appointments_for_date(date: str) -> List[Appointment]:
    return [a for a in appointments if a.date == date]

def is_time_slot_available(date: str, time_slot: str, professional_id: int) -> bool:
    """Verifica se o horário está disponível para o profissional."""
    return not any(a for a in appointments
                   if a.date == date and a.time_slot == time_slot
                   and a.professional_id == professional_id)