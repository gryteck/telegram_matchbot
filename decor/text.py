import random

menu_main_text = '1. Погнали знакомиться o(>ω<)o \n' \
                 '2. Хочу поменять анкету (* ^ ω ^) \n' \
                 '3. Удалить анкету ＼(º □ º l|l)/'

my_form_text = '1. Переписать всё с нуля (・人・)\n' \
               '2. Изменить описание (* ^ ω ^)\n' \
               '3. Изменить фотокарточку ＼(≧▽≦)／\n' \
               '4. Погнали знакомиться o(>ω<)o'

del_form = "Твоя анкета удалена(\n" \
           "Ты всегда можешь рассчитывать на меня. Просто нажми команду /start"

info = "Аригато! Я Акира - бот по поиску друзей из  o(>ω<)o Москвы\n" \
       "Будьте здоровы, любите себя и своих близких (* ^ ω ^) \n " \
    # + link('Мы в телеграм', 'https://t.me/asiaparty')

ban = "1. Мошенничество и шантаж (＃＞＜)\n" \
      "2. Порно без цензурных пикселей (￢_￢;)\n" \
      "3. Передать личную жалобу модератору\n" \
      "4. Забей, погнали дальше знакомиться o(>ω<)o"

claim_text = "Напиши подробнее свою жалобу. Модераторы с ней однакомятся"

admin_menu = "Что делать будем, семпай? ( ◡‿◡ *) \n" \
             "1. Банить негодяев ψ(▼へ▼メ)～→ \n" \
             "2. Вычисли по id (・人・) \n" \
             "3. Вычисли по username (・人・) \n" \
             "4. Потерять божий дар ＼(º □ º l|l)/"

warning_ban = "Сообщение от модератора:\n- Убедительно просим незамедлительно изменить свою анкету, она нарушает " \
              "политику нашего портала " \
              "В ином случае мы направим к Вам Якудзу!"

hello_text = "Меня зовут Акира, я помогу найти интересных для тебя людей из Москвы"

delete_q = "Ты уверен, что хочешь покинуть нас? (μ_μ)"

no_found = "Мне не удалось найти пары для тебя (・人・)"

form = "Вот твоя анкета: "

age_out_of_range = "Бот предназначен для пользователей от 18 до 35 лет"

text_out_of_range = "Превышен лимит в 400 символов, попробуй снова"

invalid_answer = "Нет такого варианта ответа"

set_gender = "Давай заполним анкету!\nДля начала выбери свой пол"

def set_interest(): return random.choice(["Кто тебя интересует?", "Кого ты ищешь?"])


def set_name(): return random.choice(["Как тебя зовут?", "Можно твое имя?", "Теперь нужно указать имя"])


def set_age(): return random.choice(["Damn, какое красивое имя, ", "Рада знакомству, ", "Супер, буду звать тебя "])


def enough(): return random.choice(["На сегодня достаточно, приходи завтра",
                                    "Достигнут дневной лимит, жду тебя завтра!",
                                    "Продолжишь завтра, на сегодня все)"])


set_text = "Теперь расскажи немного о себе:\n" \
           "- чем занимаешься, увлечения\n" \
           "- откуда ты/национальность\n" \
           "- кого ищешь и чем предалагаешь заняться"

set_photo = "Отправляй свое фото!"

check_liked = "сперва просмотри тех, кому понравилась твоя анкета!"


def like_match(): return random.choice(["У тебя произошел мэтч! ", "Вау, взаимная симпатия!"])


ban_thq = "Спасибо, мы обязательно исправим ситуацию!"

notice = "Это совет от Акиры - как не стать жертвой мошенников? Будь осторожнее когда после знакомства:\n" \
         "- тебя просят прислать личные фотографии интимного характера.Их могут использовать против тебя.\n" \
         "- тебе прислали ссылку, в которой необходимо ввести личные данные.\n" \
         "- тебя просят одолжить денег или сделать покупку, например билеты в кино/театр.\n" \
         "- тебе предлагают выгодную сделку, платные, инвестиционные и другие услуги."

instruction = "Небольшая инструкция по боту. Я буду присылать тебе анкеты, твоя задача - оставлять реакцию на них:\n" \
              "❤️ - понравился человечек\n" \
              "👎 - не понравился человечек\n" \
              "🚫 - подать жалобу на человека\n\n" \
              "Если тот, кого ты лайкнул ответит взаимностью - тебе придет сообщение!\n\n" \
              "(Анкеты могут повторяться из-за маленькой базы, приложение только набирает обороты)"


def ad():
    return random.choice([
        "А ты в курсе про наши <a href='https://t.me/asiaparty'>азиатские вечеринки</a> в Москве? "
        "Тусим каждую субботу, не пропусти",
        "В эту субботу город заснет и только настоящие тусеры застанут <a href='https://t.me/asiaparty'>АЗИЯ ПАТИ</a>!",
        "Больше, чем просто азиатские вечеринки в Москве - <a href='https://t.me/asiaparty'>ASIAN KINGS</a>. Ждем тебя каждую субботу!",
        "Вливайся в семью <a href='https://t.me/asiaparty'>ASIAN KINGS</a> - где каждую субботу проводят бомбезные вечеринки в центре Москвы!",
        "<a href='https://t.me/asiaparty'>ASIAN KINGS</a> - единство наций и дружба народов на одном танцполе каждую субботу!",
        "<a href='https://t.me/asiaparty'>ASIAN KINGS</a> - там, где все свои!",
        "Damn, тебе сегодня повезло! Ты получил бесплатную проходку на <a href='https://t.me/asiaparty'>ASIAN KINGS</a> в эту субботу, "
        "просто покажи переписку на входе!",
        "Знакомьтесь, листайте мемчики и приходите на вечеринки от <a href='https://t.me/asiaparty'>Asian Kings</a>!"
    ])


def q_boys() -> str:
    return random.choice(["По парням, значит...)", "Ты что, гей... Прикольно)", "Ах ты, шалун)))"])


def q_girls() -> str:
    return random.choice(["Значит по девчонкам...)", "Подруг ищешь, или не совсем?)", "Только не шали...)"])


def liked(a: dict):
    l = len(a['liked'])
    if l == 1:
        return random.choice(["Кто-то тобой заинтересовался", "Псс, тебя лайкнули)"])
    elif a['interest'] == 'парни':
        return f"{a['name']}, {l} парней из Москвы хотят с тобой познакомиться!"
    elif a['interest'] == 'девушки':
        return f"{a['name']}, {l} девушек из Москвы хотят с тобой познакомиться!"


def like_list(a: dict):
    return random.choice(["Твоя анкета понравилась данному пользователю:",
                          "Смотри, кто тобой заинтересовался!",
                          "Данный пользователь хочет с тобой познакомиться!"
                          ]) + (f" (и еще {len(a['liked'])-1}" if len(a['liked']) > 1 else "") + "\n\n"


def cap(a: dict):
    if a['text'] == '':
        return f"{a['name']}, {a['age']}"
    else:
        return f"{a['name']}, {a['age']}, {a['text']}"


def miss_u():
    return random.choice(["Ты где? Я уже соскучилась, давай возвращайся!)\n\nА пока твоя анкета будет неактивна",
                          "Я пока отключила твою анкету, включу как решишь продолжить)",
                          "Хей? Тебя давно не видно(\n\nПока отключу твою анкету, включу как решишь продолжить)"])


def daily_miss_u():
    return random.choice(["Новый день новые знакомства! Возвращайся, тебя уже ждут!",
                          "Хей! Продолжим листать анкеты?"])


def day_fact():
    fact = [
        "Слово «самба» означает «тереться пупками».",
        "Кетчуп вытекает из бутылки со скоростью 30 километров в год.",
        "Рекордная длительность полёта курицы – 13 секунд.",
        "Коровы мычат с региональным акцентом.",
        "Знакомо то чувство, когда твой язык покалывает после ананаса? В ананасе есть фермент, переваривающий другие белки. Так что когда ты ешь ананас, ананас ест тебя.",
        "Корова может подняться по лестнице, но не может спуститься.",
        "В мире всего 7% левшей.",
        "В пиве мало витаминов. По этому пиво нужно пить много",
        "В алфавите 32 буквы. Подумай об этом, если твой план Б не сработает",
        "Чтобы не сидеть без денег - приляг",
        "Все грибы съедобны. Просто некоторые — один раз.",
        "На самом деле девушки умеют хранить секреты. Группами. Человек по 40.",
        "Создатель этого бота был азиатом. Но это не точно."
    ]
    return "Факт дня:\n\n" + random.choice(fact)
