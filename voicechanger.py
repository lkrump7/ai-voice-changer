import librosa
import soundfile as sf
import numpy as np

def change_voice(input_audio, output_audio, pitch_shift=2.0, speed_factor=1.0):
    """
    Change the voice in an audio file by altering pitch and speed.
    
    Parameters:
    - input_audio: Path to input audio file (MP3, WAV, etc.).
    - output_audio: Path to save the modified audio.
    - pitch_shift: Number of semitones to shift (positive for higher, negative for lower).
    - speed_factor: Speed change (greater than 1 = faster, less than 1 = slower).
    """
    # Load the audio file
    y, sr = librosa.load(input_audio, sr=None)
    
    # Pitch shifting
    y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=pitch_shift)
    
    # Speed alteration
    y_shifted = librosa.effects.time_stretch(y_shifted, speed_factor)
    
    # Save the modified audio
    sf.write(output_audio, y_shifted, sr)
    print(f"Voice changed and saved to '{output_audio}'")

# Example usage:
input_file = 'input_voice.mp3'  # Path to your input MP3
output_file = 'output_voice.wav'  # Path to save the modified output
change_voice(input_file, output_file, pitch_shift=4.0, speed_factor=1.2)  # Increase pitch and speed slightly