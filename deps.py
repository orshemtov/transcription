from typing import Annotated

from fastapi import Depends

from service import TranscriptionService
from settings import settings


def get_transcription_service() -> TranscriptionService:
    return TranscriptionService(settings.model, settings.device, settings.compute_type)


TranscriptionServiceDep = Annotated[TranscriptionService, Depends(get_transcription_service)]
