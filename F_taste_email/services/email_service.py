from smtplib import SMTPRecipientsRefused
from F_taste_email.utils.mail_service import send_mail_registrazione_paziente,send_mail_registrazione_medico,EmailNotFound




class EmailService:

    
    @staticmethod
    def registrazione_paziente(s_email):
        if "id_paziente" not in s_email or "email_paziente" not in s_email:
            return {"status_code":"400"}, 400
        id_paziente=s_email["id_paziente"]
        email_paziente=s_email["email_paziente"]
        try:
            send_mail_registrazione_paziente(id_paziente,email_paziente)
        except SMTPRecipientsRefused as e:
            return{"status_code":"400"}, 400
        return {"status_code":"200"}, 200
    
    @staticmethod
    def nutrizionista_registrazione_paziente(s_email):
        if "id_paziente" not in s_email or "email_paziente" not in s_email or "email_nutrizionista" not in s_email or "password" not in s_email:
            return {"status_code":"400"}, 400
        id_paziente=s_email["id_paziente"]
        email_paziente=s_email["email_paziente"]
        email_nutrizionista=s_email["email_nutrizionista"]
        password=s_email["password"]
        try:
            send_mail_registrazione_medico(id_paziente,password,email_nutrizionista,email_paziente)
        except EmailNotFound:
            return {"status_code":"404"}