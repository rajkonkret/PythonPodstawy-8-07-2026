import matplotlib.pyplot as plt

labels = ['Jabłka', "Banany", "Winogrono", "Pomarańcza"]
sizes = [30, 25, 20, 45]
colors = ["red", "blue", "green", 'yellow']

plt.pie(
    sizes, labels=labels, colors=colors, autopct='%1.1f%%',
    shadow=True,
    startangle=90,
    explode=(0.1, 0, 0, 0)
)

plt.axis('equal')

plt.savefig('wykres.png')
plt.show()
