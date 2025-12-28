"""Demo: Real-time Meeting Assistant with Mock Meeting"""
import asyncio
from datetime import datetime
from agent import MeetingAssistant, MockAgentSession

async def run_demo():
    print("=" * 70)
    print("🎯 REAL-TIME AI MEETING ASSISTANT - DEMO")
    print("=" * 70)
    print("")
    
    session = MockAgentSession(room_name="demo_product_meeting")
    assistant = MeetingAssistant(session)
    print(f"✅ Meeting started: {assistant.state.room_name}")
    print(f"⏰ Start time: {assistant.state.start_time.strftime('%H:%M:%S')}")
    print("")
    
    meeting_messages = [
        ("Alice", "Good morning everyone. Let's talk about the Q2 product launch."),
        ("Bob", "Thanks for organizing. I have concerns about our timeline."),
        ("Charlie", "Our engineering team needs at least 12 weeks to prepare."),
        ("Alice", "Marketing needs 3 weeks, so we're looking at 15 weeks total."),
        ("Bob", "What if we approve additional budget for more resources?"),
        ("Alice", "Great idea. Let's approve a $50K budget increase."),
        ("Charlie", "With extra budget, we can reduce our timeline to 10 weeks."),
        ("Bob", "Perfect. So we're approved for April 15, 2024 launch."),
        ("Alice", "Correct. Marketing starts campaign prep on January 15."),
        ("Charlie", "Engineering will submit detailed resource request by January 10."),
        ("Bob", "This is great progress. When's our next sync?"),
        ("Alice", "Let's meet again next Wednesday at 2 PM to review progress."),
    ]
    
    print("📝 Processing meeting messages...")
    print("")
    
    for i, (speaker, message) in enumerate(meeting_messages, 1):
        print(f"[{i:2d}] {speaker:8s}: {message}")
        await assistant.process_user_input(message, speaker)
        await asyncio.sleep(0.3)
    
    print("")
    print("=" * 70)
    print("📊 MEETING ANALYSIS")
    print("=" * 70)
    print("")
    
    status = await assistant.get_meeting_status()
    print(f"Meeting Duration: {status['duration_minutes']:.1f} minutes")
    print(f"Total Messages: {status['message_count']}")
    print(f"Speakers: {len(status['speakers'])}")
    print("")
    
    print("👥 Speaker Contributions:")
    for speaker, info in status['speakers'].items():
        print(f"  • {speaker}: {info['message_count']} messages")
    print("")
    
    print("📄 Generating summary...")
    await assistant._update_summary()
    print("")
    print("SUMMARY:")
    print("-" * 70)
    print(assistant.state.summary_buffer)
    print("-" * 70)
    print("")
    
    print("❓ Q&A DEMONSTRATION")
    print("-" * 70)
    
    test_questions = [
        "What is the launch date?",
        "What decisions were made about the budget?",
        "What are the next steps?",
    ]
    
    for question in test_questions:
        print(f"Q: {question}")
        answer = await assistant.answer_question(question)
        print(f"A: {answer}")
        print("")
    
    print("=" * 70)
    print("✅ Demo completed successfully!")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(run_demo())
