import dataclasses
import os
import typing
import math
import settings
import hashlib
import threading
import pkgutil

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .Items import IWBTGItem, ItemData, item_table, junk_table, item_groups
from .Locations import IWBTGLocation, setup_locations, all_locations, location_groups
from .Regions import create_regions, connect_regions
from .Names import ItemName, LocationName, EventName
from .Options import IWBTGOptions, mmx_option_groups
from .Levels import location_id_to_level_id

#class IWBTGSettings(settings.Group):

class IWBTGWeb(WebWorld):
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing I Wanna Be the Guy with Archipelago",
        "English",
        "setup_en.md",
        "setup/en",
        ["Seltzy"]
    )

    tutorials = [setup_en]

    option_groups = iwbtg_option_groups


class IWBTGWorld(World):
    """
    I Wanna Be the Guy: The Movie: The Game is a 2D platform indie freeware video game created by independent developer Michael "Kayin" O'Reilly for Microsoft Windows using Multimedia Fusion 2. First released in October 2007, the game is not in active development despite being listed as a beta, though the source code for the game was released by Kayin in November 2011. IWBTG is most famous for its difficulty. Most of the landscape is engineered specifically to kill the player character. Alongside a traditional range of recognizable dangers, such as spikes and pits, there are many less obvious threats as well, most of which are all but impossible to avoid without either previous knowledge or trial and error.
    """
    game = "I Wanna Be the Guy"
    web = IWBTGWeb()

    settings: typing.ClassVar[IWBTGSettings]
    
    options_dataclass = IWBTGOptions
    options: IWBTGOptions
    
    required_client_version = (0, 5, 0)

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = all_locations
    item_name_groups = item_groups
    location_name_groups = location_groups
    hint_blacklist = {
        LocationName.boss_defeated,
        LocationName.victory,
	LocationName.dev_room,
    }

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def create_regions(self) -> None:
        location_table = setup_locations(self)
        create_regions(self.multiworld, self.player, self, location_table)

        itempool: typing.List[IWBTGItem] = []
        
        connect_regions(self)
        
        total_required_locations = 67 #location num needs verifying (73 counted - bosses)
		
        #if self.options.<deathsanity?>:
        #    total_required_locations += 26
		
		orb_piece_list = [
			ItemName.orb_piece_mike_tyson,
			ItemName.orb_piece_mecha_birdo,
			ItemName.orb_piece_dracula,
			ItemName.orb_piece_kraidgeif,
			ItemName.orb_piece_mother_brain,
			ItemName.orb_piece_bowser]
		
        if "Orbs" in self.options.guy_open.value:
			if self.options.divide_orbs.value == 0: # whole orbs
				itempool += [
					self.create_item(ItemName.orb_mike_tyson),
					self.create_item(ItemName.orb_mecha_birdo),
					self.create_item(ItemName.orb_dracula),
					self.create_item(ItemName.orb_kraidgief),
					self.create_item(ItemName.orb_mother_brain),
					self.create_item(ItemName.orb_bowser),]
				total_required_locations += 6
			else:
				for i in orb_piece_list:
					orb_piece_number = self.options.divide_orbs.value #2 or 4 per orb
					for j in range(orb_piece_number):
						itempool += [self.create_item(orb_piece_list[i])]
				total_required_locations += 6*orb_piece_number
						
		if self.options.set_goal.value == 1:
			itempool += [
				self.create_item(ItemName.secret_item_1, ItemClassification.progression),
				self.create_item(ItemName.secret_item_2, ItemClassification.progression),
				self.create_item(ItemName.secret_item_3, ItemClassification.progression),
				self.create_item(ItemName.secret_item_4, ItemClassification.progression),
				self.create_item(ItemName.secret_item_5, ItemClassification.progression),
				self.create_item(ItemName.secret_item_6, ItemClassification.progression),]
		else
			itempool += [
				self.create_item(ItemName.secret_item_1),
				self.create_item(ItemName.secret_item_2),
				self.create_item(ItemName.secret_item_3),
				self.create_item(ItemName.secret_item_4),
				self.create_item(ItemName.secret_item_5),
				self.create_item(ItemName.secret_item_6),]
		
        # Add bow into the pool
        itempool += [self.create_item(ItemName.bow)]

		# Add gun upgrades to the pool
        if self.options.gun_upgrades.value:
            for u in range(self.options.gun_upgrades_count.value):
				itempool += [self.create_item(gun_upgrade)]
				total_required_locations += 1
        


        itempool += [self.create_item(ItemName.helmet)]

        itempool += [self.create_item(ItemName.legs)]
        if self.options.air_dash.value:
            if "Armor Upgrades" in sigma_open and self.options.sigma_upgrade_count.value > 0:
                itempool += [self.create_item(ItemName.legs)]
            else:
                itempool += [self.create_item(ItemName.legs, ItemClassification.useful)]

        # Add heart tanks into the pool
        if "Heart Tanks" in sigma_open and self.options.sigma_heart_tank_count.value > 0:
            i = self.options.sigma_heart_tank_count.value
            itempool += [self.create_item(ItemName.heart_tank) for _ in range(i)]
            if i != 8:
                itempool += [self.create_item(ItemName.heart_tank, ItemClassification.useful) for _ in range(8 - i)]
        else:
            itempool += [self.create_item(ItemName.heart_tank, ItemClassification.useful) for _ in range(8)]

        # Add sub tanks into the pool
        if "Sub Tanks" in sigma_open and self.options.sigma_sub_tank_count.value > 0:
            i = self.options.sigma_sub_tank_count.value
            itempool += [self.create_item(ItemName.sub_tank) for _ in range(i)]
            if i != 4:
                itempool += [self.create_item(ItemName.sub_tank, ItemClassification.useful) for _ in range(4 - i)]
        else:
            itempool += [self.create_item(ItemName.sub_tank, ItemClassification.useful) for _ in range(4)]

        # Add junk items into the pool
        junk_count = total_required_locations - len(itempool)

        junk_weights = []
        junk_weights += ([ItemName.bird_trap] * 30)
        junk_weights += ([ItemName.fruit_trap] * 40)
        junk_weights += ([ItemName.error_trap] * 10)
        junk_weights += ([ItemName.stone_trap] * 30)
        junk_weights += ([ItemName.death_trap] * 10)

        junk_pool = []
        for i in range(junk_count):
            junk_item = self.random.choice(junk_weights)
            junk_pool.append(self.create_item(junk_item))

        itempool += junk_pool

        # Set Victories
        boss_location_names = [
            LocationName.mike_tyson_defeated,
			LocationName.mecha_birdo_defeated,
			LocationName.dracula_defeated,
			LocationName.kraidgief_defeated,
			LocationName.bowser_defeated,
        ]
        for location_name in boss_location_names:
            self.multiworld.get_location(location_name, self.player).place_locked_item(self.create_item(ItemName.boss_defeated))

        # Set victory items
        self.multiworld.get_location(LocationName.guy_defeated, self.player).place_locked_item(self.create_item(ItemName.guy_defeated))
        self.multiworld.get_location(LocationName.dev_room, self.player).place_locked_item(self.create_item(ItemName.dev_room))

        # Finish
        self.multiworld.itempool += itempool


    def create_item(self, name: str, force_classification=False) -> Item:
        data = item_table[name]

        if force_classification:
            classification = force_classification
        elif data.progression:
            classification = ItemClassification.progression
        elif data.trap:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
        
        created_item = IWBTGItem(name, classification, data.code, self.player)

        return created_item


    def set_rules(self):
        from .Rules import set_rules
        if hasattr(self.multiworld, "generation_is_fake"):
            if hasattr(self.multiworld, "re_gen_passthrough"):
                if "Mega Man X" in self.multiworld.re_gen_passthrough:
                    slot_data = self.multiworld.re_gen_passthrough["Mega Man X"]
                    self.boss_weaknesses = slot_data["weakness_rules"]
        set_rules(self)



    def fill_slot_data(self):
        slot_data = {}
        # Write options to slot_data
        slot_data["energy_link"] = self.options.energy_link.value
        slot_data["boss_weakness_rando"] = self.options.boss_weakness_rando.value
        slot_data["boss_weakness_strictness"] = self.options.boss_weakness_strictness.value
        slot_data["pickupsanity"] = self.options.pickupsanity.value
        slot_data["jammed_buster"] = self.options.jammed_buster.value
        slot_data["hadouken_in_pool"] = self.options.hadouken_in_pool.value
        slot_data["pickupsanity"] = self.options.pickupsanity.value
        slot_data["logic_boss_weakness"] = self.options.logic_boss_weakness.value
        slot_data["logic_leg_sigma"] = self.options.logic_leg_sigma.value
        slot_data["logic_charged_shotgun_ice"] = self.options.logic_charged_shotgun_ice.value
        slot_data["sigma_all_levels"] = self.options.sigma_all_levels.value
        value = 0
        sigma_open = self.options.sigma_open.value
        if "Medals" in sigma_open:
            value |= 0x01
        if "Weapons" in sigma_open:
            value |= 0x02
        if "Armor Upgrades" in sigma_open:
            value |= 0x04
        if "Heart Tanks" in sigma_open:
            value |= 0x08
        if "Sub Tanks" in sigma_open:
            value |= 0x10
        slot_data["sigma_open"] = value
        slot_data["sigma_medal_count"] = self.options.sigma_medal_count.value
        slot_data["sigma_weapon_count"] = self.options.sigma_weapon_count.value
        slot_data["sigma_upgrade_count"] = self.options.sigma_upgrade_count.value
        slot_data["sigma_heart_tank_count"] = self.options.sigma_heart_tank_count.value
        slot_data["sigma_sub_tank_count"] = self.options.sigma_sub_tank_count.value

        # Write boss weaknesses to slot_data (and for UT)
        slot_data["boss_weaknesses"] = {}
        slot_data["weakness_rules"] = {}
        for boss, entries in self.boss_weaknesses.items():
            slot_data["weakness_rules"][boss] = entries.copy()
            slot_data["boss_weaknesses"][boss] = []
            for entry in entries:
                slot_data["boss_weaknesses"][boss].append(entry[1])
                
        return slot_data


    def generate_early(self):
        if ItemName.legs not in self.options.start_inventory_from_pool and self.options.early_legs:
            self.multiworld.early_items[self.player][ItemName.legs] = 1
            
        # Generate weaknesses
        self.boss_weakness_data = {}
        self.boss_weaknesses = {}
        handle_weaknesses(self)


    def interpret_slot_data(self, slot_data):
        local_weaknesses = dict()
        for boss, entries in slot_data["weakness_rules"].items():
            local_weaknesses[boss] = entries.copy()
        return {"weakness_rules": local_weaknesses}
    

    def write_spoiler(self, spoiler_handle: typing.TextIO) -> None:
        if self.options.boss_weakness_rando != "vanilla":
            spoiler_handle.write(f"\nMega Man X boss weaknesses for {self.multiworld.player_name[self.player]}:\n")
            
            for boss, data in self.boss_weaknesses.items():
                weaknesses = ""
                for i in range(len(data)):
                    weaknesses += f"{weapon_id[data[i][1]]}, "
                weaknesses = weaknesses[:-2]
                spoiler_handle.writelines(f"{boss + ':':<30s}{weaknesses}\n")


    def extend_hint_information(self, hint_data: typing.Dict[int, typing.Dict[int, str]]):
        if not self.options.boss_weakness_rando:
            return
        
        boss_to_id = {
            0x00: "Armored Armadillo",
            0x01: "Chill Penguin",
            0x02: "Spark Mandrill",
            0x03: "Launch Octopus",
            0x04: "Boomer Kuwanger",
            0x05: "Sting Chameleon",
            0x06: "Storm Eagle",
            0x07: "Flame Mammoth",
            0x08: "Bospider",
            0x09: "Vile",
            0x0A: "Boomer Kuwanger",
            0x0B: "Chill Penguin",
            0x0C: "Storm Eagle",
            0x0D: "Rangda Bangda",
            0x0E: "Armored Armadillo",
            0x0F: "Sting Chameleon",
            0x10: "Spark Mandrill",
            0x11: "Launch Octopus",
            0x12: "Flame Mammoth",
            0x17: "Thunder Slimer",
            0x1E: "D-Rex",
            0x13: "Velguarder",
            0x1F: "Sigma",
        }
        boss_weakness_hint_data = {}
        for loc_name, level_data in location_id_to_level_id.items():
            if level_data[1] == 0x000:
                boss_id = level_data[2]
                if boss_id not in boss_to_id.keys():
                    continue
                boss = boss_to_id[boss_id]
                data = self.boss_weaknesses[boss]
                weaknesses = ""
                for i in range(len(data)):
                    weaknesses += f"{weapon_id[data[i][1]]}, "
                weaknesses = weaknesses[:-2]
                if boss == "Sigma":
                    data = self.boss_weaknesses["Wolf Sigma"]
                    weaknesses += ". Wolf Sigma: "
                    for i in range(len(data)):
                        weaknesses += f"{weapon_id[data[i][1]]}, "
                    weaknesses = weaknesses[:-2]
                location = self.multiworld.get_location(loc_name, self.player)
                boss_weakness_hint_data[location.address] = weaknesses

        hint_data[self.player] = boss_weakness_hint_data


    def get_filler_item_name(self) -> str:
        return self.random.choice(list(junk_table.keys()))


    def generate_output(self, output_directory: str):
        try:
            patch = MMXProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
            patch.write_file("mmx_basepatch.bsdiff4", pkgutil.get_data(__name__, "data/mmx_basepatch.bsdiff4"))
            patch_rom(self, patch)

            self.rom_name = patch.name

            patch.write(os.path.join(output_directory,
                                     f"{self.multiworld.get_out_file_name_base(self.player)}{patch.patch_file_ending}"))
        except Exception:
            raise
        finally:
            self.rom_name_available_event.set()  # make sure threading continues and errors are collected


    def modify_multidata(self, multidata: dict):
        import base64
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]
