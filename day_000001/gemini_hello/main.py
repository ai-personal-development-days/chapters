import os
from google import genai
from dotenv import load_dotenv

load_dotenv() # .envから設定を読み込む
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

try:
    print("--- 利用可能なモデル一覧 ---")
    # models.list() はイテレータを返すので、そのままループ回します
    for m in client.models.list():
        # 最新のSDKでは supported_actions に 'generateContent' が含まれるか確認
        if 'generateContent' in m.supported_actions:
            # m.name は 'models/gemini-2.0-flash' のような形式です
            print(f"Model ID: {m.name}")

    # リストで確認できた正確なIDを指定します
    # 'gemini-2.5-flash' か 'gemini-2.0-flash' を使用してください
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents="Pythonからこんにちは！AI学習を始めたエンジニアの私に、これからのAI時代を生き抜くための熱いエールをください。"
    )
    
    print("\n" + "="*40)
    print("✨ Geminiからのメッセージ ✨")
    print(response.text)
    print("="*40 + "\n")

except Exception as e:
    print(f"実行エラーが発生しました:\n{e}")