# Image_Filter
画像フィルター

# 各メンバーの役割


|役割|名前(k00000)|内容|状況|備考|
|---|---|---|---|---|
|Web|青島巧典(k22003)|閲覧ページの作成|||
|Web|胡田哲志(k22024)|アップロード、加工ページの作成|||
|Web|佐伯祐人(k22058)|ホームページの作成|||
|画像処理|大屋萌奈(k22027)|リーダー、READサポートなど|本日(1/11)は休養||
|画像処理|加藤大地(k22035)|暖色・寒色、ビンテージ風フィルタの作成|||
|画像処理|北沢直暉(k22044)|グレースケール、セピア調、ぼかしフィルタの作成|||
|画像処理|西田拓磨(k21092)|背景切り取り・追加、二値化フィルタの作成|||

#　決め事
```
Image_Filter
├─ static
│   ├─ style.css
│   │
│   ├─ preview
│   │    ├─preview.png
│   │    └─tenporary.png
│   │
│   ├─ processed
│   │
│   └─ uploads
│
│
├─ templates
│   └─ index.html
│
├─ function
│   ├─ Glayscale
│   ├─ Warm_Color
│   ├─ Cold_Color
│   ├─ Vintage
│   ├─ Sepia
│   ├─ Gradation
│   ├─ Bg_Cutout
│   ├─ Bg_Add
│   └─ Binarization
│
├─ main.py
├─ README.md
├─ .DS_Store
├─ .python-version
├─ 

```
- アップロードした画像は ../static/uploads/xxx.png に保存してください

- フィルタ等で加工した画像は ../static/processed/xxx.png に保存してください
また、元画像や加工情報等を纏めたファイルを　../static/processed/xxx.json (xxxは加工した画像名と同じ)に保存してください

-　../static/processed/xxx.json のサンプル
```
{
    "ORIGIN_IMAGE": "xxx.png", #このjsonファイルと同じ名前になること
    "process_info": {
        "GLAYSCALE": "none", #加工が行われていない場合は"none"とする
        "WARM_COLOR": "on", #加工が行われている場合は"on"とする
        "COLD_COLOR": "none",
        "VINTAGE": "none",
        "SEPIA": "none",
        "GRADATION": "none",
        "BG_CUTOUT": "none",
        "BINARIZATION": "none",
        "bg_add": {
            "BG": "on",
            "ADD_IMAGE": "yyy.png" #bg_addを行う場合は追加アップロードした画像名、行わない場合は"none"とする
        }
    }
}
```

- 加工ページにて各種フィルタ等を選択した際、元画像にフィルタを掛けた画像が ../static/preview/tenporary.png に上書きされます

- 関数名
Glayscale:画像のグレースケール化
Warm_Color:画像の暖色化
Cold_Color:画像の寒色化
Vintage:画像のビンテージ風加工フィルタ
Sepia:画像のセピア調加工フィルタ
Gradation:画像のぼかし加工フィルタ
Bg_Cutout:画像背景の切り取り
Bg_Add:画像背景の追加(画像の追加アップロードが必要)
Binarization:画像の二値化


## システムの動作確認方法
ここからmainを確認できます
<https://github.com/2023AIT-OOP2-G15/Image_Filter>

動かしたい場合は、ブランチをmainにしてターミナルで起動

## 使用するライブラリのバージョン


