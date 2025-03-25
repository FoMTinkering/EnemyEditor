"""Contains dict representation of every default enemy configuration in FoM."""

# bat
bat = {
    "hp": 32,
    "damage": 18,
    "essence": 15,
    "variant_attack": False,
    "drops": [
        {"item": "essence_drop", "chance": 70, "count_range": [1, 1]},
        {"item": "monster_wing", "chance": 30, "count_range": [1, 1]},
        {"cosmetic": "head_essence_bat_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_essence_bat_main_idle_north",
            "south": "spr_monster_essence_bat_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_essence_bat_main_alert_north",
            "south": "spr_monster_essence_bat_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_essence_bat_main_fly_north",
            "south": "spr_monster_essence_bat_main_fly_south",
        },
        "windup": {
            "north": "spr_monster_essence_bat_main_windup_north",
            "south": "spr_monster_essence_bat_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_essence_bat_main_attack_north",
            "south": "spr_monster_essence_bat_main_attack_south",
        },
        "hurt": {
            "north": "spr_monster_essence_bat_main_hurt_north",
            "south": "spr_monster_essence_bat_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_essence_bat_main_hurt_north",
            "south": "spr_monster_essence_bat_main_hurt_south",
        },
        "flee": {
            "north": "spr_monster_essence_bat_main_fly_north",
            "south": "spr_monster_essence_bat_main_fly_south",
        },
        "misc": {
            "breath_east": "spr_fx_monster_essence_bat_breath_windup_east",
            "breath_west": "spr_fx_monster_essence_bat_breath_windup_west",
            "breath_north": "spr_fx_monster_essence_bat_breath_windup_north",
            "breath_south": "spr_fx_monster_essence_bat_breath_windup_south",
        },
    },
}
bat_blue = {
    "hp": 48,
    "damage": 32,
    "essence": 15,
    "variant_attack": True,
    "knockback": 4,
    "drops": [
        {"item": "essence_drop", "chance": 70, "count_range": [1, 1]},
        {"item": "monster_wing", "chance": 30, "count_range": [1, 1]},
        {"cosmetic": "head_essence_bat_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_essence_bat_blue_main_idle_north",
            "south": "spr_monster_essence_bat_blue_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_essence_bat_blue_main_alert_north",
            "south": "spr_monster_essence_bat_blue_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_essence_bat_blue_main_fly_north",
            "south": "spr_monster_essence_bat_blue_main_fly_south",
        },
        "windup": {
            "north": "spr_monster_essence_bat_blue_main_windup_north",
            "south": "spr_monster_essence_bat_blue_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_essence_bat_blue_main_attack_north",
            "south": "spr_monster_essence_bat_blue_main_attack_south",
        },
        "hurt": {
            "north": "spr_monster_essence_bat_blue_main_hurt_north",
            "south": "spr_monster_essence_bat_blue_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_essence_bat_blue_main_hurt_north",
            "south": "spr_monster_essence_bat_blue_main_hurt_south",
        },
        "flee": {
            "north": "spr_monster_essence_bat_blue_main_fly_north",
            "south": "spr_monster_essence_bat_blue_main_fly_south",
        },
        "misc": {
            "breath_east": "spr_fx_monster_essence_bat_breath_windup_east",
            "breath_west": "spr_fx_monster_essence_bat_breath_windup_west",
            "breath_north": "spr_fx_monster_essence_bat_breath_windup_north",
            "breath_south": "spr_fx_monster_essence_bat_breath_windup_south",
        },
    },
}

# clod
copperclod = {
    "hp": 16,
    "damage": 12,
    "essence": 5,
    "coin_count": [1, 5],
    "attack_legion": 2,
    "drops": [
        {"item": "ore_copper", "chance": 70, "count_range": [1, 3]},
        {"item": "monster_shell", "chance": 25, "count_range": [1, 1]},
        {"item": "ore_ruby", "chance": 5, "count_range": [1, 1]},
        {"cosmetic": "head_oreclod_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_copperclod_main_idle_north",
            "east": "spr_monster_copperclod_main_idle_east",
            "south": "spr_monster_copperclod_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_copperclod_main_alert_north",
            "east": "spr_monster_copperclod_main_alert_east",
            "south": "spr_monster_copperclod_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_copperclod_main_walk_north",
            "east": "spr_monster_copperclod_main_walk_east",
            "south": "spr_monster_copperclod_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_copperclod_main_windup_north",
            "east": "spr_monster_copperclod_main_windup_east",
            "south": "spr_monster_copperclod_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_copperclod_main_attack_north",
            "east": "spr_monster_copperclod_main_attack_east",
            "south": "spr_monster_copperclod_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_copperclod_main_idle_north",
            "east": "spr_monster_copperclod_main_idle_east",
            "south": "spr_monster_copperclod_main_idle_south",
        },
        "hurt": {
            "north": "spr_monster_copperclod_main_hurt_north",
            "east": "spr_monster_copperclod_main_hurt_east",
            "south": "spr_monster_copperclod_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_copperclod_main_death_south",
            "east": "spr_monster_copperclod_main_death_east",
            "south": "spr_monster_copperclod_main_death_south",
        },
        "misc": {
            "projectile": "spr_monster_copperclod_projectile_main",
            "rock_particle": "spr_part_copperclod_projectile",
        },
    },
}
goldclod = {
    "hp": 48,
    "damage": 28,
    "essence": 20,
    "coin_count": [6, 12],
    "split_depth": 2,
    "split_angle": 40,
    "split_distance": 40,
    "split_depreciation": 1.25,
    "projectile_speed": 2.0,
    "drops": [
        {"item": "ore_gold", "count_range": [1, 3], "exclusive": False},
        {"item": "monster_shell", "chance": 25, "count_range": [1, 4]},
        {"item": "ore_diamond", "chance": 5},
        {"cosmetic": "head_oreclod_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_goldclod_main_idle_north",
            "east": "spr_monster_goldclod_main_idle_east",
            "south": "spr_monster_goldclod_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_goldclod_main_alert_north",
            "east": "spr_monster_goldclod_main_alert_east",
            "south": "spr_monster_goldclod_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_goldclod_main_walk_north",
            "east": "spr_monster_goldclod_main_walk_east",
            "south": "spr_monster_goldclod_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_goldclod_main_windup_north",
            "east": "spr_monster_goldclod_main_windup_east",
            "south": "spr_monster_goldclod_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_goldclod_main_attack_north",
            "east": "spr_monster_goldclod_main_attack_east",
            "south": "spr_monster_goldclod_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_goldclod_main_idle_north",
            "east": "spr_monster_goldclod_main_idle_east",
            "south": "spr_monster_goldclod_main_idle_south",
        },
        "hurt": {
            "north": "spr_monster_goldclod_main_hurt_north",
            "east": "spr_monster_goldclod_main_hurt_east",
            "south": "spr_monster_goldclod_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_goldclod_main_death_south",
            "east": "spr_monster_goldclod_main_death_east",
            "south": "spr_monster_goldclod_main_death_south",
        },
        "misc": {
            "projectile": "spr_monster_goldclod_projectile_main",
            "rock_particle": "spr_part_goldclod_projectile",
        },
    },
}
ironclod = {
    "hp": 32,
    "damage": 17,
    "essence": 15,
    "coin_count": [2, 6],
    "attack_radial_degree": 45,
    "projectile_speed": 2.0,
    "drops": [
        {"item": "ore_iron", "chance": 70, "count_range": [1, 3]},
        {"item": "monster_shell", "chance": 25, "count_range": [1, 2]},
        {"item": "ore_sapphire", "chance": 5, "count_range": [1, 1]},
        {"cosmetic": "head_oreclod_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_ironclod_main_idle_north",
            "east": "spr_monster_ironclod_main_idle_east",
            "south": "spr_monster_ironclod_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_ironclod_main_alert_north",
            "east": "spr_monster_ironclod_main_alert_east",
            "south": "spr_monster_ironclod_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_ironclod_main_walk_north",
            "east": "spr_monster_ironclod_main_walk_east",
            "south": "spr_monster_ironclod_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_ironclod_main_windup_north",
            "east": "spr_monster_ironclod_main_windup_east",
            "south": "spr_monster_ironclod_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_ironclod_main_attack_north",
            "east": "spr_monster_ironclod_main_attack_east",
            "south": "spr_monster_ironclod_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_ironclod_main_idle_north",
            "east": "spr_monster_ironclod_main_idle_east",
            "south": "spr_monster_ironclod_main_idle_south",
        },
        "hurt": {
            "north": "spr_monster_ironclod_main_hurt_north",
            "east": "spr_monster_ironclod_main_hurt_east",
            "south": "spr_monster_ironclod_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_ironclod_main_death_south",
            "east": "spr_monster_ironclod_main_death_east",
            "south": "spr_monster_ironclod_main_death_south",
        },
        "misc": {
            "projectile": "spr_monster_ironclod_projectile_main",
            "rock_particle": "spr_part_ironclod_projectile",
        },
    },
}
mistrilclod = {
    "hp": 1000,
    "damage": 20,
    "essence": 15,
    "attack_sequence": 5,
    "attack_legion": 5,
    "drops": [
        {"item": "ore_mistril", "count": [1, 2], "exclusive": False},
        {"item": "ore_pink_diamond", "chance": 5},
        {"item": "perfect_pink_diamond", "chance": 1},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_mistrilclod_main_idle_north",
            "east": "spr_monster_mistrilclod_main_idle_east",
            "south": "spr_monster_mistrilclod_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_mistrilclod_main_alert_north",
            "east": "spr_monster_mistrilclod_main_alert_east",
            "south": "spr_monster_mistrilclod_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_mistrilclod_main_walk_north",
            "east": "spr_monster_mistrilclod_main_walk_east",
            "south": "spr_monster_mistrilclod_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_mistrilclod_main_windup_north",
            "east": "spr_monster_mistrilclod_main_windup_east",
            "south": "spr_monster_mistrilclod_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_mistrilclod_main_attack_north",
            "east": "spr_monster_mistrilclod_main_attack_east",
            "south": "spr_monster_mistrilclod_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_mistrilclod_main_idle_north",
            "east": "spr_monster_mistrilclod_main_idle_east",
            "south": "spr_monster_mistrilclod_main_idle_south",
        },
        "hurt": {
            "north": "spr_monster_mistrilclod_main_hurt_north",
            "east": "spr_monster_mistrilclod_main_hurt_east",
            "south": "spr_monster_mistrilclod_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_mistrilclod_main_death_south",
            "east": "spr_monster_mistrilclod_main_death_east",
            "south": "spr_monster_mistrilclod_main_death_south",
        },
        "misc": {
            "projectile": "spr_monster_mistrilclod_projectile_main",
            "rock_particle": "spr_part_mistrilclod_projectile",
        },
    },
}
rockclod = {
    "hp": 8,
    "damage": 10,
    "essence": 5,
    "coin_count": [1, 5],
    "drops": [
        {"item": "ore_stone", "chance": 70, "count_range": [1, 2]},
        {"item": "monster_shell", "chance": 30, "count_range": [1, 1]},
        {"cosmetic": "head_rockclod_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_rockclod_main_idle_north",
            "east": "spr_monster_rockclod_main_idle_east",
            "south": "spr_monster_rockclod_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_rockclod_main_alert_north",
            "east": "spr_monster_rockclod_main_alert_east",
            "south": "spr_monster_rockclod_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_rockclod_main_walk_north",
            "east": "spr_monster_rockclod_main_walk_east",
            "south": "spr_monster_rockclod_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_rockclod_main_windup_north",
            "east": "spr_monster_rockclod_main_windup_east",
            "south": "spr_monster_rockclod_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_rockclod_main_attack_north",
            "east": "spr_monster_rockclod_main_attack_east",
            "south": "spr_monster_rockclod_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_rockclod_main_idle_north",
            "east": "spr_monster_rockclod_main_idle_east",
            "south": "spr_monster_rockclod_main_idle_south",
        },
        "hurt": {
            "north": "spr_monster_rockclod_main_hurt_north",
            "east": "spr_monster_rockclod_main_hurt_east",
            "south": "spr_monster_rockclod_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_rockclod_main_death_south",
            "east": "spr_monster_rockclod_main_death_east",
            "south": "spr_monster_rockclod_main_death_south",
        },
        "misc": {
            "projectile": "spr_monster_rockclod_projectile_main",
            "rock_particle": "spr_part_rockclod_projectile",
        },
    },
}
rockclod_blue = {
    "hp": 16,
    "damage": 12,
    "essence": 10,
    "coin_count": [2, 6],
    "attack_sequence": 2,
    "projectile_speed": 2.0,
    "drops": [
        {"item": "ore_stone", "chance": 70, "count_range": [2, 4]},
        {"item": "monster_shell", "chance": 30, "count_range": [1, 2]},
        {"cosmetic": "head_rockclod_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_rockclod_blue_main_idle_north",
            "east": "spr_monster_rockclod_blue_main_idle_east",
            "south": "spr_monster_rockclod_blue_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_rockclod_blue_main_alert_north",
            "east": "spr_monster_rockclod_blue_main_alert_east",
            "south": "spr_monster_rockclod_blue_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_rockclod_blue_main_walk_north",
            "east": "spr_monster_rockclod_blue_main_walk_east",
            "south": "spr_monster_rockclod_blue_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_rockclod_blue_main_windup_north",
            "east": "spr_monster_rockclod_blue_main_windup_east",
            "south": "spr_monster_rockclod_blue_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_rockclod_blue_main_attack_north",
            "east": "spr_monster_rockclod_blue_main_attack_east",
            "south": "spr_monster_rockclod_blue_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_rockclod_blue_main_idle_north",
            "east": "spr_monster_rockclod_blue_main_idle_east",
            "south": "spr_monster_rockclod_blue_main_idle_south",
        },
        "hurt": {
            "north": "spr_monster_rockclod_blue_main_hurt_north",
            "east": "spr_monster_rockclod_blue_main_hurt_east",
            "south": "spr_monster_rockclod_blue_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_rockclod_blue_main_death_south",
            "east": "spr_monster_rockclod_blue_main_death_east",
            "south": "spr_monster_rockclod_blue_main_death_south",
        },
        "misc": {
            "projectile": "spr_monster_rockclod_blue_projectile_main",
            "rock_particle": "spr_part_rockclod_blue_projectile",
        },
    },
}
rockclod_green = {
    "hp": 32,
    "damage": 24,
    "essence": 15,
    "coin_count": [4, 8],
    "projectile_speed": 2.0,
    "drops": [
        {"item": "ore_stone", "chance": 70, "count_range": [4, 6]},
        {"item": "monster_shell", "chance": 30, "count_range": [1, 3]},
        {"cosmetic": "head_rockclod_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_rockclod_green_main_idle_north",
            "east": "spr_monster_rockclod_green_main_idle_east",
            "south": "spr_monster_rockclod_green_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_rockclod_green_main_alert_north",
            "east": "spr_monster_rockclod_green_main_alert_east",
            "south": "spr_monster_rockclod_green_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_rockclod_green_main_walk_north",
            "east": "spr_monster_rockclod_green_main_walk_east",
            "south": "spr_monster_rockclod_green_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_rockclod_green_main_windup_north",
            "east": "spr_monster_rockclod_green_main_windup_east",
            "south": "spr_monster_rockclod_green_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_rockclod_green_main_attack_north",
            "east": "spr_monster_rockclod_green_main_attack_east",
            "south": "spr_monster_rockclod_green_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_rockclod_green_main_idle_north",
            "east": "spr_monster_rockclod_green_main_idle_east",
            "south": "spr_monster_rockclod_green_main_idle_south",
        },
        "hurt": {
            "north": "spr_monster_rockclod_green_main_hurt_north",
            "east": "spr_monster_rockclod_green_main_hurt_east",
            "south": "spr_monster_rockclod_green_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_rockclod_green_main_death_south",
            "east": "spr_monster_rockclod_green_main_death_east",
            "south": "spr_monster_rockclod_green_main_death_south",
        },
        "misc": {
            "projectile": "spr_monster_rockclod_green_projectile_main",
            "rock_particle": "spr_part_rockclod_green_projectile",
        },
    },
}
rockclod_purple = {
    "hp": 1000,
    "damage": 50,
    "essence": 25,
    "drops": [
        {"item": "ore_stone", "count": [1, 2], "exclusive": False},
        {"item": "ore_pink_diamond", "chance": 5},
        {"item": "perfect_pink_diamond", "chance": 1},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_rockclod_purple_main_idle_north",
            "east": "spr_monster_rockclod_purple_main_idle_east",
            "south": "spr_monster_rockclod_purple_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_rockclod_purple_main_alert_north",
            "east": "spr_monster_rockclod_purple_main_alert_east",
            "south": "spr_monster_rockclod_purple_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_rockclod_purple_main_walk_north",
            "east": "spr_monster_rockclod_purple_main_walk_east",
            "south": "spr_monster_rockclod_purple_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_rockclod_purple_main_windup_north",
            "east": "spr_monster_rockclod_purple_main_windup_east",
            "south": "spr_monster_rockclod_purple_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_rockclod_purple_main_attack_north",
            "east": "spr_monster_rockclod_purple_main_attack_east",
            "south": "spr_monster_rockclod_purple_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_rockclod_purple_main_idle_north",
            "east": "spr_monster_rockclod_purple_main_idle_east",
            "south": "spr_monster_rockclod_purple_main_idle_south",
        },
        "hurt": {
            "north": "spr_monster_rockclod_purple_main_hurt_north",
            "east": "spr_monster_rockclod_purple_main_hurt_east",
            "south": "spr_monster_rockclod_purple_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_rockclod_purple_main_death_south",
            "east": "spr_monster_rockclod_purple_main_death_east",
            "south": "spr_monster_rockclod_purple_main_death_south",
        },
        "misc": {
            "projectile": "spr_monster_rockclod_purple_projectile_main",
            "rock_particle": "spr_part_rockclod_purple_projectile",
        },
    },
}
rockclod_red = {
    "hp": 48,
    "damage": 36,
    "coin_count": [6, 12],
    "essence": 20,
    "attack_sequence": 9,
    "attack_legion": 1,
    "attack_sequence_turn": 45,
    "attack_sequence_image_speed": 2,
    "projectile_speed": 2.0,
    "death_explosion_count": 9,
    "death_explosion_angle": 45,
    "death_explosion_speed": 1.8,
    "death_explosion_delay": 30,
    "drops": [
        {"item": "ore_stone", "chance": 70, "count_range": [6, 12]},
        {"item": "monster_shell", "chance": 30, "count_range": [1, 4]},
        {"cosmetic": "head_rockclod_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_rockclod_red_main_idle_north",
            "east": "spr_monster_rockclod_red_main_idle_east",
            "south": "spr_monster_rockclod_red_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_rockclod_red_main_alert_north",
            "east": "spr_monster_rockclod_red_main_alert_east",
            "south": "spr_monster_rockclod_red_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_rockclod_red_main_walk_north",
            "east": "spr_monster_rockclod_red_main_walk_east",
            "south": "spr_monster_rockclod_red_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_rockclod_red_main_windup_north",
            "east": "spr_monster_rockclod_red_main_windup_east",
            "south": "spr_monster_rockclod_red_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_rockclod_red_main_attack_north",
            "east": "spr_monster_rockclod_red_main_attack_east",
            "south": "spr_monster_rockclod_red_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_rockclod_red_main_idle_north",
            "east": "spr_monster_rockclod_red_main_idle_east",
            "south": "spr_monster_rockclod_red_main_idle_south",
        },
        "hurt": {
            "north": "spr_monster_rockclod_red_main_hurt_north",
            "east": "spr_monster_rockclod_red_main_hurt_east",
            "south": "spr_monster_rockclod_red_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_rockclod_red_main_death_south",
            "east": "spr_monster_rockclod_red_main_death_east",
            "south": "spr_monster_rockclod_red_main_death_south",
        },
        "misc": {
            "projectile": "spr_monster_rockclod_red_projectile_main",
            "rock_particle": "spr_part_rockclod_red_projectile",
        },
    },
}
silverclod = {
    "hp": 48,
    "damage": 22,
    "essence": 15,
    "coin_count": [4, 8],
    "projectile_speed": 2.0,
    "drops": [
        {"item": "ore_silver", "chance": 70, "count_range": [1, 3]},
        {"item": "monster_shell", "chance": 25, "count_range": [1, 3]},
        {"item": "ore_emerald", "chance": 5, "count_range": [1, 1]},
        {"cosmetic": "head_oreclod_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_silverclod_main_idle_north",
            "east": "spr_monster_silverclod_main_idle_east",
            "south": "spr_monster_silverclod_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_silverclod_main_alert_north",
            "east": "spr_monster_silverclod_main_alert_east",
            "south": "spr_monster_silverclod_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_silverclod_main_walk_north",
            "east": "spr_monster_silverclod_main_walk_east",
            "south": "spr_monster_silverclod_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_silverclod_main_windup_north",
            "east": "spr_monster_silverclod_main_windup_east",
            "south": "spr_monster_silverclod_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_silverclod_main_attack_north",
            "east": "spr_monster_silverclod_main_attack_east",
            "south": "spr_monster_silverclod_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_silverclod_main_idle_north",
            "east": "spr_monster_silverclod_main_idle_east",
            "south": "spr_monster_silverclod_main_idle_south",
        },
        "hurt": {
            "north": "spr_monster_silverclod_main_hurt_north",
            "east": "spr_monster_silverclod_main_hurt_east",
            "south": "spr_monster_silverclod_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_silverclod_main_death_south",
            "east": "spr_monster_silverclod_main_death_east",
            "south": "spr_monster_silverclod_main_death_south",
        },
        "misc": {
            "projectile": "spr_monster_silverclod_projectile_main",
            "rock_particle": "spr_part_silverclod_projectile",
        },
    },
}

# enchantern
enchantern = {
    "hp": 24,
    "damage": 12,
    "essence": 5,
    "coin_count": [1, 5],
    "electrocute_kind": "yellow",
    "drops_balls": False,
    "drops": [
        {"item": "glass", "chance": 70, "count_range": [1, 1]},
        {"item": "monster_core", "chance": 30, "count_range": [1, 1]},
        {"cosmetic": "head_enchantern_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_enchantern_off_idle_north",
            "south": "spr_monster_enchantern_off_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_enchantern_off_alert_north",
            "south": "spr_monster_enchantern_off_alert_south",
        },
        "flicker_on": {
            "north": "spr_monster_enchantern_state_transition_main_on_north",
            "south": "spr_monster_enchantern_state_transition_main_on_south",
        },
        "charge": {
            "north": "spr_monster_enchantern_on_charge_north",
            "south": "spr_monster_enchantern_on_charge_south",
        },
        "flee": {
            "north": "spr_monster_enchantern_off_flee_north",
            "south": "spr_monster_enchantern_off_flee_south",
        },
        "go_home": {
            "north": "spr_monster_enchantern_off_walk_north",
            "south": "spr_monster_enchantern_off_walk_south",
        },
        "hurt": {
            "north": "spr_monster_enchantern_off_hurt_north",
            "south": "spr_monster_enchantern_off_hurt_south",
        },
        "dying": {
            "north": "spr_monster_enchantern_off_death_south",
            "south": "spr_monster_enchantern_off_death_south",
        },
        "misc": {
            "static_effect": "spr_fx_monster_enchantern_static",
            "charge": "spr_fx_monster_enchantern_charge",
            "charge_off_north": "spr_monster_enchantern_off_charge_north",
            "charge_off_south": "spr_monster_enchantern_off_charge_south",
            "attack_north": "spr_monster_enchantern_on_attack_north",
            "attack_south": "spr_monster_enchantern_on_attack_south",
            "gibs": "spr_part_enchantern_bits",
            "proj_mask_index": "spr_monster_enchantern_projectile_main_loop",
            "proj_main_start": "spr_monster_enchantern_floor_ball_main_start",
            "proj_main_loop": "spr_monster_enchantern_floor_ball_main_loop",
            "proj_main_fizzle": "spr_monster_enchantern_floor_ball_main_fizzle",
        },
    },
}
enchantern_blue = {
    "hp": 48,
    "damage": 20,
    "essence": 10,
    "coin_count": [2, 6],
    "drops_balls": True,
    "electrocute_kind": "blue",
    "drops": [
        {"item": "glass", "chance": 70, "count_range": [1, 2]},
        {"item": "monster_core", "chance": 30, "count_range": [1, 2]},
        {"cosmetic": "head_enchantern_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_enchantern_blue_off_idle_north",
            "south": "spr_monster_enchantern_blue_off_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_enchantern_blue_off_alert_north",
            "south": "spr_monster_enchantern_blue_off_alert_south",
        },
        "flicker_on": {
            "north": "spr_monster_enchantern_blue_state_transition_main_on_north",
            "south": "spr_monster_enchantern_blue_state_transition_main_on_south",
        },
        "charge": {
            "north": "spr_monster_enchantern_blue_on_charge_north",
            "south": "spr_monster_enchantern_blue_on_charge_south",
        },
        "flee": {
            "north": "spr_monster_enchantern_blue_off_flee_north",
            "south": "spr_monster_enchantern_blue_off_flee_south",
        },
        "go_home": {
            "north": "spr_monster_enchantern_blue_off_walk_north",
            "south": "spr_monster_enchantern_blue_off_walk_south",
        },
        "hurt": {
            "north": "spr_monster_enchantern_blue_off_hurt_north",
            "south": "spr_monster_enchantern_blue_off_hurt_south",
        },
        "dying": {
            "north": "spr_monster_enchantern_blue_off_death_south",
            "south": "spr_monster_enchantern_blue_off_death_south",
        },
        "misc": {
            "static_effect": "spr_fx_monster_enchantern_blue_static",
            "charge": "spr_fx_monster_enchantern_blue_charge",
            "charge_off_north": "spr_monster_enchantern_blue_off_charge_north",
            "charge_off_south": "spr_monster_enchantern_blue_off_charge_south",
            "attack_north": "spr_monster_enchantern_blue_on_attack_north",
            "attack_south": "spr_monster_enchantern_blue_on_attack_south",
            "gibs": "spr_part_enchantern_blue_bits",
            "proj_mask_index": "spr_monster_enchantern_blue_projectile_main_loop",
            "proj_main_start": "spr_monster_enchantern_blue_floor_ball_main_start",
            "proj_main_loop": "spr_monster_enchantern_blue_floor_ball_main_loop",
            "proj_main_fizzle": "spr_monster_enchantern_blue_floor_ball_main_fizzle",
        },
    },
}

# mimic
mimic = {
    "damage": 20,
    "essence": 0,
    "sprites": {
        "idle": {
            "north": "spr_monster_mimic_main_idle_south",
            "south": "spr_monster_mimic_main_idle_south",
        },
        "attack": {
            "north": "spr_monster_mimic_main_attack_south",
            "south": "spr_monster_mimic_main_attack_south",
        },
        "hurt": {
            "north": "spr_monster_mimic_main_hurt_south",
            "south": "spr_monster_mimic_main_hurt_south",
        },
        "gobble": {
            "north": "spr_monster_mimic_main_eat_south",
            "south": "spr_monster_mimic_main_eat_south",
        },
        "dying": {
            "north": "spr_monster_mimic_main_idle_south",
            "south": "spr_monster_mimic_main_idle_south",
        },
        "fade": {
            "north": "spr_monster_mimic_main_disappear_south",
            "south": "spr_monster_mimic_main_disappear_south",
        },
        "misc": {"idle_two": "spr_monster_mimic_main_idle_2_south"},
    },
}

# mite
stalagmite = {
    "hp": 24,
    "damage": 25,
    "essence": 5,
    "coin_count": [2, 6],
    "drops": [
        {"item": "ore_copper", "chance": 70, "count_range": [1, 1]},
        {"item": "monster_horn", "chance": 30, "count_range": [1, 1]},
        {"cosmetic": "head_stalagmite_hat", "chance": 5},
    ],
    "sprites": {
        "idle": "spr_nothing",
        "walk": "spr_nothing",
        "windup": "spr_monster_stalagmite_blue_windup",
        "attack": "spr_monster_stalagmite_blue_attack",
        "tired": "spr_monster_stalagmite_blue_tired",
        "flee": "spr_monster_stalagmite_blue_flee",
        "hurt": "spr_monster_stalagmite_blue_hurt",
        "dying": "spr_monster_stalagmite_blue_hurt",
        "misc": {
            "ground_walk": "spr_monster_stalagmite_ground_blue_walk",
            "ground_windup": "spr_monster_stalagmite_ground_blue_windup",
            "ground_attack": "spr_monster_stalagmite_ground_blue_attack",
            "ground_flee": "spr_monster_stalagmite_ground_blue_flee",
            "giblits": "spr_part_rockclod_blue_projectile",
        },
    },
}
stalagmite_green = {
    "hp": 36,
    "damage": 30,
    "essence": 10,
    "coin_count": [5, 10],
    "secondary_spikes": [[-16, 0], [16, 0], [-8, -16], [8, -16], [-8, 16], [8, 16]],
    "drops": [
        {"item": "ore_iron", "chance": 70, "count_range": [1, 1]},
        {"item": "monster_horn", "chance": 30, "count_range": [1, 2]},
        {"cosmetic": "head_stalagmite_hat", "chance": 5},
    ],
    "sprites": {
        "idle": "spr_nothing",
        "walk": "spr_nothing",
        "windup": "spr_monster_stalagmite_green_windup",
        "attack": "spr_monster_stalagmite_green_attack",
        "tired": "spr_monster_stalagmite_green_tired",
        "flee": "spr_monster_stalagmite_green_flee",
        "hurt": "spr_monster_stalagmite_green_hurt",
        "dying": "spr_monster_stalagmite_green_hurt",
        "misc": {
            "ground_walk": "spr_monster_stalagmite_ground_green_walk",
            "ground_windup": "spr_monster_stalagmite_ground_green_windup",
            "ground_attack": "spr_monster_stalagmite_ground_green_attack",
            "ground_flee": "spr_monster_stalagmite_ground_green_flee",
            "giblits": "spr_part_rockclod_green_projectile",
            "secondary_ground_windup": "spr_monster_stalagmite_green_secondary_ground_windup",
            "secondary_spike_windup": "spr_monster_stalagmite_green_secondary_main_windup",
            "secondary_ground_attack": "spr_monster_stalagmite_green_secondary_ground_attack",
            "secondary_spike_attack": "spr_monster_stalagmite_green_secondary_main_attack",
            "secondary_ground_tired": "spr_monster_stalagmite_green_secondary_ground_tired",
            "secondary_spike_tired": "spr_monster_stalagmite_green_secondary_main_tired",
        },
    },
    "tango": {
        "dying": "SoundEffects/Enemies/Rockclod/Die",
        "windup": "SoundEffects/Enemies/Stalagmite/LargeFormHole",
        "attack": "SoundEffects/Enemies/Stalagmite/BigPunchThru",
        "misc": {
            "withdraw": "SoundEffects/Enemies/Stalagmite/Withdraw",
            "form_mound": "SoundEffects/Enemies/Stalagmite/FormMound",
            "weak_damage": "SoundEffects/Enemies/TakeDamageRockWeak",
            "strong_damage": "SoundEffects/Enemies/TakeDamageRockStrong",
            "death": "SoundEffects/Enemies/Rockclod/Die",
        },
    },
}
stalagmite_purple = {
    "hp": 42,
    "damage": 35,
    "essence": 15,
    "coin_count": [5, 10],
    "secondary_spikes": [
        [-16, 0],
        [16, 0],
        [-8, -16],
        [8, -16],
        [0, -24],
        [-8, 16],
        [8, 16],
        [0, 24],
    ],
    "drops": [
        {"item": "ore_gold", "chance": 70, "count_range": [1, 1]},
        {"item": "monster_horn", "chance": 30, "count_range": [1, 3]},
        {"cosmetic": "head_stalagmite_hat", "chance": 5},
    ],
    "sprites": {
        "idle": "spr_nothing",
        "walk": "spr_nothing",
        "windup": "spr_monster_stalagmite_purple_windup",
        "attack": "spr_monster_stalagmite_purple_attack",
        "tired": "spr_monster_stalagmite_purple_tired",
        "flee": "spr_monster_stalagmite_purple_flee",
        "hurt": "spr_monster_stalagmite_purple_hurt",
        "dying": "spr_monster_stalagmite_purple_hurt",
        "misc": {
            "ground_walk": "spr_monster_stalagmite_ground_purple_walk",
            "ground_windup": "spr_monster_stalagmite_ground_purple_windup",
            "ground_attack": "spr_monster_stalagmite_ground_purple_attack",
            "ground_flee": "spr_monster_stalagmite_ground_purple_flee",
            "giblits": "spr_part_rockclod_purple_projectile",
            "secondary_ground_windup": "spr_monster_stalagmite_purple_secondary_ground_windup",
            "secondary_spike_windup": "spr_monster_stalagmite_purple_secondary_main_windup",
            "secondary_ground_attack": "spr_monster_stalagmite_purple_secondary_ground_attack",
            "secondary_spike_attack": "spr_monster_stalagmite_purple_secondary_main_attack",
            "secondary_ground_tired": "spr_monster_stalagmite_purple_secondary_ground_tired",
            "secondary_spike_tired": "spr_monster_stalagmite_purple_secondary_main_tired",
        },
    },
}

# sap
sapling = {
    "hp": 24,
    "damage": 10,
    "essence": 5,
    "coin_count": [1, 5],
    "drops": [
        {"item": "sap", "chance": 70},
        {"item": "monster_fang", "chance": 30},
        {"cosmetic": "head_sapling_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_sapling_main_idle_north",
            "south": "spr_monster_sapling_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_sapling_main_alert_north",
            "south": "spr_monster_sapling_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_sapling_main_walk_north",
            "south": "spr_monster_sapling_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_sapling_main_windup_north",
            "south": "spr_monster_sapling_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_sapling_main_attack_jump_south",
            "south": "spr_monster_sapling_main_attack_jump_south",
        },
        "tired": {
            "north": "spr_monster_sapling_main_tired_north",
            "south": "spr_monster_sapling_main_tired_south",
        },
        "hurt": {
            "north": "spr_monster_sapling_main_hurt_north",
            "south": "spr_monster_sapling_main_hurt_south",
        },
        "splitting": {
            "north": "spr_monster_sapling_main_hurt_north",
            "south": "spr_monster_sapling_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_sapling_main_death_south",
            "south": "spr_monster_sapling_main_death_south",
        },
        "misc": {
            "idle_variant": "spr_monster_sapling_main_idle_2_south",
            "landing_north": "spr_monster_sapling_main_land_north",
            "landing_south": "spr_monster_sapling_main_land_south",
            "sap_particle": "spr_part_sapling_bits",
            "hit_back_north": "spr_monster_sapling_main_hit_back_south",
            "hit_back_south": "spr_monster_sapling_main_hit_back_south",
        },
    },
}
sapling_blue = {
    "hp": 36,
    "damage": 24,
    "essence": 10,
    "coin_count": [2, 6],
    "speed": 0.7,
    "attack_radius": 52,
    "max_jump_radius": 68,
    "sticky": True,
    "drops": [
        {"item": "sap", "chance": 70, "count_range": [1, 2]},
        {"item": "monster_fang", "chance": 30, "count_range": [1, 2]},
        {"cosmetic": "head_sapling_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_sapling_blue_main_idle_north",
            "south": "spr_monster_sapling_blue_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_sapling_blue_main_alert_north",
            "south": "spr_monster_sapling_blue_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_sapling_blue_main_walk_north",
            "south": "spr_monster_sapling_blue_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_sapling_blue_main_windup_north",
            "south": "spr_monster_sapling_blue_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_sapling_blue_main_attack_jump_south",
            "south": "spr_monster_sapling_blue_main_attack_jump_south",
        },
        "tired": {
            "north": "spr_monster_sapling_blue_main_tired_north",
            "south": "spr_monster_sapling_blue_main_tired_south",
        },
        "hurt": {
            "north": "spr_monster_sapling_blue_main_hurt_north",
            "south": "spr_monster_sapling_blue_main_hurt_south",
        },
        "splitting": {
            "north": "spr_monster_sapling_blue_main_hurt_north",
            "south": "spr_monster_sapling_blue_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_sapling_blue_main_death_south",
            "south": "spr_monster_sapling_blue_main_death_south",
        },
        "misc": {
            "idle_variant": "spr_monster_sapling_blue_main_idle_2_south",
            "landing_north": "spr_monster_sapling_blue_main_land_north",
            "landing_south": "spr_monster_sapling_blue_main_land_south",
            "sap_particle": "spr_part_sapling_blue_bits",
            "hit_back_north": "spr_monster_sapling_blue_main_hit_back_south",
            "hit_back_south": "spr_monster_sapling_blue_main_hit_back_south",
        },
    },
}
sapling_cool = {
    "hp": 36,
    "damage": 17,
    "essence": 10,
    "coin_count": [1, 5],
    "speed": 0.7,
    "attack_radius": 52,
    "max_jump_radius": 68,
    "death_bits": "spr_monster_sapling_cool_bits",
    "drops": [
        {"item": "sap", "chance": 70},
        {"item": "monster_fang", "chance": 30},
        {"cosmetic": "face_gear_sunglasses", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_sapling_cool_main_idle_north",
            "south": "spr_monster_sapling_cool_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_sapling_cool_main_alert_north",
            "south": "spr_monster_sapling_cool_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_sapling_cool_main_walk_north",
            "south": "spr_monster_sapling_cool_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_sapling_cool_main_windup_north",
            "south": "spr_monster_sapling_cool_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_sapling_cool_main_attack_jump_south",
            "south": "spr_monster_sapling_cool_main_attack_jump_south",
        },
        "tired": {
            "north": "spr_monster_sapling_cool_main_tired_north",
            "south": "spr_monster_sapling_cool_main_tired_south",
        },
        "hurt": {
            "north": "spr_monster_sapling_cool_main_hurt_north",
            "south": "spr_monster_sapling_cool_main_hurt_south",
        },
        "splitting": {
            "north": "spr_monster_sapling_cool_main_hurt_north",
            "south": "spr_monster_sapling_cool_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_sapling_cool_main_death_south",
            "south": "spr_monster_sapling_cool_main_death_south",
        },
        "misc": {
            "idle_variant": "spr_monster_sapling_cool_main_idle_2_south",
            "sap_particle": "spr_part_sapling_bits",
            "landing_north": "spr_monster_sapling_cool_main_land_north",
            "landing_south": "spr_monster_sapling_cool_main_land_south",
            "hit_back_north": "spr_monster_sapling_cool_main_hit_back_south",
            "hit_back_south": "spr_monster_sapling_cool_main_hit_back_south",
        },
    },
}
sapling_orange = {
    "hp": 72,
    "damage": 44,
    "essence": 20,
    "speed": 0.8,
    "attack_radius": 60,
    "max_jump_radius": 78,
    "sap_children_birth_timer": 60,
    "sap_children_birth_distance": 15,
    "sap_children": 2,
    "sap_children_species": "sapling_orange_mini",
    "drops": [
        {"item": "sap", "chance": 70, "count_range": [1, 3]},
        {"item": "monster_fang", "chance": 30, "count_range": [1, 3]},
        {"cosmetic": "head_sapling_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_sapling_orange_main_idle_north",
            "south": "spr_monster_sapling_orange_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_sapling_orange_main_alert_north",
            "south": "spr_monster_sapling_orange_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_sapling_orange_main_walk_north",
            "south": "spr_monster_sapling_orange_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_sapling_orange_main_windup_north",
            "south": "spr_monster_sapling_orange_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_sapling_orange_main_attack_jump_south",
            "south": "spr_monster_sapling_orange_main_attack_jump_south",
        },
        "tired": {
            "north": "spr_monster_sapling_orange_main_tired_north",
            "south": "spr_monster_sapling_orange_main_tired_south",
        },
        "hurt": {
            "north": "spr_monster_sapling_orange_main_hurt_north",
            "south": "spr_monster_sapling_orange_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_sapling_orange_main_death_south",
            "south": "spr_monster_sapling_orange_main_death_south",
        },
        "splitting": {
            "north": "spr_monster_sapling_orange_main_split_south",
            "south": "spr_monster_sapling_orange_main_split_south",
        },
        "misc": {
            "idle_variant": "spr_monster_sapling_orange_main_idle_2_south",
            "landing_north": "spr_monster_sapling_orange_main_land_north",
            "landing_south": "spr_monster_sapling_orange_main_land_south",
            "sap_particle": "spr_part_sapling_orange_bits",
            "hit_back_north": "spr_monster_sapling_orange_main_hit_back_south",
            "hit_back_south": "spr_monster_sapling_orange_main_hit_back_south",
        },
    },
}
sapling_orange_mini = {
    "hp": 24,
    "damage": 10,
    "essence": 5,
    "speed": 0.5,
    "attack_radius": 50,
    "max_jump_radius": 60,
    "drops": [{"item": "sap", "chance": 35}, {"item": "monster_fang", "chance": 15}],
    "sprites": {
        "idle": {
            "north": "spr_monster_sapling_orange_mini_main_idle_north",
            "south": "spr_monster_sapling_orange_mini_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_sapling_orange_mini_main_alert_north",
            "south": "spr_monster_sapling_orange_mini_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_sapling_orange_mini_main_walk_north",
            "south": "spr_monster_sapling_orange_mini_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_sapling_orange_mini_main_windup_north",
            "south": "spr_monster_sapling_orange_mini_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_sapling_orange_mini_main_attack_jump_south",
            "south": "spr_monster_sapling_orange_mini_main_attack_jump_south",
        },
        "tired": {
            "north": "spr_monster_sapling_orange_mini_main_tired_north",
            "south": "spr_monster_sapling_orange_mini_main_tired_south",
        },
        "hurt": {
            "north": "spr_monster_sapling_orange_mini_main_hurt_north",
            "south": "spr_monster_sapling_orange_mini_main_hurt_south",
        },
        "splitting": {
            "north": "spr_monster_sapling_orange_mini_main_hurt_north",
            "south": "spr_monster_sapling_orange_mini_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_sapling_orange_mini_main_death_south",
            "south": "spr_monster_sapling_orange_mini_main_death_south",
        },
        "misc": {
            "idle_variant": "spr_monster_sapling_orange_mini_main_idle_2_south",
            "landing_north": "spr_monster_sapling_orange_mini_main_land_north",
            "landing_south": "spr_monster_sapling_orange_mini_main_land_south",
            "sap_particle": "spr_part_sapling_orange_bits",
            "hit_back_north": "spr_monster_sapling_orange_mini_main_hit_back_south",
            "hit_back_south": "spr_monster_sapling_orange_mini_main_hit_back_south",
        },
    },
}
sapling_pink = {
    "hp": 144,
    "damage": 60,
    "essence": 25,
    "speed": 0.85,
    "attack_radius": 64,
    "max_jump_radius": 82,
    "drops": [
        {"item": "sap", "chance": 20, "exclusive": False},
        {"item": "sap", "chance": 10, "exclusive": False},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_sapling_pink_main_idle_north",
            "south": "spr_monster_sapling_pink_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_sapling_pink_main_alert_north",
            "south": "spr_monster_sapling_pink_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_sapling_pink_main_walk_north",
            "south": "spr_monster_sapling_pink_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_sapling_pink_main_windup_north",
            "south": "spr_monster_sapling_pink_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_sapling_pink_main_attack_jump_south",
            "south": "spr_monster_sapling_pink_main_attack_jump_south",
        },
        "tired": {
            "north": "spr_monster_sapling_pink_main_tired_north",
            "south": "spr_monster_sapling_pink_main_tired_south",
        },
        "hurt": {
            "north": "spr_monster_sapling_pink_main_hurt_north",
            "south": "spr_monster_sapling_pink_main_hurt_south",
        },
        "splitting": {
            "north": "spr_monster_sapling_pink_main_hurt_north",
            "south": "spr_monster_sapling_pink_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_sapling_pink_main_death_south",
            "south": "spr_monster_sapling_pink_main_death_south",
        },
        "misc": {
            "idle_variant": "spr_monster_sapling_pink_main_idle_2_south",
            "landing_north": "spr_monster_sapling_pink_main_land_north",
            "landing_south": "spr_monster_sapling_pink_main_land_south",
            "sap_particle": "spr_part_sapling_pink_bits",
            "hit_back_north": "spr_monster_sapling_pink_main_hit_back_south",
            "hit_back_south": "spr_monster_sapling_pink_main_hit_back_south",
        },
    },
}
sapling_purple = {
    "hp": 48,
    "damage": 34,
    "essence": 15,
    "coin_count": [4, 8],
    "speed": 0.75,
    "attack_radius": 56,
    "max_jump_radius": 72,
    "drops": [
        {"item": "sap", "chance": 70, "count_range": [1, 2]},
        {"item": "monster_fang", "chance": 30, "count_range": [1, 2]},
        {"cosmetic": "head_sapling_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_sapling_purple_main_idle_north",
            "south": "spr_monster_sapling_purple_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_sapling_purple_main_alert_north",
            "south": "spr_monster_sapling_purple_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_sapling_purple_main_walk_north",
            "south": "spr_monster_sapling_purple_main_walk_south",
        },
        "windup": {
            "north": "spr_monster_sapling_purple_main_windup_north",
            "south": "spr_monster_sapling_purple_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_sapling_purple_main_attack_jump_south",
            "south": "spr_monster_sapling_purple_main_attack_jump_south",
        },
        "tired": {
            "north": "spr_monster_sapling_purple_main_tired_north",
            "south": "spr_monster_sapling_purple_main_tired_south",
        },
        "hurt": {
            "north": "spr_monster_sapling_purple_main_hurt_north",
            "south": "spr_monster_sapling_purple_main_hurt_south",
        },
        "splitting": {
            "north": "spr_monster_sapling_purple_main_hurt_north",
            "south": "spr_monster_sapling_purple_main_hurt_south",
        },
        "dying": {
            "north": "spr_monster_sapling_purple_main_death_south",
            "south": "spr_monster_sapling_purple_main_death_south",
        },
        "misc": {
            "idle_variant": "spr_monster_sapling_purple_main_idle_2_south",
            "landing_north": "spr_monster_sapling_purple_main_land_north",
            "landing_south": "spr_monster_sapling_purple_main_land_south",
            "sap_particle": "spr_part_sapling_purple_bits",
            "hit_back_north": "spr_monster_sapling_purple_main_hit_back_south",
            "hit_back_south": "spr_monster_sapling_purple_main_hit_back_south",
        },
    },
}

# shroom
mushroom = {
    "hp": 24,
    "damage": 15,
    "essence": 5,
    "coin_count": [1, 5],
    "drops": [
        {"item": "red_toadstool", "chance": 70},
        {"item": "monster_powder", "chance": 30},
        {"cosmetic": "head_mushroom_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_mushroom_main_idle_north",
            "south": "spr_monster_mushroom_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_mushroom_main_alert_north",
            "south": "spr_monster_mushroom_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_mushroom_main_walk_north",
            "south": "spr_monster_mushroom_main_walk_south",
        },
        "windup_slide": {
            "north": "spr_monster_mushroom_main_windup_slide_south",
            "south": "spr_monster_mushroom_main_windup_slide_south",
        },
        "windup": {
            "north": "spr_monster_mushroom_main_windup_south",
            "south": "spr_monster_mushroom_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_mushroom_main_attack_south",
            "south": "spr_monster_mushroom_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_mushroom_main_tired_south",
            "south": "spr_monster_mushroom_main_tired_south",
        },
        "shell": {
            "north": "spr_monster_mushroom_main_shield_enter_south",
            "south": "spr_monster_mushroom_main_shield_enter_south",
        },
        "dying": {
            "north": "spr_monster_mushroom_main_death_south",
            "south": "spr_monster_mushroom_main_death_south",
        },
        "wiggle": {
            "north": "spr_monster_mushroom_main_wiggle_south",
            "south": "spr_monster_mushroom_main_wiggle_south",
        },
        "wiggle_exit": {
            "north": "spr_monster_mushroom_main_wiggle_exit_south",
            "south": "spr_monster_mushroom_main_wiggle_exit_south",
        },
        "explode": {
            "north": "spr_monster_mushroom_main_death_capoff_south",
            "south": "spr_monster_mushroom_main_death_capoff_south",
        },
        "misc": {
            "sleep": "spr_monster_mushroom_main_sleep_south",
            "attack_vfx": "spr_fx_monster_mushroom_spore_attack",
            "shell_hit": "spr_monster_mushroom_main_shield_hit_south",
            "enter_wiggle": "spr_monster_mushroom_main_wiggle_enter_south",
            "hurt_wiggle": "spr_monster_mushroom_main_wiggle_hurt_south",
        },
    },
}
mushroom_blue = {
    "hp": 72,
    "damage": 35,
    "essence": 15,
    "coin_count": [4, 8],
    "speed": 0.75,
    "drops": [
        {"item": "glowing_mushroom", "chance": 70, "count_range": [1, 1]},
        {"item": "monster_powder", "chance": 30, "count_range": [1, 2]},
        {"cosmetic": "head_mushroom_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_mushroom_blue_main_idle_north",
            "south": "spr_monster_mushroom_blue_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_mushroom_blue_main_alert_north",
            "south": "spr_monster_mushroom_blue_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_mushroom_blue_main_walk_north",
            "south": "spr_monster_mushroom_blue_main_walk_south",
        },
        "windup_slide": {
            "north": "spr_monster_mushroom_blue_main_windup_slide_south",
            "south": "spr_monster_mushroom_blue_main_windup_slide_south",
        },
        "windup": {
            "north": "spr_monster_mushroom_blue_main_windup_south",
            "south": "spr_monster_mushroom_blue_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_mushroom_blue_main_attack_south",
            "south": "spr_monster_mushroom_blue_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_mushroom_blue_main_tired_south",
            "south": "spr_monster_mushroom_blue_main_tired_south",
        },
        "shell": {
            "north": "spr_monster_mushroom_blue_main_shield_enter_south",
            "south": "spr_monster_mushroom_blue_main_shield_enter_south",
        },
        "dying": {
            "north": "spr_monster_mushroom_blue_main_death_south",
            "south": "spr_monster_mushroom_blue_main_death_south",
        },
        "wiggle": {
            "north": "spr_monster_mushroom_blue_main_wiggle_south",
            "south": "spr_monster_mushroom_blue_main_wiggle_south",
        },
        "wiggle_exit": {
            "north": "spr_monster_mushroom_blue_main_wiggle_exit_south",
            "south": "spr_monster_mushroom_blue_main_wiggle_exit_south",
        },
        "explode": {
            "north": "spr_monster_mushroom_blue_main_death_capoff_south",
            "south": "spr_monster_mushroom_blue_main_death_capoff_south",
        },
        "misc": {
            "sleep": "spr_monster_mushroom_blue_main_sleep_south",
            "attack_vfx": "spr_fx_monster_mushroom_spore_attack",
            "shell_hit": "spr_monster_mushroom_blue_main_shield_hit_south",
            "enter_wiggle": "spr_monster_mushroom_blue_main_wiggle_enter_south",
            "hurt_wiggle": "spr_monster_mushroom_blue_main_wiggle_hurt_south",
        },
    },
}
mushroom_green = {
    "hp": 48,
    "damage": 25,
    "essence": 10,
    "coin_count": [2, 6],
    "speed": 0.7,
    "explodes": True,
    "explode": [100, 120],
    "drops": [
        {"item": "wild_mushroom", "chance": 70, "count_range": [1, 1]},
        {"item": "monster_powder", "chance": 30, "count_range": [1, 2]},
        {"cosmetic": "head_mushroom_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_mushroom_green_main_idle_north",
            "south": "spr_monster_mushroom_green_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_mushroom_green_main_alert_north",
            "south": "spr_monster_mushroom_green_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_mushroom_green_main_walk_north",
            "south": "spr_monster_mushroom_green_main_walk_south",
        },
        "windup_slide": {
            "north": "spr_monster_mushroom_green_main_windup_slide_south",
            "south": "spr_monster_mushroom_green_main_windup_slide_south",
        },
        "windup": {
            "north": "spr_monster_mushroom_green_main_windup_south",
            "south": "spr_monster_mushroom_green_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_mushroom_green_main_attack_south",
            "south": "spr_monster_mushroom_green_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_mushroom_green_main_tired_south",
            "south": "spr_monster_mushroom_green_main_tired_south",
        },
        "shell": {
            "north": "spr_monster_mushroom_green_main_shield_enter_south",
            "south": "spr_monster_mushroom_green_main_shield_enter_south",
        },
        "dying": {
            "north": "spr_monster_mushroom_green_main_death_south",
            "south": "spr_monster_mushroom_green_main_death_south",
        },
        "wiggle": {
            "north": "spr_monster_mushroom_green_main_wiggle_south",
            "south": "spr_monster_mushroom_green_main_wiggle_south",
        },
        "wiggle_exit": {
            "north": "spr_monster_mushroom_green_main_wiggle_exit_south",
            "south": "spr_monster_mushroom_green_main_wiggle_exit_south",
        },
        "explode": {
            "north": "spr_monster_mushroom_green_main_death_capoff_south",
            "south": "spr_monster_mushroom_green_main_death_capoff_south",
        },
        "misc": {
            "sleep": "spr_monster_mushroom_green_main_sleep_south",
            "attack_vfx": "spr_fx_monster_mushroom_green_spore_attack",
            "shell_hit": "spr_monster_mushroom_green_main_shield_hit_south",
            "enter_wiggle": "spr_monster_mushroom_green_main_wiggle_enter_south",
            "hurt_wiggle": "spr_monster_mushroom_green_main_wiggle_hurt_south",
            "mushroom_bits": "spr_monster_mushroom_green_bits_hat",
        },
    },
}
mushroom_purple = {
    "hp": 96,
    "damage": 50,
    "essence": 20,
    "speed": 0.8,
    "spew_lava": True,
    "lava_damage": 1,
    "lava_angle": 90,
    "lava_distance": 16,
    "lava_timer": 300,
    "drops": [
        {"item": "purple_mushroom", "chance": 70, "count_range": [1, 1]},
        {"item": "monster_powder", "chance": 30, "count_range": [1, 3]},
        {"cosmetic": "head_mushroom_hat", "chance": 5},
    ],
    "sprites": {
        "idle": {
            "north": "spr_monster_mushroom_purple_main_idle_north",
            "south": "spr_monster_mushroom_purple_main_idle_south",
        },
        "acknowledgment": {
            "north": "spr_monster_mushroom_purple_main_alert_north",
            "south": "spr_monster_mushroom_purple_main_alert_south",
        },
        "walk": {
            "north": "spr_monster_mushroom_purple_main_walk_north",
            "south": "spr_monster_mushroom_purple_main_walk_south",
        },
        "windup_slide": {
            "north": "spr_monster_mushroom_purple_main_windup_slide_south",
            "south": "spr_monster_mushroom_purple_main_windup_slide_south",
        },
        "windup": {
            "north": "spr_monster_mushroom_purple_main_windup_south",
            "south": "spr_monster_mushroom_purple_main_windup_south",
        },
        "attack": {
            "north": "spr_monster_mushroom_purple_main_attack_south",
            "south": "spr_monster_mushroom_purple_main_attack_south",
        },
        "tired": {
            "north": "spr_monster_mushroom_purple_main_tired_south",
            "south": "spr_monster_mushroom_purple_main_tired_south",
        },
        "shell": {
            "north": "spr_monster_mushroom_purple_main_shield_enter_south",
            "south": "spr_monster_mushroom_purple_main_shield_enter_south",
        },
        "dying": {
            "north": "spr_monster_mushroom_purple_main_death_south",
            "south": "spr_monster_mushroom_purple_main_death_south",
        },
        "wiggle": {
            "north": "spr_monster_mushroom_purple_main_wiggle_south",
            "south": "spr_monster_mushroom_purple_main_wiggle_south",
        },
        "wiggle_exit": {
            "north": "spr_monster_mushroom_purple_main_wiggle_exit_south",
            "south": "spr_monster_mushroom_purple_main_wiggle_exit_south",
        },
        "explode": {
            "north": "spr_monster_mushroom_purple_main_death_capoff_south",
            "south": "spr_monster_mushroom_purple_main_death_capoff_south",
        },
        "misc": {
            "sleep": "spr_monster_mushroom_purple_main_sleep_south",
            "attack_vfx": "spr_fx_monster_mushroom_spore_attack",
            "shell_hit": "spr_monster_mushroom_purple_main_shield_hit_south",
            "enter_wiggle": "spr_monster_mushroom_purple_main_wiggle_enter_south",
            "hurt_wiggle": "spr_monster_mushroom_purple_main_wiggle_hurt_south",
        },
    },
}


#### --------------------- DEFAULTS ---------------------


defaults = {
    "clod": {
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
    },
    "enchantern": {
        "hp": 1,
        "damage": 0,
        "essence": 0,
        "drops": [],
        "projectile_timer": [60, 90],
        "drops_balls": True,
        "charge_timer": [360, 400],
        "flee_timer": [180, 240],
        "charge_speed": 1.6,
        "flee_speed": 1.8,
        "coin_count": [1, 3],
        "starting_dir": [0, 360],
        "damage_number_offset": -21,
        "electrocute_kind": "yellow",
        "attack_frame": 1,
        "iframes": 1,
        "gm_object": "obj_monster_enchantern",
        "hitbox": "spr_monster_enchantern_off_hurt_box",
        "hurtbox": "spr_monster_enchantern_off_hurt_box",
        "patience_acknowledgement_reset": -120,
        "aggro_radius": 384,
        "use_circle": True,
        "attack_radius": 96,
        "windup": [70, 110],
        "acknowledgment": [45, 60],
        "waiting": [90, 110],
        "hurt": [24, 32],
        "push_radius": 4,
        "push_force": 0.25,
        "pushed_radius": 7,
        "sprites": {"misc": {}},
        "tango": {
            "flicker_on": "SoundEffects/Enemies/Enchantern/TurnOn",
            "dying": "SoundEffects/Enemies/Rockclod/Die",
            "misc": {
                "active_footstep": "SoundEffects/Enemies/Enchantern/ActiveFootstep",
                "inactive_footstep": "SoundEffects/Enemies/Enchantern/InactiveFootstep",
                "active_loop": "SoundEffects/Enemies/Enchantern/ActiveLoop",
                "wind_down": "SoundEffects/Enemies/Enchantern/WindDown",
                "turn_off": "SoundEffects/Enemies/Enchantern/TurnOff",
                "spawn_orb": "SoundEffects/Enemies/Enchantern/SpawnOrb",
                "weak_damage": "SoundEffects/Enemies/TakeDamageRockStrong",
                "strong_damage": "SoundEffects/Enemies/TakeDamageRockStrong",
            },
        },
    },
    "mimic": {
        "hp": 1000,
        "damage": 0,
        "essence": 0,
        "drops": [],
        "coin_count": [1, 3],
        "starting_dir": [181, 181],
        "damage_number_offset": -15,
        "iframes": 1,
        "gm_object": "obj_monster_mimic",
        "hurtbox": "spr_monster_mimic_main_idle_south",
        "patience_acknowledgement_reset": -120,
        "spit_frame": 17,
        "idle_variant": [120, 240],
        "sprites": {"misc": {}},
        "tango": {
            "attack": "SoundEffects/Enemies/MimicChest/MimicChestAttackOpen",
            "hurt": "SoundEffects/Enemies/MimicChest/MimicChestFlicker",
            "acknowledgment": "SoundEffects/Enemies/EnemyAlerted",
            "misc": {
                "idle_shake": "SoundEffects/Enemies/MimicChest/MimicChestRumble",
                "weak_damage": "SoundEffects/Enemies/TakeDamageFleshWeak",
                "strong_damage": "SoundEffects/Enemies/TakeDamageFleshStrong",
            },
        },
    },
    "mite": {
        "hp": 1,
        "damage": 0,
        "essence": 0,
        "drops": [],
        "speed": 0.5,
        "starting_dir": [0, 360],
        "hide_timer": [30, 45],
        "coin_count": [1, 3],
        "secondary_spikes": False,
        "gm_object": "obj_monster_mite",
        "hitbox": "spr_monster_stalagmite_blue_attack",
        "hurtbox": "spr_monster_stalagmite_blue_attack",
        "damage_number_offset": -14,
        "patience_acknowledgement_reset": -120,
        "aggro_radius": 384,
        "use_circle": True,
        "attack_radius": 8,
        "iframes": 1,
        "hurt": [30, 38],
        "push_radius": 4,
        "push_force": 0.25,
        "pushed_radius": 7,
        "sprites": {"misc": {}},
        "tango": {
            "windup": "SoundEffects/Enemies/Stalagmite/FormHole",
            "attack": "SoundEffects/Enemies/Stalagmite/PunchThru",
            "dying": "SoundEffects/Enemies/Rockclod/Die",
            "misc": {
                "withdraw": "SoundEffects/Enemies/Stalagmite/Withdraw",
                "form_mound": "SoundEffects/Enemies/Stalagmite/FormMound",
                "weak_damage": "SoundEffects/Enemies/TakeDamageRockWeak",
                "strong_damage": "SoundEffects/Enemies/TakeDamageRockStrong",
                "death": "SoundEffects/Enemies/Rockclod/Die",
            },
        },
    },
    "shroom": {
        "hp": 1,
        "damage": 0,
        "essence": 0,
        "drops": [],
        "explodes": False,
        "iframes": 7,
        "gm_object": "obj_monster_shroom",
        "hurtbox": "spr_monster_mushroom_hurtbox",
        "starting_dir": [180, 360],
        "coin_count": [1, 3],
        "damage_number_offset": -15,
        "speed": 0.6,
        "windup_friction": 0.97,
        "patience_acknowledgement_reset": -120,
        "attack_radius": 36,
        "shell_radius": 32,
        "hide_radius": 96,
        "ari_bounce_distance": 4,
        "knockback_multiplier": 0.5,
        "knockback_friction": 0.5,
        "windup_hold_frame": 0,
        "windup": [25, 40],
        "acknowledgment": [45, 55],
        "tired": [45, 55],
        "wiggle": [50, 60],
        "hurt": 12,
        "push_radius": 4,
        "push_force": 0.25,
        "pushed_radius": 7,
        "flip_jump_speed": -1,
        "jump_speed": -2,
        "jump_gravity": 0.12,
        "jump_zx_factor": 8,
        "spew_lava": -1,
        "lava_damage": -1,
        "lava_timer": -1,
        "lava_count": -1,
        "lava_angle": -1,
        "lava_distance": -1,
        "sprites": {"misc": {}},
        "tango": {
            "acknowledgment": "SoundEffects/Enemies/EnemyAlerted",
            "attack": "SoundEffects/Enemies/Mushroom/ExplodeAndSpore",
            "shell": "SoundEffects/Enemies/Mushroom/HideInHat",
            "windup_slide": "SoundEffects/Enemies/Mushroom/Windup",
            "wiggle": "SoundEffects/Enemies/Mushroom/FlipOver",
            "dying": "SoundEffects/Enemies/DieFlesh",
            "misc": {
                "weak_damage": "SoundEffects/Enemies/TakeDamageFleshWeak",
                "strong_damage": "SoundEffects/Enemies/TakeDamageFleshStrong",
                "un_shell": "SoundEffects/Enemies/Mushroom/UnHideInHat",
                "bounce_off": "SoundEffects/Enemies/Mushroom/BounceOff",
                "windup_sparke": "SoundEffects/Enemies/Mushroom/WindupStart",
            },
        },
    },
    "bat": {
        "hp": 1,
        "damage": 0,
        "essence": 0,
        "drops": [],
        "coin_count": [1, 3],
        "attack_duration": [45, 90],
        "windup_duration": [60, 90],
        "flee_timer": [120, 180],
        "starting_dir": [0, 360],
        "acknowledgment": [45, 55],
        "damage_number_offset": -15,
        "iframes": 1,
        "gm_object": "obj_monster_bat",
        "hurtbox": "spr_monster_essence_bat_hurt_box",
        "knockback": 2,
        "knockback_decline": 0.8,
        "flee_speed": 0.75,
        "speed": 0.75,
        "patience_acknowledgement_reset": -120,
        "aggro_radius": 384,
        "attack_radius": 96,
        "sprites": {"misc": {}},
        "tango": {
            "idle": "SoundEffects/Enemies/EssenceBat/WingFlap",
            "walk": "SoundEffects/Enemies/EssenceBat/WingFlap",
            "flee": "SoundEffects/Enemies/EssenceBat/WingFlap",
            "acknowledgment": "SoundEffects/Enemies/EnemyAlerted",
            "windup": "SoundEffects/Enemies/EssenceBat/AttackWindup",
            "dying": "SoundEffects/Enemies/Sapling/SaplingDie",
            "attack": "SoundEffects/Enemies/EssenceBat/AttackSpit",
            "misc": {
                "magic_particles": "SoundEffects/Enemies/EssenceBat/MagicParticles",
                "projectile_spawn": "SoundEffects/Enemies/EssenceBat/EchoProjectile",
                "weak_damage": "SoundEffects/Enemies/TakeDamageFleshWeak",
                "strong_damage": "SoundEffects/Enemies/TakeDamageFleshStrong",
            },
        },
    },
    "sap": {
        "hp": 1,
        "damage": 0,
        "essence": 0,
        "drops": [],
        "sticky": False,
        "coin_count": [1, 1],
        "starting_dir": [0, 360],
        "damage_number_offset": -15,
        "iframes": 1,
        "gm_object": "obj_monster_sap",
        "hitbox": "spr_monster_sapling_main_hit_box",
        "hurtbox": "spr_monster_sapling_main_idle_south",
        "speed": 0.6,
        "patience_acknowledgement_reset": -120,
        "attack_radius": 48,
        "max_jump_radius": 64,
        "windup": [35, 55],
        "acknowledgment": [45, 55],
        "tired": [90, 110],
        "landing": 8,
        "hurt": 12,
        "jump_speed": -2.0,
        "jump_gravity": 0.1,
        "jump_zx_factor": 36,
        "push_radius": 4,
        "push_force": 0.25,
        "pushed_radius": 7,
        "sap_children_birth_distance": 0,
        "sap_children_birth_timer": 0,
        "sap_children": 0,
        "sap_children_species": -1,
        "sprites": {"misc": {}},
        "tango": {
            "acknowledgment": "SoundEffects/Enemies/EnemyAlerted",
            "windup": "SoundEffects/Enemies/Sapling/ChargeUp",
            "dying": "SoundEffects/Enemies/Sapling/SaplingDie",
            "attack": "SoundEffects/Enemies/Sapling/SaplingJump",
            "misc": {
                "land": "SoundEffects/Enemies/Sapling/Land",
                "weak_damage": "SoundEffects/Enemies/TakeDamageFleshWeak",
                "strong_damage": "SoundEffects/Enemies/TakeDamageFleshStrong",
            },
        },
    },
}
"""This variable contains the default configuration of each of the monster types.

Use this to find all possible valid keys you can edit/add in each monster's configuration."""
