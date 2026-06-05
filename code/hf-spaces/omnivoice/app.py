"""OmniVoice - Arabic TTS on Hugging Face Space"""
import gradio as gr
import os

def generate_voice(text: str, language: str = "ar", speed: float = 1.0) -> str:
    """Generate voiceover audio"""
    # This runs on Hugging Face with GPU
    try:
        # Using Edge TTS as fallback (free, high quality)
        import edge_tts, asyncio, tempfile
        voice_map = {"ar": "ar-SA-HamedNeural", "en": "en-US-GuyNeural"}
        voice = voice_map.get(language, "ar-SA-HamedNeural")
        
        async def generate():
            communicate = edge_tts.Communicate(text, voice, rate=f"+{int((speed-1)*50)}%")
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
                await communicate.save(f.name)
                return f.name
        
        return asyncio.run(generate())
    except Exception as e:
        return f"Error: {e}"

demo = gr.Interface(
    fn=generate_voice,
    inputs=[
        gr.Textbox(label="النص", placeholder="اكتب النص هنا...", lines=5),
        gr.Radio(["ar", "en"], label="اللغة", value="ar"),
        gr.Slider(0.5, 2.0, value=1.0, label="السرعة"),
    ],
    outputs=gr.Audio(label="الصوت المولّد"),
    title="🎙️ TubeMind Voice Generator",
    description="توليد صوت احترافي للفيديوهات"
)

if __name__ == "__main__":
    demo.launch()
