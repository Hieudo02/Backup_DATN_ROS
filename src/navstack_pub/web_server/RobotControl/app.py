from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_to_pgm(image_path):
    with Image.open(image_path) as img:
        gray_img = img.convert('L')
        binary_img = gray_img.point(lambda p: p > 128 and 255)
        pgm_path = image_path.rsplit('.', 1)[0] + '.pgm'
        binary_img.save(pgm_path)
    return pgm_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files and 'resolution' in request.form:
            file = request.files['file']
            resolution = request.form['resolution']
            if file.filename != '' and allowed_file(file.filename):
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)
                
                pgm_filename = convert_to_pgm(filename)

                points = []
                for key in request.form:
                    if key.startswith('points'):
                        index = key[key.find('[')+1:key.find(']')]
                        if key.endswith('[x]'):
                            if len(points) <= int(index):
                                points.append({})
                            points[int(index)]['x'] = request.form[key]
                        elif key.endswith('[y]'):
                            if len(points) <= int(index):
                                points.append({})
                            points[int(index)]['y'] = request.form[key]

                print('Uploaded file:', pgm_filename)
                print('Resolution:', resolution)
                print('Points:', points)
                return jsonify({'url': url_for('uploaded_file', filename=file.filename)})
        if request.json and 'direction' in request.json:
            data = request.json
            # 'left', 'right', 'forward', 'backward' biến lưu giá trị các hướng đi
            direction = data['direction'] 
            print('Received direction:', direction)
            # Thực hiện xử lý với direction ở đây
            return jsonify({'status': 'success'})
        return jsonify({'status': 'failure'})
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
