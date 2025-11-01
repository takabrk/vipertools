Linux application "Viper Tools"
Web site URL : https://note.com/vsrx
Created by takamitsu_h
Updated November 1,2025

詳しいリファレンスは、以下で公開しています。

http://vsrx.work/viperdocs/index.html

このアプリケーションを使うには、Pythonなどをインストールする必要があります。
「install_libraryapps」というシェルスクリプトがありますので、これを端末で起動させれば、必要なソフトウェアやライブラリをインストールします。

$ scripts/install_libraryapps

To use the reading features, you need to install Open Jtalk, Mecab, and mecab-python3.

$ sudo apt install open-jtalk open-jtalk-mecab-naist-jdic mecab
$ sudo pip install mecab-python3

[動作環境]
・Ubuntu 22.04.5 LTS
・Python 3.10,Python2.7
・GTK+3
・libglade
・xfce4-terminal

[主な機能]
・数字選択式宝くじ予想機能
・tmpfsのRAMDISK量の調整機能
・アニメーションGIFのようなアニメーションSVG、APNGを作成する機能
・アプリケーションやライブラリのインストール
・Ubuntu系ディストリビューションのリマスター機能
・人工音声で朗読する機能
・YouTubeなどで公開されている動画をダウンロードする機能
・画像切り抜き機能


◇viperクラスとメソッドを使う
必要なライブラリのインストールは、端末で以下のようにして実行します。
$python viper.py import

各種メソッドは、viper.pyを該当するスクリプトにimport文を使ってインポートして使っていきます。

◇tmpfs_ramdisk_slider.py
端末から「python vipertools.py」と入力して起動して項目を選択する。
tmpfsのRAMディスクの容量を変更出来ます。

◇宝くじ予想機能
端末から「python vipertools.py」と入力して起動して項目を選択する。

◇アニメーションSVG機能
端末から「python vipertools.py」と入力して起動して項目を選択する。

1.アニメーションSVGの作成する
TumblrなどでアニメーションGIFを公開しているケースが多いですが、256色の色制限などがあります。
ベクターグラフィックスのSVGには、パラパラアニメを実現する機能が搭載されています。
これを使って、アニメーションSVGを作ることが可能です。
このPythonスクリプトは、連番になっている画像ファイルを一つのフォルダにまとめておいて、コマンドでアニメーションSVGを生成するものです。
ファイルをダウンロードした後に、zipを解凍して、中に入っているスクリプトと画像フォルダを同じ場所に設置します。
使用する画像フォーマットはJPEGです。
このスクリプトの対応OSは、シェルスクリプトが使用出来るLinuxなどのUNIX系OSです。
ここでは画像フォルダを「test」とし、出力する画像サイズは640x480とします。
速度を変更したい場合は、３つ目の引数でアニメーションの実行時間を変更します。
ここでは5秒でアニメーションが終わるように設定しています。
コマンドは以下の通りです。

$python viper.py asvg test 640 480 5

これで同じディレクトリに「test.svg」が生成されます。

２．パラパラアニメのJavaScript付きのHTMLを生成する
ahtml.pyは、パラパラアニメを行なうJavaScript付きのHTMLを生成します。
asvg.pyでは、画像ファイルをBase64に変換してSVGの中に画像データを取り込んでいますが、ahtml.pyを使いますと、一つのHTMLと画像フォルダの組み合わせでパラパラアニメを実現することができ、アニメーションSVGよりも負荷が低くなっています。
３つ目の引数は、setIntervalの時間を設定します。これを変更することでアニメーション速度を変更出来ます。
ここでは50msに設定しています。
コマンドは以下の通りです。

$python viper.py ahtml test 640 480 50

ディレクトリに「test.html」が生成されます。

3.PNG画像を一括でJPEGにする
このモードは、複数のPNG画像を一括でJPEG画像に変換する物です。
ターミナルエミュレーターで以下のコマンドを使います。
ここでは、PNG画像をまとめたフォルダを「inputdir」、JPEG画像をまとめたフォルダを「outputdir」とします。
各フォルダはスクリプトと同じディレクトリに置いてください。

$python viper.py png2jpg inputdir outputdir 640 480 80

このコマンドの意味は、「inputdirに入っているPNG画像を一括で640x480の解像度・80%の圧縮率のJPEGに変換する」というものです。

4.JPEG画像を一括で回転させて保存する
このモードは、一括でJPEG画像を任意の角度に回転させる物です。
ターミナルエミュレーターで以下のコマンドを使います。
ここでは、JPEG画像をまとめたフォルダを「inputdir」とします。
各フォルダはスクリプトと同じディレクトリに置いてください。

$python viper.py rotatejpg inputdir -90

このコマンドの意味は、「inputdirに入っているJPEG画像を一括で-90度回転させて上書き保存する」というものです。

◇音声ファイルエンコード機能
この機能には、「MP3→AAC,Ogg Vorbis(mp3aac,mp3ogg)」、「AAC→MP3,Ogg Vorbis(aacmp3,aacogg)」、「Ogg Vorbis→MP3(oggmp3)」の５方式の音声ファイルのフォーマットやコンテナをエンコードする事が出来ます。
以下のコマンドを入力して使います。

$python viper.py mp3ogg xxx 128

上の例は、xxx.mp3というファイルをOgg Vorbisで作成したxxx.oggというファイルにビットレート128kbpsで変換する事が出来ます。
Pythonモジュールであるviper.pyの後に、モード・ファイル名（拡張子含まない）・ビットレートの順に指定していきます。

◇Waifu2Xを使用する
waifu2x.pyをベースにしたスクリプトが組み込まれており、画像を綺麗に拡大する事が可能になります。
使い方は、「Waifu2x」ボタンを押してアプリを起動させます。
入力ファイルと出力ファイルを記載し、Modelの項目には「scale2x」「noise1」「noise2」のいずれかを指定します。

◇リマスターしたLiveCDをQEmuでテストする。
リマスターしたLiveCDをQEmu上でテストするには、scriptsフォルダにある「qemu.sh」というスクリプトを使います。

$./qemu.sh xxxx

xxxxは、LiveCDのISOのパスを指定してください。
