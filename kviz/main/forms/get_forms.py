from main.models import Form
from main.forms.interface import FormI, OptionI


def find_furthest(start: FormI, forms_tree, forms):
    if start not in forms_tree:
        return 1

    ns = [n for n in set(forms_tree[start])]

    if not ns:
        return 1

    return max(find_furthest(n, forms_tree, forms) for n in ns) + 1


def get_forms():
    forms = Form.objects.all()
    forms = [
        FormI(
            name=form.name,
            title=form.title,
            type=form.type,
            options=[
                OptionI(
                    text=option.text,
                    next=option.next.name if option.next else '',
                    field=option.field
                ) for option in form.options.all()
            ],
            next=form.next.name if form.next else '',
            another_field=form.another_field,
            show_next=form.show_next
        ) for form in forms
    ]

    for form in forms:
        form.options_count = len(form.options)

    forms = {form.name: form for form in forms}


    forms_tree = {}
    for form in forms.values():
        n = []
        if form.next:
            n.append(form.next)
        if form.options:
            for option in form.options:
                if option.next:
                    n.append(option.next)

        forms_tree[form.name] = n

    for form in forms:
        forms[form].max_steps = find_furthest(form, forms_tree, forms)
    for form in forms:
        print(form, forms[form].max_steps)
    return forms