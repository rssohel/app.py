# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template_string

app = Flask(__name__)

# এই টেমপ্লেটে প্রতিটি বক্সকে লিঙ্কে (Anchor Tag) রূপান্তর করা হয়েছে
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>সাইবার আইডি - Rana.nj</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Hind+Siliguri:wght@400;700&display=swap');
        
        body { 
            background-color: #020502; 
            color: #00ff41; 
            font-family: 'Share Tech Mono', 'Hind Siliguri', monospace;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }

        .cyber-card {
            max-width: 450px;
            width: 100%;
            border: 2px solid #00ff41;
            box-shadow: 0 0 25px rgba(0, 255, 65, 0.3);
            border-radius: 24px;
            padding: 30px;
            background: rgba(0, 15, 0, 0.95);
        }

        .neon-glow {
            text-shadow: 0 0 10px #00ff41;
        }

        /* ক্লিকেবল বক্স ডিজাইন */
        .grid-link {
            display: block;
            background: rgba(0, 255, 65, 0.05);
            border: 1px solid rgba(0, 255, 65, 0.2);
            border-radius: 12px;
            padding: 15px;
            text-align: center;
            text-decoration: none;
            color: inherit;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .grid-link:hover {
            background: rgba(0, 255, 65, 0.2);
            border-color: #00ff41;
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(0, 255, 65, 0.4);
        }

        .grid-link:active {
            transform: scale(0.95);
        }

        .animate-blink {
            animation: blink 1.5s infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.2; }
        }
    </style>
</head>
<body>

    <div class="cyber-card">
        <!-- হেডার অংশ -->
        <div class="text-center mb-8">
            <div class="text-[10px] tracking-[4px] opacity-70 font-bold">[ STATUS: UNTRACEABLE ]</div>
            <h1 class="text-5xl font-black neon-glow mt-2 tracking-tighter">RANA.NJ</h1>
            <p class="text-sm text-white/80 mt-1 uppercase">ALIAS: <span class="text-[#00ff41]">Black Herix</span></p>
            <div class="mt-4 border-b border-dashed border-[#00ff41]/30 pb-2">
                <span class="text-[10px] text-red-500 font-bold animate-blink uppercase">● System: Interactive Link Enabled</span>
            </div>
        </div>

        <!-- তথ্য গ্রিড (সবগুলো ক্লিকেবল) -->
        <div class="grid grid-cols-2 gap-4 mb-8">
            <!-- নাম বক্স (https://www.facebook.com/Rana6694 ) -->
            <a href="https://www.facebook.com/Rana6694" target="_blank" class="grid-link">
                <i class="fa-solid fa-user text-xl mb-2"></i>
                <div class="text-[9px] uppercase opacity-50">Real Name</div>
                <div class="text-sm font-bold text-white">Rana.nj</div>
            </a>

            <!-- বার্থডেট বক্স -->
            <a href="#" class="grid-link">
                <i class="fa-solid fa-cake-candles text-xl mb-2"></i>
                <div class="text-[9px] uppercase opacity-50">Birth Date</div>
                <div class="text-sm font-bold text-white">10February 2000</div>
            </a>

            <!-- ধর্ম বক্স -->
            <a href="#" class="grid-link">
                <i class="fa-solid fa-star-and-crescent text-xl mb-2"></i>
                <div class="text-[9px] uppercase opacity-50">Religion</div>
                <div class="text-sm font-bold text-white">Islam</div>
            </a>

            <!-- রিলেশনশিপ বক্স -->
            <a href="#" class="grid-link">
                <i class="fa-solid fa-heart text-xl mb-2"></i>
                <div class="text-[9px] uppercase opacity-50">Relationship</div>
                <div class="text-sm font-bold text-white">Single</div>
            </a>

            <!-- ব্লাড গ্রুপ বক্স -->
            <a href="#" class="grid-link border-red-900/40">
                <i class="fa-solid fa-droplet text-xl mb-2 text-red-500"></i>
                <div class="text-[9px] uppercase opacity-50">Blood Group</div>
                <div class="text-sm font-bold text-white">o Negative</div>
            </a>

            <!-- টাইপ বক্স -->
            <a href="#" class="grid-link">
                <i class="fa-solid fa-mask text-xl mb-2"></i>
                <div class="text-[9px] uppercase opacity-50">Type</div>
                <div class="text-sm font-bold text-white">Grey Hat</div>
            </a>
        </div>

        <!-- এক্সপার্টাইজ সেকশন -->
        <div class="flex items-center gap-2 mb-4">
            <i class="fa-solid fa-microchip text-xs"></i>
            <span class="text-[10px] font-bold uppercase tracking-widest">Dark Expertise</span>
        </div>
        <div class="grid grid-cols-2 gap-4">
            <!-- অ্যাপ ডেভেলপার লিঙ্ক (আপনার পোর্টফোলিও বা গিটহাব লিঙ্ক দিতে পারেন) -->
            <a href="https://github.com" target="_blank" class="grid-link border-[#00ff41]/40">
                <i class="fa-solid fa-mobile-button text-xl mb-1"></i>
                <div class="text-[10px] font-bold text-white">App Developer</div>
            </a>
            <!-- ওয়েব ডেভেলপার লিঙ্ক -->
            <a href="https://github.com" target="_blank" class="grid-link border-[#00ff41]/40">
                <i class="fa-solid fa-terminal text-xl mb-1"></i>
                <div class="text-[10px] font-bold text-white">Web Developer</div>
            </a>
        </div>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
