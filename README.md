# Morse MIDI

This Python package encodes a string input to Morse code and then converts it to a melodic MIDI file using a minor scale with randomized melodies.

## Features

- Converts text to Morse code
- Generates melodic MIDI files from Morse code using a natural minor scale
- Randomized melody for each input, making each generation unique
- Default tempo of 180 BPM for a more upbeat sound
- Customizable tempo and base pitch

## Installation

You can install this package using pip:

```
pip install morse_midi
```

For local development, you can install it in editable mode:

```
pip install -e .
```

## Usage

Here's a simple example of how to use the package:

```python
from morse_midi import string_to_morse_midi

input_string = "Hello World"
output_file = "hello_world.mid"

morse_code, word_count = string_to_morse_midi(input_string, output_file)
```

This will create a MIDI file named "hello_world.mid" in your current directory, containing a melodic representation of the Morse code for "Hello World" using a randomized melody in a minor scale.

You can also customize the tempo and base pitch:

```python
morse_code, word_count = string_to_morse_midi(
    "SOS This is a test",
    "sos_test.mid",
    tempo=200,
    base_pitch=72
)
```

## Melodic Pattern

The MIDI output uses the following characteristics:

- Uses a natural minor scale for a more somber sound
- Generates a random melody for each word, making each output unique
- Dots are represented by short notes
- Dashes are represented by longer notes
- Each word starts a new random melody
- Dashes are played as a perfect fifth above the corresponding dot pitch
- Default tempo is set to 180 BPM for a more upbeat sound

## Dependencies

This package requires the `midiutil` library, which will be automatically installed when you install this package using pip.

## License

This project is licensed under the MIT License.