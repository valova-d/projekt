{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "6027aaf1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cesta nalezena\n"
     ]
    },
    {
     "data": {
      "image/png": "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dX/fqK2tDR0dHR59arPZUFxc7Hd/B/xvh0DrRJrD4YDFYsFNN90UsNzly5eRl5eH0aNH4+GHH0Zzc3OUWtivsbERo0aNwpe//GV85zvfwYULFwKW162///a3v2HPnj146qmngpbVob/9MU3gunjxInp7e5GZmemxPDMzEx0dHT7X6ejo8Fm+p6cHFy9ejFhb/RFCYNWqVbj33ntx1113+S2XnZ2NV155BXV1ddi5cycmTpyI2bNn49ChQ1Fr61e/+lW88cYbeOedd/Dqq6+io6MDM2fOxGeffeazvG593WfXrl34/PPPsWzZMr9ldOjvgfr26XD29771wl0nkq5evYrVq1fjiSeeCHiz1/z8fGzduhW7d+9GbW0tkpOTcc8996C1tTVqbZ03bx7efPNNHDhwAC+88AKOHTuGBx98EE6n0+86uvX366+/jhEjRmDBggUBy+nQ34EY714fQQz81SyECPhL2ld5X8uj4emnn8Z//dd/4b333gtYbuLEiZg4caL7+YwZM3D27Fn8+te/xqxZsyLdTADyQ9xn8uTJmDFjBsaPH4/XX38dq1at8rmOTn3dZ/PmzZg3bx5ycnL8ltGhv/0Jd38f7DqRcP36dSxevBgulwu//e1vA5adPn26x0SIe+65B1OmTMFLL72EDRs2RLqpAIBFixa5/33XXXfh7rvvRl5eHvbs2RMwEOjS3wDw2muv4R/+4R+CnqvSob8DMc2I69Zbb0ViYqLXL5kLFy54/eLpk5WV5bO81WrFLbfcErG2+vL9738fu3fvRkNDQ8jpWW40ffr0mP4aSktLw+TJk/22Qae+7nPmzBns378f3/72t8NeN9b93TeDM5z9vW+9cNeJhOvXr2PhwoVoa2vDvn37wk6tkZCQgKlTp8Z0G2RnZyMvLy9gG3TpbwB49913cerUqUHt7zr0941ME7iGDRuGoqIi9wyxPvv27cPMmTN9rjNjxgyv8nv37sXdd9+NpKSkiLX1RkIIPP3009i5cycOHDiAcePGDaqe5uZmZGdnK25d6JxOJz766CO/bdChrwfasmULRo0aha9//ethrxvr/h43bhyysrI8+vTatWs4ePCg3/0d8L8dAq2jWl/Qam1txf79+wf1w0UIgZaWlphug88++wxnz54N2AYd+rvP5s2bUVRUhIKCgrDX1aG/PcRqVkgkvPXWWyIpKUls3rxZnDx5UlRWVoq0tDTx6aefCiGEWL16tSgrK3OXP336tEhNTRU//OEPxcmTJ8XmzZtFUlKS+MMf/hC1Nn/ve98TGRkZorGxUZw/f979uHLlirvMwHb/y7/8i6ivrxeffPKJ+POf/yxWr14tAIi6urqotftHP/qRaGxsFKdPnxbvv/++ePjhh8WIESO07usb9fb2ijFjxohnn33W6zVd+vvSpUuiublZNDc3CwDixRdfFM3Nze7Zd2vXrhUZGRli586d4sSJE6K0tFRkZ2eLzs5Odx1lZWUes2r/4z/+QyQmJoq1a9eKjz76SKxdu1ZYrVbx/vvvR6Xd169fF4888ogYPXq0aGlp8djnnU6n33avWbNG/OlPfxL//d//LZqbm0VFRYWwWq3i6NGjUWn3pUuXxI9+9CNx+PBh0dbWJhoaGsSMGTPEbbfdpnV/93E4HCI1NVX87ne/81lHLPp7KEwVuIQQ4uWXXxZ5eXli2LBhYsqUKR7TysvLy0VxcbFH+cbGRlFYWCiGDRsmxo4d63fDRgoAn48tW7b4bfe6devE+PHjRXJysvjSl74k7r33XrFnz56otnvRokUiOztbJCUliZycHLFgwQLx4Ycf+m2zELHv6xu98847AoA4deqU12u69HffNPyBj/LyciGEnBL/3HPPiaysLGGz2cSsWbPEiRMnPOooLi52l++zY8cOMXHiRJGUlCTy8/OVB+BA7W5ra/O7zzc0NPhtd2VlpRgzZowYNmyYGDlypCgpKRGHDx+OWruvXLkiSkpKxMiRI0VSUpIYM2aMKC8vF+3t7R516Nbfff71X/9VpKSkiM8//9xnHbHo76FgWhMiIjIU05zjIiKi+MDARUREhsLARUREhsLARUREhsLARUREhsLARUREhsLARUREhsLARUREhsLARUREhsLARUREhsLARUREhsLARUREhvL/eouZzs1IQk0AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import csv\n",
    "from collections import deque\n",
    "import matplotlib.pyplot as plt\n",
    "import random\n",
    "\n",
    "class Bludiste:\n",
    "    def __init__(self, parametry:np.ndarray):\n",
    "        self.parametry = parametry\n",
    "        self.n = parametry.shape[0]\n",
    "def nacti_data(nazev_souboru):\n",
    "    soubor = np.genfromtxt(nazev_souboru, delimiter=\",\", dtype=int)\n",
    "    matice = soubor.astype(bool)\n",
    "    return matice\n",
    "  \n",
    "def vykresli_cestu(matice, trasa, nalezeni):\n",
    "    plt.imshow(matice, cmap='gray_r', origin='upper')\n",
    "    if nalezeni ==1:\n",
    "        for x, y in trasa:\n",
    "            plt.plot(y,x, marker='o', color='red', markersize=7)\n",
    "\n",
    "def najdi_cestu(zadane_bludiste):\n",
    "    navstiveno = set()\n",
    "    k_prohledani = deque()\n",
    "    k_prohledani.append((0,0))\n",
    "    navstiveno.add((0,0))\n",
    "\n",
    "    predchudce = {}\n",
    "    cesta = []\n",
    "    nalezeno = 0\n",
    "    while k_prohledani:\n",
    "        x, y = k_prohledani.popleft()\n",
    "        if x==n-1 and y==n-1:\n",
    "            print (\"cesta nalezena\")\n",
    "            nalezeno = 1\n",
    "            break\n",
    "        smery = [(0,1), (1,0), (0,-1), (-1,0)]\n",
    "        random.shuffle(smery)\n",
    "\n",
    "        for dx, dy in smery:\n",
    "            nx, ny = x+dx, y+dy\n",
    "\n",
    "            if 0<=nx<n and 0<=ny<n and not zadane_bludiste[nx,ny] and (nx, ny) not in navstiveno:\n",
    "                    k_prohledani.append((nx, ny))\n",
    "                    navstiveno.add((nx, ny))\n",
    "                    predchudce[(nx, ny)] = (x, y)\n",
    "\n",
    "\n",
    "    if x != n-1 and y!= n-1:\n",
    "        print(\"cesta nenalezena\")\n",
    "\n",
    "    if nalezeno == 1:\n",
    "        while (x,y) != (0,0):\n",
    "            \n",
    "            cesta.append((x,y))\n",
    "            x, y = predchudce[(x, y)]\n",
    "        cesta.append((0,0)) \n",
    "    vykresli_cestu(bludiste.parametry, cesta, nalezeno)        \n",
    "\n",
    "data = nacti_data(\"data/maze_3.csv\")\n",
    "bludiste = Bludiste(data)\n",
    "n = data.shape[0]\n",
    "  \n",
    "najdi_cestu(bludiste.parametry)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
