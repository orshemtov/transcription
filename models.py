from pydantic import BaseModel


class MetadataResponse(BaseModel):
    duration: float
    language: str
    language_probability: float


class SegmentResponse(BaseModel):
    start: float
    end: float
    text: str


class TranscriptionResponse(BaseModel):
    metadata: MetadataResponse
    segments: list[SegmentResponse]
