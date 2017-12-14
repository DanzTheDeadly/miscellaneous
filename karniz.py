text = '{}, изготовлен из {}, предназначен для штор из {}. В комплект входит: труба - {} шт., кронштейны - {} шт., кольца - {} шт. Чтобы полностью скомплектовать данный карниз необходимо добавить наконечники - {} шт. соответствующего диаметра.'
file = open(r'f:\marsal_result.txt', 'w')

def write_text():
    for line in open(r'f:\marsal.txt'):
        line_items = line.rstrip().split('\t')
        karniz = line_items[0].split(',')[0][:-12]
        material = "латуни" if line_items[1] == "Латунь" else "стали"
        weight = "лёгких и средней тяжести тканей" if int(line_items[4].split("x")[0]) <= 20 else "любых тканей"
        tube = 1 if "одинарный" in line_items[0] else 2
        kron = line_items[2]
        try:
            rings = int(line_items[3])
        except ValueError:
            rings = eval(line_items[3])
        ends = tube*2
        new_text = text.format(karniz, material, weight, tube, kron, rings, ends)
        print(new_text, file = file)

write_text()
file.close()
