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
	option_bosses = 2
    default = 0

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
    How many orbs needed to be defeated to acces The Guy's fortress.
    """
    display_name = "Guy Orb Count"
    range_start = 0
    range_end = 6
    default = 6
	
class DivideOrbs(choice)
	"""
	Orbs will be whole or in pieces to add additional items to the pool
	"""
	display_name = "Divide Orbs"
	option_whole = 0
    option_half = 2
	option_quarter = 4
    default = 0
	
class GuyBossCount(Range):
    """
    How many bosses need to be defeated to acces The Guy's fortress.
    """
    display_name = "Guy Orb Count"
    range_start = 0
    range_end = 6
    default = 6

class SecretItemCount(Range):
    """
    How many secret items needed to access the dev room.
    """
    display_name = "Secret Item Count"
    range_start = 0
    range_end = 6
    default = 6

iwbtg_option_groups = [
    OptionGroup("Gameplay Options", [
        StartingLifeCount,
        StartingHP,
        HeartTankEffectiveness,
        JammedBuster,
        BetterWallJump,
        LongJumps,
        AirDash,
        HadoukenInPool,
        LogicChargedShotgunIce,
        LogicHelmetCheckpoints,
    ]),
    OptionGroup("Sigma Fortress Options", [
        SigmaOpen,
        SigmaMedalCount,
        SigmaWeaponCount,
        SigmaArmorUpgradeCount,
        SigmaHeartTankCount,
        SigmaSubTankCount,
        FortressBundleUnlock,
        LogicLegSigma,
    ]),
    OptionGroup("Boss Weaknesses", [
        BossWeaknessRando,
        BossWeaknessStrictness,
        BossRandomizedHP,
        LogicBossWeakness,
    ]),
    OptionGroup("Enemy Tweaks", [
        ChillPenguinTweaks,
        ArmoredArmadilloTweaks,
        SparkMandrillTweaks,
    ]),
]

@dataclass
class IWBTGOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink
    energy_link: EnergyLink
    button_configuration: ButtonConfiguration
    starting_life_count: StartingLifeCount
    starting_hp: StartingHP
    heart_tank_effectiveness: HeartTankEffectiveness
    boss_weakness_rando: BossWeaknessRando
    boss_weakness_strictness: BossWeaknessStrictness
    boss_weakness_plando: PlandoWeaknesses
    boss_randomize_hp: BossRandomizedHP
    jammed_buster: JammedBuster
    better_walljump: BetterWallJump
    air_dash: AirDash
    long_jumps: LongJumps
    hadouken_in_pool: HadoukenInPool
    pickupsanity: PickupSanity
    early_legs: EarlyLegs
    logic_boss_weakness: LogicBossWeakness
    logic_leg_sigma: LogicLegSigma
    logic_charged_shotgun_ice: LogicChargedShotgunIce
    logic_helmet_checkpoints: LogicHelmetCheckpoints
    sigma_all_levels: FortressBundleUnlock
    sigma_open: SigmaOpen
    sigma_medal_count: SigmaMedalCount
    sigma_weapon_count: SigmaWeaponCount
    sigma_upgrade_count: SigmaArmorUpgradeCount
    sigma_heart_tank_count: SigmaHeartTankCount
    sigma_sub_tank_count: SigmaSubTankCount
    chill_penguin_tweaks: ChillPenguinTweaks
    armored_armadillo_tweaks: ArmoredArmadilloTweaks
    spark_mandrill_tweaks: SparkMandrillTweaks
