import requests

def nome_api(nome: str):
    url = f"https://api.nationalize.io/?name={nome}"
    resposta = requests.get(url)
    return resposta.json()

def exibir_resultado(dados: dict):
    nome = dados.get("name", "desconhecido")
    count = dados.get("count", 0)
    paises = dados.get("country", [])

    print(f"\n🔍 Resultado para o nome: {nome.capitalize()}")
    print(f"   Total de ocorrências no mundo: {count:,}\n")

    if paises:
        print("   Países mais prováveis:")
        for pais in paises:
            pais_id = pais["country_id"]
            prob = pais["probability"] * 100
            print(f"   - {pais_id}: {prob:.1f}%")
    else:
        print("   Nenhum país encontrado para esse nome.")

nome_completo = input("Digite seu nome completo: ").strip()
partes = nome_completo.split()
primeiro_nome = partes[0]
sobrenome = partes[-1]

print("\n--- Primeiro Nome ---")
exibir_resultado(nome_api(primeiro_nome))

print("\n--- Sobrenome ---")
exibir_resultado(nome_api(sobrenome))