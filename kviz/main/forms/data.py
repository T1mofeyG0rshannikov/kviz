
'''
FORMS = [
    FormI(
        name="interes",
        title="Что Вас интересует?",
        type="radio",
        options=[
            Option(
                text="Работа",
                next="work"
            ),
            Option(
                text="Подработка",
                next="has_work"
            ),
            Option(
                text="Халтуры",
            ),
            Option(
                text="Сотрудники",
                next="interest_professions"
            ),
            Option(
                text="Объекты строительства",
                next="OPF"
            ),
            Option(
                text="Продолжить объем работ",
                next="object_region"
            ),
            Option(
                text="Сотрудничество",
                next="cooperation"
            )
        ],
        next="profession"
    ),
    Form(
        name="profession",
        type="radio",
        title="Какая у Вас профессия?",
        options=[
            Option(
                text="Сварщик",
                next="welding_types"
            ),
            Option(
                text="Монтажник ТТ",
                next="installer_skills"
            ),
            Option(
                text="Изолировщик на термоизоляции",
                next="insulator_skills"
            ),
            Option(
                text="Разнорабочий",
            ),
            Option(
                text="Электрик",
            ),
            Option(
                text="Сантехник",
            ),
            Option(
                text="Отделочник-универсал",
            ),
            Option(
                text="Плиточник",
            )
        ],
        next="work_experience"
    ),
    Form(
        name="installer_skills",
        title="Укажите Ваши навыки.",
        type="checkbox",
        options=[
            Option(
                text="Читаю чертежи и схемы",
                field="read_drawings_diagrams"
            ),
            Option(
                text="Знаю нормы и стандарты",
                field="know_norms_standards"
            ),
            Option(
                text="Провожу гидроиспытания",
                field="conducting_hydrotests"
            ),
            Option(
                text="Организаторские навыки",
                field="organizational_skills"
            ),
            Option(
                text="Работа с инструментами",
                field="working_with_tools"
            )
        ],
        next="qualities",
        another_field="another_installer_skills"
    ),
    Form(
        name="work",
        type="checkbox",
        title="Какая работа Вас интересует?",
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
        next="profession",
        another_field="work_another"
    ),
    Form(
        name="has_work",
        type="radio",
        title="У вас есть основная работа?",
        options=[
            Option(
                text="Да, пятидневка",
            ),
            Option(
                text="Да, сменный график",
            ),
            Option(
                text="Да, свободный график",
            ),
            Option(
                text="Нет, только подработки",
            ),
            Option(
                text="Нет",
            )
        ],
        next="profession",
        another_field="has_work_another"
    ),

    Form(
        name="region",
        title="Укажите регион объекта",
        type="radio",
        options=[
            Option(
                text="Москва"
            ),
            Option(
                text="Санкт-Петербург"
            )
        ],
        next="form2"
    ),
    Form(
        name="welding_types",
        type="checkbox",
        title="Какими видами сварки вы владеете?",
        options=[
            Option(
                text="Ручная электродуговая",
                field="manual_electric_arc"
            ),
            Option(
                text="Полуавтоматическая",
                field="semiautomatic"
            ),
            Option(
                text="Аргоновая",
                field="argon"
            ),
            Option(
                text="Газовая",
                field="gasfired"
            ),
            Option(
                text="Плазменная",
                field="plasma"
            ),
            Option(
                text="Сварка в среде газа",
                field="welding_gas_environment"
            )
        ],
        next="welding_what",
        another_field="another_welding"
    ),
    Form(
        name="welding_what",
        type="checkbox",
        title="Что вы умеете сваривать?",
        options=[
            Option(
                text="Простые конструкции",
                field="can_weld_simple_constructions"
            ),
            Option(
                text="Каркасы зданий",
                field="can_weld_building_frames"
            ),
            Option(
                text="Балки, колонны",
                field="can_weld_columns"
            ),
            Option(
                text="Трубопроводы",
                field="can_weld_pipelines"
            ),
            Option(
                text="Энергетические котлы",
                field="can_weld_energy_boilers"
            ),
            Option(
                text="Оборудование",
                field="can_weld_equipment"
            ),
        ],
        next="welder_qualities",
        another_field="can_weld_another"
    ),
    Form(
        name="welder_qualities",
        type="checkbox",
        title="Укажите Ваши преимущества",
        options=[
            Option(
                text="Ответственный",
                field="responsible"
            ),
            Option(
                text="НАКСТ",
                field="NAKCT"
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
        next="work_experience",
        another_field="another_skills"
    ),
    Form(
        name="qualities",
        type="checkbox",
        title="Укажите Ваши преимущества",
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
        next="work_experience",
        another_field="another_skills"
    ),
    Form(
        name="work_experience",
        type="radio",
        title="Какой у Вас опыт работ по специальности?",
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
        next="birth_year"
    ),
    Form(
        name="birth_year",
        type="text",
        title="Напишите год вашего рождения",
        next="min_zp"
    ),
    Form(
        name="min_zp",
        type="text",
        title="Укажите минимальную приемлемую для вас зарплату",
        next="citizenship"
    ),
    Form(
        name="citizenship",
        type="radio",
        title="Какое у вас гражданство?",
        options=[
            Option(
                text="РФ"
            ),
            Option(
                text="РБ"
            )
        ],
        next="residence"
    ),
    Form(
        name="residence",
        type="radio",
        title="Укажите ваше место жительства",
        options=[
            Option(
                text="Москва"
            ),
            Option(
                text="Санкт-Петербург"
            )
        ],
        next="skills"
    ),
    Form(
        name="skills",
        type="text",
        title="Расскажите о своих профессиональных навыках.",
        next="-callback"
    ),
    Form(
        name="insulator_skills",
        type="checkbox",
        title="Укажите ваши навыки.",
        options=[
            Option(
                text="Монтаж окожушки",
                field="installation_window_frame"
            ),
            Option(
                text="Монтаж фольг. цилиндров",
                field="installation_foil_cylinders"
            ),
            Option(
                text="Монтаж K-Flex",
                field="installation_kflex"
            ),
            Option(
                text="Монтаж ППУ скорлупы",
                field="installation_PPU_shell"
            ),
            Option(
                text="Монтаж пеностекла",
                field="foam_glass_installation"
            ),
            Option(
                text="Изготовление окожушки",
                field="manufacture_shell"
            ),
            Option(
                text="Напыление ППУ",
                field="spraying_PPU"
            )
        ],
        next="insulate_what",
        another_field="another_installer_skills"
    ),
    Form(
        name="insulate_what",
        type="checkbox",
        title="Что вы умеете изолировать?",
        options=[
            Option(
                text="Трубопроводы",
                field="pipelines"
            ),
            Option(
                text="Воздуховоды",
                field="airducts"
            ),
            Option(
                text="Резервуары",
                field="reservoirs"
            ),
            Option(
                text="Оборудование",
                field="equipment"
            )
        ],
        next="qualities",
        another_field="another_can_installer_skills"
    ),
    Form(
        name="OPF",
        title="Организационно-правовая форма вашей деятельности.",
        type="radio",
        options=[
            Option(
                text="ООО",
            ),
            Option(
                text="ИП",
            ),
            Option(
                text="Самозанятый",
                next="profession"
            ),
            Option(
                text="Нет",
                next="profession"
            )
        ],
        next="activity_direction"
    ),
    Form(   
        name="activity_direction",
        title="Укажите направление вашей деятельности",
        type="text",
        next="activity_region",
    ),
    Form(
        name="activity_region",
        title="В каком регионе Вас интересуют объекты?",
        type="radio",
        options=[
            Option(
                text="Москва"
            ),
            Option(
                text="Санкт-Петербург"
            ),
            Option(
                text="Все регионы РФ"
            )
        ],
        another_field="activity_region",
        next="contract_price"
    ),
    Form(
        name="contract_price",
        title="В каком ценовом диапазоне вас интересует цена контрактов?",
        type="text",
        next="ceh_count",
    ),
    Form(
        name="ceh_count",
        title="Какова численность вашего рабочего персонала?",
        type="text",
        next="-callback",
    ),
    Form(
        name="interest_professions",
        type="text",
        title="Специалисты каких профессий Вас интересуют?",
        next="region_professions"
    ),
    Form(
        name="region_professions",
        type="radio",
        title="В каком городе Вам нужны сотрудники?",
        options=[
            Option(
                text="Москва"
            ),
            Option(
                text="Санкт-Петербург"
            )
        ],
        next="-cooperation"
    ),
    Form(
        name="object_region",
        title="Укажите регион объекта",
        type="radio",
        options=[
            Option(
                text="Москва"
            ),
            Option(
                text="Санкт-Петербург"
            )
        ],
        another_field="another_object_region",
        next="-cooperation"
    )
]
'''

forms_graph = {form.name: form for form in FORMS}


def find_furthest(start: Form, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    if start not in forms_tree:
        return 1

    ns = [n for n in set(forms_tree[start]) - visited]
    if not ns:
        return 1
    
    return max(find_furthest(n, visited) for n in ns) + 1


#print(forms_graph)

forms_tree = {}
for form in FORMS:
    n = []
    if form.next:
        n.append(form.next)
    if form.options:
        for option in form.options:
            if option.next:
                n.append(option.next)

    forms_tree[form.name] = n


#print(forms_tree)

#print(find_furthest('interes'))