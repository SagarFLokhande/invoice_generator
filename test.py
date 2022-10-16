from flask import Flask, render_template, send_file
from weasyprint import HTML

app = Flask(__name__)
@app.route('/')


def func():
    rendered = render_template('./templates/invoice.html', date = "Oct 16, 2022")
    html = HTML(string=rendered)
    rendered_pdf = html.write_pdf('./static/invoice.pdf') 
    return send_file('./static/invoice.pdf')

print("hello world")


