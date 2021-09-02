#Create hospital admission application
#Sets the bed capacity
#Then admit patients provided there is remaining bed capacity

#define a class called hospital
class Hospital():
    def __init__ (self, capacity):
        self.bed_capacity = capacity
        self.patients = []

    #Method to admit patients
    def admit_patients(self, name):
        if not self.available_beds():
            return False  
        self.patients.append(name)   
        return True   

    #Method to check the available beds
    def available_beds(self):    #self allows you to use variables in above method
        return self.bed_capacity - len(self.patients)    


# hospital_one = Hospital(3)

# patient_list = ["Jane","Mark","Emily","Mike"]

# for patient in patient_list:
#     if hospital_one.admit_patients(patient):
#         print(f"We have admitted {patient} into the ward")
#     else:
#         print(f"Hospital capacity exhausted.cannot admit {patient}") 


hospital_two = Hospital(5)

patient_list = ["Jane","Mark","Emily","Mike"]

for patient in patient_list:
    if hospital_two.admit_patients(patient):
        print(f"We have admitted {patient} into the ward")
    else:
        print(f"Hospital capacity exhausted.cannot admit {patient}") 

