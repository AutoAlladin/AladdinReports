from string import Template


def prepare_temlate(path):
    with(open("templates\\files\\"+path, mode="r", encoding="UTF8")) as f:
        file1 = f.read()

    return Template(file1)

def get_report(template, uuuuu):
    return template.substitute(uuuuu)