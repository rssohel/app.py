from flask import Flask, request, render_template_string
from diffusers import StableDiffusionImg2ImgPipeline
import torch
from PIL import Image
import io
import base64

app = Flask(__name__)

# Load model
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda" if torch.cuda.is_available() else "cpu")

HTML = """
<!doctype html>
<title>AI Face Editor</title>
<h2>Upload Image</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=image>
  <input type=submit value=Upload>
</form>
{% if image %}
<h3>Result:</h3>
<img src="data:image/png;base64,{{image}}">
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["image"]
        init_image = Image.open(file).convert("RGB")
        init_image = init_image.resize((512, 512))

        prompt = "Add beautiful golden jewelry on the face"

        result = pipe(prompt=prompt, image=init_image, strength=0.6).images[0]

        buffered = io.BytesIO()
        result.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return render_template_string(HTML, image=img_str)

    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
