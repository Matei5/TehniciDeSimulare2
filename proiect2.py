import random
import math
import matplotlib.pyplot as plt

# Proiect 2 – Varianta 9
# Generez prin doua metode variabila Beta(2, 4). Generez histogramele asociate celor doua metode. 

# -------------------------
# Metoda 1: Beta din doua Gama
# Folosesc relatia Beta(a,b): X = X1/(X1+X2), unde X1~=Gama(0,1,a), X2~=Gama(0,1,b)
# Pentru a = 2 si b = 4 (intregi), obtin Gama(0,1,k) ca suma de k exponentiale Exp(1)
# Generez Exp(1) prin: -ln(U)
# -------------------------

def beta_din_gama(numar_selectii):
    esantion_beta = []
    for _ in range(numar_selectii):
        gama_a = - math.log(random.random()) - math.log(random.random())
        gama_b = - math.log(random.random()) - math.log(random.random()) - math.log(random.random()) - math.log(random.random())
        esantion_beta.append(gama_a / (gama_a + gama_b))
    return esantion_beta

# -------------------------
# Metoda 2: Statistica de ordine
# Pentru a = 2, b = 4 am: n = a + b - 1 = 5
# Generez U1..U5 uniforme, le sortez, iau U(2)
# -------------------------

def beta_din_statistica_ordin(numar_selectii):
    esantion_beta = []
    for _ in range(numar_selectii):
        valori_uniforme = [random.random() for _ in range(5)]
        valori_uniforme.sort()
        esantion_beta.append(valori_uniforme[1])
    return esantion_beta


# Validare cu media si dispersia de selectie

def media_si_dispersia_selectiei(valori):
    n = len(valori)
    media = sum(valori) / n
    media_patratica = sum(x * x for x in valori) / n
    dispersia = media_patratica - media * media
    return media, dispersia


numar_selectii = 100_000

parametru_a = 2
parametru_b = 4

# Valori teoretice: E[X] = a/(a+b), Var[X] = ab/((a+b)^2 (a+b+1))

media_teoretica = parametru_a / (parametru_a + parametru_b)
dispersia_teoretica = parametru_a * parametru_b / ((parametru_a + parametru_b) ** 2 * (parametru_a + parametru_b + 1))

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
