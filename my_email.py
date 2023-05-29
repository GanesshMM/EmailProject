import fpdf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def fill_pdf(pdf_file, data):
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=21, style='BU')
    pdf.cell(190, 20, txt="R.M.K College Of Engineering And Technology", ln=1, align="C")
    pdf.cell(190, 20, txt="Outing Form", ln=3, align="C")
    pdf.cell(190, 13, txt="", ln=4, align="C")
    for key, value in data.items():
        pdf.set_font("Times", style='BU', size=17)
        pdf.cell(77, 14, txt=key, ln=0, align="L")
        pdf.set_font("Times", size=15)
        pdf.cell(73, 14, txt=value, ln=1, align="L")
    pdf.cell(220, 80, txt="", ln=3, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(50, 13, txt="H.O.D", ln=0, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(65, 13, txt="Class Counsellor", ln=0, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(75, 13, txt="Branch Co-Ordinator", ln=1, align="C")
    pdf.output(pdf_file, "F")


def send_email(pdf_file, recipient, sender, password):
    msg = MIMEMultipart()
    with open(pdf_file, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={pdf_file}")
    msg.attach(part)
    msg["To"] = recipient
    msg["From"] = sender
    msg["Subject"] = "Outing Form"
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(msg)

def email_data(datas):
    student_name = datas['student_name']
    reg_no = datas['reg_no']
    department = datas['department']
    email = datas['email']
    phone_no = datas['phone_no']
    address = datas['address']
    leaving_date = datas['leaving_date']
    arriving_date = datas['arriving_date']

    data = {}
    num = 0
    keys = ["Name", "Registeration Number", "Department", "Email", "Phone Number", "Address", "Leaving Date", "Arriving Date",]
    for key,num in keys:
        value =  datas[num]
        data[key] = value
    pdf_file = "Outing Form.pdf"
    fill_pdf(pdf_file, data)
    recipient = data['Email']
    sender = "ganessh7114@gmail.com"
    password = "krvqssopqhulecul"
    send_email(pdf_file, recipient, sender, password)
    print("\"Successfully Sent the E-mail\"")


    
