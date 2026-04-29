from flask import Flask,request,render_template
import pdfplumber
def extract(n):
    with pdfplumber.open(n) as pdf:
        text=""
        pages=pdf.pages
        for page in pages:
            text+=(page.extract_text() or "")+"\n"
        return text
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        file=request.files.get("content")
        print("file_successfully recieved")
        pdf = extract(file)
        print("successfully the pdf operation has been done...")
        return pdf
    return render_template("index.html")
app.run(debug=True)