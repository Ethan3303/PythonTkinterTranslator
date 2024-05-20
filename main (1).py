#importing tkinter so I can use the commands to make the entire window
import tkinter
#tkinter as tk for abreviation
import tkinter as tk
#imported ttk so that i could use the commands to create the combobox
from tkinter import ttk
#from deep_translator I imported GoogleTranslator so that I could translate the text
from deep_translator import GoogleTranslator

# Create a window whilst also applying tk
window = tk.Tk()
#applying the window title to the top of the window
window.title("Translator")
#applying the width and height to the window using geometry 
window.geometry("500x400")

#here i applied a dark red to the background of the page by using the config function to set the background (bg) to red 4
windowcolour="red4"
window.config(bg=windowcolour)

#I made this label to make it more obisous as to wherw the user would need to input their text that they wanted to translate
tk.Label(window, text="Input Text Here:", bg="gray40").grid(row=1, column=1, pady=25)

#This is the box that you are able to input text into, tanslation input is shortened to transinput
transinput=tk.Entry(window, width=50)
transinput.grid(padx=50, pady=25, row=2, column=1)

#This is the def i used to translate the text that the user has inputed into the transinput box
def translate():
  #text1 will get the text that the user has inputed into the transinput box
  text1=transinput.get()
  #selectlan will get the language that the user has selected from the dropdown menu
  selectlan=sellang.get()
  #text 2 uses googletranslator to translate the text that the user has inputed into the transinput box and the source being auto means it will auto detect what language has been chosen and then the translate function will be used to translate text1 into the selected language.
  text2=GoogleTranslator(source="auto", target=selectlan).translate(text1)
  
  translated.config(text=text2)

#Here is every language that the translator is either able to translate to or translate from
langopts={'afrikaans': 'af', 'albanian': 'sq', 'arabic': 'ar', 'armenian': 'hy', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'javanese': 'jw', 'kazakh': 'kk', 'kinyarwanda': 'rw', 'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'maltese': 'mt', 'maori': 'mi', 'mizo': 'lus', 'mongolian': 'mn', 'norwegian': 'no', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tatar': 'tt',  'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

#This is the dropdown menu that the user can choose from to translate from
sellang=tk.StringVar(window)
#This makes it so that the select a langauge text shows up rather than just the langauges
sellang.set("Select A Language")

#Using combobox i was able to make the languages appear on a scrollable dropdwon menu making the selection process easier.
#textvariable displays the text onto the menu
#with the values being a list can display the languages that the user can choose from without any issues which i had with optionMenu on my initial attempt
#the langopts variable geta the list of languages that the translator is able to translate.
#keys() displays the actual language names rather than the language codes
options= ttk.Combobox(window, textvariable = sellang, values=list(langopts.keys()))
options.grid(row=3, column=1)

#This is the button that the user can click to translate the text that they have inputed into the transinput with different colours to make it more obvious to the user that the button is a translation button
button=tk.Button(window, text="Translate", command=translate, width=10, height=2, bg="gray40").grid(row=4, column=1,pady=30)

#This is the label that the user will see when they click the translate button and will display the translated text
translated = tk.Label(window, width=50, bg="gray40")
translated.grid(row=6, column=1, pady=10)

#This is the end of the window and keeps it running till the program is ended manually
window.mainloop()
