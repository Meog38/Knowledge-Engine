import csv
import re

def clean_string(s):
    if not s:
        return 'null'
    
    s = str(s).lower().strip()
    s = s.replace(' ', '_').replace('-', '_').replace('.', '')
    # Remove qualquer caractere que não seja letra minúscula, número ou underscore
    s = re.sub(r'[^a-z0-9_]', '', s)
    
    if s and s[0].isdigit():
        s = 'c_' + s
    
    return s if s else 'null'

def clean_number(n):
    try:
        if n is None or str(n).strip() == "":
            return "null"
        
        n = str(n).replace(",", ".")
        num = float(n)
        
        # deixa número mais limpo (10 ao invés de 10.0)
        return str(int(num)) if num.is_integer() else str(num)
    
    except:
        return "null"

def main():
    with open('cryptocurrency_market_dataset.csv', 'r', encoding='utf-8') as f_in, \
         open('base_conhecimento.pl', 'w', encoding='utf-8') as f_out:
        
        reader = csv.DictReader(f_in)
        
        contador = 0
        for row in reader:
            coin = clean_string(row.get('coin_id'))
            symbol = clean_string(row.get('symbol'))
            price = clean_number(row.get('current_price_usd'))
            rank = clean_number(row.get('market_cap_rank'))
            change = clean_number(row.get('price_change_24h_percent'))
            ath = clean_number(row.get('all_time_high_usd'))
            vol = clean_number(row.get('total_volume_usd'))

            # filtros importantes
            if coin == "null" or symbol == "null":
                continue
            if price == "null" or rank == "null" or change == "null":
                continue
            if ath == "null" or vol == "null":
                continue

            predicado = f"crypto({coin}, {symbol}, {price}, {rank}, {change}, {ath}, {vol}).\n"
            f_out.write(predicado)
            contador += 1

            # limita tamanho da base
            if contador >= 500:
                break

    print(f"Sucesso! {contador} predicados foram gerados no arquivo 'base_conhecimento.pl'.")

if __name__ == '__main__':
    main()