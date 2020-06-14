"""
5.  Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
    результаты из байтовового в строковый тип на кириллице.
"""
import subprocess

LIMIT_PING = 5

VARS = [
    ['ping', 'yandex.ru'],
    ['ping', 'youtube.com']
]

for args in VARS:
    ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    limit = 0
    for line in ping.stdout:
        if limit > LIMIT_PING:
            break

        result = line.decode('utf-8')
        print(result)
        limit += 1

# Результат вывода
# PING yandex.ru(yandex.ru (2a02:6b8:a::a)) 56 data bytes
# 64 bytes from yandex.ru (2a02:6b8:a::a): icmp_seq=1 ttl=56 time=11.0 ms
# 64 bytes from yandex.ru (2a02:6b8:a::a): icmp_seq=2 ttl=56 time=12.2 ms
# 64 bytes from yandex.ru (2a02:6b8:a::a): icmp_seq=3 ttl=56 time=10.4 ms
# 64 bytes from yandex.ru (2a02:6b8:a::a): icmp_seq=4 ttl=56 time=10.3 ms
# 64 bytes from yandex.ru (2a02:6b8:a::a): icmp_seq=5 ttl=56 time=11.3 ms
#
# PING youtube.com(lo-in-x5d.1e100.net (2a00:1450:4010:c0b::5d)) 56 data bytes
# 64 bytes from lo-in-x5d.1e100.net (2a00:1450:4010:c0b::5d): icmp_seq=1 ttl=109 time=21.1 ms
# 64 bytes from lo-in-x5d.1e100.net (2a00:1450:4010:c0b::5d): icmp_seq=2 ttl=109 time=20.0 ms
# 64 bytes from lo-in-x5d.1e100.net (2a00:1450:4010:c0b::5d): icmp_seq=3 ttl=109 time=20.3 ms
# 64 bytes from lo-in-x5d.1e100.net (2a00:1450:4010:c0b::5d): icmp_seq=4 ttl=109 time=21.0 ms
# 64 bytes from lo-in-x5d.1e100.net (2a00:1450:4010:c0b::5d): icmp_seq=5 ttl=109 time=19.9 ms
#
# Process finished with exit code 0

