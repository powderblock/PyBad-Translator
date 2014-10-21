from translate import Translator
import random
text = str(raw_input("Enter the text you want to translate: "))
startText = text
endText = text
numberOfTranslations = int(raw_input("Enter the number of times you want to run over the translations: "))
# List of all supported langauges:
langs = ["af", "ach", "ak", "am", "ar", "az", "be", "bem", "bg", "bh", "bn", "br", "bs", "ca", "chr", "ckb", "co", "crs", "cs", "cy", "da", "de", "ee", "el", "en", "eo", "es", "es-419", "et", "eu", "fa", "fi", "fo", "fr", "fy", "ga", "gaa", "gd", "gl", "gn", "gu", "ha", "haw", "hi", "hr", "ht", "hu", "hy", "ia", "id", "ig", "is", "it", "iw", "ja", "jw", "ka", "kg", "kk", "km", "kn", "ko", "kri", "ku", "ky", "la", "lg", "ln", "lo", "loz", "lt", "lua", "lv", "mfe", "mg", "mi", "mk", "ml", "mn", "mo", "mr", "ms", "mt", "ne", "nl", "nn", "no", "nso", "ny", "nyn", "oc", "om", "or", "pa", "pcm", "pl", "ps", "pt-BR", "pt-PT", "qu", "rm", "rn", "ro", "ru", "rw", "sd", "sh", "si", "sk", "sl", "sn", "so", "sq", "sr", "sr-ME", "st", "su", "sv", "sw", "ta", "te", "tg", "th", "ti", "tk", "tl", "tn", "to", "tr", "tt", "tum", "tw", "ug", "uk", "ur", "uz", "vi", "wo", "xh", "xx-bork", "xx-elmer", "xx-hacker", "xx-klingon", "xx-pirate", "yi", "yo", "zh-CN", "zh-TW","zu"]
print startText
for i in range(0, numberOfTranslations):
    # Language (element number in langs) we are going to use for translations
    lang = random.randint(0, len(langs))
    # Set up the language we are going to translate TO:
    translator = Translator(to_lang=langs[lang])
    # Set up the language we are going to translate From:
    translator2 = Translator(to_lang="en")
    # Phrase we want to translate:
    translation = translator.translate(endText.encode('utf-8'))
    # Print what the translation is at first run:
    # Actually do the translation:
    # (utf-8 so it doesn't break between langs)
    translation2 = translator2.translate(translation.encode('utf-8'))
    # Print what the translation is at final run:
    endText = translation2
print endText
print(str(numberOfTranslations)+" translations later gives us: '"+endText+"' From: '"+startText+"'")
