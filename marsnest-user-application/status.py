import enum

# Using enum class create enumerations
class Status(enum.Enum):
  Pending = 1
  InProgress = 2
  Approved = 3
  Rejected = 4