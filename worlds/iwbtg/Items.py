import typing

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World
from .Names import ItemName

class IWBTGItemData(typing.NamedTuple):
    code: int
    classification: ItemClassification

class IWBTGItem(Item):
    game = "I Wanna be The Guy"

# Item tables
event_table = {
    ItemName.boss_defeated:       		IWBTGItemData(92000, ItemClassification.progression),
    ItemName.become_the_guy:          	IWBTGItemData(92001, ItemClassification.progression),
    ItemName.dev_room:                  IWBTGItemData(92002, ItemClassification.progression),
}

access_item_table = {
    ItemName.spike_platform:            IWBTGItemData(92100, ItemClassification.progression),
    ItemName.link:                      IWBTGItemData(92101, ItemClassification.progression),
    ItemName.graveyard_moon:            IWBTGItemData(92102, ItemClassification.progression),
    ItemName.ryu:                       IWBTGItemData(92103, ItemClassification.progression),
    ItemName.tourian_key:               IWBTGItemData(92104, ItemClassification.progression),
}

orb_table = {
    ItemName.orb_mike_tyson:       		IWBTGItemData(92200, ItemClassification.progression),
    ItemName.orb_mecha_birdo:      		IWBTGItemData(92201, ItemClassification.progression),
    ItemName.orb_dracula:          		IWBTGItemData(92202, ItemClassification.progression),
    ItemName.orb_kraidgief:        		IWBTGItemData(92203, ItemClassification.progression),
    ItemName.orb_mother_brain:     		IWBTGItemData(92204, ItemClassification.progression),
    ItemName.orb_bowser:           		IWBTGItemData(92205, ItemClassification.progression),
	
    ItemName.orb_piece_mike_tyson: 		IWBTGItemData(92300, ItemClassification.progression),
    ItemName.orb_piece_mecha_birdo: 	IWBTGItemData(92301, ItemClassification.progression),
    ItemName.orb_piece_dracula:     	IWBTGItemData(92302, ItemClassification.progression),
    ItemName.orb_piece_kraidgief:   	IWBTGItemData(92303, ItemClassification.progression),
    ItemName.orb_piece_mother_brain:	IWBTGItemData(92304, ItemClassification.progression),
    ItemName.orb_piece_bowser:      	IWBTGItemData(92305, ItemClassification.progression),
	
    ItemName.orb_shard_mike_tyson: 		IWBTGItemData(92306, ItemClassification.progression),
    ItemName.orb_shard_mecha_birdo: 	IWBTGItemData(92307, ItemClassification.progression),
    ItemName.orb_shard_dracula:     	IWBTGItemData(92308, ItemClassification.progression),
    ItemName.orb_shard_kraidgief:   	IWBTGItemData(92309, ItemClassification.progression),
    ItemName.orb_shard_mother_brain:	IWBTGItemData(92310, ItemClassification.progression),
    ItemName.orb_shard_bowser:      	IWBTGItemData(92311, ItemClassification.progression),
}

secret_item_table = {
    ItemName.secret_item_1:       		IWBTGItemData(92400, ItemClassification.filler),
    ItemName.secret_item_2:       		IWBTGItemData(92401, ItemClassification.filler),
    ItemName.secret_item_3:       		IWBTGItemData(92402, ItemClassification.filler),
    ItemName.secret_item_4:       		IWBTGItemData(92403, ItemClassification.filler),
    ItemName.secret_item_5:       		IWBTGItemData(92404, ItemClassification.filler),
    ItemName.secret_item_6:       		IWBTGItemData(92405, ItemClassification.filler),
}

trap_table = {
    ItemName.bird_trap:      			IWBTGItemData(92500, ItemClassification.trap),
    ItemName.fruit_trap:     			IWBTGItemData(92501, ItemClassification.trap),
    ItemName.error_trap:     			IWBTGItemData(92502, ItemClassification.trap),
    ItemName.stone_trap:     			IWBTGItemData(92503, ItemClassification.trap),
    ItemName.death_trap:     			IWBTGItemData(92504, ItemClassification.trap),
}

buff_table = {
	ItemName.gun_upgrade:				IWBTGItemData(92600, ItemClassification.useful),
}

junk_table = {
    ItemName.bow:      					IWBTGItemData(92700, ItemClassification.trap),
}

item_groups = {
    "Orbs": {
        ItemName.orb_mike_tyson,
        ItemName.orb_mecha_birdo,
        ItemName.orb_dracula,
		ItemName.orb_kraidgief,
		ItemName.orb_mother_brain,
        ItemName.orb_bowser,

		ItemName.orb_piece_mike_tyson,
        ItemName.orb_piece_mecha_birdo,
        ItemName.orb_piece_dracula,
		ItemName.orb_piece_kraidgief,
		ItemName.orb_piece_mother_brain,
        ItemName.orb_piece_bowser,
		
		ItemName.orb_shard_mike_tyson,
        ItemName.orb_shard_mecha_birdo,
        ItemName.orb_shard_dracula,
		ItemName.orb_shard_kraidgief,
		ItemName.orb_shard_mother_brain,
        ItemName.orb_shard_bowser,
    },
    "Access": {
        ItemName.spike_platform,
        ItemName.link,
        ItemName.graveyard_moon,
        ItemName.ryu,
        ItemName.tourian_key,
    },
    "Secrets": {
        ItemName.secret_item_1,
        ItemName.secret_item_2,
        ItemName.secret_item_3,
        ItemName.secret_item_4,
        ItemName.secret_item_5,
        ItemName.secret_item_6,
    },
    "Traps": {
        ItemName.bird_trap,
        ItemName.fruit_trap,
        ItemName.error_trap,
        ItemName.stone_trap,
        ItemName.death_trap,
    },
	"""
	"Filler": {
		ItemName.char_kid,
		ItemName.char_owata,
		ItemName.char_vic,
	}
	"""
	"Buffs": {
		ItemName.gun_upgrade,
	},
	"Junk": {
		ItemName.bow,
	},
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