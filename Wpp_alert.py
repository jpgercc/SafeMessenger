import pyautogui
import time

# Abrir o Chrome
pyautogui.press('win')
pyautogui.typewrite('chrome')
pyautogui.press('enter')

# Aguardar o Chrome abrir
time.sleep(2)

# Abrir uma guia do WhatsApp
pyautogui.hotkey('ctrl', 't')
pyautogui.typewrite('https://web.whatsapp.com/')
pyautogui.press('enter')

# Aguardar o WhatsApp carregar
time.sleep(5)

# Clicar no primeiro contato
pyautogui.click(x=299, y=283)

# Aguardar o chat abrir
time.sleep(2)

# Digitar e enviar mensagem
pyautogui.typewrite('MENSAGEM ENVIADA AUTOMATICAMENTE PRO PRIMEIRO CONTATO QUER O CÓDIGO ?PODE SER DE SUMA IMPORTANCIA')
pyautogui.press('enter')
