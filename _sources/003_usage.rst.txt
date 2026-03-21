.. _tutorial:

チュートリアル
##############

1. ゲームプロジェクトを解析する
----------------------------

.. image:: img/langscore_exe.gif

Langscore.exeを開いて、ゲームプロジェクトの *フォルダ* をドラッグアンドドロップします。

ゲームプロジェクトのフォルダは、rvproj2(VXAce) rpgproject(MV) rmmzproject(MZ) があるフォルダを指します。

「解析」ボタンを押すことで、ゲーム内で使用されているテキスト等の解析を始めます。

.. warning:: 
    | **Ver.0.8.0ではドラッグ・アンド・ドロップするフォルダのパスに空白文字が含まれていると、正しく解析できません。**
    | NG)C:\\Users\\Documents\\Game Projects\\MyGame
    | OK)C:\\Users\\Documents\\GameProjects\\MyGame
    | お手数ですがフォルダ名に空白を含んでいる場合、フォルダ名を変える等で対応してください。


2. 対応する言語を選ぶ
---------------------------------


正しく解析できた場合、画面が切り替わります。

「言語」タブを選び、対応したい言語を選択してください。

.. image:: img/usage1.png

3. 翻訳ファイルを書き出す
--------------------------------

ツール下部にある「翻訳CSVの書き出し」を押すと、指定したフォルダにCSVファイルを書き出します。
書き出しが完了すると、書き出し先のフォルダが自動で表示されます。

.. image:: img/edit_mode9.png

書き出されたこれらのCSVファイルを、翻訳者に渡してください。

.. image:: img/edit_mode6.png



4. 翻訳したCSVファイルを所定の場所に置く
------------------------------------------

翻訳したCSVファイルは、ゲームプロジェクトの以下の場所に置いてください。

* VXAce : Data/Translate

.. image:: img/edit_mode7.png

    
* MV/MZ : data/translates

.. image:: img/edit_mode8.png


5. ゲーム中で言語を切り替える
---------------------------------

VX Aceの場合
~~~~~~~~~~~~

スクリプト中のLangscore.changeLanguage(lang)関数に、言語文字列を指定して呼び出してください。

.. image:: img/script_usage_ex.png

また、言語選択メニュークラス"Scene_Language"を用意しています。
こちらも用途に応じてご利用ください。


MV/MZの場合
~~~~~~~~~~~~

プラグインコマンドに Langscore changeLanguage (言語文字列) を指定してください

.. image:: img/script_usage_ex_mvmz.png
