midi_notes = {
	'note_48': 0,
	'note_49': 1,
	'note_50': 2,
	'note_51': 3,
	'note_52': 4,
	'note_53': 5,
}

def midiTrigger(channel):
	note_played = channel.rsplit('/',1)[1]
	if note_played in midi_notes:
		print("Code working!")
		print(midi_notes[note_played])
	else:
		print("Code not working!")


midiTrigger('midi/t45/TdaMIDI/ch1/note_52')
