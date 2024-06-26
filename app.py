import streamlit as st
import openai

# OpenAI API key 설정
openai.api_key = "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"

def generate_recipe(ingredients):
    # ChatGPT를 사용하여 요리 레시피 생성
    prompt = f"요리할 수 있는 반찬 재료: {', '.join(ingredients)}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    recipe = response.choices[0].text.strip()
    return recipe

def main():
    st.title('냉장고를 지켜줘 - 반찬 재료로 요리 추천하기')
    st.write('반찬 재료를 입력하세요.')

    # 사용자에게 입력 받기
    ingredient1 = st.text_input('재료 1:')
    ingredient2 = st.text_input('재료 2:')
    ingredient3 = st.text_input('재료 3:')
    ingredient4 = st.text_input('재료 4:')
    ingredient5 = st.text_input('재료 5:')

    ingredients = [ingredient1, ingredient2, ingredient3, ingredient4, ingredient5]
    ingredients = [ing for ing in ingredients if ing]  # 빈칸 제외

    if st.button('레시피 찾기'):
        if ingredients:
            recipe = generate_recipe(ingredients)
            st.write(f"추천된 레시피:\n{recipe}")
        else:
            st.write("반찬 재료를 입력해주세요.")

if __name__ == '__main__':
    main()
