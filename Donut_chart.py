import matplotlib.pyplot as plt

sizes = [30, 20, 25, 25]
labels = ['Python', 'Java', 'C++', 'Javascript']

fig, ax = plt.subplot()
wedges, texts = ax.pie(sizes, labels=labels)

centre_circle = plt.Circle((0,0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

plt.title('Programming Language Usage')
plt.show()