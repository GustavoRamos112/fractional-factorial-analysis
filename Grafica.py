import matplotlib.pyplot as plt
import numpy as np

def grafica_modelo(modelo, nombre, fontsize=10, inicio=0, final=0, largo=18, ancho=6, _dpi=100, mostrar=False, color='blue'):

    #? Gráfica de efectos principales
    coeficientes = modelo.params
    comb = list(coeficientes.index.values)

    if final == 0:
        final = len(coeficientes)
        
    x = np.linspace(-1, 1, 3)

    fig = plt.figure(figsize=(largo,ancho))
    gs = fig.add_gridspec(nrows=1, ncols=(final-inicio)+1, hspace=0)
    axs = gs.subplots(sharex=True, sharey=True)

    j = 0
    for i in range(inicio-1, final):
        y = float(coeficientes[i])*x
        axs[j].plot(x, y, color=color)
        axs[j].set_title(f"{comb[i]}", fontsize=fontsize)
        j += 1

    plt.subplots_adjust(left=0.06, bottom=0.11, right=0.97, wspace=0.0, hspace=0)

    plt.savefig(nombre, dpi=_dpi)

    if mostrar:
        plt.show()