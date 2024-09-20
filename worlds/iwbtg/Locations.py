import typing

from BaseClasses import Location
from worlds.AutoWorld import World
from .Names import LocationName

class MMXLocation(Location):
    game = "I Wanna Be the Guy"

    def __init__(self, player: int, name: str = '', address: int = None, parent=None):
        super().__init__(player, name, address, parent)

save_location_table = {
	#guy land
    LocationName.start_first_save:                	ID,
    LocationName.start_tree_easy_save:              STARTING_ID + 0x0001,
    LocationName.start_cloud_save:                  STARTING_ID + 0x0002,
    LocationName.start_water_save:                  STARTING_ID + 0x0002,
    LocationName.start_first_easy_save:             STARTING_ID + 0x0002,
    LocationName.start_divine_save:                 STARTING_ID + 0x0002,
	
	#guy land sky
	LocationName.start_sky_easy_save:               STARTING_ID + 0x0002,
    LocationName.start_tyson_save:                  STARTING_ID + 0x0002,
	
	#zelda
	LocationName.zelda_save:                   		STARTING_ID + 0x0002,
	
	#graveyard
	LocationName.gng_start_save:                   	STARTING_ID + 0x0002,
	LocationName.gng_spikes_easy_save:             	STARTING_ID + 0x0002,
	LocationName.gng_fruit_save:                   	STARTING_ID + 0x0002,
	LocationName.gng_fruit_easy_save:               STARTING_ID + 0x0002,
	LocationName.gng_zombies_easy_save:             STARTING_ID + 0x0002,
	LocationName.gng_birdo_save:                   	STARTING_ID + 0x0002,
	
	#tower from mecha birdo
	LocationName.tower_egg_save:                   	STARTING_ID + 0x0002,
	LocationName.tower_outside_save:                STARTING_ID + 0x0002,
	LocationName.tower_drones_easy_save:            STARTING_ID + 0x0002,
	LocationName.tower_fan_save:                   	STARTING_ID + 0x0002,
	LocationName.tower_fan_easy_save:               STARTING_ID + 0x0002,
	
	#tower from tourian
	LocationName.tower_bottom_save:                 STARTING_ID + 0x0002,
	LocationName.tower_bottom_easy_save:            STARTING_ID + 0x0002,
	LocationName.tower_couches_save:                STARTING_ID + 0x0002,
	LocationName.tower_couches_easy_save:           STARTING_ID + 0x0002,
	LocationName.tower_yoku_save:                   STARTING_ID + 0x0002,
	LocationName.tower_right_save:                  STARTING_ID + 0x0002,
	
	#tower from bowser
	LocationName.tower_bowser_save:                 STARTING_ID + 0x0002,
	LocationName.tower_left_easy_save:              STARTING_ID + 0x0002,
	LocationName.tower_left_save:                   STARTING_ID + 0x0002,
	LocationName.tower_spikes_save:                 STARTING_ID + 0x0002,
	
	#dracula
	LocationName.dracula_stairs_save:               STARTING_ID + 0x0002,
	LocationName.dracula_spikes_easy_save:          STARTING_ID + 0x0002,
	LocationName.dracula_final_save:                STARTING_ID + 0x0002,
	
	#gate
	LocationName.gate_save:                   		STARTING_ID + 0x0002,
	
	#kraidgief lair
	LocationName.gief_first_save:                   STARTING_ID + 0x0002,
	LocationName.gief_cave_save:                   	STARTING_ID + 0x0002,
	LocationName.gief_secret_save:                  STARTING_ID + 0x0002,
	LocationName.gief_descent_easy_save:            STARTING_ID + 0x0002,
	LocationName.gief_descent_save:                 STARTING_ID + 0x0002,
	
	#factory
	LocationName.factory_first_save:                STARTING_ID + 0x0002,
	LocationName.factory_tourian_easy_save:         STARTING_ID + 0x0002,
	LocationName.factory_laser_save:                STARTING_ID + 0x0002,
	LocationName.factory_bowser_easy_save:          STARTING_ID + 0x0002,
	LocationName.factory_bowser_save:               STARTING_ID + 0x0002,
	
	#tourian
	LocationName.tourian_save:						STARTING_ID + 0x0002,
	LocationName.tourian_escape_save:				STARTING_ID + 0x0002,
	
	#guy road
	LocationName.road_first_save:                   STARTING_ID + 0x0002,
	LocationName.road_second_save:                  STARTING_ID + 0x0002,
	LocationName.road_third_easy_save:              STARTING_ID + 0x0002,
	LocationName.road_fourth_save:                  STARTING_ID + 0x0002,
	LocationName.road_fifth_easy_save:              STARTING_ID + 0x0002,
	LocationName.road_dragon_save:                  STARTING_ID + 0x0002,
	
	#castle
	LocationName.castle_entrance_save:              STARTING_ID + 0x0002,
	LocationName.castle_entrance_easy_save:         STARTING_ID + 0x0002,
	LocationName.castle_labyrinth_save:             STARTING_ID + 0x0002,
	LocationName.castle_labyrinth_easy_save:        STARTING_ID + 0x0002,
	LocationName.castle_hall_save:                  STARTING_ID + 0x0002,
	LocationName.castle_sinistar_save:              STARTING_ID + 0x0002,
	LocationName.castle_vic_save:                   STARTING_ID + 0x0002,
	LocationName.castle_haggar_save:                STARTING_ID + 0x0002,
	LocationName.castle_error_easy_save:            STARTING_ID + 0x0002,
	LocationName.castle_frontdoor_save:             STARTING_ID + 0x0002,
	LocationName.castle_tower_save:                 STARTING_ID + 0x0002,
	LocationName.castle_guy_save:                   STARTING_ID + 0x0002,
}

boss_location_table = {
    LocationName.mike_tyson_defeated:    			STARTING_ID + 0x0040,
    LocationName.mecha_birdo_defeated:            	STARTING_ID + 0x0041,
    LocationName.dracula_defeated:          		STARTING_ID + 0x0042,
    LocationName.kraidgief_defeated:            	STARTING_ID + 0x0043,
    LocationName.bowser_defeated:            		STARTING_ID + 0x0044,
    LocationName.dragon_defeated:            		STARTING_ID + 0x0044,
}

orb_location_table = {
    LocationName.mike_tyson_orb:    				STARTING_ID + 0x0040,
    LocationName.mecha_birdo_orb:            		STARTING_ID + 0x0041,
    LocationName.dracula_orb:          				STARTING_ID + 0x0042,
    LocationName.kraidgief_orb:            			STARTING_ID + 0x0043,
    LocationName.mother_brain_orb:            		STARTING_ID + 0x0043,
    LocationName.bowser_orb:            			STARTING_ID + 0x0044,
	LocationName.dragon_defeated:					STARTING_ID + 0x0002,
}

secret_location_table = {
    LocationName.secret_item_1:      				STARTING_ID + 0x0030,
    LocationName.secret_item_2:        				STARTING_ID + 0x0031,
    LocationName.secret_item_3:          			STARTING_ID + 0x0032,
    LocationName.secret_item_4:           			STARTING_ID + 0x0033,
    LocationName.secret_item_5:         			STARTING_ID + 0x0034,
    LocationName.secret_item_6:         			STARTING_ID + 0x0035,
	LocationName.dev_room:							NUM,
}

optional_locations_table = {
	LocationName.guy_defeated:						STARTING_ID + 0x0002,
}

# deathsanity?

all_locations = {
    **stave_location_table,
    **orb_location_table,
	**boss_location_table,
    **secret_location_table,
}

location_table = {}

location_groups = {
    "The Beginning of the Adventure": {
        LocationName.start_first_save,
        LocationName.start_tree_easy_save,
        LocationName.start_cloud_save,
        LocationName.start_sky_easy_save,
        LocationName.start_tyson_save,
        LocationName.start_water_save,
        LocationName.start_first_easy_save,
        LocationName.start_divine_save,
		LocationName.mike_tyson_orb,
		LocationName.secret_item_1,
    },
	"Zelda": {
		LocationName.zelda_save
	}
    "Graveyard": {
        LocationName.gng_start_save,
	    LocationName.gng_spikes_easy_save,
	    LocationName.gng_fruit_save,
	    LocationName.gng_fruit_easy_save,
	    LocationName.gng_zombies_easy_save,
	    LocationName.gng_birdo_save,
		LocationName.mecha_birdo_orb,
		LocationName.secret_item_2,
    },
    "Guy Industries Tower": {
        LocationName.tower_egg_save,
	    LocationName.tower_outside_save,
	    LocationName.tower_drones_easy_save,
	    LocationName.tower_fan_save,
	    LocationName.tower_fan_easy_save,
	    LocationName.tower_bottom_save,
	    LocationName.tower_bottom_easy_save,
	    LocationName.tower_couches_save,
	    LocationName.tower_couches_easy_save,
	    LocationName.tower_yoku_save,
	    LocationName.tower_right_save,
	    LocationName.tower_bowser_save,
	    LocationName.tower_left_easy_save,
	    LocationName.tower_left_save,
	    LocationName.tower_spikes_save,
		LocationName.secret_item_4,
    },
	"Dracula's Castle": {
	    LocationName.dracula_stairs_save,
	    LocationName.dracula_spikes_easy_save,
	    LocationName.dracula_final_save,
		LocationName.dracula_orb,
	},
	"Gate": {
	    LocationName.gate_save
	},
	"Kraidgief's Lair": {
	    LocationName.gief_first_save,
	    LocationName.gief_cave_save,
	    LocationName.gief_secret_save,
	    LocationName.gief_descent_easy_save,
	    LocationName.gief_descent_save,
		LocationName.kraidgief_orb,
		LocationName.secret_item_5,
	}
	"The Factory": {
		LocationName.factory_first_save,
		LocationName.factory_tourian_easy_save,
		LocationName.factory_laser_save,
		LocationName.factory_bowser_easy_save,
		LocationName.factory_bowser_save,
		LocationName.bowser_orb,
	}
	"Tourian" :{
		LocationName.tourian_save,
		LocationName.tourian_escape_save,
		LocationName.mother_brain_orb,
		LocationName.secret_item_3,
	}
	"Road to The Guy": {
		LocationName.road_first_save,
		LocationName.road_second_save,
		LocationName.road_third_easy_save,
		LocationName.road_fourth_save,
		LocationName.road_fifth_easy_save,
		LocationName.road_dragon_save,
		LocationName.dragon_defeated,
	}
	"Fotress of The Guy": {
		LocationName.castle_entrance_save,
		LocationName.castle_entrance_easy_save,
		LocationName.castle_labyrinth_save,
		LocationName.castle_labyrinth_easy_save,
		LocationName.castle_hall_save,
		LocationName.castle_sinistar_save,
		LocationName.castle_vic_save,
		LocationName.castle_haggar_save,
		LocationName.castle_error_easy_save,
		LocationName.castle_frontdoor_save,
		LocationName.castle_tower_save,
		LocationName.castle_guy_save,
		LocationName.guy_defeated,
		LocationName.secret_item_6,
	}
}
    
def setup_locations(world: World):
    location_table = {
        **save_location_table,
        **orb_location_table,
        **item_location_table,
    }
	
	if world.options.set_goal.value == 1:
		locations_table += **optional_locations_table

    #if world.options.<addLocationsOption>.value: (maybe use for deathsanity? remaster tracks culprits)

    return location_table

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in all_locations.items()}
