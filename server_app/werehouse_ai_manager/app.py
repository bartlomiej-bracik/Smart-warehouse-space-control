from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import learning_utils
import image_analyzer as ia
import trainer as tr
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    analyzer_respnse = ia.analyzer('static/img/img4.jpg')
    feature = learning_utils.Feature(analyzer_respnse,0)
    text1 = feature.getFeature()
    className = tr.classify(text1)
    #text1 = str(cout_of_co)
    return render_template("index.html",additional_text = className)




@app.route('/learn')
def learn():
    tr.createDatasetfromImages()
    return index()
@app.route('/upload', methods=['POST'])
def upload():
    if 'uploaded_image' in request.files:
        image_file = request.files['uploaded_image']
        if image_file.filename != '':
            image_file.save('static/img/img4.jpg')
        return index()
    if 'file' in request.files:
        image_file = request.files['uploaded_image']
        if image_file.filename != '':
            image_file.save('static/img/img4.jpg')
        return jsonify({ 'message': 'File uploaded successfully'})

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

