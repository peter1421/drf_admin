import openai

openai.api_key = "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"  # 替换为您的 OpenAI API 密钥


def get_gpt_response(prompt):
    # 建立ChatCompletion端點的請求
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:personal::8NcRQDt1",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt},
        ],
    )
    # print(response.choices[0].message)

    return response.choices[0].message["content"]