from translate import Translator

translator= Translator(to_lang="en")
translation = translator.translate("Me encanta comer pastel.")

print(translation)