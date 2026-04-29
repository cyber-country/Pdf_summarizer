from flask import Flask,request,render_template
import pdfplumber
import re
def extract(n):
    with pdfplumber.open(n) as pdf:
        text=""
        pages=pdf.pages
        for page in pages:
            text+=(page.extract_text() or "")+"\n"
        return text
def text_organizer(s):
    s=re.sub(r'\s+',' ',s)
    return s
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        file=request.files.get("content")
        if file and file.name!="":
            print("file_successfully recieved")
        text = extract(file)
        clean_text=text_organizer(text)
        print("successfully the pdf operation has been done...")
        return clean_text
    return render_template("index.html")
app.run(debug=True)