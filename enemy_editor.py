"""Contains EnemyEditor class, designed to streamline editing enemy behaviours in FoM."""
import json, os
from _typeshed import SupportsWrite

class EnemyEditor:
    """Base class to modify enemy configurations in the fiddle file."""
    def __init__(self, *, fiddle_path:str):
        """Base class to modify enemy configurations in the fiddle file.
        
        Args:
            fiddle_path (str): The absolute path to the fiddle file.
        """
        self.fiddle_path = fiddle_path
        with open(fiddle_path, encoding='utf8') as fp:
            self.fiddle = json.load(fp)
        self.monsters = {monster_type: list(self.fiddle[f"monsters/{monster_type}"].keys()) for monster_type in fiddle["monsters"]}
        self.all_monsters = [v for variants in self.monsters.values() for v in variants if v != "default"]
        self.monsters_b = {monster: monster_type for monster in self.all_monsters for monster_type in self.monsters if monster in self.monsters[monster_type]}

    def replace(self, monster:str, new:dict, force_explicit:bool = False):
        """Updates the `EnemyEditor` fiddle attribute directly. 
        Adds or modifies values in the dictionary.
        
        Args:
            monster (str): The name of the monster to be edited.
            new (dict): The dictionary with new or updated key/value pairs.
            force_explicit (bool, Optional): Whether to replace the dictionary entirely or just update it. Defaults to False.
        """
        if monster not in self.all_monsters:
            raise ValueError(f"{monster} is not a valid monster variant")
        monster_type = self.monsters_b[monster]
        unknown_keys = set(new)-set(fiddle[f"monsters/{monster_type}/default"])
        if unknown_keys != set():
            raise ValueError(f"Unknown dict keys : {unknown_keys}")
        current = fiddle[f"monsters/{monster_type}/{monster}"] if not force_explicit else {}
        for k,v in new.items():
            if type(current[k]) == dict:
                for key, val in v.items():
                    current[k][key] = val
            else:
                current[k] = v
        fiddle[f"monsters/{monster_type}/{monster}"] = current
        fiddle[f"monsters/{monster_type}"][monster] = current
        fiddle["monsters"][monster_type][monster] = current

    def _save(self, monster:str, fp:SupportsWrite[str]):
        """Internal function to save the `EnemyEditor` fiddle values of a specified monster to a file.
        
        Args:
            monster (str): The name of the monster to be edited.
            fp (SupportsWrite[str]): The `.write()`-supporting file-like object to be written to.
        """
        if monster not in self.all_monsters:
            raise ValueError(f"{monster} is not a valid monster variant")
        monster_type = self.monsters_b[monster]
        d1 = fiddle[f"monsters/{monster_type}/{monster}"]
        d2 = fiddle[f"monsters/{monster_type}"][monster]
        d3 = fiddle["monsters"][monster_type][monster]
        if not (d1 == d2 == d3):
            raise ValueError("Inconsistencies in enemy data.")
        json.dump(d1, fp)


    def save(self, monster:str, variant_name:str):
        """Saves the `EnemyEditor` fiddle values of a monster to a file with a custom name for the new variant.
        
        Args:
            monster (str): The name of the monster to be edited.
            variant_name (str): The new name of the variant that the file will be named after.
        """
        monster_type = self.monsters_b[monster]
        if not os.path.exists("monsters"):
            os.mkdir("monsters")
        if not os.path.exists("monsters/patched"):
            os.mkdir("monsters/patched")
        if not os.path.exists(f"monsters/patched/{monster_type}"):
            os.mkdir(f"monsters/patched/{monster_type}")
        if not os.path.exists(f"monsters/patched/{monster_type}/{monster}"):
            os.mkdir(f"monsters/patched/{monster_type}/{monster}")
        with open(f"monsters/patched/{monster_type}/{monster}/{variant_name}.json", "w") as fp:
            self._save(monster, fp)

    def update(self, monster, variant_name):
        """Updates the `__fiddle__.json` file with the current values of the specified monster using 
        the saved variant. Make sure the variant has been saved first (with `EnemyEditor.save`).
        
        Args:
            monster (str): The name of the monster to be edited.
            variant_name (str): The name of the saved variant that will be used to update the fiddle file.
        """
        global fiddle
        monster_type = self.monsters_b[monster]
        with open(f"monsters/patched/{monster_type}/{monster}/{variant_name}.json") as fp:
            variant = json.load(fp)
        fiddle[f"monsters/{monster_type}/{monster}"] = variant
        fiddle[f"monsters/{monster_type}"][monster] = variant
        fiddle["monsters"][monster_type][monster] = variant
        with open(self.fiddle_path, mode="w", encoding='utf8') as fp:
            json.dump(fiddle, fp)
        with open(self.fiddle_path, encoding='utf8') as fp:
            fiddle = json.load(fp)


