import enum

class ConfigEnv(str, enum.Enum):
    QA = "qa"
    PRD = "prd"

    @classmethod
    def from_value(cls, value):
        values = (env.value for env in cls)
        if value in values:
            return cls(value)
        raise ValueError(f"{value} is not a valid ConfigEnv value")