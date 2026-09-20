import numpy as np
# Códigos de Álgebra Linear para a calculadora

# Soma

class Soma:
    def __init__(self, vetorA1, vetorA2, vetorB1, vetorB2):
        self.vetorA1 = vetorA1
        self.vetorB1 = vetorB1
        self.vetorA2 = vetorA2
        self.vetorB2 = vetorB2

    def VetoresNumpy(self, vetorA1, vetorB1):
        x = np.arrange(self.vetorA1, self.vetorA2)
        y = np.arrange(self.vetorB1, self.vetorB2)

                