from random import randint
from numpy import empty
from db_methods import select_new_renewals
import utils
import db_methods

def main():
    renewals = select_new_renewals()
    if renewals is not empty:
        for renewal in renewals:
            patient_name = renewal[0]
            medicine = renewal[1]
            email = renewal[2]
            utils.send_mail(patient_name, medicine, email)

    prescription_id = db_methods.check_if_has_prescription(patient_name)
    if prescription_id is not None:
        pharmacy_id = randint(1,3)
        db_methods.accept_prescription(prescription_id, pharmacy_id)
        pharmacist, pharmacy = db_methods.pharmacist_to_give_prescription(pharmacy_id)
        utils.write_prescription_info_to_csv(patient_name, renewal[1], pharmacy, pharmacist)


if __name__ == "__main__":
   main()