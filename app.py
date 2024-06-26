import streamlit as st
import openai  # OpenAI API를 사용하기 위한 라이브러리

# OpenAI API 설정 (본인의 API 키를 사용해야 함)
openai.api_key = "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"

def generate_recipes(ingredients):
    prompt = f"Given these ingredients: {', '.join(ingredients)}, suggest 5 recipes."
    response = openai.Completion.create(
        engine="text-davinci-002",  # ChatGPT 모델 엔진 선택
        prompt=prompt,
        max_tokens=150
    )
    recipes = response.choices
    return recipes

def main():
    st.title("냉장고를 지켜줘 - 요리 레시피 생성기")
    
    # 반찬 재료 입력 받기
    ingredients = []
    for i in range(5):
        ingredient = st.text_input(f"반찬 재료 {i+1}")
        if ingredient:
            ingredients.append(ingredient)
    
    if ingredients:
        st.subheader("입력된 반찬 재료:")
        st.write(ingredients)
        
        # ChatGPT를 이용해 레시피 생성
        st.subheader("생성된 요리 레시피:")
        recipes = generate_recipes(ingredients)
        
        for idx, recipe in enumerate(recipes):
            st.markdown(f"**레시피 {idx+1}:** {recipe.text}")
            st.markdown("*(레시피 클릭 시 상세 요리법 표시)*")
    
if __name__ == "__main__":
    main()
