import sys


def getheader(title, css):
    header = '<!DOCTYPE html>\n'
    header += '<html lang="en">\n'
    header += '<head>\n'
    header += '\t<meta charset="UTF-8">\n'
    header += '\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    if css.find(".css") != -1:
        header += '\t<link rel="stylesheet" href="' + css + '">\n'
    header += '\t<title>'+title+'</title>\n'
    header += '</head>\n'
    header += '<body>\n'
    return header


def getfooter():
    footer = '</body>\n</html>\n'
    return footer


def get_electrons(electrons):
    electrons = electrons[electrons.find(":") + 1:]
    lst = []
    while electrons.find(" ") != -1:
        el = int(electrons[:electrons.find(" ")])
        lst.append(el)
        electrons = electrons[electrons.find(" ") + 1:].strip()
    lst.append(int(electrons))
    return lst


def extract_data(line):
    data = line[line.find(":") + 1: line.find(",")]
    return data


def next_element(line):
    line = line[line.find(",")+1:]
    return line 


def parsefile(path):
    data = {}
    with open(path) as file:
        line = file.readline()
        while(len(line) !=0):
            element = {}
            el = line[:line.find(" =")].strip()
            line = line[line.find(" =")+2:].strip()
            element["position"] = int(extract_data(line))
            line = next_element(line)
            element["number"] = int(extract_data(line))
            line = next_element(line)
            element["small"] = extract_data(line)
            line = next_element(line)
            element["molar"] = float(extract_data(line))
            line = next_element(line)
            element["electron"] = get_electrons(line)
            data[el] = element
            line = file.readline()
    return data


def create_col(el, data):
        element = '\n\t\t\t<td style="border: 1px solid black; padding:5px">'
        element += '\n\t\t\t\t<h4>' + data['small'] + '</h4>'
        element += '\n\t\t\t\t<ul>'
        element += '\n\t\t\t\t\t<li>No '+ str(data['number']) + '</li>'
        element += '\n\t\t\t\t\t<li>' + el + '</li>'
        element += '\n\t\t\t\t\t<li>' + str(data['molar']) + '</li>'
        element += '\n\t\t\t\t\t<li>' + str(sum(data['electron'])) + ' e</li>'
        element += '\n\t\t\t\t</ul>'
        element += '\n\t\t\t</td>\n'
        return element


def create_blank_col():
        element = '\t\t\t<td style="border: none; padding:5px"></td>\n'
        return element

def generate_css():
    filename = 'periodic_table.css'
    css = "*\n{\n\tmargin:0;\n\tpadding:0\n}\n\n"
    css += "body\n{\n\tfont-size: 12px;\n}\n\n"
    css += "h4\n{\n\tfont-family: Arial, Helvetica, sans-serif;\n"
    css += "\tfont-size: 2rem;\n}\n\n"
    css += "table\n{\n\tborder-collapse: collapse;\n"
    css += "\ttable-layout: fixed;\n\twidth: 100%;\n}\n\n"
    css += "td\n{\n\twidth: var(100/18)'%';\n}\n\n"
    css += "li\n{\n\tfont-size: 0.7rem;\n\tlist-style: none;"
    css += "\n\tposition: relative;\n\tleft:7px\n}"
    with open(filename,'w') as file:
        file.write(css)


def main():
    page = getheader('Mendeleiev','periodic_table.css')

    data = parsefile("periodic_table.txt")
    offset = [1, 2, 2, 19, 19, 19, 19, 19, 19]
    complement = [17, 12, 12, 0, 0, 0,0,0]
    row = 0
    page += "\t<table>\n"
    count = 0
    page += "\t\t<tr>"
    for el in data:
        while count < data[el]['position']:
                page += create_blank_col()
                count +=1
        if data[el]['position'] == count:
            page += create_col(el, data[el])
            count +=1
        if (count >= 18):
            page += "\t\t</tr>\n"
            count = 0
            row +=1
            if row < 7:
                page += "\t\t<tr>\n"
    page +="\t</table>\n"
    page += getfooter()
    with open("page.html", 'w') as file:
        file.write(page)
    generate_css()


if __name__ == "__main__":
    main()