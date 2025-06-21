from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, ClassVar
import csv


@dataclass
class Player:
    """Represents a tennis player that can be paired into a doubles team.

    Attributes
    ----------
    name : str
        Player's display name (unique identifier).
    base_swing : int
        Baseline-shot ability.
    net_work : int
        Ability at the net.
    serve : int
        Serve quality.
    is_fast : int
        Speed / court-coverage metric.
    is_balanced : int
        Balance / stability metric.
    is_cunning : int
        Tactical cleverness metric.
    dislikes : List[str]
        Names of players this player refuses to partner with.
    """

    name: str
    base_swing: int
    net_work: int
    serve: int
    is_fast: int
    is_balanced: int
    is_cunning: int
    group: int = -1
    dislikes: List[str] = field(default_factory=list)

    # ---------------------------------------------------------------------
    # Factory / IO helpers
    # ---------------------------------------------------------------------

    @classmethod
    def load_csv(cls, filepath: str, delimiter: str = ",") -> List["Player"]:
        """Load a CSV file and return a list of ``Player`` instances.

        Expected columns (case-sensitive):
            name, base_swing, net_work, serve, is_fast, is_balanced, is_cunning, group, dislikes
        The *dislikes* column can contain zero or more names separated by semicolons.
        """
        players: List["Player"] = []
        with open(filepath, newline="") as fh:
            reader = csv.DictReader(fh, delimiter=delimiter)
            for row in reader:
                try:
                    dislikes_raw = row.get("dislikes", "") or ""
                    dislikes = [s.strip() for s in dislikes_raw.split(";") if s.strip()]
                    group_val = int(row.get("group", -1)) if row.get("group", "").strip() else -1
                    players.append(
                        cls(
                            name=row["name"].strip(),
                            base_swing=int(row["base_swing"]),
                            net_work=int(row["net_work"]),
                            serve=int(row["serve"]),
                            is_fast=int(row["is_fast"]),
                            is_balanced=int(row["is_balanced"]),
                            is_cunning=int(row["is_cunning"]),
                            group=group_val,
                            dislikes=dislikes,
                        )
                    )
                except KeyError as exc:
                    raise ValueError(f"Missing required column {exc.args[0]!r} in CSV") from exc
        return players

    # Convenience methods -------------------------------------------------

    def total_skill(self) -> int:
        """Simple aggregate score that could be used as a strength metric."""
        return (
            self.base_swing
            + self.net_work
            + self.serve
            + self.is_fast
            + self.is_balanced
            + self.is_cunning
        )

    def dislikes_player(self, other: "Player") -> bool:
        """Return True if *other* is in this player's `dislikes` list."""
        return other.name in self.dislikes

    # Representation ------------------------------------------------------

    def __str__(self) -> str:  # pragma: no cover
        return f"Player({self.name})"

    def __repr__(self) -> str:  # pragma: no cover
        return (
            "Player("
            f"name={self.name!r}, base_swing={self.base_swing}, net_work={self.net_work}, "
            f"serve={self.serve}, is_fast={self.is_fast}, is_balanced={self.is_balanced}, "
            f"is_cunning={self.is_cunning}, group={self.group}, dislikes={self.dislikes!r})"
        )
