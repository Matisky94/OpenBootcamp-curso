import time
tiempo_segundos = time.time()
tiempo_cadena = time.ctime(tiempo_segundos)
print(tiempo_cadena)
tiempo_st = time.gmtime(tiempo_segundos)
if tiempo_st.tm_hour >= 22:
    print("Es hora de ir a casa")
else:
    tiempo_restante = 21 - tiempo_st.tm_hour
    print("Quedan", tiempo_restante, "horas y", 60 - tiempo_st.tm_min, "minutos de trabajo")

# Hice el ejercicio para la zona horaria de Argentina (UTC-3)