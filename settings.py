from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model: Literal["small", "medium", "large-v3"] = "small"
    device: Literal["cpu", "cuda"] = "cpu"
    compute_type: Literal["int8", "float16"] = "int8"


settings = Settings()
