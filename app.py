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
    query = "김치"  # 검색할 키워드 입력
    recipes = get_recipes(query)

    for recipe in recipes:
        print(recipe['title'])
        print(recipe['link'])
        print()

if __name__ == "__main__":
    main()
