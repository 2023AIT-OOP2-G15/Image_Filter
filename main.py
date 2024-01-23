from flask import Flask, render_template, request, redirect, url_for, jsonify

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PREVIEW_FOLDER'] = 'static/preview'
app.config['PROCESSED_FOLDER'] = 'static/processed'
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

def get_preview_image():
    return os.path.join(app.config['PREVIEW_FOLDER'], 'temporary.png')

def save_preview_image(file):
    file.save(get_preview_image())

def save_processed_image(processed_name):
    processed_image = os.path.join(app.config['PROCESSED_FOLDER'], f'{processed_name}.png')
    os.replace(get_preview_image(), processed_image)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/processing', methods=['GET', 'POST'])
def processing():
    if request.method == 'POST':
        # Handle image upload
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                save_preview_image(file)

    return render_template('processing.html', preview_image=get_preview_image())

@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        processed_name = request.form['processed_name']
        save_processed_image(processed_name)
        return redirect(url_for('view', filename=f'{processed_name}.png'))

    return redirect(url_for('processing'))

@app.route('/view', methods=['GET', 'POST'])
def view():
    # 静的フォルダのパスを取得
    static_folder = os.path.join(app.root_path, 'static')

    # 静的フォルダ内の画像のリストを取得
    images_folder = os.path.join(static_folder, 'processed')
    image_files = [f for f in os.listdir(images_folder) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]

    # 画像のパスリストを作成
    image_paths = [os.path.join('processed', img) for img in image_files]

    return render_template('view.html', image_paths=image_paths)


# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("home.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)