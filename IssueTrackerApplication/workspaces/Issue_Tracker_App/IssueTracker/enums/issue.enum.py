from enum import Enum

class IssueStatus(Enum):
    NEW = 'new'
    INPROGRESS = 'inprogress' 
    RESOLVED = 'resolved'
    FEEDBACK = 'feedback'
    OPEN = 'open'
    CLOSED = 'closed'

class IssueLabel(Enum):
    ONE = 'one'
    TWO = 'two'
    THREE = 'three'
    FOUR = 'four'
    FIVE = 'five'

class IssueType(Enum):
    TASK = 'task'
    BUG = 'bug'
    FEATURE = 'feature'
    OTHER = 'other'

# STATUS=(
#     ('NEW','new'),
#     ('INPROGRESS','inprogress'),
#     ('RESOLVED','resolved'),
#     ('FEEDBACK','feedback'),
#     ('OPEN','open'),
#     ('CLOSED','closed')
# )

# Label=(
#     ('1','one'),
#     ('2','two'),
#     ('3','three'),
#     ('4','four'),
#     ('5','five')
# )

# TYPES=(
#     ('TASK','task'),
#     ('BUG','bug'),
#     ('FEATURE','feature'),
#     ('OTHER','other')
# )