import requests
import lxml.html as html

def get_games(is_discount = False):
    url = "https://store.steampowered.com/search/?category1=998"
    if is_discount: 
        url = "https://store.steampowered.com/search/?specials=1&category1=998"
    response = requests.get(url)
    games = '//div[@id="search_resultsRows"]/a'
    first_page = response.content.decode('utf-8')
    parser = html.fromstring(first_page)
    games_list = parser.xpath(games)
    return games_list

def get_title(game_obj):
    title_list = game_obj.xpath(".//span[@class='title']")
    title_string = title_list[0].text_content()
    return title_string

def get_release_date(game_obj):
    release_list = game_obj.xpath(".//div[@class='col search_released responsive_secondrow']")
    release_string = release_list[0].text_content()[2:].split(' '*16)[1].split(' '*3)[1]
    return release_string

def get_price(game_obj):
    price_list = game_obj.xpath(".//div[contains(@class,'discount_final_price')]")
    price_string = price_list[0].text_content()
    if price_string.lower() == 'free':
        return 'Gratis'
    price_float = float(price_string[1:])
    return price_float

def get_discount(game_obj):
    discount_list = game_obj.xpath(".//div[@class='discount_pct']")
    if len(discount_list) >= 1:
        discount_string = discount_list[0].text_content()
        return discount_string
    return "Sin descuento"

def get_rating(game_obj):
    rating_list = game_obj.xpath(".//span[contains(@class,'search_review_summary')]/@data-tooltip-html")
    rating_string = rating_list[0].split('<br>')[0]
    return rating_string