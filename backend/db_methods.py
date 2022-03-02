from audioop import add
from random import randint
from numpy import full
from connection import conn
from random_address import real_random_address
import names
from psycopg2 import sql
import traceback
from random import randint
from utils import send_mail

def generate_sql_insert(db_table,returning,obj,conn,cursor):
    try:
        sql_statement = """
        insert into db_assignment2.{} ({}) values ({}) returning {}
        """
        column_names = list(obj.keys())
        qry_str = sql.SQL(sql_statement).format(
                sql.SQL(db_table),
                sql.SQL(",").join(map(sql.Identifier, column_names)),
                sql.SQL(",").join(sql.Placeholder() * len(column_names)),
                sql.SQL(returning)
                )
        cursor.execute(qry_str.as_string(conn), list(obj.values()))
        return_id = cursor.fetchone()[0]
        return return_id
    except:
        traceback.print_exc()

def insert_patients():
    with conn:
        with conn.cursor() as cursor:
            for _ in range(100):
                patient = {}
                patient["full_name"] = names.get_full_name()
                patient["address"] = real_random_address().get('address1')
                patient["city"] = real_random_address().get('city')
                patient["postal"] = real_random_address().get('postalCode')
                patient["email"] = "cph-sd152@cphbusiness.dk"
                generate_sql_insert("patient", "null", patient, conn, cursor)

def insert_doctors():
    specialities = ['Neurolog', 'Ordontolog', 'Kardiolog']
    with conn:
        with conn.cursor() as cursor:
            for speciality in specialities:
                speciality_dict = {}
                speciality_dict["name"] = names.get_full_name()
                speciality_dict["speciality"] = speciality
                generate_sql_insert("doctor", "null", speciality_dict, conn, cursor)


def insert_pharmacies():
    pharmacies = ['Taastrup apotek', 'Hillerød apotek', 'Lyngbys apotek']
    with conn:
        with conn.cursor() as cursor:
            for pharmacy in pharmacies:
                pharmacy_dict = {}
                pharmacy_dict["name"] = pharmacy
                pharmacy_dict["address"] = real_random_address().get('address1')
                pharmacy_dict["city"] = real_random_address().get('city')
                pharmacy_dict["postal"] = real_random_address().get('postalCode')
                generate_sql_insert("pharmacy", "null", pharmacy_dict, conn, cursor)

def insert_medicine():
    medicines = {"medicine_name":"Pandodil", "instructions": "Tag 1 pille morgen og aften"}, {"medicine_name": "Kodimagnyl", "instructions": "Tag 1 pille om dagen"}, {"medicine_name": "Benadryl", "instructions": "Tag 2 piller morgen og aften"}
    with conn:
        with conn.cursor() as cursor:
            for medicine in medicines:
                generate_sql_insert("medicine", "null", medicine, conn, cursor)


def insert_pharmacists():
    with conn:
        with conn.cursor() as cursor:   
            for _ in range(20):
                try:
                    pharmacist = {}
                    pharmacist["name"] = names.get_full_name()
                    pharmacist["fk_pharmacy_id"] = randint(1, 3)
                    generate_sql_insert("pharmacist", "null", pharmacist, conn, cursor)
                except Exception as e:
                    print(e)
                    import sys
                    sys.exit()

def create_prescription(new_prescription):
    with conn:
        with conn.cursor() as cursor:
            generate_sql_insert("prescription", "null", new_prescription, conn, cursor)

def select_new_renewals():
    with conn:
        with conn.cursor() as cursor:
            sql_statement = "select * from db_assignment2.select_new_renewals();"
            cursor.execute(sql_statement)  
            result_set = cursor.fetchall()
            return result_set

renewals = select_new_renewals()
for renewal in renewals:
    send_mail(renewal[0], renewal[1], renewal[2])