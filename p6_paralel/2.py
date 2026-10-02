# 2 Pekerjaan dengan masing masing tugas
import asyncio

data = [1, 2, 3, 4]

async def hitung_kuadrat(data):
    hasil = []
    for x in data:
        print(f"Tugas Kuadrat: {x}²")
        hasil.append(x ** 2)
        await asyncio.sleep(0)
    return hasil

async def hitung_kubik(data):
    hasil = []
    for x in data:
        print(f"Tugas Kubik: {x}³")
        hasil.append(x ** 3)
        await asyncio.sleep(0)
    return hasil

async def main():
    kuadrat, kubik = await asyncio.gather(
        hitung_kuadrat(data),
        hitung_kubik(data)
    )

    print("Hasil kuadrat:", kuadrat)
    print("Jumlah kuadrat:", sum(kuadrat))
    print("Hasil kubik:", kubik)
    print("Jumlah kubik:", sum(kubik))

asyncio.run(main())
