from src.imp import *

BotDB = BotDB()


@dp.message_handler(state=Wait.my_form_answer)
async def my_form_answer(message: types.Message, state: FSMContext):
    id = message.from_user.id
    if message.text == "1":
        await message.answer("Для начала давай выберем пол", reply_markup=kb.key_gender())
        await Wait.choosing_gender.set()
    elif message.text == "2":
        await message.answer("Вводи новый текст анкеты", reply_markup=kb.key_empty())
        await Wait.change_text.set()
    elif message.text == "3":
        await message.answer("Отправляй фото!", reply_markup=types.ReplyKeyboardRemove())
        await Wait.photo.set()
    elif message.text == "4" or message.text == "Продолжить":
        f = BotDB.get_form(id)
        if len(f["liked"].split()) > 1:
            while not BotDB.user_exists(f["liked"].split()[-1]) and len(f["liked"].split()) != 1:
                f["liked"] = b.crop_list(f["liked"])
            BotDB.patch_liked(id, f["liked"])
            if len(f["liked"].split()) != 1:
                l = BotDB.get_form(f["liked"].split()[-1])
                await state.update_data(liked_id=l["id"])
                await bot.send_photo(photo=l["photo"], chat_id=id, caption=t.like_list + b.cap(l),
                                     reply_markup=kb.react())
                await Wait.form_reaction.set()
                return
        try:
            r = BotDB.get_random_user(id, f["age"], f["interest"])
        except ValueError:
            await message.answer(t.no_found)
            await bot.send_photo(photo=f["photo"], caption=b.cap(f), chat_id=id)
            await message.answer(t.my_form_text, reply_markup=kb.key_1234())
            await Wait.my_form_answer.set()
            return
        await state.update_data(liked_id=r["id"])
        await bot.send_photo(photo=r["photo"], caption=b.cap(r), chat_id=id, reply_markup=kb.react())
        await Wait.form_reaction.set()
    else:
        await message.reply("Нет такого варианта ответа")
        return


@dp.message_handler(state=Wait.choosing_gender)
async def choose_gender(message: types.Message, state: FSMContext):
    if message.text not in ["Парень", "Девушка"]:
        await message.answer("Нет такого варианта ответа")
        return
    await state.update_data(gender=message.text.lower())
    await message.answer(t.set_interest, reply_markup=kb.key_interest())
    await Wait.choosing_interest.set()


@dp.message_handler(state=Wait.choosing_interest)
async def choose_interest(message: types.Message, state: FSMContext):
    if message.text == "Парни" or message.text == "Девушки":
        await state.update_data(interest=message.text.lower())
        try:
            data = await state.get_data()
            await message.answer(t.set_name, reply_markup=kb.custom(data['name']))
        except KeyError:
            await message.answer(t.set_name, reply_markup=types.ReplyKeyboardRemove())
        await Wait.name.set()
    else:
        await message.reply("Нет такого варианта ответа")
        return


@dp.message_handler(state=Wait.name)
async def name(message: types.Message, state: FSMContext):
    if len(message.text) > 20:
        await message.answer("Недопустимая длина имени")
        return
    await state.update_data(name=message.text)
    await message.reply(t.set_age+f"{message.text}!")
    try:
        data = await state.get_data()
        await message.answer('Сколько тебе лет?', reply_markup=kb.custom(data['age']))
    except KeyError:
        await message.answer('Сколько тебе лет?', reply_markup=types.ReplyKeyboardRemove())
    await Wait.age.set()


@dp.message_handler(state=Wait.age)
async def age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) < 18 or int(message.text) > 30:
            await message.reply("Бот предназначен для пользователей от 18 до 30 лет")
            return
    except(TypeError, ValueError):
        await message.reply("Некорректный возраст")
        return
    await state.update_data(age=message.text)
    await message.answer(t.set_text, reply_markup=kb.custom("Оставить пустым"))
    await Wait.text.set()


@dp.message_handler(state=Wait.text)
async def text(message: types.Message, state: FSMContext):
    if message.text == "Оставить пустым":
        await state.update_data(text='')
    else:
        if len(message.text) > 400:
            await message.reply("Превышен лимит в 400 символов")
            return
        await state.update_data(text=message.text)
    await message.answer("Загрузите своё фото", reply_markup=types.ReplyKeyboardRemove())
    await Wait.photo.set()


@dp.message_handler(state=Wait.photo, content_types=["photo"])
async def set_photo(message: types.Message, state: FSMContext):
    id = message.from_user.id
    photo = message.photo[-1].file_id
    await state.update_data(liked="0", username=message.from_user.username, photo=photo)
    f = await state.get_data()
    await message.answer(t.form)
    if BotDB.user_exists(id):
        await bot.send_photo(photo=f["photo"], caption=f"#upd_user {id} \n"+b.cap(f), chat_id=supp_id)
        BotDB.patch_user(id, f['gender'], f['interest'], f['name'], f['age'], f['photo'], f['text'])
    else:
        await bot.send_photo(photo=f["photo"], caption=f"#new_user {id} \n" + b.cap(f), chat_id=supp_id)
        BotDB.post_user(f["username"], id, f["gender"], f["interest"], f["name"], f["age"], f["photo"], f["text"])
    await bot.send_photo(photo=f["photo"], caption=b.cap(f), chat_id=id)
    await message.answer(t.menu_main_text, reply_markup=kb.key_123())
    await Wait.menu_answer.set()


@dp.message_handler(state=Wait.delete_confirm)
async def delete_confirm(message: types.Message, state: FSMContext):
    if message.text not in ("Да", "Нет"):
        await message.reply("Нет такого варианта ответа")
        return
    id = message.from_user.id
    if message.text == "Да":
        BotDB.patch_visible(id, False)
        await message.answer(t.del_form, reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "Нет":
        f = BotDB.get_form(id)
        await bot.send_photo(photo=f["photo"], caption=b.cap(f), chat_id=id)
        await message.answer(t.my_form_text, reply_markup=kb.key_1234())
        await Wait.my_form_answer.set()


@dp.message_handler(state=Wait.change_text)
async def change_text(message: types.Message, state: FSMContext):
    id = message.from_user.id
    if message.text == "Оставить пустым":
        BotDB.patch_text(id, '')
        await state.update_data(text='')
    else:
        if len(message.text) > 400:
            await message.reply("Превышен лимит в 400 символов(")
            return
        BotDB.patch_text(id, message.text)
        await state.update_data(text=message.text)
    f = BotDB.get_form(id)
    await bot.send_photo(photo=f["photo"], caption=f"#upd {id}\n"+b.cap(f), chat_id=supp_id)
    await bot.send_photo(photo=f["photo"], caption=b.cap(f), chat_id=id)
    await message.answer(t.menu_main_text, reply_markup=kb.key_123())
    await Wait.menu_answer.set()