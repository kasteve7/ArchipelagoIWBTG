from dataclasses import dataclass
import typing

from Options import OptionGroup, Choice, Range, Toggle, DefaultOnToggle, OptionSet, OptionDict, DeathLink, PerGameCommonOptions, StartInventoryPool
from schema import Schema, And, Use, Optional

class SetGoal(Choice):
	"""
	What the player has to do to win.
	"""
	display_name = "Goal"
	option_guy = 0
	option_devroom = 1
	default = 0
	
class GuyOpen(OptionSet):
	"""
	Conditions for The Guy's fortress to open
	Orbs: Orb items need to be collected in the multiworld.
	Bosses: Bosses need to be defeated.
	"""
	display_name = "Guy Fortress Rules"
	valid_keys = {
		"Orbs",
		"Bosses",
	}
	default = {
		"Orbs",
	}

class GuyOrbCount(Range):
	"""
	How many orbs needed to be defeated to access The Guy's fortress.
	"""
	display_name = "Guy Orb Count"
	range_start = 0
	range_end = 6
	default = 6
	
class GuyBossCount(Range):
	"""
	Number of bosses to be defeated to enter The Guy's Fortress.
	"""
	display_name = "Guy Boss Count"
	range_start = 0
	range_end = 6
	default = 6
	
	
class DivideOrbs(Choice):
	"""
	Orbs will be whole or in pieces to add additional items to the pool
	"""
	display_name = "Divide Orbs"
	option_whole = 0
	option_half = 2
	option_quarter = 4
	default = 0

class SecretItemCount(Range):
	"""
	How many secret items needed to access the dev room.
	"""
	display_name = "Secret Item Count"
	range_start = 0
	range_end = 6
	default = 6
	
class AdditionalProgressionItems(OptionSet):
	"""
	Additional progression items are added to the pool.
	Spike Platform - The spike platform on the path to Mike Tyson will not drop.
	Link - Link will be absent in the Zelda room until collected
	Graveyard Moon - The graveyard's moon will not open mecha birdo access until collected
	Ryu - Ryu will not appear in the fan room until collected
	Tourian Key - The entrance to Tourian will be blocked until the collected
	"""
	display_name = "Additional Progression Items"
	valid_keys = {
		"Spike Platform",
		"Link",
		"Graveyard Moon",
		"Ryu",
		"Tourian Key",
	}
	default = {
		"Spike Platform",
		"Link",
		"Graveyard Moon",
		"Ryu",
		"Tourian Key",
	}
	
class FreeWarping(Toggle):
	"""
	Pressing backspace will allow you to warp instantly to previously visited important locations.
	This helps reduce time backtracking.
	"""
	display_name = "Free Warping"

class GunUpgrades(Toggle):
	"""
	Your gun starts with 1 bullet allowed on screen at a time and three progressive gun items are shuffled into the pool.
	"""
	display_name = "Gun Upgrades"
	
class GunUpgradesCount(Range):
	"""
	If gun upgrades are enabled, how many gun upgrades are in the pool.
	"""
	display_name = "Gun Upgrades Count"
	range_start = 0
	range_end = 3
	default = 3

iwbtg_option_groups = [
	OptionGroup("Gameplay Options", [
		SetGoal,
		GunUpgrades,
		GunUpgradesCount,
		AdditionalProgressionItems,
		SecretItemCount,
	]),
	OptionGroup("Guy Fortress Options", [
		GuyOpen,
		DivideOrbs,
		GuyOrbCount,
		GuyBossCount,
	]),
]

@dataclass
class IWBTGOptions(PerGameCommonOptions):
	set_goal: SetGoal
	gun_upgrades: GunUpgrades
	gun_upgrades_count: GunUpgradesCount
	free_warping: FreeWarping
	additional_progression_items: AdditionalProgressionItems
	guy_open: GuyOpen
	divide_orbs: DivideOrbs
	guy_orb_count: GuyOrbCount
	guy_boss_count: GuyBossCount
	secret_item_count: SecretItemCount