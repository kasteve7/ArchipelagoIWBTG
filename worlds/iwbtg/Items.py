import typing

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World
from .Names import ItemName

class ItemData(typing.NamedTuple):
    code: int
    classification: ItemClassification

class IWBTGItem(Item):
    game = "I Wanna Be the Guy"

# Item tables
event_table = {
    ItemName.boss_defeated:       		ItemData(92000, ItemClassification.event),
    ItemName.guy_defeated:          	ItemData(92006, ItemClassification.event),
    ItemName.dev_room:                  ItemData(92007, ItemClassification.event),
}

access_item_table = {
    ItemName.spike_platform:            ItemData(92100, ItemClassification.progression),
    ItemName.link:                      ItemData(92101, ItemClassification.progression),
    ItemName.graveyard_moon:            ItemData(92102, ItemClassification.progression),
    ItemName.ryu:                       ItemData(92103, ItemClassification.progression),
    ItemName.tourian_key:               ItemData(92104, ItemClassification.progression),
}

orb_table = {
    ItemName.orb_mike_tyson:       		ItemData(92200, ItemClassification.progression),
    ItemName.orb_mecha_birdo:      		ItemData(92201, ItemClassification.progression),
    ItemName.orb_dracula:          		ItemData(92202, ItemClassification.progression),
    ItemName.orb_kraidgeif:        		ItemData(92203, ItemClassification.progression),
    ItemName.orb_mother_brain:     		ItemData(92204, ItemClassification.progression),
    ItemName.orb_bowser:           		ItemData(92205, ItemClassification.progression),
	
    ItemName.orb_piece_mike_tyson: 		ItemData(92300, ItemClassification.progression),
    ItemName.orb_piece_mecha_birdo: 	ItemData(92301, ItemClassification.progression),
    ItemName.orb_piece_dracula:     	ItemData(92302, ItemClassification.progression),
    ItemName.orb_piece_kraidgeif:   	ItemData(92303, ItemClassification.progression),
    ItemName.orb_piece_mother_brain:	ItemData(92304, ItemClassification.progression),
    ItemName.orb_piece_bowser:      	ItemData(92305, ItemClassification.progression),
}

secret_item_table = {
    ItemName.item_1:       				ItemData(92400, ItemClassification.filler),
    ItemName.item_2:       				ItemData(92401, ItemClassification.filler),
    ItemName.item_3:       				ItemData(92402, ItemClassification.filler),
    ItemName.item_4:       				ItemData(92403, ItemClassification.filler),
    ItemName.item_5:       				ItemData(92404, ItemClassification.filler),
    ItemName.item_6:       				ItemData(92405, ItemClassification.filler),
}

trap_table = {
    ItemName.bird_trap:      			ItemData(92500, ItemClassification.trap),
    ItemName.fruit_trap:     			ItemData(92501, ItemClassification.trap),
    ItemName.error_trap:     			ItemData(92502, ItemClassification.trap),
    ItemName.stone_trap:     			ItemData(92503, ItemClassification.trap),
    ItemName.death_trap:     			ItemData(92504, ItemClassification.trap),
}

buff_table = {
	ItemName.gun_upgrade				ItemData(92600, ItemClassification.useful),
}

junk_table = {
    ItemName.bow:      					ItemData(92600, ItemClassification.trap),
}

item_groups = {
    "Orbs": {
        ItemName.orb_mike_tyson,
        ItemName.orb_mecha_birdo,
        ItemName.orb_dracula,
		ItemName.orb_kraidgeif,
		ItemName.orb_mother_brain,
        ItemName.orb_bowser,

		
		ItemName.orb_piece_mike_tyson,
        ItemName.orb_piece_mecha_birdo,
        ItemName.orb_piece_dracula,
		ItemName.orb_piece_kraidgeif,
		ItemName.orb_piece_mother_brain,
        ItemName.orb_piece_bowser,
    },
    "Access": {
        ItemName.spike_platform,
        ItemName.link,
        ItemName.graveyard_moon,
        ItemName.ryu,
        ItemName.tourian_key,
    },
    "Secrets": {
        ItemName.item_1,
        ItemName.item_2,
        ItemName.item_3,
        ItemName.item_4,
        ItemName.item_5,
        ItemName.item_6,
    },
    "Traps": {
        ItemName.bird_trap,
        ItemName.fruit_trap,
        ItemName.error_trap,
        ItemName.stone_trap,
        ItemName.death_trap,
    },
	"Filler": {
		ItemName.char_kid,
		ItemName.char_owata,
		ItemName.char_vic,
	}
	"Buffs": {
		ItemName.gun_upgrade,
	}
	"Junk": {
		ItemName.bow,
	}
}

item_table = {
    **event_table,
    **orb_table,
    **access_item_table,
    **secret_item_table,
    **trap_table,
	**buff_table,
	**junk_table,
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}