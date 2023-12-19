from flask import Flask, render_template, request
import learning_utils
import image_analyzer as ia
import trainer as tr
app = Flask(__name__)

@app.route('/')
def index():
    analyzer_respnse = ia.analyzer('static/img/img4.jpg')
    feature = learning_utils.Feature(analyzer_respnse,10,10)
    text1 = feature.getFeature()
    #text1 = str(cout_of_co)
    return render_template("index.html",additional_text = text1)




@app.route('/learn')
def learn():
    tr.createDatasetfromImages()

@app.route('/upload', methods=['POST'])
def upload():
    if 'uploaded_image' in request.files:
        image_file = request.files['uploaded_image']
        if image_file.filename != '':
            image_file.save('static/img/img4.jpg')

    return index()

if __name__ == "__main__":
    app.run(debug=True)

