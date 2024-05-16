print("How many kilometers did you cycle today?")
kms = input()
miles = round(float(kms) / 1.60934, 2)
print(f"{kms} kilometers! So that is equal to {miles} miles")