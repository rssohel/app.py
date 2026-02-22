import requests
import base64
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hugging Face API (এটি আপনার ফোনের র‍্যাম খরচ করবে না)
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
# আপনার Hugging Face টোকেনটি এখানে বসাবেন
headers = {"Authorization": "Bearer YOUR_HF_TOKEN_HERE"}

HTML = """
<!doctype html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Face Editor</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding: 20px; background-color: #f4f4f9; }
        .container { max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        input[type="file"] { margin-bottom: 15px; }
        input[type="submit"] { background-color: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
        img { max-width: 100%; margin-top: 20px; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>AI Face Editor</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="image" accept="image/*"><br>
            <input type="submit" value="এডিট করুন (AI)">
        </form>
        {% if image %}
        <h3>রেজাল্ট:</h3>
        <img src="data:image/png;base64,{{image}}">
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
            # API রিকোয়েস্ট
            response = requests.post(API_URL, headers=headers, data=file.read())
            if response.status_code == 200:
                img_str = base64.b64encode(response.content).decode()
                return render_template_string(HTML, image=img_str)
            else:
                return "AI সার্ভার এখন ব্যস্ত, কিছুক্ষণ পর চেষ্টা করুন।"
    return render_template_string(HTML)

if __name__ == "__main__":
    # অনলাইন সার্ভারে চালানোর জন্য পোর্ট ৭৮৬০ ব্যবহার করা হয়
    app.run(host='0.0.0.0', port=7860)
