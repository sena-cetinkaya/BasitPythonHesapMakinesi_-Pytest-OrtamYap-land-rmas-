from calculator import operations
from config import settings

def run():
    if settings.ENVIRONMENT != "development":
        print("Bu script sadece development ortamında çalıştırılabilir.")
        return

    print("Basit Hesap Makinesi")
    a = float(input("Birinci sayı: "))
    b = float(input("İkinci sayı: "))
    op = input("İşlem (+, -, *, /): ")

    if op == "+":
        print("Sonuç:", operations.add(a, b))
    elif op == "-":
        print("Sonuç:", operations.subtract(a, b))
    elif op == "*":
        print("Sonuç:", operations.multiply(a, b))
    elif op == "/":
        try:
            print("Sonuç:", operations.divide(a, b))
        except ValueError as e:
            print("Hata:", e)
    else:
        print("Geçersiz işlem!")

if __name__ == "__main__":
    run()
