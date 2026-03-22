document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridWeek',
        locale: 'pt-br',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'timeGridWeek,timeGridDay'
        },
        slotMinTime: '08:00:00',
        slotMaxTime: '18:00:00',
        allDaySlot: false,
        slotDuration: '01:00:00',
        editable: false,
        selectable: true,
        select: function(info) {
            // Ao clicar em um horário vazio, abre modal para agendamento
            openAppointmentModal(info.startStr, info.endStr);
        },
        eventClick: function(info) {
            // Exibe modal com detalhes do agendamento e opção de cancelar
            openEventModal(info.event);
        },
        events: function(info, successCallback, failureCallback) {
            // Buscar agendamentos do período exibido
            fetch(`/api/appointments/${info.startStr.split('T')[0]}`)
                .then(response => response.json())
                .then(events => successCallback(events))
                .catch(error => {
                    console.error('Erro ao carregar eventos:', error);
                    failureCallback(error);
                });
        }
    });
    calendar.render();

    // Elementos do modal de agendamento
    var modalAppointment = document.getElementById('appointmentModal');
    var closeAppointmentBtn = modalAppointment.querySelector('.close-button');
    var appointmentForm = document.getElementById('appointmentForm');
    var formMessage = document.getElementById('formMessage');
    var professionalSelect = document.getElementById('professional_id');
    var areaInput = document.getElementById('area');

    // Preencher área automaticamente ao selecionar profissional
    professionalSelect.addEventListener('change', function() {
        var selectedOption = professionalSelect.options[professionalSelect.selectedIndex];
        var area = selectedOption.getAttribute('data-area');
        areaInput.value = area || '';
    });

    // Fechar modal ao clicar no X ou fora do conteúdo
    function closeModal(modal) {
        modal.style.display = 'none';
        formMessage.innerHTML = '';
        appointmentForm.reset();
    }

    closeAppointmentBtn.onclick = function() { closeModal(modalAppointment); };
    window.onclick = function(event) {
        if (event.target == modalAppointment) closeModal(modalAppointment);
        if (event.target == modalEvent) closeModal(modalEvent);
    };

    // Abrir modal com dados do horário selecionado
    function openAppointmentModal(startStr, endStr) {
        const date = startStr.split('T')[0];
        const startTime = startStr.split('T')[1].substring(0,5);
        const endTime = endStr.split('T')[1].substring(0,5);
        const timeSlot = `${startTime}-${endTime}`;

        document.getElementById('date').value = date;
        document.getElementById('time_slot').value = timeSlot;
        modalAppointment.style.display = 'block';
    }

    // Enviar formulário
    appointmentForm.onsubmit = async function(e) {
        e.preventDefault();
        formMessage.innerHTML = '';

        const formData = {
            patient_name: document.getElementById('patient_name').value,
            patient_contact: document.getElementById('patient_contact').value,
            professional_id: parseInt(document.getElementById('professional_id').value),
            date: document.getElementById('date').value,
            time_slot: document.getElementById('time_slot').value,
            area: document.getElementById('area').value
        };

        try {
            const response = await fetch('/api/appointments', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            const result = await response.json();
            if (response.ok) {
                formMessage.innerHTML = '<div class="message success">' + result.message + '</div>';
                calendar.refetchEvents(); // atualiza calendário
                setTimeout(() => closeModal(modalAppointment), 1500);
            } else {
                formMessage.innerHTML = '<div class="message error">' + (result.error || 'Erro ao agendar') + '</div>';
            }
        } catch (err) {
            formMessage.innerHTML = '<div class="message error">Erro de conexão. Tente novamente.</div>';
            console.error(err);
        }
    };

    // Modal de detalhes/cancelamento
    var modalEvent = document.getElementById('eventModal');
    var closeEventBtn = modalEvent.querySelector('.close-button');
    var eventDetailsDiv = document.getElementById('eventDetails');
    var cancelEventBtn = document.getElementById('cancelEventBtn');
    var eventMessage = document.getElementById('eventMessage');
    let currentEventId = null;

    closeEventBtn.onclick = function() { closeModal(modalEvent); };

    function openEventModal(event) {
        currentEventId = event.id;
        const title = event.title;
        const start = moment(event.start).format('DD/MM/YYYY HH:mm');
        const end = moment(event.end).format('HH:mm');
        const props = event.extendedProps;
        const details = `
            <p><strong>Paciente:</strong> ${title.split(' - ')[0]}</p>
            <p><strong>Área:</strong> ${props.area || 'Não informada'}</p>
            <p><strong>Profissional:</strong> ${props.professional_name || 'Não informado'}</p>
            <p><strong>Contato:</strong> ${props.patient_contact || 'Não informado'}</p>
            <p><strong>Data/Hora:</strong> ${start} - ${end}</p>
        `;
        eventDetailsDiv.innerHTML = details;
        eventMessage.innerHTML = '';
        modalEvent.style.display = 'block';
    }

    cancelEventBtn.onclick = async function() {
        if (!currentEventId) return;
        eventMessage.innerHTML = '';

        try {
            const response = await fetch(`/api/appointments/${currentEventId}`, {
                method: 'DELETE'
            });
            const result = await response.json();
            if (response.ok) {
                eventMessage.innerHTML = '<div class="message success">Agendamento cancelado com sucesso. Vaga liberada.</div>';
                calendar.refetchEvents();
                setTimeout(() => closeModal(modalEvent), 1500);
            } else {
                eventMessage.innerHTML = '<div class="message error">' + (result.error || 'Erro ao cancelar') + '</div>';
            }
        } catch (err) {
            eventMessage.innerHTML = '<div class="message error">Erro de conexão. Tente novamente.</div>';
            console.error(err);
        }
    };
});