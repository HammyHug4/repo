# 1 pekerjaan di bagi menjadi 2 tugas
import asyncio
data = [1, 2, 3, 4]
async def hitung_kuadrat(nama, data):
    hasil = []
    for x in data:
        print(f"{nama}: menghitung {x}²")
        hasil.append(x ** 2)
        await asyncio.sleep(0)
    return hasil
async def main():
    hasil_A, hasil_B = await asyncio.gather(
        hitung_kuadrat("Tugas A", data[:2]),
        hitung_kuadrat("Tugas B", data[2:])
    )
    hasil = hasil_A + hasil_B
    print("Hasil:", hasil)
    print("Jumlah:", sum(hasil))
asyncio.run(main())
# 2 Pekerjaan dengan masing masing tugas