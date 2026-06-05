"""Flux Image Generator on Hugging Face Space"""
import gradio as gr
import os
import fal_client

def generate_image(prompt: str, style: str = "thumbnail") -> str:
    """Generate YouTube thumbnail"""
    style_prompts = {
        "thumbnail": "YouTube thumbnail, vibrant, eye-catching, professional, 16:9",
        "educational": "educational infographic style, clean, professional",
        "dramatic": "dramatic lighting, cinematic, high contrast"
    }
    full_prompt = f"{prompt}, {style_prompts.get(style, '')}"
    
    try:
        result = fal_client.run(
            "fal-ai/flux/schnell",
            arguments={
                "prompt": full_prompt,
                "image_size": "landscape_16_9",
                "num_images": 1
            }
        )
        return result["images"][0]["url"]
    except Exception as e:
        return f"Error: {e}"

demo = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(label="وصف الصورة", placeholder="اكتب وصفاً للصورة..."),
        gr.Radio(["thumbnail", "educational", "dramatic"], label="الأسلوب", value="thumbnail"),
    ],
    outputs=gr.Image(label="الصورة المولّدة"),
    title="🖼️ TubeMind Image Generator",
    description="توليد صور احترافية للفيديوهات"
)

if __name__ == "__main__":
    demo.launch()
