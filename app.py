import requests
import base64
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hugging Face API URL
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
# আপনার আসল টোকেনটি এখানে বসান
headers = {"Authorization": "Bearer YOUR_REAL_TOKEN_HERE"}

HTML = """
<!doctype html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Face Editor</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding: 20px; background-color: #f4f4f9; }
        .card { max-width: 400px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        .btn { background-color: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; width: 100%; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h2>✨ AI Face Editor</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="image" accept="image/*" required><br><br>
            <input type="submit" class="btn" value="এডিট শুরু করুন">
        </form>
        {% if image %}
        <h3>ফলাফল:</h3>
        <img src="data:image/png;base64,{{image}}" style="max-width:100%; border-radius:10px;">
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("image")
        if file:
            response = requests.post(API_URL, headers=headers, data=file.read())
            if response.status_code == 200:
                img_str = base64.b64encode(response.content).decode()
                return render_template_string(HTML, image=img_str)
            else:
                return "সার্ভার এখন ব্যস্ত। আপনার টোকেনটি চেক করুন।"
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7860)
