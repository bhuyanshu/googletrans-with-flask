from flask import Flask,render_template,url_for,request
from googletrans import Translator
import requests

app = Flask(__name__,template_folder='templates')
translator = Translator()

@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            text_to_translate = request.form["text-to-translate"].lower()
            selected_language = request.form["select-language"]
            translated_text = translator.translate(text_to_translate, dest=selected_language)
            text = translated_text.text
            pron = translated_text.pronunciation
        except:
            pron = "-"
            text = "{ERROR :please Try again }"
        return render_template('index.html',result =text,data =pron)
    return render_template('index.html')

if __name__ =="__main__":
    app.run(debug=True)