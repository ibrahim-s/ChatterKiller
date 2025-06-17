# NVDA Add-on: ChatterKiller
# 'Shush the sheesh' on boundary alerts!
#No speech, please?
# Copyright (C) 2025 [Jason Bratcher]
# License: GNU General Public License (version 2) - See LICENSE file for details

import addonHandler
import api
import globalPluginHandler
import speech
import tones  # Replaced import audio with import tones
import log
import text
from scriptHandler import script

addonHandler.initTranslation()

# --- Tone Definitions ---
# Customize these values (frequency in Hz, duration in milliseconds, and left+right volumes in percentage from 0 to 100)
# First four tone statements are hard panned to show that navigation is not possible beyond those points.
TONE_LEFT = (330, 50, 45, 0)
TONE_RIGHT = (330, 50, 0, 45)
TONE_NO_PREVIOUS = (330, 65, 45, 0)
TONE_NO_NEXT = (330, 65, 0, 45)
TONE_NO_PARENT = (262, 60, 45, 45)
TONE_NO_CHILD = (131, 60, 45, 45)
TONE_AT_LINE_START = (440, 65, 45, 45)
TONE_AT_LINE_END = (220, 65, 45, 45)
TONE_AT_DOC_TOP = (880, 65, 45, 45)
TONE_AT_DOC_BOTTOM = (440, 65, 45, 45)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    # Translators: script category for add-on gestures (Shown in Input Gestures dialog of NVDA).
    scriptCategory = _("Chatter Killer")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        log.debug("Chatter Killer: Got code? Let's go!")
# This just confirms we got in on the ground floor.
tones.beep(440, 55, 30, 30)
tones.beep(220, 55, 30, 30)

        # After this point, all Hell (or is that Heaven) should break loose - if it works, that is!
        self.original_scripts = {
            "home": globalPluginHandler.GlobalPlugin.script_home,
            "end": globalPluginHandler.GlobalPlugin.script_end,
            "pageUp": globalPluginHandler.GlobalPlugin.script_pageUp,
            "pageDown": globalPluginHandler.GlobalPlugin.script_pageDown,
"review_currentObject": globalPluginHandler.GlobalPlugin.script_review_currentObject,
        "review_previousObject": globalPluginHandler.GlobalPlugin.script_review_previousObject,
            "review_nextObject": globalPluginHandler.GlobalPlugin.script_review_nextObject,
"review_top": globalPluginHandler.GlobalPlugin.script_review_top,
            "review_bottom": globalPluginHandler.GlobalPlugin.script_review_bottom,
"review_parent": globalPluginHandler.GlobalPlugin.script_review_parent,
            "review_firstChild": globalPluginHandler.GlobalPlugin.script_review_firstChild,
"review_lastChild": globalPluginHandler.GlobalPlugin.script_review_lastChild,
            

    def _play_tone_and_silence(self, tone_tuple):
        frequency, duration = tone_tuple
        tones.beep(frequency, duration, 30, 30)  # Replaced audio.beep with tones.beep and added volumes
        speech.cancelSpeech()
        log.debug(f"Chatter Killer: Played tone {frequency} Hz, {duration} ms and silenced speech.")

    def script_home(self, gesture):
        caret = api.getCaret()
        if caret and caret.isStartOfLine:
            self._play_tone_and_silence(TONE_AT_LINE_START)
            return True
        return self.original_scripts["home"](gesture)

    def script_end(self, gesture):
        caret = api.getCaret()
        if caret and caret.isEndOfLine:
            self._play_tone_and_silence(TONE_AT_LINE_END)
            return True
        return self.original_scripts["end"](gesture)

    def script_pageUp(self, gesture):
        caret = api.getCaret()
        if caret and caret.isStartOfDocument:
            self._play_tone_and_silence(TONE_AT_DOC_TOP)
            return True
        return self.original_scripts["pageUp"](gesture)

    def script_pageDown(self, gesture):
        caret = api.getCaret()
        if caret and caret.isEndOfDocument:
            self._play_tone_and_silence(TONE_AT_DOC_BOTTOM)
            return True
        return self.original_scripts["pageDown"](gesture)

    def script_review_previousObject(self, gesture):
        current_obj = api.getReviewObject()
        if current_obj is None or current_obj.previous is None:
            self._play_tone_and_silence(TONE_NO_PREVIOUS)
            return True
        return self.original_scripts["review_previousObject"](gesture)

    def script_review_nextObject(self, gesture):
        current_obj = api.getReviewObject()
        if current_obj is None or current_obj.next is None:
            self._play_tone_and_silence(TONE_NO_NEXT)
            return True
        return self.original_scripts["review_nextObject"](gesture)

    def script_review_parent(self, gesture):
        current_obj = api.getReviewObject()
        if current_obj is None or current_obj.parent is None:
            self._play_tone_and_silence(TONE_NO_PARENT)
            return True
        return self.original_scripts["review_parent"](gesture)

    def script_review_firstChild(self, gesture):
        current_obj = api.getReviewObject()
        if current_obj and current_obj.firstChild is None:
            self._play_tone_and_silence(TONE_NO_CHILD)
            return True
        return self.original_scripts["review_firstChild"](gesture)

    def script_review_lastChild(self, gesture):
        current_obj = api.getReviewObject()
        if current_obj and current_obj.lastChild is None:
            self._play_tone_and_silence(TONE_NO_CHILD)
            return True
        return self.original_scripts["review_lastChild"](gesture)

    def script_review_top(self, gesture):
        review_position = api.getReviewPosition()
        if review_position.isStart:
            self._play_tone_and_silence(TONE_AT_DOC_TOP)
            return True
        return self.original_scripts["review_top"](gesture)

    def script_review_bottom(self, gesture):
        review_position = api.getReviewPosition()
        if review_position.isEnd:
            self._play_tone_and_silence(TONE_AT_DOC_BOTTOM)
            return True
        return self.original_scripts["review_bottom"](gesture)

    def script_review_currentObject(self, gesture):
        return self.original_scripts["review_currentObject"](gesture)

    def terminate(self):
        log.debug("Chatter Killer: Back to normal.")
        pass

# No settings panel is included in this version;
# Edit this file directly to change behaviors/conditions.