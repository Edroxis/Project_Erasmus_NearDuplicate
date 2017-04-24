# -*- coding: utf-8 -*-
from simhash import Simhash

if __name__ == '__main__':
    sim = Simhash("hello world")
    print(sim.get_hash())
    sim = Simhash("hello world.")
    print(sim.get_hash())
    sim = Simhash("hello world!")
    print(sim.get_hash())
    sim = Simhash("hello aetqye tworlqy qyr d.")
    print(sim.get_hash())
    sim = Simhash("""Demain, dès l'aube, à l'heure où blanchit la campagne,
                    Je partirai. Vois-tu, je sais que tu m'attends.
                    J'irai par la forêt, j'irai par la montagne.
                    Je ne puis demeurer loin de toi plus longtemps.""")
    print(sim.get_hash())
    sim = Simhash("""Demain, dès l'aube, à l'heure où blanchit la campagne,
                    Je partirai. Vois-tu, je sais que tu m'attends.
                    J'irai par la forêt, j'irai par la montagne.
                    Je ne puis demeurer loin de toi plus longtemps. 
                    [...]
                    Et quand j'arriverai, je mettrai sur ta tombe
                    Un bouquet de houx vert et de bruyère en fleur.""")
    print(sim.get_hash())
