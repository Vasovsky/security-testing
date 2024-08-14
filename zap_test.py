from zapv2 import ZAPv2

# Пробуем использовать полный URL для подключения
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}, apikey='YOUR_API_KEY_HERE')

try:
    version = zap.core.version()
    print(f"Подключено к ZAP API. Версия ZAP: {version}")
except Exception as e:
    print(f"Не удалось подключиться к ZAP API: {e}")

