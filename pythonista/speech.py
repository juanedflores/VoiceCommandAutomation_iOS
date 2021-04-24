
import speech
import time
import sound
import dialogs
import sys
import clipboard
import webbrowser


def finish_speaking():
    while speech.is_speaking():
        time.sleep(0.5)


def getSpeech():
    # Record an audio file using sound.Recorder:
    recorder = sound.Recorder('speech.m4a')
    recorder.record()
    # Record for 3 seconds
    for i in range(3):
        sound.play_effect('game:Beep')
        time.sleep(1)

    # Stop recording
    recorder.stop()
    time.sleep(1)

    result = 'no speech detected'
    try:
        speechDetect = speech.recognize('speech.m4a')
        result = speechDetect[0][0]
        #print('=== Details ===')
        # print(result)
        #print('=== Transcription ===')
        # print(result[0][0])
    except RuntimeError as e:
        print('Speech recognition failed: %s' % (e,))
        sound.play_effect('game:Error')

    return result


# get words detected and set to clipboard.
r = getSpeech()
clipboard.set(r)

url = "shortcuts://x-callback-url/run-shortcut?name=SSH&input=clipboard"

if (r.split()[0] == 'Open'):

    if (r.split()[1] == 'website'):
        appStrig = 'website'
        clipboard.set(appString)

    if (r.split()[1] == 'radio'):
        appString = 'radio'
        clipboard.set(appString)

    if (r.split()[1] == 'PECO'):
        appString = 'pico'
        clipboard.set(appString)

    url = "shortcuts://x-callback-url/run-shortcut?name=SSH_Open&input=clipboard"

elif (r.split()[0] == 'Task'):
    #taskName = r.split()[1]
    taskName = r.split('Task', 1)[1]
    allCaps = taskName.upper()
    clipboard.set(allCaps)

    url = "shortcuts://x-callback-url/run-shortcut?name=Start_Task&input=clipboard"


elif (r == 'Play'):
    url = "shortcuts://x-callback-url/run-shortcut?name=SSH_Play"

webbrowser.open(url)n
