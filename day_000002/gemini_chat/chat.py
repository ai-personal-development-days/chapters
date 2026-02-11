import os
import json
from datetime import datetime
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. 記憶が格納されているフォルダの指定
HISTORY_DIR = "day_000002/gemini_chat/history"

# フォルダがない場合は作成する
if not os.path.exists(HISTORY_DIR):
    os.makedirs(HISTORY_DIR)

# 2. フォルダ内のすべてのJSONファイルを自動で読み込む
combined_history = []
# ファイル名でソートして順番に読み込む（Day1, Day2...の順になるように）
all_files = sorted([f for f in os.listdir(HISTORY_DIR) if f.endswith(".json")])

for file_name in all_files:
    file_path = os.path.join(HISTORY_DIR, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for entry in data:
            # 1つずつの発言をSDKが求める形式に整形
            formatted_entry = {
                "role": entry["role"],
                "parts": [{"text": p} for p in entry["parts"]]
            }
            combined_history.append(formatted_entry)
    print(f"記憶をロードしました: {file_name}")

# 3. AIの設定
system_instruction = "あなたはユーザーの全ての学習過程を記憶しているメンターです。過去の経緯を踏まえて回答してください。"

chat = client.chats.create(
    model="gemini-3-flash-preview",
    config={'system_instruction': system_instruction},
    history=combined_history
)

print(f"--- Gemini 3 起動（記憶数: {len(combined_history)}件） ---")

# 4. 対話ループ
while True:
    user_input = input("あなた: ")
    if user_input.lower() in ["quit", "exit", "save"]:
        
        # 終了時に「今回の会話」を要約して保存
        print("今回の会話を要約して保存中...")
        summary_prompt = "今回の会話の内容を、後であなたが読み返して理解できるように、重要なポイントを数行で簡潔に要約して。形式はroleとpartsを持つJSONリスト形式に合うようにして。"
        response = chat.send_message(summary_prompt)
        
        # 新しいファイル名の作成（例: day2_20260211_2030.json）
        new_filename = f"day2_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        new_file_path = os.path.join(HISTORY_DIR, new_filename)
        
        # AIの要約結果を保存（ここでは簡易的に今回のやり取りを保存する形にしています）
        save_data = [
            {"role": "user", "parts": [f"セッション記録: {datetime.now()}"]},
            {"role": "model", "parts": [response.text]}
        ]
        
        with open(new_file_path, "w", encoding="utf-8") as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)
            
        print(f"新しい記憶を保存しました: {new_filename}")
        break
    
    response = chat.send_message(user_input)
    print(f"\nAI: {response.text}\n")