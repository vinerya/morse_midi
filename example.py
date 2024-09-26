from morse_midi import string_to_morse_midi

# Example 1: Default settings (180 BPM, minor scale, randomized melody)
input_string = "Hello World"
output_file = "hello_world.mid"
morse_code, word_count = string_to_morse_midi(input_string, output_file)

# Example 2: Custom tempo and base pitch
input_string = "SOS This is a test"
output_file = "sos_test.mid"
morse_code, word_count = string_to_morse_midi(input_string, output_file, tempo=200, base_pitch=72)

print("\nExample 2:")
print(f"Morse code MIDI file created: {output_file}")
print(f"Morse code: {morse_code}")
print(f"Number of words: {word_count}")

# Example 3: Demonstrating randomized melody
print("\nExample 3 (Demonstrating randomized melody):")
for i in range(3):
    output_file = f"random_melody_{i+1}.mid"
    morse_code, word_count = string_to_morse_midi("Random Melody Test", output_file)
    print(f"Created: {output_file}")