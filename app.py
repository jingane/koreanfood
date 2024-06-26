import streamlit as st

# 가상의 레시피 데이터셋 (실제 데이터셋을 사용해야 함)
recipes = {
    "김치볶음밥": {
        "ingredients": ["밥", "김치", "돼지고기", "고추장", "계란"],
        "recipe": "1. 밥과 김치, 돼지고기, 고추장을 볶습니다.\n2. 계란을 풀어 넣고 볶으면 완성입니다."
    },
    "된장찌개": {
        "ingredients": ["된장", "물", "돼지고기", "두부", "미나리"],
        "recipe": "1. 된장, 물, 돼지고기, 두부를 넣고 끓입니다.\n2. 마지막에 미나리를 넣고 끓이면 완성입니다."
    },
    # 실제 데이터셋에서 수집한 데이터를 여기에 추가해야 함
}

def main():
    st.title('냉장고를 지켜줘 - 반찬 재료 기반 요리 레시피 추천')

    ingredients = []
    st.write("반찬 재료를 입력하세요:")
    for i in range(5):
        ingredient = st.text_input(f'반찬 재료 {i+1}')
        ingredients.append(ingredient)

    recommended_recipes = []

    for recipe_name, recipe_info in recipes.items():
        if all(ingredient in recipe_info["ingredients"] for ingredient in ingredients if ingredient):
            recommended_recipes.append(recipe_name)

    if recommended_recipes:
        st.write("\n추천 요리 레시피:")
        for recipe in recommended_recipes:
            if st.button(recipe):
                show_recipe(recipe)
    else:
        st.write("일치하는 요리가 없습니다.")

def show_recipe(recipe_name):
    st.write(f"{recipe_name} 요리 레시피:")
    st.write(recipes[recipe_name]["recipe"])

if __name__ == "__main__":
    main()
