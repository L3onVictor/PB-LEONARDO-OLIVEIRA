from hashlib import sha1

print("🗡️ Bem-vindo(a), Guerreiro(a) de Hyrule! O destino de um reino está nas suas mãos! 🌟")
print("A Triforce aguarda um novo portador... Somente quem é digno pode revelar os seus segredos ocultos.")

while True:
    palavra = str(input("💫 Fale a palavra mística que abrirá o portal para a sabedoria e o poder: "))

    palavra_hash = sha1(palavra.encode()).hexdigest()
    
    print("✨ Você ouviu o som da Triforce se ativando... Aqui está a magia que o(a) conecta à Triforce:")
    print(f"🌟 {palavra_hash} 🌟")

    cond = str(input("🗡️ Deseja continuar sua jornada pela Hyrule? [Y/n]")).upper()

    if cond == 'N':
        print("💫 O(a) Guerreiro(a) descansará por agora. Até logo, nobre GUerreiro(a).")
        break
