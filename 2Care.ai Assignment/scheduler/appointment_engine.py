appointments = []

def book_appointment(data):

    doctor = data.get("doctor")
    date = data.get("date")
    time = data.get("time")

    for appt in appointments:

        if appt["doctor"] == doctor and appt["time"] == time:
            return "That slot is already booked."

    appointment = {
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)

    return f"Your appointment with {doctor} is booked at {time} on {date}."


def cancel_appointment(data):

    doctor = data.get("doctor")

    for appt in appointments:

        if appt["doctor"] == doctor:
            appointments.remove(appt)
            return "Your appointment has been cancelled."

    return "No appointment found."


def reschedule_appointment(data):

    doctor = data.get("doctor")
    new_time = data.get("time")

    for appt in appointments:

        if appt["doctor"] == doctor:
            appt["time"] = new_time
            return f"Your appointment has been moved to {new_time}."

    return "Appointment not found."