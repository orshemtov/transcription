from typing import BinaryIO, Iterable, Literal

from faster_whisper import WhisperModel
from faster_whisper.transcribe import Segment, TranscriptionInfo


class TranscriptionService:
    def __init__(
        self,
        model: Literal["small", "medium", "large-v3"],
        device: Literal["cpu", "cuda"],
        compute_type: Literal["int8", "float16"],
        beam_size: int = 5,
    ):
        self.model = WhisperModel(model, device=device, compute_type=compute_type)
        self.beam_size = beam_size

    def transcribe_audio(self, audio: BinaryIO) -> tuple[TranscriptionInfo, Iterable[Segment]]:
        segments, info = self.model.transcribe(
            audio,
            beam_size=self.beam_size,
        )
        return info, segments
