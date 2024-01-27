from flask import Flask, render_template, request,flash, redirect, url_for, jsonify
import function.BgAdd.BgAdd,function.BgCutout.BgCutout,function.Binarization.Binarization,function.ColorCold.ColorCold,function.ColorWarm.ColorWarm,function.Glayscale.Glayscale,function.Gradation.Gradation,function.Sepia.Sepia,function.Vintage.Vintage
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Flashメッセージを使用するための秘密鍵
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

@app.route('/processing', methods=['GET', 'POST'])
def processing():
    func_num=request.args.get('func_num')
    if func_num==None:
        if request.method == 'POST':
          # Handle image upload
            if 'file' in request.files:
                file = request.files['file']
                if file.filename != '':
                    save_preview_image(file)
                else:
                    flash('ファイルが選択されていません', 'error')
                    return redirect(url_for('processing'))
            else:
                flash('ファイルが選択されていません', 'error')
                return redirect(url_for('processing'))

        return render_template('processing.html', preview_image=get_preview_image())
    else:
        if not os.path.exists('static/preview/temporary.png'):
            flash('ファイルをアップロードしてください', 'error')
            return redirect(url_for('processing'))
        if func_num == '1':
            if 'file' in request.files:
                file = request.files['file']
                if file.filename != '':
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'background.png'))
                    processed_image = function.BgAdd.BgAdd.convert_to_BgAdd('static/preview/temporary.png','static/uploads/background.png')
                else:
                    flash('ファイルが選択されていません', 'error')
                    return redirect(url_for('processing'))
            else:
                flash('ファイルが選択されていません', 'error')
                return redirect(url_for('processing'))
        elif func_num == '2':
            processed_image = function.BgCutout.BgCutout.convert_to_BgCutout('static/preview/temporary.png')
        elif func_num == '3':
            processed_image = function.Binarization.Binarization.convert_to_Binarization('static/preview/temporary.png')
        elif func_num == '4':
            processed_image = function.ColorCold.ColorCold.ColorCold('static/preview/temporary.png')
        elif func_num == '5':
            processed_image = function.ColorWarm.ColorWarm.ColorWarm('static/preview/temporary.png')
        elif func_num == '6':
            processed_image = function.Glayscale.Glayscale.convert_to_grayscale('static/preview/temporary.png')
        elif func_num == '7':
            processed_image = function.Gradation.Gradation.convert_to_gradation('static/preview/temporary.png')
        elif func_num == '8':
            processed_image = function.Sepia.Sepia.convert_to_Sepia('static/preview/temporary.png')
        elif func_num == '9':
            processed_image = function.Vintage.Vintage.Vintage('static/preview/temporary.png')
        else:
            return redirect(url_for('processing'))
        # 他の処理関数も同様に実装
        os.remove(get_preview_image())
        save_preview_image(processed_image)
        return render_template('processing.html', preview_image=get_preview_image())

#@app.route('/processing/<int:func_num>', methods=['POST'])
#def filter(func_num):
    

@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        if not os.path.exists('static/preview/temporary.png'):
            flash('ファイルをアップロードしてから保存してください', 'error')
            return redirect(url_for('processing'))
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
def home():
    return render_template('home.html')


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)