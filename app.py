import streamlit as st
import requests
from bs4 import BeautifulSoup
import streamlit.components.v1 as components

def get_recipes(query):
    url = f"https://m.10000recipe.com/recipe/list.html?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find first recipe link and return its URL
    results = soup.find_all('li', class_='common_sp_list_li')
    if results:
        first_result = results[0]
        link = first_result.find('a')['href']
        return link
    else:
        return None

def main():
    st.title('단일 음식재료 기반 요리 레시피 검색')

    ingredient = st.text_input('음식재료')

    if st.button('레시피 검색'):
        recipe_link = get_recipes(ingredient)

        if recipe_link:
            st.header('검색 결과')
            st.markdown(f"### 레시피 링크")
            components.iframe(recipe_link, width=700, height=600)
        else:
            st.write('검색 결과가 없습니다.')

if __name__ == "__main__":
    main()
