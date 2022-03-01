from audioop import add
from numpy import full
from connection import conn
from random_address import real_random_address
import names

def insert_persons():
    with conn:
        with conn.cursor() as cursor:
            sql_statement = 'insert into db_assignment2.patient (full_name, address, city, postal, email) values(%s, %s, %s, %s, %s)'

            for _ in range(10):
                full_name = names.get_full_name()
                address = real_random_address().get('address1')
                city = real_random_address().get('city')
                postal = real_random_address().get('postalCode')
                email = "cph-sd152@cphbusiness.dk"
                cursor.execute(sql_statement, [full_name, address, city, postal, email])

def insert_doctors():
    specialities = ['Neurolog', 'Ordontolog', 'kardiolog']
    with conn:
        with conn.cursor() as cursor:
            sql_statement = 'insert into db_assignment2.doctor (name, speciality) values(%s, %s)'
            for speciality in specialities:
                full_name = names.get_full_name()
                cursor.execute(sql_statement, [full_name, speciality])

def insert_pharmacies():
    pharmacies = ['Taastrup apotek', 'Hillerød apotek', 'Lyngbys apotek']
    with conn:
        with conn.cursor() as cursor:
            sql_statement = 'insert into db_assignment2.pharmacy (name, address, city, postal) values(%s, %s, %s, %s)'
            for pharmacy in pharmacies:
                address = real_random_address().get('address1')
                city = real_random_address().get('city')
                postal = real_random_address().get('postalCode')
                cursor.execute(sql_statement, [pharmacy, address, city, postal])

def insert_medicine():
    medicines = {"Panodil": "Tag 1 pille morgen og aften", "Kodimagnyl": "Tag 1 pille om dagen", "Benadryl": "Tag 2 piller morgen og aften"}
    with conn:
        with conn.cursor() as cursor:
            sql_statement = 'insert into db_assignment2.medicine (medicine_name, instructions) values(%s, %s)'
            for medicine in medicines:
                instructions = medicines.get(medicine)
                cursor.execute(sql_statement, [medicine, instructions])

def insert_pharmacists():
    pharmacists = ['Sumit Dey', 'Christoffer Wegner', 'Lukas Bang']
    with conn:
        with conn.cursor() as cursor:
            sql_statement = 'insert into db_assignment2.pharmacist (name, fk_pharmacy_id) values(%s, %s)'
            for pharmacist in pharmacists:

                cursor.execute(sql_statement, [pharmacist, "speciality"])


def create_prescription(patient_id, doctor_id, medicine_id):
    with conn:
        with conn.cursor() as cursor:
            sql_statement = "insert into db_assignment2.prescription (fk_patient_id, fk_doctor_id, fk_medicine_id) values (%s, %s, %s)"
            cursor.execute(sql_statement, [patient_id, doctor_id, medicine_id])

