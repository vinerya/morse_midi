from .morse_encoder import encode_to_morse
from .midi_generator import morse_to_midi

def string_to_morse_midi(input_string, output_file, tempo=180, base_pitch=60):
    """
    Convert a string to Morse code and then to a melodic MIDI file.
    """
    morse_code = encode_to_morse(input_string)
    word_count = morse_to_midi(morse_code, output_file, tempo, base_pitch)
    print(f"Morse code MIDI file created: {output_file}")
    print(f"Morse code: {morse_code}")
    print(f"Number of words: {word_count}")
    return morse_code, word_count