
from weasyprint import HTML
from flask import Flask, render_template, send_file, request
import os, io
from datetime import datetime, timedelta

app = Flask(__name__)
@app.route('/')


def invoice_func():
    dtoday_raw = datetime.today()
    today = dtoday_raw.strftime("%B %-d, %Y")
    dueraw = dtoday_raw + timedelta(days=7)
    duedate = dueraw.strftime("%B %-d, %Y")
    invoice_number = 123,
    from_addr = {
        "company_name" : "Corporation XYZ",
        "addr1" : "Lane ABC",
        "addr2" : "Townville, EFG 12345"
        }
    items = [
        {
            "title" : "website design",
            "charge" : 300
        },{
            "title" : "hosting (3 months)",
            "charge" : 150
        },{
            "title" : "domain name",
            "charge" : 30
        }]
    to_addr = {
        "company_name" : "Customer Corp LLC",
        "person_name" : "John Doe",
        "person_email" : "john@example.com"
        }
    total = sum([i["charge"] for i in items])

    rd = render_template('invoice.html', date = today, from_addr = from_addr, to_addr = to_addr, items = items, total = total, invoice_numer = invoice_number, duedate = duedate)
    html_page = HTML(string=rd)
    rd_pdf = html_page.write_pdf()
    return send_file(io.BytesIO(rd_pdf), mimetype=None, download_name="invoice.pdf")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
