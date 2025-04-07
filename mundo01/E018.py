from math import (sin, cos, tan, radians)
print('Dissecando ângulos.')
ang = float(input('Insira um ângulo qualquer:'))
print(f'Dado o ângulo {ang}, seu seno equivale á {sin(radians(ang)):.3f}, seu cosseno {cos(radians(ang)):.3f} e sua tangente {tan(radians(ang)):.3f}')
