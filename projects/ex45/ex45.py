import scenes

class Engine(object):

  chips = 100

  def __init__(self, scene_map):
    self.scene_map = scene_map

  print """
  ***WELCOME TO THE VEGAS VACATION LOSER'S PARLOR***
  \nChevy loses almost all of his money and has one last chance to win back
  his family's savings. 
  \nHe spots a crappy casino on the outskirts of town
  with games he knows how to play. 
  \nYour mission is to help Chevy win back his savings. You have %s 
  chips to begin, and you must have 100 chips to cash out and win. Good luck!
  """ % chips

  raw_input("press enter to continue") 

  def play(self):
    current_scene = self.scene_map.opening_scene()
    last_scene = self.scene_map.next_scene('finished')

    while current_scene != last_scene:
      next_scene_name = current_scene.enter()
      current_scene = self.scene_map.next_scene(next_scene_name)

    # current_scene.enter()

class Map(object):
  _scenes = {
  'war': scenes.War(),
  'rock_paper_scissors': scenes.RockPaperScissors(),
  'pick_a_number': scenes.PickNumber(),
  'flip_a_coin': scenes.FlipCoin(),
  'death': scenes.Death(),
  'cash_out': scenes.CashOut(),
    }

  def __init__(self, start_scene):
    self.start_scene = start_scene

  def next_scene(self, scene_name):
    val = Map._scenes.get(scene_name)
    return val

  def opening_scene(self):
    return self.next_scene(self.start_scene)

a_map = Map('flip_a_coin')
a_game = Engine(a_map)
a_game.play()
