from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
path_to_webdriver = "/Users/mak/Downloads/chromedriver-mac-x64/chromedriver" 

browser = webdriver.Chrome(options=chrome_options)

# Открываем конкретную ссылку
browser.get("https://docs.google.com/spreadsheets/d/1C0B6gz2ZtCc3CvnLghtK9Q8nvheU5iUMfi7nrTpQ8as/edit#gid=0")

# Получаем размер окна
size = browser.get_window_size()
width = size['width']
height = size['height']

print(f"Width: {width}, Height: {height}")

# JS-скрипт для отлова клика и сохранения координат
script = """
let clickCoords = {x: null, y: null};
document.addEventListener('click', function(e) {
    clickCoords.x = e.clientX;
    clickCoords.y = e.clientY;
});
return clickCoords;
"""

coords = browser.execute_script(script)

print("Click anywhere in the browser window and then return to the terminal and press Enter...")
input()

# Извлекаем координаты после нажатия
coords_after_click = browser.execute_script("return window.clickCoords;")

if coords_after_click and 'x' in coords_after_click and 'y' in coords_after_click:
    print(f"Clicked at X: {coords_after_click['x']}, Y: {coords_after_click['y']}")
else:
    print("Coordinates not captured. Make sure you clicked inside the browser window.")

browser.quit()
