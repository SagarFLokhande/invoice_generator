# HTML, pdf invoice generator. 

# Contributors: Sagar F. Lokhande.

In this repo, I write a simple Python code that generates HTML and pdf invoices and also send them to the desires client. 

* invoice.HTML :

This is the HTML invoice template. It has a simple layout. As well as placeholders where the Python script will insert relevant information. 

* app.py :

This is the main code. It heavily depends on the libraries WesyPrint and Flask. Supporting libraries are os, io and datetime. The code returns an HTML invoice, a pdf invoice as well has the option to send the pdf invoice to a client. 