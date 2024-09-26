class Patient:
    def __init__(self, name, age, is_hospitalized):
        self.name = name
        self.__age = age
        self.is_hospitalized = is_hospitalized

    def get_info(self):
        return f"Patient: {self.name}, Age: {self.__age}, Hospitalized: {self.is_hospitalized}"

    def hospitalize_patient(self):
        if not self.is_hospitalized:
            self.is_hospitalized = True
            patient_record = f"Registering patient {self.name} (age {self.__age}) for hospitalization."
            staff_notification = f"Notifying medical staff to prepare a room for {self.name}."
            return f"{patient_record}\n{staff_notification}\nPatient {self.name} has been successfully hospitalized."
        else:
            return f"Patient {self.name} is already hospitalized."

    def set_data(self, name, age, is_hospitalized):
        self.name = name
        self.__age = age
        self.is_hospitalized = is_hospitalized

    @staticmethod
    def hospital_name():
        return "City General Hospital"


class MedicalStaff:
    def __init__(self, department):
        self.department = department

    def get_department(self):
        return f"Department: {self.department}"


class Doctor(Patient):
    def __init__(self, name, age, is_hospitalized, specialization):
        Patient.__init__(self, name, age, is_hospitalized)
        self.specialization = specialization

    def get_info(self):
        return f"Doctor: {self.name}, Specialization: {self.specialization}"

    def perform_surgery(self):
        if self.is_hospitalized:
            return f"Doctor {self.name} is performing surgery on a hospitalized patient."
        else:
            return f"Doctor {self.name} is conducting a routine check-up."


class Nurse(Patient, MedicalStaff):
    def __init__(self, name, age, is_hospitalized, shift, department):
        Patient.__init__(self, name, age, is_hospitalized)
        MedicalStaff.__init__(self, department)
        self.shift = shift

    def assist_doctor(self):
        return f"Nurse {self.name} is assisting during the {self.shift} shift in {self.department}."


patient_1 = Patient("John Doe", 45, False)
patient_2 = Patient("Vasyl Johnson", 25, True)
doctor_1 = Doctor("Dr. Smith", 50, False, "Cardiology")
nurse_1 = Nurse("Maria", 30, False, "Night", "Emergency Room")

print(patient_1.get_info())
print(patient_2.get_info())
print(doctor_1.get_info())
print(nurse_1.assist_doctor())
print(patient_1.hospitalize_patient())
print(patient_2.hospitalize_patient())
print(doctor_1.perform_surgery())

print(patient_1.hospitalize_patient())

print(Patient.hospital_name())
