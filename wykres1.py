import matplotlib.pyplot as plt

# pip install matplotlib

# biblioteka do wykresu

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 9, 11]

plt.plot(x, y, c="red")
plt.title("Wykres liniowy")

plt.xlabel("OŚ X")
plt.ylabel("OŚ Y")

plt.show()
