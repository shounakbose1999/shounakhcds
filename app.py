from flask import Flask, redirect, url_for,  render_template, request

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
app = Flask(__name__,template_folder='template')

@app.route("/",methods=["GET","POST"])
def home():
    if request.method== "POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        if score["neg"]!= 0:
            return render_template("index.html",message="Negative 🙁🙁")
        else:
            return render_template("index.html",message="Positive 😀😀")

    return render_template("index.html")



if __name__ =='__main__':
    app.run(debug=True)


