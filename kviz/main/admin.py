from django.contrib import admin
from main.models import Client, Form, Kviz, Option
from django.db import models
from django.forms import inlineformset_factory


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
        "call", "vk", "tg", "whatsapp", "object_region", "another_object_region",
        "plastering_works", "painting_work", "laying_tiles", "installation_drywall",
        "wallpapering", "installation_doors_and_windows", "ceiling_installation",
        "comprehensive_finishing", "metro"
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

    @admin.display(description="ТГ/ВК")
    def messanger(self, obj):
        return obj.client.messanger
    
    @admin.display(description="Уникальный ключ")
    def unique_key(self, obj):
        return f"{obj.client.id}-{obj.count}"
    
    @admin.display(description="Имя в ТГ/ВК")
    def messanger_name(self, obj):
        return obj.client.messanger_name

    def get_list_display(self, request):
        list_display = super().get_list_display(request)

        def boolean_icon(obj, field_name):
            value = getattr(obj, field_name)
            if value is True:
                return 'Да'
            elif value is False:
                return ' '
            return '-'

        for field in self.model._meta.get_fields():
            if isinstance(field, models.BooleanField):
                setattr(self, f'display_{field.name}', lambda obj, fn=field.name: boolean_icon(obj, fn))
                setattr(getattr(self, f'display_{field.name}'), 'short_description', f'{field.verbose_name}')
                list_display = list(list_display)
                list_display[list_display.index(field.name)] = f'display_{field.name}'
        return list_display
    

OptionInlineFormSet = inlineformset_factory(
    Form,
    Option,
    fk_name='form',
    fields=('text', 'next'),
    extra=3,
    can_delete=True
)

class OptionInline(admin.StackedInline):
    model = Option
    formset = OptionInlineFormSet
    fk_name='form'


class FormAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


admin.site.register(Client)
admin.site.register(Kviz, KvizAdmin)
admin.site.register(Form, FormAdmin)