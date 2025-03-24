import os

mail_sender_email = os.environ.get('MAIL_SENDER_EMAIL',"f-taste@airedstartup.it")
mail_sender_password = os.environ.get('MAIL_SENDER_PASSWORD',"1&jc8EXLgd0xH&1Q")
#port = 465
port=2525# non uso ssl , di base sarebbe 465
smtp_server = os.environ.get('SMTP_SERVER',"smtps.aruba.it")

secret_key = os.environ.get('SECRET_KEY', b"\xf2\n\xdf\x07#\xd6J/ \x88\xa0\xb4'\x0f\xc7\x15")

def get_key():
    return os.environ.get('ENCRYPTION_KEY', 'Bcsoft!1')
