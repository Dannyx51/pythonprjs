class piece:
  def __init__(self, piece, team):
    self.name = piece
    self.team = team
    self.fg = ''

    if self.team == "black":
      self.fg = '31'
    else:
      self.fg = '35'

    