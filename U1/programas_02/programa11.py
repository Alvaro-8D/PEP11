# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo
# de viaje hasta llegar a otra ciudad B es de N segundos. Escribe un programa que determine
# la hora de llegada a la ciudad B.

hh = int(input("Hora de salida (HH): "))
mm = int(input("Minutos de salida (MM): "))
ss = int(input("Segundos de salida (SS): "))
n = int(input("Duración del viaje en segundos: "))

total_seg = hh*3600 + mm*60 + ss + n
hh_llegada = (total_seg // 3600) % 24
mm_llegada = (total_seg % 3600) // 60
ss_llegada = total_seg % 60

print(f"Hora de llegada: {hh_llegada:02d}:{mm_llegada:02d}:{ss_llegada:02d}")