import os
from dotenv import load_dotenv
from google import genai # 新しいライブラリ

# 1. 環境変数の読み込み
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. クライアントの初期化
client = genai.Client(api_key=api_key)

# 3. 設定（人格・知識）
user_context = """
ユーザーはAIブームに出遅れた恐怖を抱えつつ、
PyrhonでGeminiを「解剖」しようとしている挑戦者です。
エンジニアではないが、AIを四肢のように使いこなす未来を目指しています。
"""

# 4. 人格の設定（プランA：人格）
system_instruction = f"""
{user_context}
あなたは「最新鋭の知能」であり、ユーザーの覚醒を促す「メンター」です。
最新モデルならではの、鋭く、かつ可能性に満ちたアドバイスを、小学生にもわかるようにしてください。
"""

print("--- Gemini 3 起動 ---")

# 5. 対話ループ
chat = client.chats.create(
    model="gemini-3-flash-preview",
    config={'system_instruction': system_instruction}
)

while True:
    user_input = input("あなた: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    
    # 新しいSDKでのメッセージ送信
    response = chat.send_message(user_input)
    print(f"\nAI: {response.text}\n")