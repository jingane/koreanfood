import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_recipes(query):
    url = f"https://m.10000recipe.com/recipe/list.html?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    recipes = []
    results = soup.find_all('li', class_='common_sp_list_li')
    for result in results:
        title_elem = result.find('div', class_='common_sp_caption_tit line2')
        if title_elem:
            title = title_elem.get_text(strip=True)
            link = result.find('a')['href']
            recipes.append({'title': title, 'link': link})

    return recipes

def main():
    st.title('단일 음식재료 기반 요리 레시피 검색')

    ingredient = st.text_input('음식재료')

    if st.button('레시피 검색'):
        recipes = get_recipes(ingredient)

        if recipes:
            st.header('검색 결과')
            for recipe in recipes:
                st.markdown(f"### [{recipe['title']}]({recipe['link']})")
        else:
            st.write('검색 결과가 없습니다.')

if __name__ == "__main__":
    main()
