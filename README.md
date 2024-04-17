# Alinhamento de Sequências
Esse projeto foi desenvolvido durante a disciplina de "Algoritmos para Bioinformática" da Universidade Federal de Minas Gerais (UFMG).

## Descrição do Projeto
O objetivo deste trabalho é implementar o algoritmo de Needleman-Wunsch para construir alinhamentos globais par-a-par de sequências de proteínas. 
Foi utilizado a matriz BLOSUM62, que traz em cada célula a penalidade de se substituir um aminoácido por outro ou mesmo a manutenção dele.

## How to Use


1. Instale a biblioteca necessária

```bash
pip install numpy
```

2. Clone o repositório "align_seq" para sua máquina local
   
```sh
git@github.com:furunoluiza/align_seq.git
```

3. Execute o programa

```bash
python3 ./main.py
```

Como input, o programa pedirá as duas sequências de aminoácidos e a penalidade. O output será as sequências alinhadas.
