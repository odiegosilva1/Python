from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='coordenador')  # admin, coordenador, motorista, cozinha
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Relacionamentos (opcional)
    transports_driven = db.relationship('Transport', foreign_keys='Transport.driver_id', backref='driver')

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    allergies = db.Column(db.Text)          # intolerâncias/alergias
    special_needs = db.Column(db.Text)       # cadeirinha, etc
    requires_car_seat = db.Column(db.Boolean, default=False)
    needs_transport = db.Column(db.Boolean, default=False)
    family_contacts = db.Column(db.JSON)     # lista de contatos {nome, telefone}
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))

class Professional(db.Model):
    __tablename__ = 'professionals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    weekly_schedule = db.Column(db.JSON)      # ex: {"monday": ["08:00-12:00", "14:00-18:00"], ...}
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(10), unique=True, nullable=False)
    model = db.Column(db.String(50))
    capacity = db.Column(db.Integer)          # número de passageiros
    is_active = db.Column(db.Boolean, default=True)

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=True)   # pode ser nulo para eventos
    professional_id = db.Column(db.Integer, db.ForeignKey('professionals.id'), nullable=True)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    service_type = db.Column(db.String(50))      # ex: 'Fisioterapia', 'Psicologia'
    appointment_type = db.Column(db.String(20), default='individual')  # individual, group, meeting, special_event
    is_recurring = db.Column(db.Boolean, default=False)
    recurring_pattern = db.Column(db.JSON)       # regras de recorrência
    snack_required = db.Column(db.Boolean, default=True)
    snack_takeaway = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text)             # usado para reuniões/eventos
    status = db.Column(db.String(20), default='agendado')  # agendado, cancelado, realizado
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    patient = db.relationship('Patient')
    professional = db.relationship('Professional')
    group_patients = db.relationship('GroupAppointment', backref='appointment', lazy='dynamic')

class GroupAppointment(db.Model):
    __tablename__ = 'group_appointments'
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))

class Transport(db.Model):
    __tablename__ = 'transports'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    shift = db.Column(db.String(10))        # manhã, tarde
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    vehicle = db.relationship('Vehicle')
    stops = db.relationship('TransportStop', backref='transport', lazy='dynamic', cascade='all, delete-orphan')

class TransportStop(db.Model):
    __tablename__ = 'transport_stops'
    id = db.Column(db.Integer, primary_key=True)
    transport_id = db.Column(db.Integer, db.ForeignKey('transports.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    stop_type = db.Column(db.String(10))    # 'pickup' ou 'dropoff'
    scheduled_time = db.Column(db.Time)      # horário previsto
    address = db.Column(db.String(200))      # endereço específico
    order = db.Column(db.Integer)            # ordem na rota
    notes = db.Column(db.Text)               # ex: "assento"

    patient = db.relationship('Patient')

class SnackConsumption(db.Model):
    __tablename__ = 'snack_consumptions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'), nullable=True)
    snack_time = db.Column(db.String(10))    # 'manha', 'tarde'
    takeaway = db.Column(db.Boolean, default=False)
    served = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)

    patient = db.relationship('Patient')
    appointment = db.relationship('Appointment')

class SupplyItem(db.Model):
    __tablename__ = 'supply_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(20))           # 'kg', 'unidade', 'cx'
    current_quantity = db.Column(db.Float, default=0)
    min_stock = db.Column(db.Float, default=0)

class SupplyPurchase(db.Model):
    __tablename__ = 'supply_purchases'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('supply_items.id'))
    quantity = db.Column(db.Float)
    unit = db.Column(db.String(20))
    notes = db.Column(db.Text)

    item = db.relationship('SupplyItem')

class SupplyConsumption(db.Model):
    __tablename__ = 'supply_consumptions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('supply_items.id'))
    quantity = db.Column(db.Float)
    unit = db.Column(db.String(20))
    snack_consumption_id = db.Column(db.Integer, db.ForeignKey('snack_consumptions.id'), nullable=True)
    notes = db.Column(db.Text)