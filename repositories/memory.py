from typing import Dict
from domain.crianca import Crianca
from domain.brinquedo import Brinquedo
from domain.emprestimo import Emprestimo

class MemoryDB:
    def __init__(self):
        self.criancas = []
        self.brinquedos = []
        self.emprestimos = []

db = MemoryDB()