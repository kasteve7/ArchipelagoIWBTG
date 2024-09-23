from worlds.generic.Rules import add_rule, set_rule
from BaseClasses import CollectionState

from . import IWBTGWorld
from .Names import LocationName, ItemName, RegionName, EventName

def set_rules(world: IWBTGWorld):
	player = world.player
	multiworld = world.multiworld

	if world.options.set_goal.value == 0:
		multiworld.completion_condition[player] = lambda state: state.has(ItemName.guy_defeated, player)
	else:
		multiworld.completion_condition[player] = lambda state: state.has(ItemName.dev_room, player)

	if world.options.additional_progression_items.value:
		if "Spike Platform" in world.options.additional_progression_items.value:
			# need spike platform item
			set_rule(multiworld.get_entrance(f"{RegionName.guy_level} -> {RegionName.guy_level_sky}", player),
					 lambda state: state.has(ItemName.spike_platform, player))
		if "Link" in world.options.additional_progression_items.value:
			multiworld.local_early_items[player][ItemName.link] = 1
			# need link item
			set_rule(multiworld.get_entrance(f"{RegionName.zelda_level} -> {RegionName.graveyard_level}", player),
					 lambda state: state.has(ItemName.link, player))
		if "Graveyard Moon" in world.options.additional_progression_items.value:
			multiworld.local_early_items[player][ItemName.graveyard_moon] = 1
			# need moon item
			set_rule(multiworld.get_entrance(f"{RegionName.graveyard_level} -> {RegionName.tower_level_top}", player),
					 lambda state: state.has(ItemName.graveyard_moon, player))
		if "Ryu" in world.options.additional_progression_items.value:
			# need ryu item
			set_rule(multiworld.get_entrance(f"{RegionName.tower_level_top} -> {RegionName.dracula_level}", player),
					 lambda state: state.has(ItemName.ryu, player))	
		if "Tourian Key" in world.options.additional_progression_items.value:
			# need tourian key item
			set_rule(multiworld.get_entrance(f"{RegionName.megaman_level} -> {RegionName.tourian_level}", player),
					 lambda state: state.has(ItemName.tourian_key, player))
		
	# Fortress entrance rules
	fortress_open = world.options.guy_open.value
	entrance = multiworld.get_entrance(f"{RegionName.gate_level} -> {RegionName.road_level}", player)

	if "Orbs" in fortress_open:
		if world.options.divide_orbs.value == 0:
			add_rule(entrance, lambda state: state.has_group_unique("Orbs", player, world.options.guy_orb_count.value))
		else:
			add_rule(entrance, lambda state: 
				state.has_all_counts(ItemName.orb_piece_mike_tyson, player, world.options.divide_orbs.value) and
				state.has_all_counts(ItemName.orb_piece_mecha_birdo, player, world.options.divide_orbs.value) and
				state.has_all_counts(ItemName.orb_piece_dracula, player, world.options.divide_orbs.value) and
				state.has_all_counts(ItemName.orb_piece_kraidgief, player, world.options.divide_orbs.value) and
				state.has_all_counts(ItemName.orb_piece_mother_brain, player, world.options.divide_orbs.value) and
				state.has_all_counts(ItemName.orb_piece_bowser, player, world.options.divide_orbs.value))
				
	if "Bosses" in fortress_open and world.options.guy_boss_count.value:
		add_rule(entrance, lambda state: state.has(ItemName.boss_defeated, player, world.options.guy_boss_count.value))
