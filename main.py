import requests
import time
import configparser

def search_places(base_url, api_key, keyword, location, radius=1000, num_results=10):
    results = []
    next_page_token = None

    while len(results) < num_results:
        params = {
            "key": api_key,
            "keyword": keyword,
            "location": location,
            "radius": radius
        }
        if next_page_token:
            params["pagetoken"] = next_page_token

        response = requests.get(base_url, params=params)
        data = response.json()

        results.extend(data["results"])

        if "next_page_token" in data:
            next_page_token = data["next_page_token"]
            time.sleep(2)  # Google Places APIのレート制限に対応するために待機
        else:
            break

    return results[:num_results]

def main():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    api_key = config.get('api-settings', 'apiKey') # ここにAPIキーを入力
    keyword = config.get('serach-settings', 'keyword')  # 検索するキーワード
    location = config.get('serach-settings', 'location')  # 天神の緯度と経度
    base_url = config.get('serach-settings', 'url')  # Google Places APIのURL
    num_results = int(config.get('serach-settings', 'num_results'))  # 検索結果の数

    top_50_places = search_places(base_url, api_key, keyword, location, num_results=num_results)
    file = open('result.txt', 'w')    
    for i, place in enumerate(top_50_places):
        print(f"{i + 1}. {place['name']}")
        file.write(f"{i + 1}. {place['name']}")
        file.write("\n")
    file.close()

if __name__ == "__main__":
    main()