import typing

from BaseClasses import Location
from worlds.AutoWorld import World
from .Names import LocationName

class IWBTGLocation(Location):
	game = "I Wanna be The Guy"

	def __init__(self, player: int, name: str = '', address: int = None, parent=None):
		super().__init__(player, name, address, parent)

save_location_table = {
	#guy land
	LocationName.start_first_save:					92000,
	LocationName.start_tree_easy_save:			  	92001,
	LocationName.start_cloud_save:				  	92002,
	LocationName.start_water_save:				  	92003,
	LocationName.start_first_easy_save:			 	92004,
	LocationName.start_divine_save:				 	92005,
	
	#guy land sky
	LocationName.start_sky_easy_save:			   	92006,
	LocationName.start_tyson_save:				  	92007,
	
	#zelda
	LocationName.zelda_save:				   		92008,
	
	#graveyard
	LocationName.gng_start_save:				   	92009,
	LocationName.gng_spikes_easy_save:			 	92010,
	LocationName.gng_fruit_save:				   	92011,
	LocationName.gng_fruit_easy_save:			   	92012,
	LocationName.gng_zombies_easy_save:			 	92013,
	LocationName.gng_birdo_save:				   	92014,
	
	#tower from mecha birdo
	LocationName.tower_egg_save:				   	92015,
	LocationName.tower_outside_save:				92016,
	LocationName.tower_drones_easy_save:			92017,
	LocationName.tower_fan_save:				   	92018,
	LocationName.tower_fan_easy_save:			   	92019,
	
	#tower from tourian
	LocationName.tower_bottom_save:				 	92020,
	LocationName.tower_bottom_easy_save:			92021,
	LocationName.tower_couches_save:				92022,
	LocationName.tower_couches_easy_save:		   	92023,
	LocationName.tower_yoku_save:				   	92024,
	LocationName.tower_right_save:				  	92025,
	
	#tower from bowser
	LocationName.tower_bowser_save:				 	92026,
	LocationName.tower_left_easy_save:			  	92027,
	LocationName.tower_left_save:				   	92028,
	LocationName.tower_spikes_save:				 	92029,
	
	#dracula
	LocationName.dracula_stairs_save:			   	92030,
	LocationName.dracula_spikes_easy_save:		  	92031,
	LocationName.dracula_final_save:				92032,
	
	#gate
	LocationName.gate_save:				   			92033,
	
	#kraidgief lair
	LocationName.gief_first_save:				   	92034,
	LocationName.gief_cave_save:				   	92035,
	LocationName.gief_secret_save:				  	92036,
	LocationName.gief_descent_easy_save:			92037,
	LocationName.gief_descent_save:				 	92038,
	
	#factory
	LocationName.factory_first_save:				92039,
	LocationName.factory_tourian_easy_save:		 	92040,
	LocationName.factory_laser_save:				92041,
	LocationName.factory_bowser_easy_save:		  	92042,
	LocationName.factory_bowser_save:			   	92043,
	
	#tourian
	LocationName.tourian_save:						92044,
	LocationName.tourian_escape_save:				92045,
	
	#guy road
	LocationName.road_first_save:					92046,
	LocationName.road_second_save:				  	92047,
	LocationName.road_third_easy_save:			  	92048,
	LocationName.road_fourth_save:				  	92049,
	LocationName.road_fifth_easy_save:			  	92050,
	LocationName.road_dragon_save:				  	92051,
	
	#castle
	LocationName.castle_entrance_save:			  	92052,
	LocationName.castle_entrance_easy_save:		 	92053,
	LocationName.castle_labyrinth_save:			 	92054,
	LocationName.castle_labyrinth_easy_save:		92055,
	LocationName.castle_hall_save:				  	92056,
	LocationName.castle_sinistar_save:			  	92057,
	LocationName.castle_vic_save:					92058,
	LocationName.castle_haggar_save:				92059,
	LocationName.castle_error_easy_save:			92060,
	LocationName.castle_frontdoor_save:			 	92061,
	LocationName.castle_tower_save:				 	92062,
	LocationName.castle_guy_save:				 	92063,
}

boss_location_table = {
	LocationName.mike_tyson_defeated:				92100,
	LocationName.mecha_birdo_defeated:				92101,
	LocationName.dracula_defeated:		  			92102,
	LocationName.kraidgief_defeated:				92103,
	LocationName.mother_brain_defeated:				92104,
	LocationName.bowser_defeated:					92105,
}

orb_location_table = {
	LocationName.mike_tyson_orb:					92200,
	LocationName.mecha_birdo_orb:					92201,
	LocationName.dracula_orb:		  				92202,
	LocationName.kraidgief_orb:						92203,
	LocationName.mother_brain_orb:					92204,
	LocationName.bowser_orb:						92205,
	LocationName.dragon_defeated:					92206,
}

secret_location_table = {
	LocationName.secret_item_1:	  					92300,
	LocationName.secret_item_2:						92301,
	LocationName.secret_item_3:		  				92302,
	LocationName.secret_item_4:		   				92303,
	LocationName.secret_item_5:		 				92304,
	LocationName.secret_item_6:		 				92305,
	LocationName.dev_room:							92306,
}

optional_location_table = {
	LocationName.guy_defeated:						92400,
}

# deathsanity?

all_locations = {
	**save_location_table,
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
	},
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
		LocationName.secret_item_3,
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
	},
	"The Factory": {
		LocationName.factory_first_save,
		LocationName.factory_tourian_easy_save,
		LocationName.factory_laser_save,
		LocationName.factory_bowser_easy_save,
		LocationName.factory_bowser_save,
		LocationName.bowser_orb,
	},
	"Tourian" :{
		LocationName.tourian_save,
		LocationName.tourian_escape_save,
		LocationName.mother_brain_orb,
		LocationName.secret_item_4,
	},
	"Road to The Guy": {
		LocationName.road_first_save,
		LocationName.road_second_save,
		LocationName.road_third_easy_save,
		LocationName.road_fourth_save,
		LocationName.road_fifth_easy_save,
		LocationName.road_dragon_save,
		LocationName.dragon_defeated,
	},
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
	},
}
	
def setup_locations(world: World):
	location_table = {
		**save_location_table,
		**boss_location_table,
		**orb_location_table,
		**secret_location_table,
	}
	
	if world.options.set_goal.value == 1:
		location_table.update({**optional_location_table})

	#if world.options.<addLocationsOption>.value: (maybe use for deathsanity? remaster tracks culprits)

	return location_table

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in all_locations.items()}
