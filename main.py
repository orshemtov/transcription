from fastapi import FastAPI, UploadFile

from deps import TranscriptionServiceDep
from models import MetadataResponse, SegmentResponse, TranscriptionResponse

app = FastAPI()


@app.post("/transcribe")
async def transcribe(file: UploadFile, service: TranscriptionServiceDep):
    info, segments = service.transcribe_audio(file.file)
    return TranscriptionResponse(
        metadata=MetadataResponse(
            duration=info.duration,
            language=info.language,
            language_probability=info.language_probability,
        ),
        segments=[
            SegmentResponse(
                start=segment.start,
                end=segment.end,
                text=segment.text,
            )
            for segment in segments
        ],
    )
