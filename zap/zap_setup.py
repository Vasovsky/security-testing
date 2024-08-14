import time
from zapv2 import ZAPv2

def zap_scan(target):
    zap = ZAPv2()
    zap.urlopen(target)
    time.sleep(2)  # Даем время для загрузки страницы

    print(f"Сканируем {target}")
    zap.spider.scan(target)
    time.sleep(5)

    while int(zap.spider.status()) < 100:
        print(f"Идет сканирование... {zap.spider.status()}% завершено")
        time.sleep(2)

    print("Сканирование завершено!")
    print(f"Найденные уязвимости: {zap.core.alerts_summary(target)}")

if __name__ == "__main__":
    zap_scan("http://example.com")
 
