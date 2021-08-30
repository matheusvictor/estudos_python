def gera_frequencia_nota(semitons):
    chave = semitons
    if (semitons < -12):
        chave = semitons + 12
    elif (semitons > 12):
        chave = semitons - 12

    notas = {
        "-12": "A",
        "-11": "Bb",
        "-10": "B",
        "-9": "C",
        "-8": "Db",
        "-7": "D",
        "-6": "Eb",
        "-5": "E",
        "-4": "F",
        "-3": "Gb",
        "-2": "G",
        "-1": "Ab",
        "0": "A",
        "1": "A#",
        "2": "B",
        "3": "C",
        "4": "C#",
        "5": "D",
        "6": "D#",
        "7": "E",
        "8": "F",
        "9": "F#",
        "10": "G",
        "11": "G#",
        "12": "A"
    }

    frequencia = round(440 * 2 ** (semitons / 12), 4)

    i = frequencia % 2

    if (i == 0):
        frequencia = int(frequencia)
        return [
            str(frequencia),
            notas[f"{chave}"]
        ]
    else:
        return [
            f'{frequencia:.4f}',
            notas[f"{chave}"]
        ]
