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
                modal_id="welding_types"
            ),
            Option(
                text="Монтажник ТТ",
                modal_id="installer_skills"
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
        name="installer_skills",
        question="Укажите Ваши навыки.",
        type="checkbox",
        options=[
            Option(
                text="Читаю чертежи и схемы"
            ),
            Option(
                text="Знаю нормы и стандарты"
            ),
            Option(
                text="Провожу гидроиспытания"
            ),
            Option(
                text="Организаторские навыки"
            ),
            Option(
                text="Работа с инструментами"
            )
        ],
        modal_id="qualities"
    ),
    Form(
        name="work",
        type="checkbox",
        question="Какая работа Вас интересует?",

        options=[
            Option(
                text="Постоянная",
                field="permanent_job"
            ),
            Option(
                text="Временная",
                field="temporary_job"
            ),
            Option(
                text="Без оформления",
                field="job_without_registration"
            ),
            Option(
                text="График 5/2",
                field="schedulefivetwo"
            ),
            Option(
                text="Сменный график",
                field="shift_schedule"
            ),
            Option(
                text="Ежедневная оплата",
                field="dayly_pay"
            ),
            Option(
                text="Сдельная оплата",
                field="piecework_payment"
            ),
            Option(
                text="Любая работа",
                field="any_job"
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
        name="qualities",
        type="checkbox",
        question="Укажите Ваши преимущества",
        options=[
            Option(
                text="Ответственный",
                field="responsible"
            ),
            Option(
                text="Свой инструмент",
                field="instrument"
            ),
            Option(
                text="Есть напарник",
                field="partner"
            ),
            Option(
                text="Есть бригада",
                field="brigada"
            ),
            Option(
                text="Есть авто",
                field="car"
            ),
            Option(
                text="Могу оценить объём работ",
                field="rate_work"
            ),
            Option(
                text="Есть ИП/самозанятость",
                field="have_ip"
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
        modal_id="min_zp"
    ),
    Form(
        name="min_zp",
        field="min_zp",
        type="text",
        question="Укажите минимальную приемлемую для вас зарплату",
        another=False,
        modal_id="citizenship"
    ),
    Form(
        name="citizenship",
        field="citizenship",
        type="radio",
        question="Какое у вас гражданство?",
        options=[
            Option(
                text="РФ"
            ),
            Option(
                text="РБ"
            )
        ],
        modal_id="residence"
    ),
    Form(
        name="residence",
        field="residence",
        type="radio",
        question="Укажите ваше место жительства",
        options=[
            Option(
                text="Москва"
            ),
            Option(
                text="Санкт-Петербург"
            )
        ],
        modal_id="skills"
    ),
    Form(
        name="skills",
        field="skills",
        type="text",
        question="Расскажите о своих профессиональных навыках.",
        another=False,
        modal_id="-callback"
    )
]

#Специалисты каких профессий Вас интересуют?
#……………….
