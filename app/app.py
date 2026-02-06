from flask import Flask,request,render_template
from src.predict import predict_image
import os
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/upload",methods=["POST"])
def upload():
    file=request.files["image"]
    path="dataset/test/"+file.filename
    file.save(path)
    label,score=predict_image(path)
    return f"Result: {label}, Asymmetry Score: {score}"
if __name__=="__main__":
    app.run(debug=True)
