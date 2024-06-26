import streamlit as st
from chatbot import generate_recipe

def main():
    st.title('냉장고를 지켜줘 - 반찬 재료로 요리 만들기')

    # 반찬 재료 입력 받기
    st.subheader('반찬 재료를 입력하세요 (쉼표로 구분)')
    ingredients_str = st.text_input('예: 고추장, 두부, 계란, 감자, 미나리')

    if st.button('레시피 찾기'):
        ingredients = [ingredient.strip() for ingredient in ingredients_str.split(',')]
        
        if len(ingredients) != 5:
            st.warning('정확히 5개의 반찬 재료를 입력하세요!')
        else:
            st.success('입력된 반찬 재료: {}'.format(', '.join(ingredients)))
            st.subheader('추천 요리')

            recipes = generate_recipe(ingredients)  # ChatGPT를 사용하여 요리 레시피 추천

            for i, recipe in enumerate(recipes, start=1):
                st.write(f'**레시피 {i}:** {recipe}')

def generate_recipe(ingredients):
    # 여기서는 간단하게 임의의 레시피를 생성하도록 하겠습니다.
    # 실제로는 데이터베이스나 외부 API를 사용하여 진짜 레시피를 추천할 수 있습니다.
    recipes = [
        f'반찬 재료 {", ".join(ingredients)}를 사용한 레시피 1',
        f'반찬 재료 {", ".join(ingredients)}를 사용한 레시피 2',
        f'반찬 재료 {", ".join(ingredients)}를 사용한 레시피 3',
        f'반찬 재료 {", ".join(ingredients)}를 사용한 레시피 4',
        f'반찬 재료 {", ".join(ingredients)}를 사용한 레시피 5',
    ]
    return recipes

if __name__ == '__main__':
    main()
