"""Configuration for Real-time Meeting Assistant"""
import os
from dataclasses import dataclass

@dataclass
class LiveKitConfig:
    url: str = os.getenv("LIVEKIT_URL", "ws://localhost:7880")
    api_key: str = os.getenv("LIVEKIT_API_KEY", "devkey")
    api_secret: str = os.getenv("LIVEKIT_API_SECRET", "secret")

@dataclass
class OpenAIConfig:
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    model: str = "gpt-4-turbo-preview"
    stt_model: str = "whisper-1"

@dataclass
class AssistantConfig:
    summary_update_interval_messages: int = 10
    summary_update_interval_seconds: int = 300
    transcript_buffer_size: int = 50
    enable_decision_extraction: bool = True
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

livekit = LiveKitConfig()
openai = OpenAIConfig()
assistant = AssistantConfig()
