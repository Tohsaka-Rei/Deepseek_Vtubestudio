from openai import OpenAI
from getpass import getpass

api_key = getpass("请输入 DeepSeek API Key: ").strip()

if not api_key:
    raise SystemExit("没有输入 API Key，程序退出。")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

print("\nDeepSeek API 测试")
print("输入 exit 退出。\n")

while True:
    question = input("你：").strip()

    if question.lower() in ("exit", "quit"):
        print("测试结束，喵！")
        break

    if not question:
        continue

    try:
        response = client.chat.completions.create(
            model="deepseek-flash",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=300
        )

        answer = response.choices[0].message.content
        print(f"\nDeepSeek：{answer}\n")

        if response.usage:
            print(
                f"[Token 用量] "
                f"输入 {response.usage.prompt_tokens}，"
                f"输出 {response.usage.completion_tokens}\n"
            )

    except Exception as e:
        print(f"\n请求失败：{e}\n")
