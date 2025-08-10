# EnemyEditor

Edit your Fields of Mistria enemy patterns with this tool without breaking a sweat!

All you need is Python (no added packages). 

## Before using

**IMPORTANT: Back up your fiddle file!**
If ever something goes wrong, you'll want to revert your game's `__fiddle__.json` back to its original state, so make sure to keep it somewhere.

I recommend also copying the file in a directory with this program and using the program on this copy. Once you're satisfied with the changes, copy that file over to the game directory to test out the changes in-game.
If you're feeling comfortable, you can provide the game's fiddle directly, so long as you have it backed up.

## Using

**WIP - I'm making it pip installable, I'll write instructions on how to use it once everything is settled.**

You can follow along with the `example.py` file.

### To create a JSON monster variant

This project is built to be heavily modular. This will help you create a single, small JSON file containing information on a single monster variant that will override one of the monsters in the game.

1. Create a Python file (or use the example file).
2. Import `EnemyEditor`. You can do this with :
```py
from enemy_editor import EnemyEditor
```
3. Specify the absolute path to your fiddle file, and create an editor instance using it:
```py
fiddle_path = r"<path-to-folder-with-fiddle>\__fiddle__.json"
editor = EnemyEditor(fiddle_path=fiddle_path)
```
*Note : this creates an internal copy of the fiddle file. Any changes made to this will not affect the file until explicitely saved using `save`. More on this later.*
4. Make changes to the editor's internal fiddle using `replace`, with help from the `backups.py` or `backup` folder provided with this package (see <u>### Making Edits</u> for details).
5. Save a subset of the internal fiddle, using `save`, to a small JSON file of a monster variant.

### To integrate a JSON monster variant

Assuming that you have a `monsters/patched/rockclod_blue` folder with a JSON inside it, let's call it "test.json", you can update your fiddle by following steps 1-3 from the previous section (you don't need to do them again if you already did them in the same file) and then running :
```py
editor.update("rockclod_blue", "test") 
```
This will directly modify the `__fiddle__.json` file provided in the `fiddle_path` variable, replacing the `rockclod_blue` values with what was specified in the `test.json`. You can of course do this using any monster variant.

### Making edits

To make edits, you can use the `replace` method. Specify the name of the monster you want to edit, and provide a dictionary with values you want to update or add.

To get a list of all possible keys you can use in the dictionary, take a look at your monster's monster type default variant in the `defaults` variable from `backups.py`.
For example, I know I can add `"attack_legion": 4"` to `rockclod_blue` because it's a `clod` and `attack_legion` is a key present in `clod`'s default variant. These variants are unused in the actual game and serve the only purpose of setting useless variables to default values in each variant.


Some details : `force_explicit` decides whether to consider the provided dictionary as an update or a complete makeover.

These two lines do the same thing, as `force_explicit` is optional and is set to `False` by default.
```py
editor.replace("rockclod_blue", {"speed":10})
editor.replace("rockclod_blue", {"speed":10}, force_explicit=False)
```
Here, `rockclod_blue` will be exactly the same as in the provided fiddle file, except it will have super speed.

However if I write : 
```py
editor.replace("rockclod_blue", {"speed":10}, force_explicit=True)
```
Then the dictionary will be overwritten completely in the fiddle and fully **replaced** by `{"speed":10}`.
This means that the game will turn to the default variant to fill in all the missing values.
This feature is available purely to give more control over the configuration and is not necessary to implement any specific behaviour.



## Remarks, WIP

Please let me know if you have any feedback or improvements to suggest, I'll make sure to keep an eye out for this repo from time to time. This was mostly done to make the process of experimenting on Fields Of Mistria enemies less tedious and more digestible.

For example, you can have a template such as the one below, which always modifies the enemy you specify with the dictionary you specify, using the default template explicitely, and this gives you full control with little to no effort.

```py
from enemy_editor import EnemyEditor, BACKUPS

fiddle_path = r"<path-to-folder-with-fiddle>\__fiddle__.json"
editor = EnemyEditor(fiddle_path=fiddle_path)

monster = "rockclod"
variant_name = "paperclod"
new = {
        "hp": 1,
        "damage": 0,
        "essence": 0,
        "drops": [],
        "death_explosion_count": -1,
        "death_explosion_angle": -1,
        "death_explosion_speed": -1,
        "death_explosion_delay": -1,
        "attack_sequence": 1,
        "attack_sequence_turn": -1,
        "attack_sequence_image_speed": -1,
        "attack_legion": 1,
        "attack_radial_degree": 0,
        "coin_count": [1, 3],
        "starting_dir": [180, 360],
        "damage_number_offset": -12,
        "iframes": 0,
        "gm_object": "obj_monster_clod",
        "hurtbox": "spr_monster_rockclod_hurtbox",
        "speed": 0.6,
        "projectile_speed": 1.8,
        "patience_acknowledgement_reset": -120,
        "attack_radius": 96,
        "aggro_radius": 384,
        "use_circle": True,
        "knockback_multiplier": 4,
        "knockback_friction": 0.88,
        "windup": [4, 6],
        "acknowledgment": [45, 55],
        "tired": [55, 200],
        "hurt": [24, 32],
        "push_radius": 4,
        "push_force": 0.25,
        "pushed_radius": 7,
        "split_angle": -1,
        "split_distance": -1,
        "split_depth": -1,
        "split_speed": 1.8,
        "split_depreciation": -1,
        "sprites": {"misc": {}},
        "tango": {
            "acknowledgment": "SoundEffects/Enemies/EnemyAlerted",
            "walk": "SoundEffects/Enemies/Rockclod/Hop",
            "windup": "SoundEffects/Enemies/Rockclod/ProjectileChargeUp",
            "attack": "SoundEffects/Enemies/Rockclod/ProjectileSpit",
            "dying": "SoundEffects/Enemies/Rockclod/Die",
            "misc": {
                "hit_by_projectile": "SoundEffects/Enemies/Rockclod/HitByProjectile",
                "projectile_break": "SoundEffects/Enemies/Rockclod/ProjectileBreak",
                "projectile_reflect": "SoundEffects/Tools/SwordReflectProjectile",
                "weak_damage": "SoundEffects/Enemies/TakeDamageRockWeak",
                "strong_damage": "SoundEffects/Enemies/TakeDamageRockStrong",
                "death": "SoundEffects/Enemies/Rockclod/Die",
            },
        },
    }

editor.replace(monster, new, force_explicit=True)
editor.save(monster, variant_name) 
editor.update(monster, variant_name) 
```