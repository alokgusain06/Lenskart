"""Real-time AI Meeting Assistant using LiveKit Agents"""
import logging
from datetime import datetime
from typing import Optional
from dataclasses import dataclass
from collections import deque
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class MeetingState:
    """Track meeting metadata and insights"""
    room_name: str
    start_time: datetime
    transcript_buffer: deque
    summary_buffer: str
    speakers: dict
    decisions: list
    topics: list
    last_summary_time: datetime
    message_count: int = 0

    def to_dict(self):
        return {
            "room_name": self.room_name,
            "start_time": self.start_time.isoformat(),
            "summary": self.summary_buffer,
            "speakers": self.speakers,
            "decisions": self.decisions,
            "topics": self.topics,
            "message_count": self.message_count,
            "duration_minutes": (datetime.now() - self.start_time).total_seconds() / 60,
        }

class MeetingAssistant:
    """Main meeting assistant logic"""
    def __init__(self, session):
        self.session = session
        self.state = MeetingState(
            room_name=session.room.name,
            start_time=datetime.now(),
            transcript_buffer=deque(maxlen=50),
            summary_buffer="",
            speakers={},
            decisions=[],
            topics=[],
            last_summary_time=datetime.now(),
            message_count=0,
        )
    
    def setup_components(self):
        """Configure STT, LLM, and TTS components"""
        logger.info("Components configured")
    
    async def process_user_input(self, message: str, speaker: str) -> None:
        """Process transcribed user message"""
        if speaker not in self.state.speakers:
            self.state.speakers[speaker] = {"message_count": 0, "first_seen": str(datetime.now())}
        self.state.speakers[speaker]["message_count"] += 1
        
        self.state.transcript_buffer.append({
            "speaker": speaker,
            "message": message,
            "timestamp": str(datetime.now()),
        })
        self.state.message_count += 1
        
        time_since_summary = (datetime.now() - self.state.last_summary_time).total_seconds()
        if self.state.message_count % 10 == 0 or time_since_summary > 300:
            await self._update_summary()
        
        logger.info(f"[{speaker}] {message[:100]}... | Messages: {self.state.message_count}")
    
    async def _update_summary(self) -> None:
        """Generate updated meeting summary"""
        if not self.state.transcript_buffer:
            return
        
        recent_transcript = "\n".join([f"{item['speaker']}: {item['message']}" 
                                       for item in list(self.state.transcript_buffer)[-20:]])
        
        summary = f"""Meeting Summary - {len(self.state.speakers)} participants:
Recent Discussion: {recent_transcript[:500]}...
Decisions: {len(self.state.decisions)} made
Topics: {len(set(self.state.topics))} identified"""
        
        self.state.summary_buffer = summary
        self.state.last_summary_time = datetime.now()
        logger.info("Summary updated")
    
    async def answer_question(self, question: str) -> str:
        """Answer questions about the meeting"""
        return f"Based on the meeting, here's what I know about '{question}': [Context from last {len(self.state.transcript_buffer)} messages]"
    
    async def get_meeting_status(self) -> dict:
        """Get current meeting status"""
        return self.state.to_dict()

class MockAgentSession:
    """Mock session for testing"""
    def __init__(self, room_name="demo"):
        self.room = type("Room", (), {"name": room_name})()
        self.stt = None
        self.llm = None
        self.tts = None
        self.chat = type("Chat", (), {"send_message": self._mock_send})()
    
    async def _mock_send(self, message: str):
        print(f"\n[ASSISTANT]: {message}")
