from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Section:
    section_id: str
    days: Tuple[str, ...]
    start: int
    end: int
    
    def __str__(self):
        days_str = "/".join(self.days)
        return f"{self.section_id} {days_str} {self.start}-{self.end}"

@dataclass
class Course:
    course_id: str
    name: str
    credits: int
    sections: List[Section] = field(default_factory=list)

    def __str__(self):
        return f"{self.course_id} ({self.credits} credits)"

@dataclass
class Metrics:
    runtime: float = 0.0
    nodes_visited: int = 0
    backtracks: int = 0