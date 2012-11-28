# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

# Klassenhäufigkeit
fracs = [266198, 255421, 149917, 136456, 122025, 104227, 85476, 82404, 70796, 67450, 41590, 25679, 8439 + 1448]

# Klassen
labels = ['PN', 'PQ', 'UR', 'EX', 'EV', 'XY', 'PE', 'PO', 'EW', 'AC', 'MC', 'PS', 'VS + QL']

# Farben des pie charts
colors = [(200, 77, 95), (125, 194, 75), (216, 222, 174), (142, 189, 153), (221, 194, 63)]
colors = [tuple(i / 255. for i in c) for c in colors]
#colors = ['b', 'g', 'r', 'c', 'm', 'y', 'burlywood', 'w']

fig = plt.figure(1, figsize=(10, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

patches, texts, autotexts = ax.pie(fracs,
                                   labels=labels,
                                   colors=colors,
                                   autopct='%1.1f%%')

# Schriftgröße einstellen
proptease = fm.FontProperties()
proptease.set_size('medium')
plt.setp(texts, fontproperties=proptease)
plt.setp(autotexts, fontproperties=proptease)

#plt.show()
plt.savefig('labels_fancy.png')
