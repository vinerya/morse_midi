from midiutil import MIDIFile
import random

def morse_to_midi(morse_code, output_file, tempo=180, base_pitch=60):
    """
    Convert Morse code to a MIDI file with a randomized melodic pattern in a minor scale.
    """
    midi = MIDIFile(1)  # One track
    midi.addTempo(0, 0, tempo)

    # A natural minor scale intervals
    minor_scale = [0, 2, 3, 5, 7, 8, 10]

    time = 0
    word_count = 0
    for word in morse_code.split('/'):
        # Generate a random melody for each word
        melody = [random.choice(minor_scale) for _ in range(4)]
        melody_index = 0
        
        for symbol in word.strip():
            if symbol == '.':
                duration = 1  # Short duration for dot
                pitch = base_pitch + melody[melody_index]
            elif symbol == '-':
                duration = 2  # Longer duration for dash
                pitch = base_pitch + melody[melody_index] + 7  # Add perfect fifth for variation
            else:  # space between letters
                time += 0.5
                melody_index = (melody_index + 1) % len(melody)
                continue

            midi.addNote(0, 0, pitch, time, duration, 100)
            time += duration + 0.25  # Add a short pause between symbols
            melody_index = (melody_index + 1) % len(melody)

        time += 1  # Pause between words
        word_count += 1

    with open(output_file, "wb") as output_file:
        midi.writeFile(output_file)

    return word_count