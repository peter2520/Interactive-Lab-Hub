#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2

say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say "How many pets do you have?"

arecord -D hw:1,0 -f cd -c1 -r 44100 -d 5 -t wav recorded_mono.wav
python3 test_words.py recorded_mono.wav
