import os

mail_sender_email = os.environ.get('MAIL_SENDER_EMAIL',"f-taste@airedstartup.it")
mail_sender_password = os.environ.get('MAIL_SENDER_PASSWORD',"1&jc8EXLgd0xH&1Q")
port = 465
smtp_server = os.environ.get('SMTP_SERVER',"smtps.aruba.it")
