from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command
import asyncio

API_TOKEN = ""

bot = Bot(API_TOKEN)
dp = Dispatcher()



@dp.message(Command("start"))
async def send_welcome(message: Message):
    user = message.from_user
    username = f"@{user.username}" if user.username else user.first_name
    await message.answer(
        f"Привет, {username}! Я телеграм-бот, который предлагает кино.\n"
        f"Напиши /genres чтобы выбрать жанр."
    )



@dp.message(Command("genres"))
async def cmd_genres(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Триллер", callback_data="genre_thriller"),
            InlineKeyboardButton(text="Боевик", callback_data="genre_action"),
            InlineKeyboardButton(text="Детектив", callback_data="genre_detective"),
        ]
    ])
    await message.answer("Выберите жанр:", reply_markup=keyboard)



Cinema = {
    "thriller": [
        ("Крик", "Кевин Уильямсон", "6.2", "https://upload.wikimedia.org/wikipedia/ru/thumb/8/8b/Scream_4.jpg/250px-Scream_4.jpg"),
        ("Зодиак", "Дэвид Финчер", "7.7", ""),  # нет картинки
        ("Подозрительные лица", "Брайан Сингер", "8.5", "https://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg")
    ],
    "action": [
        ("Бойцовский клуб", "Чак Паланик", "8.9", "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg"),
        ("Рэмбо: Первая кровь", "Дэвид Моррелл", "7.2", ""),
        ("Безумный Макс: Дорога ярости", "Джордж Миллер", "8.1", "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg")
    ],
    "detective": [
        ("Семь", "Дэвид Финчер", "8.6", "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg"),
        ("Остров проклятых", "Мартин Скорсезе", "8.2", "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg"),
        ("Достать ножи", "Райан Джонсон", "7.9", "")
    ]
}


@dp.callback_query(F.data.startswith("genre_"))
async def show_movies(callback: CallbackQuery):
    genre = callback.data.split("_")[1]  # thriller, action, detective

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=Cinema[genre][0][0], callback_data=f"cinema_{genre}_0")],
            [InlineKeyboardButton(text=Cinema[genre][1][0], callback_data=f"cinema_{genre}_1")],
            [InlineKeyboardButton(text=Cinema[genre][2][0], callback_data=f"cinema_{genre}_2")],
        ]
    )

    await callback.message.answer("Выберите кино:", reply_markup=keyboard)
    await callback.answer()  # вызываем только один раз



@dp.callback_query(F.data.startswith("cinema_"))
async def send_movie_info(callback: CallbackQuery):
    _, genre, index = callback.data.split("_")
    index = int(index)

    title, author, rating, photo_url = Cinema[genre][index]

    text = (
        f"Название: {title}\n"
        f"Автор: {author}\n"
        f"Рейтинг: ⭐ {rating}/10"
    )


    if photo_url:
        await callback.message.answer_photo(photo=photo_url, caption=text)
    else:
        await callback.message.answer(text)

    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
