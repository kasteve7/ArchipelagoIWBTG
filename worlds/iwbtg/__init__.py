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
from .Items import IWBTGItem, IWBTGItemData, item_table, junk_table, item_groups
from .Locations import IWBTGLocation, setup_locations, all_locations, location_groups
from .Regions import create_regions, connect_regions
from .Names import ItemName, LocationName, EventName
from .Options import IWBTGOptions, iwbtg_option_groups

#class IWBTGSettings(settings.Group):

class IWBTGWeb(WebWorld):
	theme = "grass"

	setup_en = Tutorial(
		"Multiworld Setup Guide",
		"A guide to playing I Wanna be The Guy with Archipelago",
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
	game = "I Wanna be The Guy"
	web = IWBTGWeb()

	#settings: typing.ClassVar[IWBTGSettings]
	
	options_dataclass = IWBTGOptions
	options: IWBTGOptions
	
	required_client_version = (0, 5, 0)

	item_name_to_id = {name: data.code for name, data in item_table.items()}
	location_name_to_id = all_locations
	item_name_groups = item_groups
	location_name_groups = location_groups
	hint_blacklist = {
		LocationName.mike_tyson_defeated,
		LocationName.mecha_birdo_defeated,
		LocationName.dracula_defeated,
		LocationName.kraidgief_defeated,
		LocationName.bowser_defeated,
		LocationName.guy_defeated,
		LocationName.dev_room,
	}

	def __init__(self, multiworld: MultiWorld, player: int):
		super().__init__(multiworld, player)

	def create_regions(self) -> None:
		location_table = setup_locations(self)
		create_regions(self.multiworld, self.player, self, location_table)

		itempool: typing.List[IWBTGItem] = []
		
		connect_regions(self)
		
		base_id = 92000
		
		total_required_locations = 77 #location num needs verifying (85 counted - 6 bosses)
		
		#if self.options.<deathsanity?>:
		#	total_required_locations += #
		
		self.multiworld.get_location(LocationName.guy_defeated, self.player).place_locked_item(self.create_item(ItemName.become_the_guy))
		self.multiworld.get_location(LocationName.dev_room, self.player).place_locked_item(self.create_item(ItemName.dev_room))
		
		self.multiworld.get_location(LocationName.mike_tyson_defeated, self.player).place_locked_item(self.create_item(ItemName.boss_defeated))
		self.multiworld.get_location(LocationName.mecha_birdo_defeated, self.player).place_locked_item(self.create_item(ItemName.boss_defeated))
		self.multiworld.get_location(LocationName.dracula_defeated, self.player).place_locked_item(self.create_item(ItemName.boss_defeated))
		self.multiworld.get_location(LocationName.kraidgief_defeated, self.player).place_locked_item(self.create_item(ItemName.boss_defeated))
		self.multiworld.get_location(LocationName.mother_brain_defeated, self.player).place_locked_item(self.create_item(ItemName.boss_defeated))
		self.multiworld.get_location(LocationName.bowser_defeated, self.player).place_locked_item(self.create_item(ItemName.boss_defeated))
		
		if self.options.additional_progression_items.value != 0: #add optional progression items
			add_prog_item_count = 0
			if "Spike Platform" in self.options.additional_progression_items.value:
				itempool += [self.create_item(ItemName.spike_platform)]
				add_prog_item_count += 1
			if "Link" in self.options.additional_progression_items.value:
				itempool += [self.create_item(ItemName.link)]
				add_prog_item_count += 1
			if "Graveyard Moon" in self.options.additional_progression_items.value:
				itempool += [self.create_item(ItemName.graveyard_moon)]
				add_prog_item_count += 1
			if "Ryu" in self.options.additional_progression_items.value:
				itempool += [self.create_item(ItemName.ryu)]
				add_prog_item_count += 1
			if "Tourian Key" in self.options.additional_progression_items.value:
				itempool += [self.create_item(ItemName.tourian_key)]
				add_prog_item_count += 1
			#total_required_locations += add_prog_item_count
		
		orb_piece_list = [
			ItemName.orb_piece_mike_tyson,
			ItemName.orb_piece_mecha_birdo,
			ItemName.orb_piece_dracula,
			ItemName.orb_piece_kraidgief,
			ItemName.orb_piece_mother_brain,
			ItemName.orb_piece_bowser,]
			
		orb_shard_list = [
			ItemName.orb_shard_mike_tyson,
			ItemName.orb_shard_mecha_birdo,
			ItemName.orb_shard_dracula,
			ItemName.orb_shard_kraidgief,
			ItemName.orb_shard_mother_brain,
			ItemName.orb_shard_bowser,]
		
		if self.options.guy_open.value == 0 or self.options.guy_open.value == 2:
			if self.options.divide_orbs.value == 0: # whole orbs
				itempool += [
					self.create_item(ItemName.orb_mike_tyson),
					self.create_item(ItemName.orb_mecha_birdo),
					self.create_item(ItemName.orb_dracula),
					self.create_item(ItemName.orb_kraidgief),
					self.create_item(ItemName.orb_mother_brain),
					self.create_item(ItemName.orb_bowser),]
				#total_required_locations += 6
			elif self.options.divide_orbs.value == 2:
				for i in orb_piece_list:
					orb_piece_number = 2 #2 per orb
					for j in range(orb_piece_number):
						itempool += [self.create_item(i)]
				total_required_locations += 6*orb_piece_number
			else:
				for i in orb_shard_list:
					#orb_shard_number = 4 #4 per orb
					for j in range(4):
						itempool += [self.create_item(i)]
		if self.options.set_goal.value == 1: #dev room goal
			itempool += [
				self.create_item(ItemName.secret_item_1, ItemClassification.progression),
				self.create_item(ItemName.secret_item_2, ItemClassification.progression),
				self.create_item(ItemName.secret_item_3, ItemClassification.progression),
				self.create_item(ItemName.secret_item_4, ItemClassification.progression),
				self.create_item(ItemName.secret_item_5, ItemClassification.progression),
				self.create_item(ItemName.secret_item_6, ItemClassification.progression),]
		else: #secret items are filler otherwise
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
				itempool += [self.create_item(ItemName.gun_upgrade)]
				#total_required_locations += 1
		
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

		# Finish
		self.multiworld.itempool += itempool

	def create_item(self, name: str, force_classification=False) -> Item:
		data = item_table[name]

		if force_classification:
			classification = force_classification
		else:
			classification = data.classification
		
		created_item = IWBTGItem(name, classification, data.code, self.player)

		return created_item


	def set_rules(self) -> None:
		from .Rules import set_rules
		if hasattr(self.multiworld, "generation_is_fake"):
			if hasattr(self.multiworld, "re_gen_passthrough"):
				if "I Wanna be The Guy" in self.multiworld.re_gen_passthrough:
					slot_data = self.multiworld.re_gen_passthrough["I Wanna be The Guy"]
		set_rules(self)


	def fill_slot_data(self) -> dict[int, any]:
		slot_data = {}
		# Write options to slot_data
		slot_data["additional_progression_items"] = self.options.additional_progression_items.value
		slot_data["gun_upgrades"] = self.options.gun_upgrades.value
		slot_data["free_warping"] = self.options.free_warping.value
		slot_data["guy_open"] = self.options.guy_open.value
		slot_data["guy_boss_count"] = self.options.guy_boss_count.value
		slot_data["secret_item_count"] = self.options.secret_item_count.value
		slot_data["divide_orbs"] = self.options.divide_orbs.value
		slot_data["death_link"] = self.options.death_link.value
		slot_data["death_link_count"] = self.options.divide_orbs.value
				
		return slot_data

	def get_filler_item_name(self) -> str:
		return self.random.choice(list(junk_table.keys()))
