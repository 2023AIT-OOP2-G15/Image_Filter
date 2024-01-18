from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PREVIEW_FOLDER'] = 'static/preview'
app.config['PROCESSED_FOLDER'] = 'static/processed'

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

@app.route('/view/<filename>')
def view(filename):
    processed_image = os.path.join(app.config['PROCESSED_FOLDER'], filename)
    return render_template('view.html', processed_image=processed_image)

if __name__ == '__main__':
    app.run(debug=True)
