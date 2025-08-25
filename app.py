from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    seller = {
        "name": "Магазин «Пример» на Ozon",
        "ozon_url": "https://www.ozon.ru/seller/ваш_магазин",  # замените на свой
        "description": "Мы продаём качественные товары с быстрой доставкой и поддержкой. Помогите нам расти — оставьте отзыв!",
        "socials": [
            {"name": "Instagram", "url": "https://instagram.com/your", "icon": "instagram"},
            {"name": "VK", "url": "https://vk.com/your", "icon": "vk"},
            {"name": "Telegram", "url": "https://t.me/your", "icon": "telegram"}
        ]
    }
    return render_template('index.html', seller=seller)

if __name__ == '__main__':
    app.run(debug=True)