def add_style(fields):
    for field_name, field in fields.items():
        field.widget.attrs['class'] = 'form-control mt-2'
