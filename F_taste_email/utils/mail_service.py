import smtplib
import ssl

from flask import render_template

import F_taste_email.utils.credentials as credentials
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail_registrazione_medico(codice_identificativo, password_temporanea, email_nutrizionista, email_paziente):
	message_paziente = MIMEMultipart("alternative")
	message_nutrizionista = MIMEMultipart("alternative")

	message_nutrizionista["Subject"] = f"""  Identificativo F-taste paziente "{email_paziente}" """
	message_nutrizionista["From"] = credentials.mail_sender_email
	message_nutrizionista["To"] = email_nutrizionista

	message_paziente["Subject"] = " Identificativo F-taste "
	message_paziente["From"] = credentials.mail_sender_email
	message_paziente["To"] = email_paziente

	html_paziente = f"""\
    <html>
      <body>
         <h3> Il tuo codice identificativo è: {codice_identificativo}</h3>
         <h3> La tua password temporanea è: {password_temporanea}</h3>
            <p>
            Codice identificato e password sono da utilizzare al login.
            <br>
            Dopo il primo accesso modificare la propria password nell'area riservata.     
          </p>
      </body>
    </html>
    """

	body_email_paziente = MIMEText(html_paziente, "html")
	message_paziente.attach(body_email_paziente)

	html_nutrizionista = f"""\
        <html>
          <body>
             <h3> Il  codice identificativo del paziente "{email_paziente}" è: {codice_identificativo}</h3>
                <p>
                Questo codice è da utilizzare al login con la password aggiunta alla registrazione.     
              </p>
          </body>
        </html>
        """

	body_nutrizionista = MIMEText(html_nutrizionista, "html")
	message_nutrizionista.attach(body_nutrizionista)



	

	
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(credentials.smtp_server, credentials.port, context=context) as server:
		try:
			server.login(credentials.mail_sender_email, credentials.mail_sender_password)
			server.sendmail(credentials.mail_sender_email, email_paziente, message_paziente.as_string())
			server.sendmail(credentials.mail_sender_email, email_nutrizionista, message_nutrizionista.as_string())
		except smtplib.SMTPException as e:
			if e is smtplib.SMTPRecipientsRefused:
				message = "{email_paziente} not exist or rejected"
				raise EmailNotFound(message)
			else:
				raise e
	
	
			


def send_mail_registrazione_paziente(codice_identificativo, email_paziente):
	message_paziente = MIMEMultipart("alternative")

	message_paziente["Subject"] = " Identificativo F-taste "

	html_paziente = f"""\
	<html>
		<body>
			<h3> Il tuo codice identificativo è: {codice_identificativo}</h3>
			<p>
				Codice identificativo  da utilizzare al login.
				<br>
			</p>
		</body>
	</html>
	"""

	body_email_paziente = MIMEText(html_paziente, "html")
	message_paziente.attach(body_email_paziente)


	
	
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(credentials.smtp_server, credentials.port, context=context) as server:
		try:
			server.login(credentials.mail_sender_email, credentials.mail_sender_password)
			server.sendmail(credentials.mail_sender_email, email_paziente, message_paziente.as_string())
		except smtplib.SMTPException as e:
			if e is smtplib.SMTPRecipientsRefused:
				message = "{email_paziente} not exist or rejected"
				raise EmailNotFound(message)
			else:
				raise e
				
			


def send_mail_refresh_paziente(email_paziente,link_refresh,id_paziente):
	message_paziente = MIMEMultipart("alternative")

	message_paziente["Subject"] = " Recupero password \"f-taste\" "


    #gli passo in input il link refresh
	html_paziente=render_template("paziente/email_reset_password.html",link_refresh=link_refresh,id=id_paziente)
	body_email_paziente = MIMEText(html_paziente, "html")
	message_paziente.attach(body_email_paziente)

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(credentials.smtp_server, credentials.port, context=context) as server:
		try:
			server.login(credentials.mail_sender_email, credentials.mail_sender_password)
			server.sendmail(credentials.mail_sender_email, email_paziente, message_paziente.as_string())
		except smtplib.SMTPException as e:
			breakpoint()
			if e is smtplib.SMTPRecipientsRefused:
				message = "{email_paziente} not exist or rejected"
				raise EmailNotFound(message)
			else:
				raise e


class EmailNotFound(Exception):

	def __init__(self, message):
		Exception.__init__(self)
		self.message = message

		