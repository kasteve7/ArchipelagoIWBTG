from dataclasses import dataclass
import typing

from Options import OptionGroup, Choice, Range, Toggle, DefaultOnToggle, OptionSet, OptionDict, DeathLink, PerGameCommonOptions, StartInventoryPool
from schema import Schema, And, Use, Optional

class SetGoal(Choice):
	"""
	What the player has to do to win.
    defeat_the_guy = Beat the final boss.
    access_devroom = Beat the final boss and collect all secret items from the multiworld to access the dev room.
	"""
	display_name = "Goal"
	option_defeat_the_guy = 0
	option_access_devroom = 1
	default = 0
	
class GuyOpen(Choice):
	"""
	Conditions for The Guy's fortress to open.

    collect_orbs = All orb items need to be collected from the multiworld.
    defeat_bosses = A number of Bosses need to be defeated.
    orbs_and_bosses = All orb items need to be collected from the multiworld AND a number of bosses defeated.
	"""
	display_name = "Guy Fortress Rules"
	option_collect_orbs = 0
	option_defeat_bosses = 1
	option_orbs_and_bosses = 2
	default = 0
	
class GuyBossCount(Range):
	"""
	If enabled, the number of bosses to be defeated to enter The Guy's Fortress.
	"""
	display_name = "Guy Boss Count"
	range_start = 0
	range_end = 6
	default = 6
	
	
class DivideOrbs(Choice):
	"""
	Orbs will be whole or in pieces to add additional items to the pool.
    If half, one orb will be counted if the player recieves two orb pieces.
    If quarter, one orb will be counted if the player recieves four orb shards.
    Pieces and shards are specific to each boss.
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

    Spike Platform: The spike platform/trap on the path to Mike Tyson will not drop until collected.
    Link: Link will be absent in the Zelda room until collected.
    Falling Graveyard Moon: The graveyard's full moon will not open mecha birdo access until collected.
    Ryu: Ryu will not appear in the fan room until collected.
    Tourian Key: The entrance to Tourian will be blocked until collected.
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
	
class FreeWarping(DefaultOnToggle):
	"""
	Pressing backspace will allow you to warp instantly to previously visited important locations. This helps reduce time backtracking.
    backspace will always allow the player to at least teleport to the beginning of the game.
    If The Guy is defeated, it will warp to the room of divine transportation instead of the start (like vanilla).
	"""
	display_name = "Free Warping"

class GunUpgrades(Toggle):
	"""
	Your gun starts with 1 bullet allowed on screen at a time and gun upgrade items are shuffled into the pool.
	"""
	display_name = "Gun Upgrades"
	
class GunUpgradesCount(Range):
	"""
	If gun upgrades are enabled, how many gun upgrades are in the pool.
	"""
	display_name = "Gun Upgrades Count"
	range_start = 0
	range_end = 5
	default = 3
	
class DeathLinkCount(Range):
	"""
	number of deaths before sending a death link to other players. Godspeed.
	"""
	display_name = "Death Link Count"
	range_start = 1
	range_end = 50
	default = 10

iwbtg_option_groups = [
	OptionGroup("Gameplay Options", [
		SetGoal,
		GunUpgrades,
		GunUpgradesCount,
		AdditionalProgressionItems,
		SecretItemCount,
		DeathLinkCount,
		FreeWarping,
	]),
	OptionGroup("Guy Fortress Options", [
		GuyOpen,
		DivideOrbs,
		GuyBossCount,
	]),
]

@dataclass
class IWBTGOptions(PerGameCommonOptions):
	set_goal: SetGoal
	guy_open: GuyOpen
	divide_orbs: DivideOrbs
	guy_boss_count: GuyBossCount
	secret_item_count: SecretItemCount
	additional_progression_items: AdditionalProgressionItems
	free_warping: FreeWarping
	gun_upgrades: GunUpgrades
	gun_upgrades_count: GunUpgradesCount
	death_link: DeathLink
	death_link_count: DeathLinkCount