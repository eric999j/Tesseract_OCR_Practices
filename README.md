# Tesseract_OCR_Practices
references:https://www.jianshu.com/p/2c9459059400  

# 流程說明：  
這是一個Google OCR套件Tesseract試驗  
在MacOS Mojave 10.14.4/Spyder/Python3.7環境  
brew install tesseract  
pip install pytesseract  
https://github.com/tesseract-ocr/tessdata  
的繁體中文字集chi_tra.traineddata  
置於/usr/local/Cellar/tesseract/4.0.0_1/share/tessdata/  
識別https://thestandnews.com/art/%E7%82%BA%E7%94%9A%E9%BA%BC%E4%B8%8D%E6%8E%A8%E8%96%A6%E6%96%B0%E7%B4%B0%E6%98%8E%E9%AB%94/ 
新細明體字樣圖片，命名為string.png  
得到以下結果  
runfile('/Users/yumei/ocr.py', wdir='/Users/yumei')
念 春

 

 

斧 紡

 

月 阡
並無識別出“新細明體”字樣，由於圖片結構簡潔，排除需要銳化或其他可能，但繁體中文識別不理想  
英文試試  
使用預設英文字集eng.traineddata	
命名為engString.jpg   
得到以下結果  
runfile('/Users/yumei/ocr.py', wdir='/Users/yumei')
Core Developers.

The core developer on the project is Ray Smith (theraysmith). .
Thomas Breuel (tmbdev) and Ilya Mezhirov (mezhirov) work on the
OCRopus project, for which Tesseract is one of the pluggable OCR
engines; OCRopus also provides layout analysis and statistical language
modeling. -

Most of the work on Tesseract is sponsored by Google. -

Migration.  
看來對英文字集支援較佳  
  
