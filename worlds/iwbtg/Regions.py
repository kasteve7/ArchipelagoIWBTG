import typing

from BaseClasses import CollectionState, MultiWorld, Region, Entrance, ItemClassification
from .Locations import IWBTGLocation
from .Items import IWBTGItem
from .Names import LocationName, ItemName, RegionName, EventName
from worlds.AutoWorld import World


def create_regions(multiworld: MultiWorld, player: int, world: World, active_locations):
    menu = create_region(multiworld, player, active_locations, 'Menu')

    guy_level = create_region(multiworld, player, active_locations, RegionName.guy_level)
    guy_level_sky = create_region(multiworld, player, active_locations, RegionName.guy_level_sky)
	
    zelda_level = create_region(multiworld, player, active_locations, RegionName.zelda_level)

    graveyard_level = create_region(multiworld, player, active_locations, RegionName.graveyard_level)

    tower_level_left = create_region(multiworld, player, active_locations, RegionName.tower_level_left)
    tower_level_right = create_region(multiworld, player, active_locations, RegionName.tower_level_right)
	tower_level_top = create_region(multiworld, player, active_locations, RegionName.tower_level_top)

    dracula_level = create_region(multiworld, player, active_locations, RegionName.dracula_level)

    gate_level = create_region(multiworld, player, active_locations, RegionName.gate_level)

    kraidgief_level = create_region(multiworld, player, active_locations, RegionName.kraidgief_level)

    megaman_level = create_region(multiworld, player, active_locations, RegionName.megaman_level)
	
    tourian_level = create_region(multiworld, player, active_locations, RegionName.tourian_level)
    
    road_level = create_region(multiworld, player, active_locations, RegionName.road_level)

    fortress_level = create_region(multiworld, player, active_locations, RegionName.fortress_level)

    multiworld.regions += [
        menu,
        guy_level,
        guy_level_sky,
		zelda_level,
		graveyard_level,
		tower_level_left,
		tower_level_right,
		tower_level_top,
		dracula_level,
		gate_level,
		kraidgief_level,
		megaman_level,
		tourian_level,
		road_level,
		fortress_level,
    ]

    # Guy Land
    add_location_to_region(multiworld, player, active_locations, RegionName.guy_level, LocationName.start_first_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.guy_level, LocationName.start_tree_easy_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.guy_level, LocationName.start_cloud_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.guy_level, LocationName.start_water_Save)
    add_location_to_region(multiworld, player, active_locations, RegionName.guy_level, LocationName.start_first_easy_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.guy_level, LocationName.start_divine_save)
	
    add_location_to_region(multiworld, player, active_locations, RegionName.guy_level_sky, LocationName.start_sky_easy_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.guy_level_sky, LocationName.start_tyson_save)

    # Zelda
    add_location_to_region(multiworld, player, active_locations, RegionName.zelda_level, LocationName.zelda_save)
 
    # Graveyard
    add_location_to_region(multiworld, player, active_locations, RegionName.graveyard_level, LocationName.gng_start_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.graveyard_level, LocationName.gng_spikes_easy_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.graveyard_level, LocationName.gng_fruit_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.graveyard_level, LocationName.gng_fruit_easy_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.graveyard_level, LocationName.gng_zombies_easy_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.graveyard_level, LocationName.gng_birdo_save)
 
    # Tower Top (Mecha Birdo)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_top, LocationName.tower_egg_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_top, LocationName.tower_outside_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_top, LocationName.tower_drones_easy_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_top, LocationName.tower_fan_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_top, LocationName.tower_fan_easy_save)
 
    # Tower Right (Tourian)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_left, LocationName.tower_bottom_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_left, LocationName.tower_bottom_easy_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_left, LocationName.tower_couches_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_left, LocationName.tower_couches_easy_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_left, LocationName.tower_yoku_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_left, LocationName.tower_right_save)
 
    # Tower Left (Megaman)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_right, LocationName.tower_bowser_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_right, LocationName.tower_left_easy_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_right, LocationName.tower_left_save)
    add_location_to_region(multiworld, player, active_locations, RegionName.tower_level_right, LocationName.tower_spikes_save)
	
	# Dracula
	add_location_to_region(multiworld, player, active_locations, RegionName.dracula_level, LocationName.dracula_stairs_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.dracula_level, LocationName.dracula_spikes_easy_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.dracula_level, LocationName.dracula_final_save)
	
	# Gate
	add_location_to_region(multiworld, player, active_locations, RegionName.gate_level, LocationName.gate_save)
	
	# Kraidgief's lair
	add_location_to_region(multiworld, player, active_locations, RegionName.kraidgief_level, LocationName.gief_first_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.kraidgief_level, LocationName.gief_cave_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.kraidgief_level, LocationName.gief_secret_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.kraidgief_level, LocationName.gief_descent_easy_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.kraidgief_level, LocationName.gief_descent_save)
	
	# Factory
	add_location_to_region(multiworld, player, active_locations, RegionName.factory_level, LocationName.factory_first_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.factory_level, LocationName.factory_tourian_easy_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.factory_level, LocationName.factory_laser_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.factory_level, LocationName.factory_bowser_easy_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.factory_level, LocationName.factory_bowser_save)
	
	# Guy Road
	add_location_to_region(multiworld, player, active_locations, RegionName.road_level, LocationName.road_first_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.road_level, LocationName.road_second_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.road_level, LocationName.road_third_easy_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.road_level, LocationName.road_fourth_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.road_level, LocationName.road_fifth_easy_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.road_level, LocationName.road_dragon_save)
	
	# Castle
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_entrance_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_entrance_easy_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_labyrinth_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_labyrinth_easy_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_hall_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_sinistar_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_vic_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_haggar_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_error_easy_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_frontdoor_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_tower_save)
	add_location_to_region(multiworld, player, active_locations, RegionName.fortress_level, LocationName.castle_guy_save)

    # if world.options.pickupsanity:


def connect_regions(world: World):
    connect(world, "Menu", RegionName.guy_level)

    connect(world, RegionName.guy_level, RegionName.guy_level_sky)
    connect(world, RegionName.guy_level, RegionName.zelda_level)
    connect(world, RegionName.guy_level, RegionName.megaman_level)
    connect(world, RegionName.guy_level, RegionName.kraidgief_level)
	
	connect(world, RegionName.guy_level_sky, RegionName.guy_level)

    connect(world, RegionName.zelda_level, RegionName.graveyard_level)
    
    connect(world, RegionName.graveyard_level, RegionName.tower_level_top)

    connect(world, RegionName.tower_level_top, RegionName.dracula_level)
    connect(world, RegionName.tower_level_top, RegionName.gate_level)
	
    connect(world, RegionName.gate_level, RegionName.tower_level_top)
    connect(world, RegionName.gate_level, RegionName.tower_level_right)
    connect(world, RegionName.gate_level, RegionName.guy_level)
	
    connect(world, RegionName.kraidgief_level, RegionName.megaman_level)
	
    connect(world, RegionName.megaman_level, RegionName.tourian_level)
    connect(world, RegionName.megaman_level, RegionName.tower_level_left)
	
    connect(world, RegionName.tourian_level, RegionName.tower_level_right)
	
    connect(world, RegionName.tower_level_left, RegionName.tower_level_top)
	
    connect(world, RegionName.tower_level_right, RegionName.gate_level)
	

def create_region(multiworld: MultiWorld, player: int, active_locations, name: str, locations=None):
    ret = Region(name, player, multiworld)
    if locations:
        for locationName in locations:
            loc_id = active_locations.get(locationName, 0)
            if loc_id:
                location = IWBTGLocation(player, locationName, loc_id, ret)
                ret.locations.append(location)

    return ret


def add_event_to_region(multiworld: MultiWorld, player: int, region_name: str, event_name: str, event_item=None):
    region = multiworld.get_region(region_name, player)
    event = IWBTGLocation(player, event_name, None, region)
    if event_item:
        event.place_locked_item(IWBTGItem(event_item, ItemClassification.progression, None, player))
    else:
        event.place_locked_item(IWBTGItem(event_name, ItemClassification.progression, None, player))
    region.locations.append(event)


def add_location_to_region(multiworld: MultiWorld, player: int, active_locations, region_name: str, location_name: str):
    region = multiworld.get_region(region_name, player)
    loc_id = active_locations.get(location_name, 0)
    if loc_id:
        location = IWBTGLocation(player, location_name, loc_id, region)
        region.locations.append(location)


def connect(world: World, source: str, target: str):
    source_region: Region = world.multiworld.get_region(source, world.player)
    target_region: Region = world.multiworld.get_region(target, world.player)
    source_region.connect(target_region)
