import requests
import base64
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hugging Face AI API URL
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
# আপনার Hugging Face টোকেনটি এখানে বসান (Bearer এর পরে)
headers = {"Authorization": "Bearer YOUR_HF_TOKEN_HERE"}

HTML = """
<!doctype html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Face Editor</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 20px; background-color: #f0f2f5; }
        .card { max-width: 450px; margin: auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h2 { color: #333; }
        input[type="file"] { margin: 20px 0; display: block; width: 100%; }
        .btn { background-color: #4CAF50; color: white; border: none; padding: 12px 25px; border-radius: 8px; cursor: pointer; font-size: 16px; transition: 0.3s; }
        .btn:hover { background-color: #45a049; }
        .result-img { max-width: 100%; margin-top: 25px; border-radius: 10px; border: 3px solid #ddd; }
        .footer { margin-top: 20px; font-size: 12px; color: #777; }
    </style>
</head>
<body>
    <div class="card">
        <h2>✨ AI Face Editor</h2>
        <p>আপনার ছবি আপলোড করুন এবং AI ম্যাজিক দেখুন</p>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="image" accept="image/*" required>
            <input type="submit" class="btn" value="এডিট শুরু করুন">
        </form>
        
        {% if image %}
        <div id="result">
            <h3>সাফল্য! আপনার রেজাল্ট:</h3>
            <img src="data:image/png;base64,{{image}}" class="result-img">
        </div>
        {% endif %}
        
        <div class="footer">Powered by GitHub & Hugging Face</div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("image")
        if file:
            # AI মডেলকে অনুরোধ পাঠানো
            payload = {"inputs": "Add beautiful golden jewelry on the face, high quality, realistic"}
            response = requests.post(API_URL, headers=headers, data=file.read())
            
            if response.status_code == 200:
                img_str = base64.b64encode(response.content).decode()
                return render_template_string(HTML, image=img_str)
            else:
                return f"Error: AI সার্ভার এখন ব্যস্ত (Code: {response.status_code}). টোকেন চেক করুন।"
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7860)
