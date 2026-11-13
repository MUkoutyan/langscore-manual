.. _points_to_note:

アプリとスクリプトにおける注意点
################################



競合する可能性のあるスクリプト
------------------------------

Langscoreでは下記の処理または、関数の処理を上書きしています。

他のスクリプトが同様の事を行っていた場合、Langscoreの処理と競合する可能性があります。

リアルタイム編集用のプラグイン Langscore_RemoteHub を追加した場合は、「Langscore_RemoteHub」の項目の処理も上書きされます。
Langscore_RemoteHubはテストプレイ中にだけ動作するため、通常のプレイでは上書きしません。

VX Ace
^^^^^^^^^^^^^^^^^^^^^^^

* Game_Map.setup
* Window_Base.convert_escape_characters
* Window_Base.draw_text
* DataManager.load_normal_database (eval)
* DataManager.make_save_contents (eval)
* Cache.load_bitmap (eval)
* フォントの変更

MV/MZ
^^^^^^^^^^^^^^^^^^^^^^^

* Window_Base.convertEscapeCharacters
* Window_Base.standardFontFace
* Window_Base.standardFontSize
* DataManager.loadDatabase
* DataManager.loadMapData
* DataManager.isDatabaseLoaded
* DataManager.makeSaveContents
* DataManager.extractSaveContents
* Game_System.prototype.isJapanese
* Game_System.prototype.isChinese
* Game_System.prototype.isKorean
* Game_System.prototype.isCJK
* Game_System.prototype.isRussian
* ImageManager.loadBitmap
* フォントの変更

Langscore_RemoteHub
^^^^^^^^^^^^^^^^^^^^^^^

**VX Ace**

* Langscore.translate
* Window_Base.convert_escape_characters
* Window_ChoiceList.select
* Window_Message.process_all_text
* Scene_Base.update

**MV/MZ**

* Langscore.translate
* Window_Base.convertEscapeCharacters
* Window_ChoiceList.select
* Window_Message.startMessage
* Scene_Base.update




各ソフトのMD5値
-----------------------

Powershellやハッシュ値比較ソフトでMD5の比較を行う際に利用してください。

