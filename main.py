# 22. O‘quv jadvali

class Schedule:
    def __init__(self, subject, hours):
        self.subject = subject      # fan nomi
        self.hours = hours          # haftalik dars soatlari

    def total_hours(self):
        """Fan bo‘yicha haftalik dars soatlari"""
        return self.hours

    def __str__(self):
        return f"{self.subject:14} | {self.hours:2} soat / hafta"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class MathSchedule(Schedule):
    def __str__(self):
        return f"📐 {self.subject:12} → {self.hours:2} soat / hafta"


class PhysicsSchedule(Schedule):
    def __str__(self):
        return f"⚛️ {self.subject:12} → {self.hours:2} soat / hafta"


# Qo‘shimcha fanlar uchun misollar (foydali bo‘lishi mumkin)
class LiteratureSchedule(Schedule):
    def __str__(self):
        return f"📚 {self.subject:12} → {self.hours:2} soat / hafta"


class EnglishSchedule(Schedule):
    def __str__(self):
        return f"🇬🇧 {self.subject:12} → {self.hours:2} soat / hafta"


# --------------------------------------------------
# Umumiy o‘quv jadvalini chiqarish
# --------------------------------------------------

def show_weekly_schedule(subjects):
    print("\n" + "═" * 55)
    print("     HAFTALIK O‘QUV JADVALI — DARS SOATLARI     ".center(55))
    print("═" * 55)
    print("Fan nomi               Haftalik soatlar")
    print("─" * 55)

    total = 0

    for subj in subjects:
        print(subj)
        total += subj.total_hours()

    hours = total
    print("─" * 55)
    print(f"Jami haftalik dars soatlari:          {hours:2} soat")
    print("═" * 55 + "\n")


# Test ma'lumotlari
fanlar = [
    MathSchedule("Matematika", 4),
    PhysicsSchedule("Fizika", 3),
    LiteratureSchedule("Adabiyot", 2),
    EnglishSchedule("Ingliz tili", 4),
    MathSchedule("Geometriya", 2),
    PhysicsSchedule("Kimyo", 2),
]

show_weekly_schedule(fanlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol jadvalingiz:\n")
misol_fanlar = [
    MathSchedule("Matematika", 3),
    PhysicsSchedule("Fizika", 2),
]

show_weekly_schedule(misol_fanlar)
