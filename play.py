import pyaudio
import soundfile as sf
import threading

class WAVPlayer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.stream = None
        self.p = pyaudio.PyAudio()
        self.thread = None
        self.data, self.samplerate = sf.read(file_path, dtype='float32')

    def _play(self):
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=len(self.data.shape),
                                  rate=self.samplerate,
                                  output=True)
        self.stream.write(self.data.tobytes())
        self.stream.stop_stream()
        self.stream.close()
        self.stream = None

    def play(self):
        if self.stream is None and self.thread is None:
            self.thread = threading.Thread(target=self._play)
            self.thread.start()

    def stop(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
        if self.thread is not None:
            self.thread.join()
            self.thread = None

    def __del__(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()

    def get_duration(self):
        num_frames = self.data.shape[0]
        duration = num_frames / self.samplerate
        return duration
