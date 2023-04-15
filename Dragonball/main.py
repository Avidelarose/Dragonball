from vkbottle.tools import template_gen, TemplateElement
from settings import *



@bot.on.raw_event(GroupEventType.GROUP_LEAVE, dataclass=GroupTypes.GroupLeave)
async def group_leave_handler(event: GroupTypes.GroupLeave):
    try:
        await bot.api.messages.send(
            peer_id=event.object.user_id,
            message="Вот-так закончишь свой путь?",
            random_id=0
        )
    except VKAPIError(901):
        pass



@bot.on.message(text="start")
@bot.on.message(payload={"cmd": "start"})
async def handler(message: Message):
    keyboard = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Создание героя", {"cmd": "more"}), KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Список способностей", {"cmd": "skills"}), KeyboardButtonColor.PRIMARY)
        .row()
        .add(Text("Выбрать родную планету", {"ball": "planet"}), KeyboardButtonColor.PRIMARY)
        .row()
        .add(Text("Войти в профиль", {"shat": "happend"}), KeyboardButtonColor.PRIMARY)
        .row()
        .add(Text("Регистрация", {"shat": "reg"}), KeyboardButtonColor.PRIMARY)
    ).get_json()

    await message.answer("Начни своё приключение здесь", keyboard=keyboard)



@bot.on.message(text="Регистрация")
@bot.on.message(payload={"cmd": "reg"})
async def handler(message: Message):
    bot_id = message.from_id
    bot_name = (await bot.api.users.get(user_ids=message.from_id))[0].first_name
    db_user(User_id=bot_id, nick=bot_name, Persons=0, Planet=0, lvl=0, Hero="нет", balance=0)
    await message.answer("Регистрация в мире - важный шаг для героя",)




@bot.on.message(text="войти в профиль")
@bot.on.message(payload={"shat": "happend"})
async def handler(message: Message):
    await message.answer()



@bot.on.message(text="Создание героя")
@bot.on.message(payload={"cmd": "more"})
async def handler(message: Message):
    if message.from_id == 315385319:

        await message.answer("1 Сон Гоку\n"
                             "2 Веджета\n"
                             "3 Пикколо\n"
                             "4 Куририн\n"
                             "5 Сон Гохан\n"
                             "6 Бульма\n"
                             "7 Чи-Чи\n"
                             "8 Фриза\n"
                             "9 Мастер Роши\n"
                             "10 Сон Гохан\n"
                             "11 Черепаха\n"
                             "12 Транкс\n"
                             "13 Ямча\n"
                             "14 Бра\n"
                             "- Для выбора персонажа введите: Персыонаж [1 - 14]\n"
                             "Пример:Персонаж 2")
    else:
        await message.answer("1 Сон Гоку\n"
                             "2 Веджета\n"
                             "3 Пикколо\n"
                             "4 Куририн\n"
                             "5 Сон ГоханСон\n"
                             "6 Бульма\n"
                             "7 Чи-Чи\n"
                             "8 Фриза\n"
                             "9 Мастер Роши\n"
                             "10 Сон Гохан\n"
                             "11 Черепаха\n"
                             "12  Транкс\n"
                             "13 Ямча\n"
                             "14 Бра\n"
                            "15 Зенон\n"
                             "- Для выбора персонажа введите: Персыонаж [1 - 14]\n"
                             "Пример:Персонаж 2"
        )






@bot.on.message(text="Выбор родной планеты")
@bot.on.message(payload={"ball": "planet"})
async def handler(message: Message):
    await message.answer("1 Земля\n"
                         "2 Намик\n"
                         "3 Бабари\n"
                         "4 Небеса\n"
                         "- Для выбора Планеты введите: Планета [1 - 4]\n"
                         "Пример:Планета 1")



@bot.on.message(text=["Планета <value>", 'Планеты'])
@bot.on.message(payload={"ball": "planet"})
async def handler(message: Message, value=None):

    keyboard = (
                Keyboard(one_time=True, inline=False)
                .add(Text("Назад", {"ball": "planet"}), KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("выбрать Планету", {"cm": "s"}), KeyboardButtonColor.POSITIVE)
            )

    photo_uploader = PhotoMessageUploader(bot.api)
    photo_ball = await photo_uploader.upload(
        file_source='image/zemlya.jpg',
        peer_id=message.peer_id,
    )

    if int(value) == 1:

        await message.answer("\n"
                             "\n"
                             "Планета Земля\n"
                             "\n"
                             "На этой планете мало враждебных монстров, здоровье планеты самое низкое из всех,что делает ее менее защищённой\n"
                             "\n"
                             "но есть и свои плюсы , ее защитное поле очень хорошее, так-что пролетающие мимо снаряды средней мощности не смогут нанести ей урона\n"
                             "\n"
                             "события на этой планте развиваются стремительно, не забывайте заходить в игру , чтобы в ходе случайного события не потерять планету\n"
                             "вы  сможете переминовать вашу планету!\n", keyboard=keyboard, attachment=photo_ball)





@bot.on.message(text=["Персонаж <value>", 'Персонаж'])
@bot.on.message(payload={"cmd": "Persons"})
async def handler(message: Message, value=None):

    keyboard = (
                Keyboard(one_time=True, inline=False)
                .add(Text("Назад", {"cmd": "more"}), KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("выбрать  героя", {"cmd": "lol"}), KeyboardButtonColor.POSITIVE)
            )

    photo_uploader = PhotoMessageUploader(bot.api)
    photo_ball = await photo_uploader.upload(
        file_source='image/vedjetaa.jpeg',
        peer_id=message.peer_id,
    )

    if int(value) == 2:

        await message.answer("\n"
                             "\n"
                             "\n"
                                "Cпособности:"
                                "\n"
                                "- Атака Большой Взрыв\n"
                                "- Атака Финального Сияния\n"
                                "- Галактический Крушитель\n"
                                "- Галик Хо\n"
                                "- Киензан\n"
                                "- Китанай Ханаби\n"
                                "- Максимум Флэшер\n"
                                "- Макухоидан\n"
                                "- Пальцевый Луч\n"
                                "- Рензоку Кико Дан\n"
                                "- Кольцевые Энергетические Пули\n"
                                "- Силовой Шар\n"
                                "- Финальная Вспышка\n"
                                "- Шогекиха \n"
                                "- Камехамеха\n"
                                "\n"
                                "Такой дерьмовой атакой... Ты меня не убьешь!... Я не вру... Ведь один раз я уже умер!... Будь я проклят, если меня уничтожит кто-то вроде тебя! Я принц народа воинов, сайянов!... ВЕДЖЕТА!!!\n", keyboard=keyboard, attachment=photo_ball)












@bot.on.message(payload={"cm": "s"})
async def handler(message: Message):

    keyboard = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Назад", {"cmd": "start"}), KeyboardButtonColor.POSITIVE)
    ).get_json()

    cursor.execute('SELECT Persons FROM user WHERE user_id = ?', (message.from_id,))
    result = cursor.fetchone()
    Planet = result[0]


    cursor.execute('UPDATE user SET Persons = ? WHERE user_id = ?', (str("Земля"), message.from_id,))
    conn.commit()

    await message.answer("Вы выбрали Родную планету \n'"
                         ", берегите её!\n"
                         " если она разрушится вам придется начинать игру с начала ! 🎯", keyboard=keyboard)


@bot.on.message(payload={"cmd": "lol"})
async def handler(message: Message):

    keyboard = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Назад", {"cmd": "start"}), KeyboardButtonColor.POSITIVE)
    ).get_json()

    cursor.execute('SELECT Persons FROM user WHERE user_id = ?', (message.from_id,))
    result = cursor.fetchone()
    Persons = result[0]


    cursor.execute('UPDATE user SET Persons = ? WHERE user_id = ?', (int(Persons) + 1, message.from_id,))
    conn.commit()

    await message.answer("Вы выбрали персонажа 🎯 , настало время выбрать планету!", keyboard=keyboard)

bot.run_forever()







