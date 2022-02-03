def voto(ano_nascimento):
    from datetime import datetime

    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: voto OPCIONAL!'
    else:
        return f'Com {idade} anos: voto OBRIGATÓRIO!'


print(voto(1998))
print(voto(2012))
print(voto(1937))
