from flask import Flask, render_template
import image_analyzer as ia
app = Flask(__name__)

@app.route('/')
def index():
    cout_of_co = ia.analyzer()
    text1 = str(cout_of_co)
    return render_template("index.html",additional_text = text1)



if __name__ == "__main__":
    app.run(debug=True)
