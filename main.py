from fundamentos_criptografia_hashing import *

from tabulate import tabulate

print ("CRIPTOGRAFANDO")

secretKey = os.urandom(32)

mensagem=b'desenvolvedor.io'

dadosCriptografados = encrypt_AES_GCM(mensagem, secretKey)

dados = {
    'mensagem': mensagem,
    'senha': binascii.hexlify(secretKey),
    'Cipher': binascii.hexlify(dadosCriptografados[0]),
    'Initialization vector (iv)': binascii.hexlify(dadosCriptografados[1]),
    'Auth tag': binascii.hexlify(dadosCriptografados[2])
}

print (tabulate(dados.items(), tablefmt='fancy_grid'))


print ("CRIPTOGRAFANDO")

decryptedMsg = decrypt_AES_GCM(dadosCriptografados, secretKey)
print("mensagem descriptografada", decryptedMsg.decode())


print ("HASHING")

digest = hashlib.sha256(mensagem).hexdigest()
print(f'hash da mensagem\n{mensagem.decode()}={digest}')

