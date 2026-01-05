import random
import math
import matplotlib.pyplot as plt

# Proiect 2 – Varianta 9
# Sa se genereze prin doua metode variabila Beta(2, 4) (curs 6). Sa segenereze histogramele asociate celor doua metode. (curs 8).

# -------------------------
# Metoda 1 (curs 6): Beta din doua Gama
# Beta(parametru_a, parametru_b): X = gama_a/(gama_a+gama_b), gama_a~Gama(0,1,parametru_a), gama_b~Gama(0,1,parametru_b)
# Pentru parametru_a = 2 si parametru_b = 4 (intregi), Gama(0,1,k) se obtine ca suma de k exponentiale Exp(1)
# Exp(1): -ln(U)


def beta_din_gama(numar_selectii):
    esantion_beta = []
    for _ in range(numar_selectii):
        gama_a = -math.log(random.random()) - math.log(random.random())
        gama_b = (
            -math.log(random.random())
            - math.log(random.random())
            - math.log(random.random())
            - math.log(random.random())
        )
        esantion_beta.append(gama_a / (gama_a + gama_b))
    return esantion_beta

# -------------------------
# Metoda 2 (curs 6): Statistica de ordine
# Pentru parametru_a = 2, parametru_b = 4: n = parametru_a + parametru_b - 1 = 5
# Generam valori_uniforme[0..4] uniforme, sortam, luam valori_uniforme[1] (U(2))
# -------------------------

def beta_din_statistica_ordin(numar_selectii):
    esantion_beta = []
    for _ in range(numar_selectii):
        valori_uniforme = [random.random() for _ in range(5)]
        valori_uniforme.sort()
        esantion_beta.append(valori_uniforme[1])
    return esantion_beta


# -------------------------
# Validare (curs 8): media si dispersia de selectie
# media = (sum valori)/n
# dispersia = media_patratica - media^2
# media_patratica = (sum valori^2)/n
# -------------------------

# Validare cu media si dispersia de selectie (curs 8)

def media_si_dispersia_selectiei(valori):
    n = len(valori)
    media = sum(valori) / n
    media_patratica = sum(x * x for x in valori) / n
    dispersia = media_patratica - media * media
    return media, dispersia


numar_selectii = 100_000

parametru_a = 2
parametru_b = 4

# Valori teoretice (curs 6): E[X] = parametru_a/(parametru_a+parametru_b), Var[X] = parametru_a*parametru_b/((parametru_a+parametru_b)^2 (parametru_a+parametru_b+1))

media_teoretica = parametru_a / (parametru_a + parametru_b)
dispersia_teoretica = (
    parametru_a * parametru_b
    / ((parametru_a + parametru_b) ** 2 * (parametru_a + parametru_b + 1))
)

esantion_beta_gama = beta_din_gama(numar_selectii)
esantion_beta_ordin = beta_din_statistica_ordin(numar_selectii)

# Histograme (afisate pe aceeasi figura)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(esantion_beta_gama, bins=50, density=True)
plt.title("Beta(2,4) - metoda Gama")

plt.subplot(1, 2, 2)
plt.hist(esantion_beta_ordin, bins=50, density=True)
plt.title("Beta(2,4) - statistica de ordin")

plt.tight_layout()
plt.show()

# Validare statistica

media_gama, dispersia_gama = media_si_dispersia_selectiei(esantion_beta_gama)
media_ordin, dispersia_ordin = media_si_dispersia_selectiei(esantion_beta_ordin)

print("Metoda Gama:", media_gama, dispersia_gama)
print("Statistica de ordin:", media_ordin, dispersia_ordin)
print("Teoretic:", media_teoretica, dispersia_teoretica)
