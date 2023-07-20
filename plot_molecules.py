"""
    Passo a passo para execução do código:
    
    1. Certifique-se de ter instalado as bibliotecas necessárias:
       - numpy
       - matplotlib
       - astropy

    2. Altere o diretório dos arquivos de entrada e saída nas variáveis `path` e `destiny`, se necessário.

    3. Verifique os nomes dos arquivos de entrada `h2o_neutral.dat`, `h2o_cation.dat` e `h2o_anion.dat`.
       Caso estejam em diretórios diferentes, atualize os caminhos nas variáveis `source_1`, `source_2` e `source_3`.

    4. Os arquivos de entrada devem conter duas colunas: comprimento de onda (em micrômetros) e intensidade (em km/kmol).

    5. Execute o código para carregar os dados e plotar os gráficos de intensidade em função do comprimento de onda.

    6. Serão gerados três gráficos, um para cada molécula (H2O neutra, H2O catiônica e H2O aniônica),
       com as curvas de intensidade em função do comprimento de onda.

    7. Os gráficos serão exibidos na tela e também serão salvos nos formatos PDF e PNG no diretório especificado por `destiny`.

    8. Verifique os gráficos gerados no diretório de saída para análise e compartilhamento.

    9. Fique à vontade para ajustar as configurações de plotagem e os estilos dos gráficos conforme suas necessidades.

    Código escrito por Vitor Avelaneda -- Jul/2023.

"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.table import Table
import matplotlib as mpl

# Inicio do codigo

# Altere o diretório dos arquivos, se necessário 
path = '/home/vitor/Área de Trabalho/test/plot_moleculas/input/'
destiny = '/home/vitor/Área de Trabalho/test/plot_moleculas/output/'

# Altere o nome dos arquivos, se necessário 
source_1 = path + 'h2o_neutral.dat'
source_2 = path + 'h2o_cation.dat'
source_3 = path + 'h2o_anion.dat'

wavel_1, flux_1 = np.loadtxt(source_1, usecols=[0,1], unpack=True)
wavel_2, flux_2 = np.loadtxt(source_2, usecols=[0,1], unpack=True)
wavel_3, flux_3 = np.loadtxt(source_3, usecols=[0,1], unpack=True)

# Plotagem

fig = plt.figure(figsize=(7,5))

# Configurações do gráfico

plt.xlabel(u'Wavelength [$\mu$m]', {'fontsize': 18})
plt.ylabel(u'Intensity [km/kmol]', {'fontsize': 18})
plt.xticks(size=18)
plt.yticks(size=18)

# Plotando os dados
plt.plot(wavel_1, flux_1, color='#e10069', label = u'H$_{2}$O - Neutral') 
plt.plot(wavel_2, flux_2, color='#49297e', label = u'H$_{2}$O - Cation')
plt.plot(wavel_3, flux_3, color='b', label = u'H$_{2}$O - Anion')
     
plt.tight_layout(rect=(0,0,1,1))

plt.legend(fontsize=14, loc = 'upper right')

plt.show()

# salvando a figura
fig.savefig(destiny+'plot_molecules.pdf', dpi=fig.dpi)
fig.savefig(destiny+'plot_molecules.png', dpi=fig.dpi)


