from django.contrib import admin
from main.models import Client, Kviz
from django.db import models


class KvizAdmin(admin.ModelAdmin):
    change_list_template = "main/admin/changelist_view.html"

    list_display = [
        "messanger", "messanger_name", "name", "nickname", "user_id",
        "phone", "unique_key", "created_at_tag", "interes", 
        "profession", "work_experience", "birth_year", "min_zp",
        "citizenship", "residence", "skills", "responsible", "instrument",
        "partner", "brigada", "car", "rate_work", "have_ip",
        "another_skills", "NAKCT", "installation_window_frame",
        "installation_foil_cylinders", "installation_kflex", 
        "installation_PPU_shell", "foam_glass_installation", 
        "manufacture_shell", "spraying_PPU", "another_insulator_skills",
        "pipelines", "airducts", "reservoirs", "equipment",
        "another_can_installer_skills", "manual_electric_arc", "semiautomatic",
        "argon", "gasfired", "plasma", "welding_gas_environment",
        "another_welding", "can_weld_simple_constructions", "can_weld_building_frames",
        "can_weld_columns", "can_weld_pipelines", "can_weld_energy_boilers",
        "can_weld_equipment", "can_weld_another", "read_drawings_diagrams",
        "know_norms_standards", "conducting_hydrotests", "organizational_skills",
        "working_with_tools", "another_installer_skills", "OPF",
        "activity_direction", "activity_region", "contract_price", "ceh_count",
        "interest_professions", "region_professions",
        "organization_form2", "email_form2", "message_form2", "has_work",
        "has_work_another", "permanent_job",
        "temporary_job", "job_without_registration", "schedulefivetwo",
        "shift_schedule", "dayly_pay", "piecework_payment", "any_job", "work_another",
        "call", "vk", "tg", "whatsapp"
    ]

    @admin.display(description="Дата и время")
    def created_at_tag(self, obj):
        return obj.created_at.strftime("%Y.%m.%d %H.%M")

    @admin.display(description="User ID")
    def user_id(self, obj):
        return obj.client.id

    @admin.display(description="Никнейм")
    def nickname(self, obj):
        return obj.client.nickname

    @admin.display(description="Имя, которое указал пользователь")
    def name(self, obj):
        return obj.client.name

    @admin.display(description="ТГ/ВК")
    def messanger(self, obj):
        return obj.client.messanger
    
    @admin.display(description="Уникальный ключ")
    def unique_key(self, obj):
        return f"{obj.client.id}-{obj.count}"
    
    @admin.display(description="Имя в ТГ/ВК")
    def messanger_name(self, obj):
        return obj.client.messanger_name
    
    def get_form(self, request, obj=None, **kwargs):
        4/0
        return 6/0

    def get_list_display(self, request):
        list_display = super().get_list_display(request)

        # Заменяем все булевы поля на кастомное отображение
        def boolean_icon(obj, field_name):
            value = getattr(obj, field_name)
            if value is True:
                return 'Да'
            elif value is False:
                return ' '
            return '-'

        # Создаем динамические методы для всех булевых полей
        for field in self.model._meta.get_fields():
            if isinstance(field, models.BooleanField):
                # Привязываем метод к админу
                setattr(self, f'display_{field.name}', lambda obj, fn=field.name: boolean_icon(obj, fn))
                setattr(getattr(self, f'display_{field.name}'), 'short_description', f'{field.verbose_name}')
                # Добавляем в list_display
                list_display = list(list_display)
                list_display[list_display.index(field.name)] = f'display_{field.name}'
        return list_display
    

admin.site.register(Client)
admin.site.register(Kviz, KvizAdmin)