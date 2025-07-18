# ChatterKiller for NVDA 2025.2+ and later, boundary suppression only

import addonHandler
import globalPluginHandler
import speech
import tones
#import logging
from logHandler import log
from scriptHandler import script
addonHandler.initTranslation()

TONE_LEFT = (330, 65, 45, 0)
TONE_RIGHT = (330, 65, 0, 45)
TONE_NO_PREVIOUS = (330, 65, 45, 0)
TONE_NO_NEXT = (330, 65, 0, 45)
TONE_NO_PARENT = (262, 60, 45, 45)
TONE_NO_CHILD = (131, 60, 45, 45)
TONE_AT_TOP = (880, 65, 45, 45)
TONE_AT_BOTTOM = (440, 65, 45, 45)

BOUNDARY_MESSAGES = {
	"Left": TONE_LEFT,
	"Right": TONE_RIGHT,
	"Top": TONE_AT_TOP,
	"Bottom": TONE_AT_BOTTOM,
	"No previous": TONE_NO_PREVIOUS,
	"No next": TONE_NO_NEXT,
	"No containing object": TONE_NO_PARENT,
	"No objects inside": TONE_NO_CHILD,
}

def is_boundary_message(sequence):
	# Only true if: a single string, exactly matching one of the boundary messages (case-sensitive)
	return (
		isinstance(sequence, (list, tuple))
		and len(sequence) == 1
		and isinstance(sequence[0], str)
		and sequence[0] in BOUNDARY_MESSAGES
	)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = _("Chatter Killer")
	chatterKillerEnabled = True

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._patchSpeech()
		#logging.info("Chatter Killer loaded and speech patched for NVDA 2025.2+.")
		log.info("Chatter Killer loaded and speech patched for NVDA 2025.2+.")

	def _patchSpeech(self):
		if hasattr(speech, "speech"):
			self._origSpeak = speech.speech.speak
			speech.speech.speak = self._chatterKillerSpeak
		else:
			self._origSpeak = speech.speak
			speech.speak = self._chatterKillerSpeak

	def _restoreSpeech(self):
		if hasattr(self, "_origSpeak"):
			if hasattr(speech, "speech"):
				speech.speech.speak = self._origSpeak
			else:
				speech.speak = self._origSpeak

	@script(
		description=_("Toggles ChatterKiller on or off. Assign NVDA+Shift+C to this in Input Gestures."),
		category=_("Chatter Killer"),
	)
	def script_toggleChatterKiller(self, gesture):
		self.chatterKillerEnabled = not self.chatterKillerEnabled
		state = _("enabled") if self.chatterKillerEnabled else _("disabled")
		tones.beep(880 if self.chatterKillerEnabled else 220, 50, 45, 45)
		self._origSpeak([_("Chatter Killer {state}").format(state=state)])

	def _chatterKillerSpeak(self, sequence, *args, **kwargs):
		if self.chatterKillerEnabled and is_boundary_message(sequence):
			msg = sequence[0]
			tone = BOUNDARY_MESSAGES[msg]
			tones.beep(*tone)
			speech.cancelSpeech()
			#logging.debug(f"Chatter Killer: Suppressed '{msg}', played tone.")
			log.debug(f"Chatter Killer: Suppressed '{msg}', played tone.")
			return  # Suppress speech entirely for this message
		self._origSpeak(sequence, *args, **kwargs)

	def terminate(self, *args, **kwargs):
		self._restoreSpeech()
		#logging.info("Chatter Killer: Unpatched speech.")
		log.info("Chatter Killer: Unpatched speech.")
