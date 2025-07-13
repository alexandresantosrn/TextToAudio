from gtts import gTTS

texto = """
— Che, boludo, ¿viste a la mina nueva del laburo?
— Sí, re copada. Además, tiene alta facha.
— Ayer fuimos a morfar algo y pagamos por un pomelo.
— ¡Posta! Qué quilombo que fue el bar igual.
— Sí, pero el chabón del lugar tenía mucho chamuyo.
"""

tts = gTTS(text=texto, lang='es', tld='com.ar')
tts.save("dialogo_argentino.mp3")

