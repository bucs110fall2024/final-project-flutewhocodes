import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play
import threading

class Audio:
    def __init__(self):
        """
        initializes the sound
        
        args: none
        
        """
        self.file_path = None
        self.recording = False
        self.frames = []
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.backing_track = None
        self.output_file_path = None

    def select_file(self, file_path):
        """
        determines file path for the recording
        args: file_path
        return: file_path
        """
        self.file_path = file_path
        return self.file_path

    def set_output_file(self, output_file_path):
        """
        sets up output file path
        args: output_file_path
        return: none
        """
        self.output_file_path = output_file_path

    def start_recording1(self):
        """
        starts the first recording
        opens up pyaudio
        args: none
        return: none
        """
        self.frames = []
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        self.recording = True
        threading.Thread(target=self.record_audio).start()
        
    def start_recording2(self):
        """
        starts the second recording
        opens up pyaudio
        threads the backing track
        args: none
        return: none
        """
        self.frames = []
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        self.recording = True
        threading.Thread(target=self.record_audio).start()
        threading.Thread(target=self.play_backing_track).start()

    def stop_recording1(self):
        """
        stops the first recording
        puts first recording to recorded_audio1.wav
        args: none
        return: none
        """
        self.recording = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        wf = wave.open("recorded_audio1.wav", 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        
    def stop_recording2(self):
        """
        stops the second recording
        puts second recording to recorded_audio2.wav
        args: none
        return: none
        """
        self.recording = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        wf = wave.open("recorded_audio2.wav", 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def record_audio(self):
        """
        records audio
        args: none
        return: none
        """
        while self.recording:
            data = self.stream.read(1024)
            self.frames.append(data)

    def play_backing_track(self):
        """
        plays the backing track while second recording happens
        args: none
        return: none
        """
        if self.file_path:
            self.backing_track = AudioSegment.from_wav(self.file_path)
            play(self.backing_track)

    def overlay_audio(self):
        """
        overlays second recording with selected wave file
        args: none
        return: None
        """
        
        if self.file_path and "recorded_audio2.wav" and self.output_file_path:
            original_audio = AudioSegment.from_wav(self.file_path)
            recorded_audio = AudioSegment.from_wav("recorded_audio2.wav")
            combined = original_audio.overlay(recorded_audio)
            combined.export(self.output_file_path, format='wav')
            return self.output_file_path
        return None
        
    