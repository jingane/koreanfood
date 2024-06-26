import streamlit as st

def main():
    st.title('냉장고를 지켜줘 - 반찬 재료 기반 요리 레시피 추천')

    # 사용자 입력 받기
    ingredients = []
    st.write("반찬 재료를 입력하세요:")
    for i in range(5):
        ingredient = st.text_input(f'반찬 재료 {i+1}')
        ingredients.append(ingredient)

    # ChatGPT를 이용한 요리 추천 (간략화된 예시)
    recommended_recipes = [
        "김치볶음밥",
        "된장찌개",
        "고추장불고기",
        "무생채",
        "계란말이"
    ]

    st.write("\n추천 요리 레시피:")
    for recipe in recommended_recipes:
        if all(ingredient in recipe for ingredient in ingredients if ingredient):
            if st.button(recipe):
                show_recipe(recipe)

def show_recipe(recipe_name):
    st.write(f"{recipe_name} 요리 레시피:")
    if recipe_name == "김치볶음밥":
        st.write("1. 밥과 김치, 돼지고기, 고추장을 볶습니다.")
        st.write("2. 계란을 풀어 넣고 볶으면 완성입니다.")

if __name__ == "__main__":
    main()
