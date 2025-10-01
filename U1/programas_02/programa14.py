# Escribe un programa que reciba un número de bytes y muestre por pantalla cuantos
# GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario.

bytes_total = int(input("Introduce número de bytes: "))

# Sistema decimal (SI, 1000)
gb = bytes_total // 10**9
mb = (bytes_total % 10**9) // 10**6
kb = (bytes_total % 10**6) // 10**3
b = bytes_total % 10**3
print(f"{bytes_total} bytes en sistema decimal (SI): {gb} GB, {mb} MB, {kb} KB, {b} bytes")

# Sistema binario (IEC, 1024)
gib = bytes_total // (1024**3)
mib = (bytes_total % (1024**3)) // (1024**2)
kib = (bytes_total % (1024**2)) // 1024
b = bytes_total % 1024
print(f"{bytes_total} bytes en sistema binario (IEC): {gib} GiB, {mib} MiB, {kib} KiB, {b} bytes")
