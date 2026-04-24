from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Emprestimo:
    id: int
    crianca_id: int
    brinquedo_id: int
    data_emprestimo: datetime
    data_devolucao: Optional[datetime] = None
    status: str = "ativo"
    multa: float = 0.0