from time import sleep

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)

    match bmi:
        case _ if bmi <= 18.4:
            print(f"Your BMI is {bmi}. You are underweight. Eat more nutritiously")
            return
        case _ if bmi <= 24.9:
            print(f"Your BMI is {bmi}. You are at normal weight. Keep it up!")
            return
        case _ if bmi <= 29.9:
            print(f"Your BMI is {bmi}. You are overweight. Be careful about your diet")
            return
        case _ if bmi <= 34.9:
            print(f"Your BMI is {bmi}. You are obese (class I). Be very careful")
            return
        case _ if bmi <= 39.9:
            print(f"Your BMI is {bmi}. You are obese (class II). Seek medical advice as soon as possible")
            return
        case _:
            print(f"Your BMI is {bmi}. You are Morbid obese (class III). Seek medical help immediately")
            return
    

if __name__ == "__main__":
    while True:
        entry = input("Enter your weight and height with seperating by \",\": ").lower().strip()

        weight, height = entry.split(",")
        weight = float(weight)
        height = float(height)

        bmi_calculator(weight, height)
        sleep(0.5)
