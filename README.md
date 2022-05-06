# pyseTransFree
a language translating program by using DeepL/Google Translate engine (python &amp; selenium)

For example, using DeepL.com translating service to translate a text file which writing in English language to Chinese language, we just need to specify the input text file by '-f' and the output file path by '-o'.

Checkout the *deepl.cfg* and *deepl-jp2zh.cfg* files. What you should change is the 'from' and 'to' language tags. 

> usage:
> 
> $ pip install webdriver-manager
> 
> $ python pyseDeepL.py -c deepl.cfg -f ~/Documents/text-in-en.txt -o ~/Documents/text-in-zh.txt

Now, it only supports DeepL.com and TXT file format. 

Maybe Google Translate and EPUB supports will come later.
