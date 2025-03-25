"""This file serves as an example file for users to edit enemies."""
from enemy_editor import EnemyEditor
from backups import defaults

#   I don't recommend using the game's fiddle directly 
#   (located in your game's directory, typically in the following path)
# path = r"C:\Program Files (x86)\Steam\steamapps\common\Fields of Mistria\__fiddle__.json"

# Instead, copy it somewhere else and edit it from there, and maybe back up the previous fiddle too
fiddle_path = r"<path-to-folder-with-fiddle>\__fiddle__.json"

editor = EnemyEditor(fiddle_path=fiddle_path)

# changes EnemyEditor fiddle's rockclod_blue (sets speed to 10)
editor.replace("rockclod_blue", {"speed":10}, force_explicit=False)

# saves EnemyEditor's fiddle's rockclod under the name test.json
editor.save("rockclod_blue", "test") 

# updates actual __fiddle__ using test.json
editor.update("rockclod_blue", "test") 


# print all clod keys to find what you can edit!
#print(defaults["clod"].keys())
