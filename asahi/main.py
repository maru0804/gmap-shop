import requests
import time
import configparser
from collections import namedtuple

def init_conf():
    Conf = namedtuple('Conf', ['Key', 'Keyword', 'Location', 'Url', 'Num_results', 'Detail_url'])
    config = configparser.ConfigParser()
    config.read('conf.ini')

    Key = config.get('api-settings', 'apiKey') # ここにAPIキーを入力
    Keyword = config.get('serach-settings', 'keyword')  # 検索するキーワード
    Location = config.get('serach-settings', 'location')  # 天神の緯度と経度
    Url = config.get('serach-settings', 'url')  # Google Places APIのURL
    Num_results = int(config.get('serach-settings', 'num_results'))  # 検索結果の数
    Detail_url = config.get('serach-settings', 'detail_url')  # Google Places APIのURL

    return Conf(Key, Keyword, Location, Url, Num_results, Detail_url)

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

def get_place_details(api_key, place_id, detail_url):
    params = {
        "key": api_key,
        "place_id": place_id,
        "fields": "formatted_phone_number"
    }

    response = requests.get(detail_url, params=params)
    return response.json()["result"]

def main():
    config = init_conf()

    top_50_places = search_places(config.Url, config.Key, config.Keyword, config.Location, num_results=config.Num_results)
    file = open('result.txt', 'w')   
    file_limit = open('result_limit.txt', 'w')    
    for i, place in enumerate(top_50_places):
        reviews_count = place.get('user_ratings_total', 'N/A')
        details = get_place_details(config.Key, place["place_id"], config.Detail_url)
        phone_number = details.get("formatted_phone_number", "N/A")

        # 結果の出力
        print(f"{i + 1}. {place['name']}: {reviews_count} - 電話番号: {phone_number}")
        file.write(f"{i + 1}. {place['name']}: {reviews_count} - 電話番号: {phone_number}")
        file.write("\n")

        if reviews_count < 20:
            # 口コミ数が20件未満の場合の別ファイルに結果を出力
            print(f"{i + 1}. {place['name']}: {reviews_count} - 電話番号: {phone_number}")
            file_limit.write(f"{i + 1}. {place['name']}: {reviews_count} - 電話番号: {phone_number}")
            file_limit.write("\n")
    file.close()
    file_limit.close()

if __name__ == "__main__":
    main()