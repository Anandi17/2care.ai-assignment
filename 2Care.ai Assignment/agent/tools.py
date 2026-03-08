from scheduler.appointment_engine import (
    book_appointment,
    cancel_appointment,
    reschedule_appointment
)

def handle_tool(data):

    intent = data.get("intent")

    if intent == "book":
        return book_appointment(data)

    if intent == "cancel":
        return cancel_appointment(data)

    if intent == "reschedule":
        return reschedule_appointment(data)

    return "Sorry, I couldn't process your request."