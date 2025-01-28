import sys
import re
import settings


def getheader(title, css):
    header = '<!DOCTYPE html>\n'
    header += '<html lang="en">\n'
    header += '<head>\n'
    header += '\t<meta charset="UTF-8">\n'
    header += '\t<meta name="viewport" content="width=device-width,'
    header += ' initial-scale=1.0">\n'
    if css.find(".css") != -1:
        header += '\t<link rel="stylesheet" href="' + css + '">\n'
    header += '\t<title>'+title+'</title>\n'
    header += '</head>\n'
    header += '<body>\n'
    return header


def getfooter():
    footer = '</body>\n</html>\n'
    return footer


def checkargs():
    if len(sys.argv) != 2:
        print("Error : template file missing")
        exit(1)
    filename = sys.argv[1]
    filename = filename[filename.find("."):]
    if (filename != ".template"):
        print("Error : bad extension")
        exit(1)


def get_template():
    try:
        template = ""
        with open(sys.argv[1], 'r') as file:
            lines = file.readlines()
            for line in lines:
                template += line
            return template
    except FileNotFoundError:
        print("Error: file not found")
        exit(1)


def interpolate(template, **kwargs):
    def replace(match):
        key = match.group(1)
        return kwargs.get(key, f"{{{key}}}")
    pattern = r"\{(\w+)\}"
    template = re.sub(pattern, replace, template)
    return template


def build_page(template):
    page = getheader('My CV', "style.css")
    page += template
    page += getfooter()
    return page


checkargs()
template = get_template()
v = vars(settings)
template = interpolate(template, **v)
template = build_page(template)
with open("cv.html", "w") as file:
    file.write(template)
