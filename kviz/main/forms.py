from main.form import Form, Option


FORMS = [
    Form(
        name="first",
        question="Что Вас интересует?",
        field="interes",
        type="radio",
        options=[
            Option(
                text="Работа",
                value="Работа",
                modal_id="work"
            ),
            Option(
                text="Подработка",
                value="Подработка",
                modal_id="has_work"
            ),
            Option(
                text="Халтуры",
                value="Халтуры"
            ),
            Option(
                text="Сотрудники",
                value="Сотрудники"
            ),
            Option(
                text="Объекты строительства",
                value="Объекты строительства"
            ),
            Option(
                text="Продолжить объем работ",
                value="Продолжить объем работ"
            ),
            Option(
                text="Сотрудничество",
                value="Сотрудничество"
            )
        ],
        another=False
    ),
    Form(
        name="profession",
        field="profession",
        type="radio",
        question="Какая у Вас профессия?",
        options=[
            Option(
                text="Сварщик",
                modal_id="work_experience"
            ),
            Option(
                text="Монтажник ТТ",
                modal_id="work_experience"
            ),
            Option(
                text="Изолировщик на термоизоляции",
                modal_id="work_experience"
            ),
            Option(
                text="Разнорабочий",
                modal_id="work_experience"
            ),
            Option(
                text="Электрик",
                modal_id="work_experience"
            ),
            Option(
                text="Сантехник",
                modal_id="work_experience"
            ),
            Option(
                text="Отделочник-универсал",
                modal_id="work_experience"
            ),
            Option(
                text="Плиточник",
                modal_id="work_experience"
            )
        ],
        modal_id="work_experience"
    ),
    Form(
        name="work",
        type="checkbox",
        question="Какая работа Вас интересует?",
        options=[
            Option(
                text="Постоянная"
            ),
            Option(
                text="Временная",
            ),
            Option(
                text="Без оформления",
            ),
            Option(
                text="График 5/2",
            ),
            Option(
                text="Сменный график",
            ),
            Option(
                text="Ежедневная оплата",
            ),
            Option(
                text="Сдельная оплата",
            ),
            Option(
                text="Любая работа",
            ),
        ],
        modal_id="profession"
    ),
    Form(
        name="has_work",
        type="radio",
        question="У вас есть основная работа?",
        options=[
            Option(
                text="Да, пятидневка",
                modal_id="profession"
            ),
            Option(
                text="Да, сменный график",
                modal_id="profession"
            ),
            Option(
                text="Да, свободный график",
                modal_id="profession"
            ),
            Option(
                text="Нет, только подработки",
                modal_id="profession"
            ),
            Option(
                text="Нет",
                modal_id="profession"
            )
        ]
    ),

    Form(
        name="region",
        question="Укажите регион объекта",
        type="radio",
        options=[
            Option(
                text="Москва"
            ),
            Option(
                text="Санкт-Петербург"
            )
        ],
        modal_id="form2"
    ),
    Form(
        name="welding_types",
        type="checkbox",
        question="Какими видами сварки вы владеете?",
        options=[
            Option(
                text="Ручная электродуговая"
            ),
            Option(
                text="Полуавтоматическая"
            ),
            Option(
                text="Аргоновая"
            ),
            Option(
                text="Газовая"
            ),
            Option(
                text="Плазменная"
            ),
            Option(
                text="Сварка в среде газа"
            )
        ]
    ),
    Form(
        name="welding_what",
        type="checkbox",
        question="Что вы умеете сваривать?",
        options=[
            Option(
                text="Простые конструкции"
            ),
            Option(
                text="Каркасы зданий"
            ),
            Option(
                text="Балки, колонны"
            ),
            Option(
                text="Трубопроводы"
            ),
            Option(
                text="Энергетические котлы"
            ),
            Option(
                text="Оборудование"
            )
        ],
        modal_id="welder_qualities"
    ),
    Form(
        name="welder_qualities",
        type="checkbox",
        question="Укажите Ваши преимущества",
        options=[
            Option(
                text="Ответственный"
            ),
            Option(
                text="НАКСТ"
            ),
            Option(
                text="Свой инструмент"
            ),
            Option(
                text="Есть напарник"
            ),
            Option(
                text="Есть бригада"
            ),
            Option(
                text="Есть авто"
            ),
            Option(
                text="Могу оценить объём работ"
            ),
            Option(
                text="Есть ИП/самозанятость"
            )
        ],
        modal_id="work_experience"
    ),
    Form(
        name="work_experience",
        field="work_experience",
        type="radio",
        question="Какой у Вас опыт работ по специальности?",
        options=[
            Option(
                text="без опыта"
            ),
            Option(
                text="До 1 года"
            ),
            Option(
                text="1-5 лет"
            ),
            Option(
                text="5 - 10 лет"
            ),
            Option(
                text="Более 10 лет"
            )
        ],
        another=False,
        modal_id="birth_year"
    ),
    Form(
        name="birth_year",
        field="birth_year",
        type="text",
        question="Напишите год вашего рождения",
        another=False,
        modal_id="birth_year"
    ),
    Form(
        name="min_zp",
        type="text",
        question="Укажите минимальную приемлемую для вас зарплату",
        another=False,
        modal_id="birth_year"
    )
]
