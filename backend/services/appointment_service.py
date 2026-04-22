appointments = []

def create_appointment(user, date, time):
    appt = {"user": user, "date": date, "time": time}
    appointments.append(appt)
    return appt

def get_appointments():
    return appointments