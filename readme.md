# Chatter Killer
My name's Jason Bratcher from Valrico, Florida, U.S.A.
(some of you others know me by my Mastodon id @BlindHedgehogStew@c.Im -
that's where I 'toot' with the best of the ancient elephants (granted I tend to share more content).
My job is to quietly keep NVDA from saying phrases like
'left' 'right',
'top' 'bottom',
'no previous' 'no next',
'no containing object' 'no objects inside'.
I was put here to replace NVDA's spoken object review boundary messages with tones.
The tone statements go as follows:
(For All Statements the '0' indicates a silent channel
(Meaning you can't go back any further)).
(First 4 statements still  announce the character/word/line at the boundary point).
TONE_LEFT = (330, 65, 45, 0)
TONE_RIGHT = (330, 65, 0, 45)
TONE_AT_TOP = (880, 65, 45, 45)
TONE_AT_BOTTOM = (440, 65, 45, 45)
(Last 4 statements follow NVDA's convention of Not Announcing the item you're on, hence they'll be silent).
TONE_NO_PREVIOUS = (330, 65, 45, 0)
TONE_NO_NEXT = (330, 65, 0, 45)
TONE_NO_PARENT = (262, 60, 45, 45)
TONE_NO_CHILD = (131, 60, 45, 45)
With that out of the way, onward!
GettingStarted:
1. Download+install as any other addon (this is an external install Not a Store submission
hence you'll see 'external' showing as the source).
2. Go to the NVDA Input gestures and locate the ChatterKiller branch
(one unassigned keystroke is here - to toggle the addon on or off;
Assign a keystroke to this (like NVDA+Shift+c).
3. OKay the dialog.
4. Tap the assigned keystroke so the addon is enabled
(on second thought it may Be Enabled outright so hence begins the quality of life improvement)?
Now start object navigating/review cursor with the extended NumPad (Desktop) or the alternate (laptop) commands.
If working right, tones play to indicate the boundaries of the dimensions of navigation via object navigation/review cursor.
My work is done here;
You can so totally edit the __init__.py file to change the numeric values for the pitch, duration, left channel volume and right channel volume so you don't have to use hard panning;
Some people process partial panning possibly better than a true hard pan (which is what I initially planned on for proof of concept.
TONE_LEFT = (220, 55, 42, 14)
TONE_RIGHT = (220, 55, 14, 42)
TONE_NO_PREVIOUS = (220, 75, 42, 14)
TONE_NO_NEXT = (220, 75, 14, 42)
These statements enforce partial panning and a slightly longer tone for NVDA+NumPad4/6 (or the Laptop equivalent) indicating no previous/further objects are available.
([{HugeNoteToSelf:
This won't stop the 'hanging' issue that happens when NVDA works with some programs where their code hasn't been optimized correctly,
With those programs you'll try to go to the previous or next object if you're already at the end of the sibblings and NVDA just goes quiet without saying a word.
Properly optimized programs Won't Do that behavior}])!
They will offer speedy object navigation especially on the Ultimate Performance power plan!
AnyWho I hope you have a YabbaDabbaDoo time with this.
Best wishes;
Jason A. Bratcher
ImCoocoo@GMail.Com
@BlindHedgehogStew@C.Im
