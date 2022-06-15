from enum import Enum, IntEnum
from typing import Dict

class ItemIDFlag(IntEnum):
    NON_EQUIPABBLE = 0 # params used only for references, ex. param sets
    WEAPONS = 0
    PROTECTORS = 1 << 28
    ACCESSORIES = 1 << 29
    GOODS = 1 << 30
    ASHES_OF_WAR = 1 << 31

class GoodsType(str, Enum):
    NORMAL_ITEM = "0"
    KEY_ITEM = "1"
    CRAFTING_MATERIAL = "2"
    REMEMBRANCE = "3"
    NONE_1 = "4"
    SORCERY_1 = "5"
    NONE_2 = "6"
    LESSER = "7"
    GREATER = "8"
    WONDROUS_PHYSICK = "9"
    WONDROUS_PHYSICK_TEAR = "10"
    REGENERATIVE_MATERIAL = "11"
    INFO_ITEM = "12"
    NONE_3 = "13"
    REINFORCEMENT_MATERIAL = "14"
    GREAT_RUNE = "15"
    INCANTATION_1 = "16"
    SORCERY_2 = "17"
    INCANTATION_2 = "18"

class GoodsRarity(IntEnum):
    COMMON = 1
    RARE = 2
    LEGENDARY = 3

class ReferenceCategory(str, Enum):
    ATTACK = "0"
    BULLET = "1"
    SP_EFFECT = "2"

class Affinity(str, Enum):
    STANDARD = "0"
    HEAVY = "1"
    KEEN = "2"
    QUALITY = "3"
    FIRE = "4"
    FLAME_ART = "5"
    LIGHTNING = "6"
    SACRED = "7"
    MAGIC = "8"
    COLD = "9"
    POISON = "10"
    BLOOD = "11"
    OCCULT = "12"

    def __str__(self) -> str:
        return _AFFINITY_STR[self]

_AFFINITY_STR: Dict[Affinity, str] = {
    Affinity.STANDARD: "Standard",
    Affinity.HEAVY: "Heavy",
    Affinity.KEEN: "Keen",
    Affinity.QUALITY: "Quality",
    Affinity.FIRE: "Fire",
    Affinity.FLAME_ART: "Flame Art",
    Affinity.LIGHTNING: "Lightning",
    Affinity.SACRED: "Sacred",
    Affinity.MAGIC: "Magic",
    Affinity.COLD: "Cold",
    Affinity.POISON: "Poison",
    Affinity.BLOOD: "Blood",
    Affinity.OCCULT: "Occult",
}

class AttackAttribute(str, Enum):
    STANDARD = "3"
    STRIKE = "1"
    SLASH = "0"
    PIERCE = "2"

    def __str__(self) -> str:
        return {
            AttackAttribute.STANDARD: "Standard",
            AttackAttribute.STRIKE: "Strike",
            AttackAttribute.SLASH: "Slash",
            AttackAttribute.PIERCE: "Pierce",
        }.get(self)

class AshOfWarMountType(str, Enum):
    PREVENT_CHANG = "0"
    UNUSED_VALUE = "1"
    ALLOW_CHANGE = "2"

class WeaponClass(str, Enum):
    DAGGER = "Dagger"
    STRAIGHT_SWORD = "SwordNormal"
    GREATSWORD = "SwordLarge"
    COLOSSAL_SWORD = "SwordGigantic"
    CURVED_SWORD = "SaberNormal"
    CURVED_GREATSWORD = "SaberLarge"
    KATANA = "katana" # yes, lowercase
    TWINBLADE = "SwordDoubleEdge"
    THRUSTING_SWORD = "SwordPierce"
    HEAVY_THRUSTING_SWORD = "RapierHeavy"
    AXE = "AxeNormal"
    GREATAXE = "AxeLarge"
    HAMMER = "HammerNormal"
    GREAT_HAMMER = "HammerLarge"
    FLAIL = "Flail"
    SPEAR = "SpearNormal"
    # unused spear = "SpearLarge"
    GREAT_SPEAR = "SpearHeavy"
    HALBERD = "SpearAxe"
    REAPER = "Sickle"
    FIST = "Knuckle"
    CLAW = "Claw"
    WHIP = "Whip"
    COLOSSAL_WEAPON = "AxhammerLarge"
    LIGHT_BOW = "BowSmall"
    BOW = "BowNormal"
    GREATBOW = "BowLarge"
    CROSSBOW = "ClossBow" # clossbow...
    BALLISTA = "Ballista"
    GLINTSTONE_STAFF = "Staff"
    # unused catalyst = "Sorcery"
    SACRED_SEAL = "Talisman"
    SMALL_SHIELD = "ShieldSmall"
    MEDIUM_SHIELD = "ShieldNormal"
    GREATSHIELD = "ShieldLarge"
    TORCH = "Torch"

    @staticmethod
    def from_id(index: str) -> "WeaponClass":
        return _WEAPON_CLASS_ID[index]

    def __str__(self) -> str:
        return _WEAPON_CLASS_STR[self]

_WEAPON_CLASS_ID: Dict[str, WeaponClass] = {
    "1": WeaponClass.DAGGER,
    "3": WeaponClass.STRAIGHT_SWORD,
    "5": WeaponClass.GREATSWORD,
    "7": WeaponClass.COLOSSAL_SWORD,
    "9": WeaponClass.CURVED_SWORD,
    "11": WeaponClass.CURVED_GREATSWORD,
    "13": WeaponClass.KATANA,
    "14": WeaponClass.TWINBLADE,
    "15": WeaponClass.THRUSTING_SWORD,
    "16": WeaponClass.HEAVY_THRUSTING_SWORD,
    "17": WeaponClass.AXE,
    "19": WeaponClass.GREATAXE,
    "21": WeaponClass.HAMMER,
    "23": WeaponClass.GREAT_HAMMER,
    "24": WeaponClass.FLAIL,
    "25": WeaponClass.SPEAR,
    "28": WeaponClass.GREAT_SPEAR,
    "29": WeaponClass.HALBERD,
    "31": WeaponClass.REAPER,
    "35": WeaponClass.FIST,
    "37": WeaponClass.CLAW,
    "39": WeaponClass.WHIP,
    "41": WeaponClass.COLOSSAL_WEAPON,
    "50": WeaponClass.LIGHT_BOW,
    "51": WeaponClass.BOW,
    "53": WeaponClass.GREATBOW,
    "55": WeaponClass.CROSSBOW,
    "56": WeaponClass.BALLISTA,
    "57": WeaponClass.GLINTSTONE_STAFF,
    "61": WeaponClass.SACRED_SEAL,
    "65": WeaponClass.SMALL_SHIELD,
    "67": WeaponClass.MEDIUM_SHIELD,
    "69": WeaponClass.GREATSHIELD,
    "87": WeaponClass.TORCH,
}

_WEAPON_CLASS_STR: Dict[WeaponClass, str] = {
    WeaponClass.DAGGER: "Dagger",
    WeaponClass.STRAIGHT_SWORD: "Straight Sword",
    WeaponClass.GREATSWORD: "Greatsword",
    WeaponClass.COLOSSAL_SWORD: "Colossal Sword",
    WeaponClass.CURVED_SWORD: "Curved Sword",
    WeaponClass.CURVED_GREATSWORD: "Curved Greatsword",
    WeaponClass.KATANA: "Katana",
    WeaponClass.TWINBLADE: "Twinblade",
    WeaponClass.THRUSTING_SWORD: "Thrusting Sword",
    WeaponClass.HEAVY_THRUSTING_SWORD: "Heavy Thrusting Sword",
    WeaponClass.AXE: "Axe",
    WeaponClass.GREATAXE: "Greataxe",
    WeaponClass.HAMMER: "Hammer",
    WeaponClass.GREAT_HAMMER: "Great Hammer",
    WeaponClass.FLAIL: "Flail",
    WeaponClass.SPEAR: "Spear",
    WeaponClass.GREAT_SPEAR: "Great Spear",
    WeaponClass.HALBERD: "Halberd",
    WeaponClass.REAPER: "Reaper",
    WeaponClass.FIST: "Fist",
    WeaponClass.CLAW: "Claw",
    WeaponClass.WHIP: "Whip",
    WeaponClass.COLOSSAL_WEAPON: "Colossal Weapon",
    WeaponClass.LIGHT_BOW: "Light Bow",
    WeaponClass.BOW: "Bow",
    WeaponClass.GREATBOW: "Greatbow",
    WeaponClass.CROSSBOW: "Crossbow",
    WeaponClass.BALLISTA: "Ballista",
    WeaponClass.GLINTSTONE_STAFF: "Glintstone Staff",
    WeaponClass.SACRED_SEAL: "Sacred Seal",
    WeaponClass.SMALL_SHIELD: "Small Shield",
    WeaponClass.MEDIUM_SHIELD: "Medium Shield",
    WeaponClass.GREATSHIELD: "Greatshield",
    WeaponClass.TORCH: "Torch",
}

class AttackCondition(str, Enum):
    NONE = "0"
    ON_HIT = "1"
    SUCCESSIVE_HITS = "2"
    SUCCESSIVE_3_HITS = "3"
    SUCCESSIVE_6_HITS = "4"
    SUCCESSIVE_9_HITS = "5"
    VS_GRAVITY_ENEMIES = "6",
    VS_UNDEAD_ENEMIES = "7",
    VS_ANCIENT_DRAGON_ENEMIES = "8",
    VS_DRAGON_ENEMIES = "9",

    def __str__(self) -> str:
        return _ATTACK_CONDITION_STR[self]

_ATTACK_CONDITION_STR: Dict[AttackCondition, str] = {
    AttackCondition.NONE: "0",
    AttackCondition.ON_HIT: "On Hit",
    AttackCondition.SUCCESSIVE_HITS: "Successive Hits",
    AttackCondition.SUCCESSIVE_3_HITS: "Successive 3 Hits",
    AttackCondition.SUCCESSIVE_6_HITS: "Successive 6 Hits",
    AttackCondition.SUCCESSIVE_9_HITS: "Successive 9 Hits",
    AttackCondition.VS_GRAVITY_ENEMIES: "vs Gravity Enemies",
    AttackCondition.VS_UNDEAD_ENEMIES: "vs Undead Enemies",
    AttackCondition.VS_ANCIENT_DRAGON_ENEMIES: "vs Ancient Dragon Enemies",
    AttackCondition.VS_DRAGON_ENEMIES: "vs Dragon Enemies",
}

class AttackType(str, Enum):
    NONE = "0"
    FULL_MOON_SPELL = "1"
    CARIAN_SWORD_SPELL = "2"
    GLINTBLADE_SPELL = "3"
    STONEDIGGER_SPELL = "4"
    CRYSTALIAN_SPELL = "5"
    KAROLOS_SPELL = "6"
    OLIVINUS_SPELL = "7"
    LAVA_SPELL = "8"
    THORN_SPELL = "9"
    DEATH_SPELL = "10"
    GRAVITY_SPELL = "11"
    NIGHT_SPELL = "12"
    RANNI_SPELL = "13"
    AZUR_SPELL = "14"
    LUSAT_SPELL = "15"
    BLACK_FLAME_SPELL = "20"
    FLAME_SPELL = "21"
    DRAGON_CULT_SPELL = "22"
    BESTIAL_SPELL = "23"
    GOLDEN_ORDER_SPELL = "24"
    DRAGON_COMMUNION_SPELL = "25"
    FRENZIED_FLAME_SPELL = "26"
    GODSLAYER_SPELL = "27"
    PRIMORDIAL_CRUCIBLE_SPELL = "28"
    CHARGE_ATTACK = "100"
    HORSEBACK_ATTACK = "101"
    JUMP_ATTACK = "102"
    GUARD_COUNTER_ATTACK = "103"
    FINAL_CHAIN_ATTACK = "104"
    AMMUNITION_ATTACK = "105"
    ROAR_ATTACK = "106"
    BREATH_ATTACK = "107"
    POT_ITEM_ATTACK = "108"
    PERFUME_ITEM_ATTACK = "109"
    CHARGED_ATTACK = "110"
    CHARGED_SKILL_ATTACK = "111"
    SKILL_ATTACK = "112"
    RANGED_SKILL_ATTACK = "113"
    VAPOR_ATTACK = "114"
    BUBBLE_SKILL_ATTACK = "115"
    UNKNOWN_ATTACK = "116"
    WRAITH_ATTACK = "117"
    AMMUNITION_ONHIT_ATTACK = "118"

    def __str__(self) -> str:
        return _ATTACK_TYPE_STR[self]

_ATTACK_TYPE_STR: Dict[AttackType, str] = {
    AttackType.NONE: "None",
    AttackType.FULL_MOON_SPELL: "Full Moon Spell",
    AttackType.CARIAN_SWORD_SPELL: "Carian Sword Spell",
    AttackType.GLINTBLADE_SPELL: "Glintblade Spell",
    AttackType.STONEDIGGER_SPELL: "Stonedigger Spell",
    AttackType.CRYSTALIAN_SPELL: "Crystalian Spell",
    AttackType.KAROLOS_SPELL: "Karolos Spell",
    AttackType.OLIVINUS_SPELL: "Olivinus Spell",
    AttackType.LAVA_SPELL: "Lava Spell",
    AttackType.THORN_SPELL: "Thorn Spell",
    AttackType.DEATH_SPELL: "Death Spell",
    AttackType.GRAVITY_SPELL: "Gravity Spell",
    AttackType.NIGHT_SPELL: "Night Spell",
    AttackType.RANNI_SPELL: "Ranni Spell",
    AttackType.AZUR_SPELL: "Azur Spell",
    AttackType.LUSAT_SPELL: "Lusat Spell",
    AttackType.BLACK_FLAME_SPELL: "Black Flame Spell",
    AttackType.FLAME_SPELL: "Flame Spell",
    AttackType.DRAGON_CULT_SPELL: "Dragon Cult Spell",
    AttackType.BESTIAL_SPELL: "Bestial Spell",
    AttackType.GOLDEN_ORDER_SPELL: "Golden Order Spell",
    AttackType.DRAGON_COMMUNION_SPELL: "Dragon Communion Spell",
    AttackType.FRENZIED_FLAME_SPELL: "Frenzied Flame Spell",
    AttackType.GODSLAYER_SPELL: "Godslayer Spell",
    AttackType.PRIMORDIAL_CRUCIBLE_SPELL: "Primordial Crucible Spell",
    AttackType.CHARGE_ATTACK: "Charge Attack",
    AttackType.HORSEBACK_ATTACK: "Horseback Attack",
    AttackType.JUMP_ATTACK: "Jump Attack",
    AttackType.GUARD_COUNTER_ATTACK: "Guard Counter Attack",
    AttackType.FINAL_CHAIN_ATTACK: "Final Chain Attack",
    AttackType.AMMUNITION_ATTACK: "Ammunition Attack",
    AttackType.ROAR_ATTACK: "Roar Attack",
    AttackType.BREATH_ATTACK: "Breath Attack",
    AttackType.POT_ITEM_ATTACK: "Pot Item Attack",
    AttackType.PERFUME_ITEM_ATTACK: "Perfume Item Attack",
    AttackType.CHARGED_ATTACK: "Charged Attack",
    AttackType.CHARGED_SKILL_ATTACK: "Charged Skill Attack",
    AttackType.SKILL_ATTACK: "Skill Attack",
    AttackType.RANGED_SKILL_ATTACK: "Ranged Skill Attack",
    AttackType.VAPOR_ATTACK: "Vapor Attack",
    AttackType.BUBBLE_SKILL_ATTACK: "Bubble Skill Attack",
    AttackType.UNKNOWN_ATTACK: "Unknown Attack",
    AttackType.WRAITH_ATTACK: "Wraith Attack",
    AttackType.AMMUNITION_ONHIT_ATTACK: "Ammunition OnHit Attack"
}

class SpEffectType(str, Enum):
    NONE = "0"
    POISON = "2"
    UNKNOWN = "3"
    DURABILITY_DAMAGE = "4"
    SCARLET_ROT = "5"
    HEMORRHAGE = "6"
    GHOST = "7"
    ENEMY_SIGHT_REDUCTION = "8"
    TRANQUIL_WALK_OF_PEACE = "9"
    REMOVE_POISON = "10"
    REMOVE_SCARLET_ROT = "11"
    REMOVE_HEMORRHAGE = "12"
    REMOVE_ALL_STATUS = "13"
    HUMANITY_STOLEN = "14"
    TELESCOPE = "15"
    WARP_TO_GRACE = "16"
    REVIVAL = "17"
    DISPEL_BLACK_PHANTOM = "19"
    UNKNOWN_2 = "22"
    ONREVIVEMAGIC = "23"
    DISABLES_SPELL_USAGE = "24"
    RIGHT_HAND_BUFF_VFX = "28"
    BODY_BUFF_VFX = "29"
    GHOST_PARAMETER_CHANGE = "31"
    MIDDLE_OF_PARALYSIS = "32"
    GIANT_SLIME_FREEZING = "34"
    UNKNOWN_3 = "35"
    UNKNOWN_4 = "36"
    UNKNOWN_5 = "37"
    SOUND_FEED = "39"
    GREATER_BODY_BUFF_VFX = "40"
    FLASH_SWEAT = "41"
    HP_RECOVERY = "42"
    UNKNOWN_6 = "43"
    UNKNOWN_7 = "44"
    UNKNOWN_8 = "45"
    MODIFY_TARGET_PRIORITY = "46"
    DISABLE_FALL_DAMAGE = "47"
    INCREASE_DAMAGE = "48"
    INCREASE_DEFENSE = "49"
    HP_FP_STAMINA_RECOVERY = "50"
    PLEDGE_EFFECT_TEST = "52"
    MODIFY_ENEMY_LISTEN_REDUCTION = "54"
    HOSTDEATH = "55"
    POINT_LIGHT_SOURCE_EQUIPPED = "58"
    YOUR_MESSAGE_WAS_RATED = "59"
    MAGIC_BUFF_VFX = "60"
    MAGIC_WEAPON_BUFF_VFX = "61"
    FIRE_WEAPON_BUFF_VFX = "62"
    ENCHANTED_WEAPON_BUFF_VFX = "64"
    UNKNOWN_9 = "65"
    MODIFY_ITEM_DISCOVERY = "66"
    TEARS_OF_DENIAL_VFX = "69"
    IS_DEAD_TEST_CONDITION = "70"
    SPELL_POWER_BOOST = "71"
    GREEN_BLOSSOM_VFX = "75"
    MODIFY_RUNE_GAIN = "76"
    UNKNOWN_10 = "78"
    UNKNOWN_11 = "79"
    UNKNOWN_12 = "91"
    APPLIES_CHAMELON_EFFECT = "95"
    APPLIES_DRAGON_FORM_EFFECT = "96"
    MP_DETECTION = "98"
    MP_WAIT_FOR_COOPERATION = "99"
    MP_COOPERATION = "100"
    MP_COOPERATION_SENT = "101"
    WAX_SLOW_DOWN = "102"
    USED_FOR_EVIL_EYE_EFFECT = "103"
    MP_WAIT_FOR_COOPERATION_2 = "104"
    MP_COOPERATION_LV_1 = "105"
    MP_COOPERATION_LV_2 = "106"
    MP_COOPERATION_LV_3 = "107"
    USED_FOR_EVIL_EYE_EFFECT_1 = "108"
    USED_FOR_EVIL_EYE_EFFECT_2 = "109"
    COUNTER_DAMAGE = "110"
    _1409F7282_HKS = "112"
    UNKNOWN_13 = "113"
    UNKNOWN_14 = "114"
    BACKSTEP_ANIMATION_CHANGE = "115"
    BLIGHT = "116"
    INSTANT_DEATH_ANIMATION = "117"
    CURE_BLIGHT = "118"
    UNKNOWN_15 = "119"
    DAMAGE_LEVEL_CHANGE_BEFORE_POISE_BREAK = "120"
    DAMAGE_LEVEL_CHANGE = "121"
    UNKNOWN_16 = "122"
    TRIGGER_ON_ROLL_HEAD = "123"
    TRIGGER_ON_ROLL_BODY = "124"
    TRIGGER_ON_ROLL_HANDS = "125"
    TRIGGER_ON_ROLL_LEGS = "126"
    MIMIC_SLEEP = "127"
    MIMIC_SLEEP_2 = "128"
    MIMIC_SLEEP_3 = "130"
    MIMIC_SLEEP_4 = "131"
    CHANGE_TEAM_TYPE = "132"
    ENABLE_DEVELOPER_MESSAGES = "133"
    IRON_FLESH = "134"
    MIMIC_SLEEP_5 = "135"
    BLIGHT_2 = "136"
    RESONANCELVL_0 = "137"
    RESONANCELVL_1 = "138"
    RESONANCELVL_2 = "139"
    RESONANCELVL_3 = "140"
    RESONANCELVL_4 = "141"
    NPC_BEHAVIOR_ID_CHANGE = "142"
    CHARACTER_RESPAWN = "143"
    UNKNOWN_17 = "144"
    HOLY = "145"
    RESTORE_DURABILITY = "146"
    CAST_LIGHT = "147"
    UNKNOWN_18 = "148"
    WHITE_RELIEF_MAGIC = "149"
    BLACK_RELIEF_MAGIC = "150"
    LIGHTNING_WEAPON_BUFF_VFX = "151"
    ENABLE_ATTACK_EFFECT_AGAINST_ENEMY = "152"
    ENABLE_ATTACK_EFFECT_AGAINST_PLAYER = "153"
    BLOCK_ESTUS_USAGE = "154"
    MODIFY_POISE = "155"
    DISABLE_DURABILITY = "156"
    TRANSIENT_CURSE = "157"
    LEFT_HAND_BUFF_VFX = "158"
    DESTROY_ACCESSORY_BUT_SAVE_RUNES = "159"
    RARE_RING_OF_SACRIFICE_DS1 = "160"
    WARP_TO_GRACE_2 = "161"
    WARP_TO_GRACE_3 = "162"
    WARP_TO_GRACE_4 = "163"
    WARP_TO_GRACE_5 = "164"
    WARP_TO_GRACE_6 = "165"
    PLEDGE_DISCARDED = "166"
    DRAGON_CHANGE_VFX = "167"
    BOW_DISTANCE_CHANGE = "168"
    UNKNOWN_19 = "169"
    KARMIC_JUSTICE_COUNTER = "170"
    USED_FOR_BEHAVIOR_CHANGE = "171"
    RITUAL = "173"
    POWER_OF_EVIL_SPIRITS = "174"
    REVIVAL_PRODUCTION = "175"
    AURAL_DECOY = "176"
    UNKNOWN_20 = "177"
    DEATHEFFECTLV1 = "179"
    DEATHEFFECTLV2 = "180"
    DEATHEFFECTLV3 = "181"
    DEATHEFFECTLV4 = "182"
    BLUESIGNVISUALIZATION = "183"
    HIDE_WEAPON = "184"
    UNKNOWN_21 = "185"
    UNKNOWN_22 = "186"
    UNKNOWN_23 = "188"
    UNKNOWN_24 = "189"
    UNKNOWN_25 = "190"
    UNKNOWN_26 = "191"
    UNKNOWN_27 = "192"
    MODIFY_EFFECT_DURATION = "193"
    COMPAREWITH203 = "194"
    UNKNOWN_28 = "195"
    IFWORLDCHRMANNULL = "196"
    ENHANCE_THRUSTING_COUNTER_ATTACKS = "197"
    CURE_BLIGHT_2 = "198"
    APPLY_KILL_EFFECT = "199"
    POWER_WITHIN_VFX = "200"
    VOWOFSILENCEVISUAL = "201"
    DRAGON_ROAR = "202"
    COMPAREWITH194 = "203"
    GREAT_MAGIC_SHIELD = "204"
    HOLY_WEAPON_BUFF_VFX = "205"
    UNKNOWN_29 = "206"
    JAILER_HP_DRAIN = "207"
    TRIGGER_ON_ENEMY_BACKSTAB = "213"
    UNKNOWN_30 = "221"
    ITEMBAN = "222"
    UNKNOWN_31 = "223"
    UNKNOWN_32 = "224"
    DISABLEUSEATCOLISEUM = "232"
    CALAMITY_RING = "237"
    OIL = "252"
    FIRE = "253"
    UNKNOWN_33 = "258"
    UNKNOWN_34 = "259"
    FROSTBITE = "260"
    REMOVE_EFFECT_IF_TORCH_IN_HAND = "261"
    WORMRECOVERY_TORCH = "262"
    SETCULTBOOL = "264"
    FALL_DEATH_INVALID = "266"
    AI_SIGHT_ADJUSTMENT = "267"
    UNKNOWN_35 = "269"
    UNKNOWN_36 = "270"
    UNKNOWN_37 = "271"
    UNKNOWN_38 = "272"
    PLAYER_BEHAVIOR_ID_CHANGE = "275"
    CURE_FROSTBITE = "276"
    TRIGGER_GREAT_RUNE = "277"
    DISABLESPELLEFFECT = "278"
    WATCHDOGTRIGGERFORHOST = "280"
    WETSYSTEMTRIGGER = "281"
    NPC_CORRECTION_FOR_COOP = "282"
    TEARS_OF_DENIAL_TRIGGER = "283"
    HEAL_SPELL = "284"
    UNKNOWN_39 = "285"
    WEAK_MOVEMENT_SLOW = "286"
    STRONG_MOVEMENT_SLOW = "287"
    TRIGGER_ON_CRITICAL_HIT_HP = "288"
    TRIGGER_ON_CRITICAL_HIT_FP = "289"
    EXTEND_ROLL_INVINCIBILITY = "290"
    GRANTS_ROLL_INVISIBILITY = "291"
    REPAIR1 = "292"
    CHANGE_DURABILITY = "293"
    UNKNOWN_40 = "294"
    UNKNOWN_41 = "295"
    UNKNOWN_42 = "296"
    NOT_IN_MULTIPLAYER_SESSION = "297"
    TRIGGER_ON_PLAYER_BACKSTAB = "298"
    ENEMIES_ATTACK_INVADERS = "299"
    ENEMIES_ATTACK_INVADERS_2 = "300"
    LAW_OF_REGRESSION = "301"
    WARP_TO_GRACE_7 = "302"
    CONDITIONAL_1 = "303"
    CONDITIONAL_2 = "304"
    CONDITIONAL_3 = "305"
    CONDITIONAL_4 = "306"
    CONDITIONAL_5 = "307"
    CONDITIONAL_6 = "308"
    CONDITIONAL_7 = "309"
    CONDITIONAL_8 = "310"
    CONDITIONAL_9 = "311"
    UNKNOWN_43 = "312"
    SEEK_GUIDANCE = "313"
    ADD_GUARD_STABILITY = "314"
    SCALE_ATTACK_POWER_WITH_EQUIP_LOAD = "315"
    CALCCORRECTGRAPH_33 = "316"
    REVOKE_ONLINE_PENALTY = "317"
    DEAD_AGAIN = "318"
    UNKNOWN_44 = "319"
    UNKNOWN_45 = "320"
    REVERSE_HOLLOWING = "321"
    CHRASMSTYLE_HKS_LEFTHAND = "322"
    CHRASMSTYLE_HKS_RIGHTHAND = "323"
    UNKNOWN_46 = "324"
    WET_ASPECT_PARAM = "325"
    SWITCH_ANIMATION_GENDER = "326"
    EMBER = "327"
    CHANGE_DURABILITY_2 = "328"
    GETESTUSCHARGE = "329"
    ONLINE_CHECK_RESET_EVENT_FLAG_2100 = "330"
    AIPARAM1 = "331"
    AIPARAM_EFFECT16189 = "332"
    SPELL_ENHANCE_PLUS_6_TO_ID = "333"
    BULLET_BEHAVIOR_ID_CHANGE = "334"
    TRIGGER_DURING_CRITICAL_HIT = "335"
    SUMMON_TORRENT = "336"
    UNKNOWN_47 = "337"
    UNKNOWN_48 = "338"
    RELOAD = "339"
    UNKNOWN_49 = "342"
    UNKNOWN_50 = "343"
    UNKNOWN_51 = "344"
    UNKNOWN_52 = "345"
    UNKNOWN_53 = "346"
    UNKNOWN_54 = "347"
    UNKNOWN_55 = "348"
    UNKNOWN_56 = "349"
    UNKNOWN_57 = "350"
    UNKNOWN_58 = "351"
    UNKNOWN_59 = "352"
    UNKNOWN_60 = "353"
    UNKNOWN_61 = "354"
    UNKNOWN_62 = "355"
    UNKNOWN_63 = "356"
    SPIRIT_SUMMON = "357"
    UNKNOWN_64 = "358"
    UNKNOWN_65 = "359"
    UNKNOWN_66 = "360"
    UNKNOWN_67 = "361"
    UNKNOWN_68 = "362"
    UNKNOWN_69 = "363"
    UNKNOWN_70 = "364"
    UNKNOWN_71 = "365"
    UNKNOWN_72 = "366"
    ENHANCE_CRITICAL_ATTACKS = "367"
    UNKNOWN_73 = "368"
    UNKNOWN_74 = "369"
    UNKNOWN_75 = "370"
    UNKNOWN_76 = "371"
    UNKNOWN_77 = "372"
    UNKNOWN_78 = "373"
    UNKNOWN_79 = "375"
    UNKNOWN_80 = "376"
    UNKNOWN_81 = "377"
    UNKNOWN_82 = "378"
    TRIGGER_IN_PRESENCE_OF_BLOOD_LOSS = "379"
    TRIGGER_IN_PRESENCE_OF_ROT = "380"
    UNKNOWN_83 = "381"
    UNKNOWN_84 = "382"
    UNKNOWN_85 = "383"
    UNKNOWN_86 = "384"
    UNKNOWN_87 = "385"
    UNKNOWN_88 = "387"
    UNKNOWN_89 = "388"
    UNKNOWN_90 = "389"
    PACIFY_WILD_ANIMALS = "390"
    UNKNOWN_91 = "391"
    UNKNOWN_92 = "392"
    UNKNOWN_93 = "393"
    UNKNOWN_94 = "394"
    UNKNOWN_95 = "395"
    UNKNOWN_96 = "396"
    UNKNOWN_97 = "397"
    PULL_TOWARDS_CASTER = "398"
    UNKNOWN_98 = "399"
    UNKNOWN_99 = "402"
    UNKNOWN_100 = "403"
    UNKNOWN_101 = "406"
    REVEAL_PHANTOM_SIGNS = "405"
    REQUEST_FRIENDLY_PHANTOM = "406"
    ANSWER_PHANTOM_REQUEST = "407"
    ENCOURAGE_INVASION = "408"
    SEND_SUMMON_SIGN_TO_POOL = "409"
    SEND_INVASION_SIGN_TO_POOL = "410"
    UNKNOWN_102 = "411"
    UNKNOWN_103 = "412"
    UNKNOWN_104 = "413"
    UNKNOWN_105 = "414"
    UNKNOWN_106 = "415"
    UNKNOWN_107 = "416"
    UNKNOWN_108 = "417"
    UNKNOWN_109 = "418"
    UNKNOWN_110 = "419"
    UNKNOWN_111 = "421"
    UNKNOWN_112 = "422"
    UNKNOWN_113 = "423"
    UNKNOWN_114 = "424"
    UNKNOWN_115 = "425"
    UNKNOWN_116 = "426"
    UNKNOWN_117 = "427"
    UNKNOWN_118 = "428"
    UNKNOWN_119 = "429"
    UNKNOWN_120 = "430"
    UNKNOWN_121 = "431"
    UNKNOWN_122 = "432"
    UNKNOWN_123 = "435"
    SLEEP = "436"
    MADNESS = "437"
    CURE_SLEEP = "438"
    CURE_MADNESS = "439"
    PURIFY_MOHGS_CURSE = "440"
    MOHGS_GREAT_RUNE = "441"
    UNKNOWN_124 = "442"
    UNKNOWN_125 = "443"
    UNKNOWN_126 = "445"
    UNKNOWN_127 = "446"
    PHANTOM_GREAT_RUNE = "447"
    HEAL_INVADER_WHEN_BLESSED_ENEMY_KILLS_PLAYER = "448"
    MALENIAS_GREAT_RUNE = "449"
    REDUCE_HEADSHOT_IMPACT = "450"
    RECOVERY_DAMAGE = "452"
    UNKNOWN_128 = "453"
    UNKNOWN_129 = "454"
    UNKNOWN_130 = "455"
    UNKNOWN_131 = "456"
    UNKNOWN_132 = "457"
    ATTEMPT_INVASION = "458"
    UNKNOWN_133 = "459"
    UNKNOWN_134 = "460"
    UNKNOWN_135 = "461"
    UNKNOWN_136 = "462"
    UNKNOWN_137 = "463"
    UNKNOWN_138 = "465"
    TRIGGER_ON_CROUCH = "466"
    BULLET_BEHAVIOR = "467"
    UNKNOWN_139 = "468"
    UNKNOWN_140 = "469"
    SKIPSPCATEGORYCHECK1 = "1000"
    SKIPSPCATEGORYCHECK2 = "1001"
    CUSTOM_TRIGGER = "9100"
    CUSTOM_TRIGGER_2 = "9101"
    CUSTOM_TRIGGER_3 = "9102"
    CUSTOM_TRIGGER_4 = "9103"
    CUSTOM_TRIGGER_5 = "9104"
    CUSTOM_TRIGGER_6 = "9105"
    CUSTOM_TRIGGER_7 = "9106"
    CUSTOM_TRIGGER_8 = "9107"
    CUSTOM_TRIGGER_9 = "9108"
    CUSTOM_TRIGGER_10 = "9109"
    CUSTOM_TRIGGER_11 = "9110"
    CUSTOM_TRIGGER_12 = "9111"
    CUSTOM_TRIGGER_13 = "9112"
    CUSTOM_TRIGGER_15 = "9113"
    CUSTOM_TRIGGER_16 = "9114"
    CUSTOM_TRIGGER_17 = "9115"
    CUSTOM_TRIGGER_18 = "9116"
    CUSTOM_TRIGGER_19 = "9117"
    CUSTOM_TRIGGER_20 = "9118"
    CUSTOM_TRIGGER_21 = "9119"
    CUSTOM_TRIGGER_22 = "9120"
    CUSTOM_TRIGGER_23 = "9121"
    CUSTOM_TRIGGER_24 = "9122"
    CUSTOM_TRIGGER_25 = "9123"
    CUSTOM_TRIGGER_26 = "9124"
    CUSTOM_TRIGGER_27 = "9125"
    CUSTOM_TRIGGER_28 = "9126"
    CUSTOM_TRIGGER_29 = "9127"
    CUSTOM_TRIGGER_30 = "9128"
    CUSTOM_TRIGGER_31 = "9129"
    CUSTOM_TRIGGER_32 = "9130"

    def __str__(self) -> str:
        return _SP_EFFECT_TYPE_STR[self]

    def is_passive(self) -> str:
        """
        Some stateInfo effect types act as trigger condtions for effects, others specify whether the effect
        is passive. This list can be used to check whether this type is used as a condtion.
        NOTE: This list is likely incomplete.
        """
        return self in [
            self.NONE, self.BOW_DISTANCE_CHANGE, self.INCREASE_DEFENSE, self.INCREASE_DAMAGE,
            self.MODIFY_ENEMY_LISTEN_REDUCTION, self.EXTEND_ROLL_INVINCIBILITY, self.MODIFY_RUNE_GAIN,
            self.MODIFY_ITEM_DISCOVERY, self.GREEN_BLOSSOM_VFX, self.MODIFY_EFFECT_DURATION,
            self.CONDITIONAL_1, self.CONDITIONAL_2, self.CONDITIONAL_3, self.CONDITIONAL_4,
            self.CONDITIONAL_5, self.CONDITIONAL_6, self.CONDITIONAL_7, self.CONDITIONAL_8,
            self.CONDITIONAL_9,
        ]

_SP_EFFECT_TYPE_STR: Dict[SpEffectType, str] = {
    SpEffectType.NONE: "None",
    SpEffectType.POISON: "Poison",
    SpEffectType.UNKNOWN: "Unknown",
    SpEffectType.DURABILITY_DAMAGE: "Durability Damage",
    SpEffectType.SCARLET_ROT: "Scarlet Rot",
    SpEffectType.HEMORRHAGE: "Hemorrhage",
    SpEffectType.GHOST: "Ghost",
    SpEffectType.ENEMY_SIGHT_REDUCTION: "Enemy Sight Reduction",
    SpEffectType.TRANQUIL_WALK_OF_PEACE: "Tranquil Walk of Peace",
    SpEffectType.REMOVE_POISON: "Remove Poison",
    SpEffectType.REMOVE_SCARLET_ROT: "Remove Scarlet Rot",
    SpEffectType.REMOVE_HEMORRHAGE: "Remove Hemorrhage",
    SpEffectType.REMOVE_ALL_STATUS: "Remove All Status",
    SpEffectType.HUMANITY_STOLEN: "Humanity Stolen",
    SpEffectType.TELESCOPE: "Telescope",
    SpEffectType.WARP_TO_GRACE: "Warp to Grace",
    SpEffectType.REVIVAL: "Revival",
    SpEffectType.DISPEL_BLACK_PHANTOM: "Dispel Black Phantom",
    SpEffectType.UNKNOWN_2: "Unknown",
    SpEffectType.ONREVIVEMAGIC: "OnReviveMagic",
    SpEffectType.DISABLES_SPELL_USAGE: "Disables Spell Usage",
    SpEffectType.RIGHT_HAND_BUFF_VFX: "Right-hand Buff VFX",
    SpEffectType.BODY_BUFF_VFX: "Body Buff VFX",
    SpEffectType.GHOST_PARAMETER_CHANGE: "Ghost Parameter Change",
    SpEffectType.MIDDLE_OF_PARALYSIS: "Middle of Paralysis",
    SpEffectType.GIANT_SLIME_FREEZING: "Giant Slime Freezing",
    SpEffectType.UNKNOWN_3: "Unknown",
    SpEffectType.UNKNOWN_4: "Unknown",
    SpEffectType.UNKNOWN_5: "Unknown",
    SpEffectType.SOUND_FEED: "Sound Feed",
    SpEffectType.GREATER_BODY_BUFF_VFX: "Greater Body Buff VFX",
    SpEffectType.FLASH_SWEAT: "Flash Sweat",
    SpEffectType.HP_RECOVERY: "HP Recovery",
    SpEffectType.UNKNOWN_6: "Unknown",
    SpEffectType.UNKNOWN_7: "Unknown",
    SpEffectType.UNKNOWN_8: "Unknown",
    SpEffectType.MODIFY_TARGET_PRIORITY: "Modify Target Priority",
    SpEffectType.DISABLE_FALL_DAMAGE: "Disable Fall Damage",
    SpEffectType.INCREASE_DAMAGE: "Increase Damage",
    SpEffectType.INCREASE_DEFENSE: "Increase Defense",
    SpEffectType.HP_FP_STAMINA_RECOVERY: "HP/FP/Stamina Recovery",
    SpEffectType.PLEDGE_EFFECT_TEST: "Pledge Effect Test",
    SpEffectType.MODIFY_ENEMY_LISTEN_REDUCTION: "Modify Enemy Listen Reduction",
    SpEffectType.HOSTDEATH: "HostDeath",
    SpEffectType.POINT_LIGHT_SOURCE_EQUIPPED: "Point Light Source Equipped",
    SpEffectType.YOUR_MESSAGE_WAS_RATED: "Your Message Was Rated",
    SpEffectType.MAGIC_BUFF_VFX: "Magic Buff VFX",
    SpEffectType.MAGIC_WEAPON_BUFF_VFX: "Magic Weapon Buff VFX",
    SpEffectType.FIRE_WEAPON_BUFF_VFX: "Fire Weapon Buff VFX",
    SpEffectType.ENCHANTED_WEAPON_BUFF_VFX: "Enchanted Weapon Buff VFX",
    SpEffectType.UNKNOWN_9: "Unknown",
    SpEffectType.MODIFY_ITEM_DISCOVERY: "Modify Item Discovery",
    SpEffectType.TEARS_OF_DENIAL_VFX: "Tears of Denial VFX",
    SpEffectType.IS_DEAD_TEST_CONDITION: "Is Dead Test Condition",
    SpEffectType.SPELL_POWER_BOOST: "Spell Power Boost",
    SpEffectType.GREEN_BLOSSOM_VFX: "Green Blossom VFX",
    SpEffectType.MODIFY_RUNE_GAIN: "Modify Rune Gain",
    SpEffectType.UNKNOWN_10: "Unknown",
    SpEffectType.UNKNOWN_11: "Unknown",
    SpEffectType.UNKNOWN_12: "Unknown",
    SpEffectType.APPLIES_CHAMELON_EFFECT: "Applies Chamelon effect",
    SpEffectType.APPLIES_DRAGON_FORM_EFFECT: "Applies Dragon Form effect",
    SpEffectType.MP_DETECTION: "MP Detection",
    SpEffectType.MP_WAIT_FOR_COOPERATION: "MP Wait for Cooperation",
    SpEffectType.MP_COOPERATION: "MP Cooperation",
    SpEffectType.MP_COOPERATION_SENT: "MP Cooperation Sent",
    SpEffectType.WAX_SLOW_DOWN: "Wax Slow Down",
    SpEffectType.USED_FOR_EVIL_EYE_EFFECT: "Used for Evil Eye effect",
    SpEffectType.MP_WAIT_FOR_COOPERATION_2: "MP Wait for Cooperation",
    SpEffectType.MP_COOPERATION_LV_1: "MP Cooperation LV 1",
    SpEffectType.MP_COOPERATION_LV_2: "MP Cooperation LV 2",
    SpEffectType.MP_COOPERATION_LV_3: "MP Cooperation LV 3",
    SpEffectType.USED_FOR_EVIL_EYE_EFFECT_1: "Used for Evil Eye effect (1)",
    SpEffectType.USED_FOR_EVIL_EYE_EFFECT_2: "Used for Evil Eye effect (2)",
    SpEffectType.COUNTER_DAMAGE: "Counter Damage",
    SpEffectType._1409F7282_HKS: "1409F7282_HKS",
    SpEffectType.UNKNOWN_13: "Unknown",
    SpEffectType.UNKNOWN_14: "Unknown",
    SpEffectType.BACKSTEP_ANIMATION_CHANGE: "Backstep Animation Change",
    SpEffectType.BLIGHT: "Blight",
    SpEffectType.INSTANT_DEATH_ANIMATION: "Instant Death animation",
    SpEffectType.CURE_BLIGHT: "Cure Blight",
    SpEffectType.UNKNOWN_15: "Unknown",
    SpEffectType.DAMAGE_LEVEL_CHANGE_BEFORE_POISE_BREAK: "Damage Level Change before Poise Break",
    SpEffectType.DAMAGE_LEVEL_CHANGE: "Damage Level Change",
    SpEffectType.UNKNOWN_16: "Unknown",
    SpEffectType.TRIGGER_ON_ROLL_HEAD: "Trigger on Roll (Head)",
    SpEffectType.TRIGGER_ON_ROLL_BODY: "Trigger on Roll (Body)",
    SpEffectType.TRIGGER_ON_ROLL_HANDS: "Trigger on Roll (Hands)",
    SpEffectType.TRIGGER_ON_ROLL_LEGS: "Trigger on Roll (Legs)",
    SpEffectType.MIMIC_SLEEP: "Mimic Sleep",
    SpEffectType.MIMIC_SLEEP_2: "Mimic Sleep",
    SpEffectType.MIMIC_SLEEP_3: "Mimic Sleep",
    SpEffectType.MIMIC_SLEEP_4: "Mimic Sleep",
    SpEffectType.CHANGE_TEAM_TYPE: "Change Team Type",
    SpEffectType.ENABLE_DEVELOPER_MESSAGES: "Enable Developer Messages",
    SpEffectType.IRON_FLESH: "Iron Flesh",
    SpEffectType.MIMIC_SLEEP_5: "Mimic Sleep",
    SpEffectType.BLIGHT_2: "Blight",
    SpEffectType.RESONANCELVL_0: "ResonanceLvl 0",
    SpEffectType.RESONANCELVL_1: "ResonanceLvl 1",
    SpEffectType.RESONANCELVL_2: "ResonanceLvl 2",
    SpEffectType.RESONANCELVL_3: "ResonanceLvl 3",
    SpEffectType.RESONANCELVL_4: "ResonanceLvl 4",
    SpEffectType.NPC_BEHAVIOR_ID_CHANGE: "NPC Behavior ID Change",
    SpEffectType.CHARACTER_RESPAWN: "Character Respawn",
    SpEffectType.UNKNOWN_17: "Unknown",
    SpEffectType.HOLY: "Holy",
    SpEffectType.RESTORE_DURABILITY: "Restore Durability",
    SpEffectType.CAST_LIGHT: "Cast Light",
    SpEffectType.UNKNOWN_18: "Unknown",
    SpEffectType.WHITE_RELIEF_MAGIC: "White Relief Magic",
    SpEffectType.BLACK_RELIEF_MAGIC: "Black Relief Magic",
    SpEffectType.LIGHTNING_WEAPON_BUFF_VFX: "Lightning Weapon Buff VFX",
    SpEffectType.ENABLE_ATTACK_EFFECT_AGAINST_ENEMY: "Enable Attack Effect against Enemy",
    SpEffectType.ENABLE_ATTACK_EFFECT_AGAINST_PLAYER: "Enable Attack Effect against Player",
    SpEffectType.BLOCK_ESTUS_USAGE: "Block Estus usage",
    SpEffectType.MODIFY_POISE: "Modify Poise",
    SpEffectType.DISABLE_DURABILITY: "Disable Durability",
    SpEffectType.TRANSIENT_CURSE: "Transient Curse",
    SpEffectType.LEFT_HAND_BUFF_VFX: "Left-hand Buff VFX",
    SpEffectType.DESTROY_ACCESSORY_BUT_SAVE_RUNES: "Destroy Accessory but Save Runes",
    SpEffectType.RARE_RING_OF_SACRIFICE_DS1: "Rare Ring of Sacrifice [DS1]",
    SpEffectType.WARP_TO_GRACE_2: "Warp to Grace",
    SpEffectType.WARP_TO_GRACE_3: "Warp to Grace",
    SpEffectType.WARP_TO_GRACE_4: "Warp to Grace",
    SpEffectType.WARP_TO_GRACE_5: "Warp to Grace",
    SpEffectType.WARP_TO_GRACE_6: "Warp to Grace",
    SpEffectType.PLEDGE_DISCARDED: "Pledge Discarded",
    SpEffectType.DRAGON_CHANGE_VFX: "Dragon Change VFX",
    SpEffectType.BOW_DISTANCE_CHANGE: "Bow Distance Change",
    SpEffectType.UNKNOWN_19: "Unknown",
    SpEffectType.KARMIC_JUSTICE_COUNTER: "Karmic Justice Counter",
    SpEffectType.USED_FOR_BEHAVIOR_CHANGE: "Used for Behavior Change",
    SpEffectType.RITUAL: "Ritual",
    SpEffectType.POWER_OF_EVIL_SPIRITS: "Power of Evil Spirits",
    SpEffectType.REVIVAL_PRODUCTION: "Revival Production",
    SpEffectType.AURAL_DECOY: "Aural Decoy",
    SpEffectType.UNKNOWN_20: "Unknown",
    SpEffectType.DEATHEFFECTLV1: "DeathEffectLv1",
    SpEffectType.DEATHEFFECTLV2: "DeathEffectLv2",
    SpEffectType.DEATHEFFECTLV3: "DeathEffectLv3",
    SpEffectType.DEATHEFFECTLV4: "DeathEffectLv4",
    SpEffectType.BLUESIGNVISUALIZATION: "BlueSignVisualization",
    SpEffectType.HIDE_WEAPON: "Hide Weapon",
    SpEffectType.UNKNOWN_21: "Unknown",
    SpEffectType.UNKNOWN_22: "Unknown",
    SpEffectType.UNKNOWN_23: "Unknown",
    SpEffectType.UNKNOWN_24: "Unknown",
    SpEffectType.UNKNOWN_25: "Unknown",
    SpEffectType.UNKNOWN_26: "Unknown",
    SpEffectType.UNKNOWN_27: "Unknown",
    SpEffectType.MODIFY_EFFECT_DURATION: "Modify Effect Duration",
    SpEffectType.COMPAREWITH203: "CompareWith203",
    SpEffectType.UNKNOWN_28: "Unknown",
    SpEffectType.IFWORLDCHRMANNULL: "IfWorldChrManNull",
    SpEffectType.ENHANCE_THRUSTING_COUNTER_ATTACKS: "Enhance Thrusting Counter Attacks",
    SpEffectType.CURE_BLIGHT_2: "Cure Blight",
    SpEffectType.APPLY_KILL_EFFECT: "Apply Kill Effect",
    SpEffectType.POWER_WITHIN_VFX: "Power Within VFX",
    SpEffectType.VOWOFSILENCEVISUAL: "VowOfSilenceVisual",
    SpEffectType.DRAGON_ROAR: "Dragon Roar",
    SpEffectType.COMPAREWITH194: "CompareWith194",
    SpEffectType.GREAT_MAGIC_SHIELD: "Great Magic Shield",
    SpEffectType.HOLY_WEAPON_BUFF_VFX: "Holy Weapon Buff VFX",
    SpEffectType.UNKNOWN_29: "Unknown",
    SpEffectType.JAILER_HP_DRAIN: "Jailer HP Drain",
    SpEffectType.TRIGGER_ON_ENEMY_BACKSTAB: "Trigger on Enemy Backstab",
    SpEffectType.UNKNOWN_30: "Unknown",
    SpEffectType.ITEMBAN: "ItemBan",
    SpEffectType.UNKNOWN_31: "Unknown",
    SpEffectType.UNKNOWN_32: "Unknown",
    SpEffectType.DISABLEUSEATCOLISEUM: "DisableUseAtColiseum",
    SpEffectType.CALAMITY_RING: "Calamity Ring",
    SpEffectType.OIL: "Oil",
    SpEffectType.FIRE: "Fire",
    SpEffectType.UNKNOWN_33: "Unknown",
    SpEffectType.UNKNOWN_34: "Unknown",
    SpEffectType.FROSTBITE: "Frostbite",
    SpEffectType.REMOVE_EFFECT_IF_TORCH_IN_HAND: "Remove Effect If Torch In Hand",
    SpEffectType.WORMRECOVERY_TORCH: "WormRecovery(Torch)",
    SpEffectType.SETCULTBOOL: "SetCultBool",
    SpEffectType.FALL_DEATH_INVALID: "Fall Death Invalid",
    SpEffectType.AI_SIGHT_ADJUSTMENT: "AI Sight Adjustment",
    SpEffectType.UNKNOWN_35: "Unknown",
    SpEffectType.UNKNOWN_36: "Unknown",
    SpEffectType.UNKNOWN_37: "Unknown",
    SpEffectType.UNKNOWN_38: "Unknown",
    SpEffectType.PLAYER_BEHAVIOR_ID_CHANGE: "Player Behavior ID Change",
    SpEffectType.CURE_FROSTBITE: "Cure Frostbite",
    SpEffectType.TRIGGER_GREAT_RUNE: "Trigger Great Rune",
    SpEffectType.DISABLESPELLEFFECT: "DisableSpellEffect",
    SpEffectType.WATCHDOGTRIGGERFORHOST: "WatchdogTriggerForHost",
    SpEffectType.WETSYSTEMTRIGGER: "WetSystemTrigger",
    SpEffectType.NPC_CORRECTION_FOR_COOP: "NPC Correction for Coop",
    SpEffectType.TEARS_OF_DENIAL_TRIGGER: "Tears of Denial Trigger",
    SpEffectType.HEAL_SPELL: "Heal Spell",
    SpEffectType.UNKNOWN_39: "Unknown",
    SpEffectType.WEAK_MOVEMENT_SLOW: "Weak Movement Slow",
    SpEffectType.STRONG_MOVEMENT_SLOW: "Strong Movement Slow",
    SpEffectType.TRIGGER_ON_CRITICAL_HIT_HP: "Trigger on Critical Hit (HP)",
    SpEffectType.TRIGGER_ON_CRITICAL_HIT_FP: "Trigger on Critical Hit (FP)",
    SpEffectType.EXTEND_ROLL_INVINCIBILITY: "Extend Roll Invincibility",
    SpEffectType.GRANTS_ROLL_INVISIBILITY: "Grants roll invisibility",
    SpEffectType.REPAIR1: "Repair1",
    SpEffectType.CHANGE_DURABILITY: "Change Durability",
    SpEffectType.UNKNOWN_40: "Unknown",
    SpEffectType.UNKNOWN_41: "Unknown",
    SpEffectType.UNKNOWN_42: "Unknown",
    SpEffectType.NOT_IN_MULTIPLAYER_SESSION: "Not in Multiplayer Session",
    SpEffectType.TRIGGER_ON_PLAYER_BACKSTAB: "Trigger on Player Backstab",
    SpEffectType.ENEMIES_ATTACK_INVADERS: "Enemies attack Invaders",
    SpEffectType.ENEMIES_ATTACK_INVADERS_2: "Enemies attack Invaders",
    SpEffectType.LAW_OF_REGRESSION: "Law of Regression",
    SpEffectType.WARP_TO_GRACE_7: "Warp to Grace",
    SpEffectType.CONDITIONAL_1: "Conditional 1",
    SpEffectType.CONDITIONAL_2: "Conditional 2",
    SpEffectType.CONDITIONAL_3: "Conditional 3",
    SpEffectType.CONDITIONAL_4: "Conditional 4",
    SpEffectType.CONDITIONAL_5: "Conditional 5",
    SpEffectType.CONDITIONAL_6: "Conditional 6",
    SpEffectType.CONDITIONAL_7: "Conditional 7",
    SpEffectType.CONDITIONAL_8: "Conditional 8",
    SpEffectType.CONDITIONAL_9: "Conditional 9",
    SpEffectType.UNKNOWN_43: "Unknown",
    SpEffectType.SEEK_GUIDANCE: "Seek Guidance",
    SpEffectType.ADD_GUARD_STABILITY: "Add Guard Stability",
    SpEffectType.SCALE_ATTACK_POWER_WITH_EQUIP_LOAD: "Scale Attack Power with Equip Load",
    SpEffectType.CALCCORRECTGRAPH_33: "CalcCorrectGraph_33",
    SpEffectType.REVOKE_ONLINE_PENALTY: "Revoke Online Penalty",
    SpEffectType.DEAD_AGAIN: "Dead Again",
    SpEffectType.UNKNOWN_44: "Unknown",
    SpEffectType.UNKNOWN_45: "Unknown",
    SpEffectType.REVERSE_HOLLOWING: "Reverse Hollowing",
    SpEffectType.CHRASMSTYLE_HKS_LEFTHAND: "ChrAsmStyle_HKS_LEFTHAND",
    SpEffectType.CHRASMSTYLE_HKS_RIGHTHAND: "ChrAsmStyle_HKS_RIGHTHAND",
    SpEffectType.UNKNOWN_46: "Unknown",
    SpEffectType.WET_ASPECT_PARAM: "Wet Aspect Param",
    SpEffectType.SWITCH_ANIMATION_GENDER: "Switch Animation Gender",
    SpEffectType.EMBER: "Ember",
    SpEffectType.CHANGE_DURABILITY_2: "Change Durability",
    SpEffectType.GETESTUSCHARGE: "GetEstusCharge",
    SpEffectType.ONLINE_CHECK_RESET_EVENT_FLAG_2100: "Online Check Reset Event Flag 2100",
    SpEffectType.AIPARAM1: "AiParam1",
    SpEffectType.AIPARAM_EFFECT16189: "AiParam_effect16189",
    SpEffectType.SPELL_ENHANCE_PLUS_6_TO_ID: "Spell Enhance (+6 to ID)",
    SpEffectType.BULLET_BEHAVIOR_ID_CHANGE: "Bullet Behavior ID Change",
    SpEffectType.TRIGGER_DURING_CRITICAL_HIT: "Trigger during Critical Hit",
    SpEffectType.SUMMON_TORRENT: "Summon Torrent",
    SpEffectType.UNKNOWN_47: "Unknown",
    SpEffectType.UNKNOWN_48: "Unknown",
    SpEffectType.RELOAD: "Reload",
    SpEffectType.UNKNOWN_49: "Unknown",
    SpEffectType.UNKNOWN_50: "Unknown",
    SpEffectType.UNKNOWN_51: "Unknown",
    SpEffectType.UNKNOWN_52: "Unknown",
    SpEffectType.UNKNOWN_53: "Unknown",
    SpEffectType.UNKNOWN_54: "Unknown",
    SpEffectType.UNKNOWN_55: "Unknown",
    SpEffectType.UNKNOWN_56: "Unknown",
    SpEffectType.UNKNOWN_57: "Unknown",
    SpEffectType.UNKNOWN_58: "Unknown",
    SpEffectType.UNKNOWN_59: "Unknown",
    SpEffectType.UNKNOWN_60: "Unknown",
    SpEffectType.UNKNOWN_61: "Unknown",
    SpEffectType.UNKNOWN_62: "Unknown",
    SpEffectType.UNKNOWN_63: "Unknown",
    SpEffectType.SPIRIT_SUMMON: "Spirit Summon",
    SpEffectType.UNKNOWN_64: "Unknown",
    SpEffectType.UNKNOWN_65: "Unknown",
    SpEffectType.UNKNOWN_66: "Unknown",
    SpEffectType.UNKNOWN_67: "Unknown",
    SpEffectType.UNKNOWN_68: "Unknown",
    SpEffectType.UNKNOWN_69: "Unknown",
    SpEffectType.UNKNOWN_70: "Unknown",
    SpEffectType.UNKNOWN_71: "Unknown",
    SpEffectType.UNKNOWN_72: "Unknown",
    SpEffectType.ENHANCE_CRITICAL_ATTACKS: "Enhance Critical Attacks",
    SpEffectType.UNKNOWN_73: "Unknown",
    SpEffectType.UNKNOWN_74: "Unknown",
    SpEffectType.UNKNOWN_75: "Unknown",
    SpEffectType.UNKNOWN_76: "Unknown",
    SpEffectType.UNKNOWN_77: "Unknown",
    SpEffectType.UNKNOWN_78: "Unknown",
    SpEffectType.UNKNOWN_79: "Unknown",
    SpEffectType.UNKNOWN_80: "Unknown",
    SpEffectType.UNKNOWN_81: "Unknown",
    SpEffectType.UNKNOWN_82: "Unknown",
    SpEffectType.TRIGGER_IN_PRESENCE_OF_BLOOD_LOSS: "Trigger in Presence of Blood Loss",
    SpEffectType.TRIGGER_IN_PRESENCE_OF_ROT: "Trigger in Presence of Rot",
    SpEffectType.UNKNOWN_83: "Unknown",
    SpEffectType.UNKNOWN_84: "Unknown",
    SpEffectType.UNKNOWN_85: "Unknown",
    SpEffectType.UNKNOWN_86: "Unknown",
    SpEffectType.UNKNOWN_87: "Unknown",
    SpEffectType.UNKNOWN_88: "Unknown",
    SpEffectType.UNKNOWN_89: "Unknown",
    SpEffectType.UNKNOWN_90: "Unknown",
    SpEffectType.PACIFY_WILD_ANIMALS: "Pacify Wild Animals",
    SpEffectType.UNKNOWN_91: "Unknown",
    SpEffectType.UNKNOWN_92: "Unknown",
    SpEffectType.UNKNOWN_93: "Unknown",
    SpEffectType.UNKNOWN_94: "Unknown",
    SpEffectType.UNKNOWN_95: "Unknown",
    SpEffectType.UNKNOWN_96: "Unknown",
    SpEffectType.UNKNOWN_97: "Unknown",
    SpEffectType.PULL_TOWARDS_CASTER: "Pull towards Caster",
    SpEffectType.UNKNOWN_98: "Unknown",
    SpEffectType.UNKNOWN_99: "Unknown",
    SpEffectType.UNKNOWN_100: "Unknown",
    SpEffectType.UNKNOWN_101: "Unknown",
    SpEffectType.REVEAL_PHANTOM_SIGNS: "Reveal Phantom Signs",
    SpEffectType.REQUEST_FRIENDLY_PHANTOM: "Request Friendly Phantom",
    SpEffectType.ANSWER_PHANTOM_REQUEST: "Answer Phantom Request",
    SpEffectType.ENCOURAGE_INVASION: "Encourage Invasion",
    SpEffectType.SEND_SUMMON_SIGN_TO_POOL: "Send Summon Sign to Pool",
    SpEffectType.SEND_INVASION_SIGN_TO_POOL: "Send Invasion Sign to Pool",
    SpEffectType.UNKNOWN_102: "Unknown",
    SpEffectType.UNKNOWN_103: "Unknown",
    SpEffectType.UNKNOWN_104: "Unknown",
    SpEffectType.UNKNOWN_105: "Unknown",
    SpEffectType.UNKNOWN_106: "Unknown",
    SpEffectType.UNKNOWN_107: "Unknown",
    SpEffectType.UNKNOWN_108: "Unknown",
    SpEffectType.UNKNOWN_109: "Unknown",
    SpEffectType.UNKNOWN_110: "Unknown",
    SpEffectType.UNKNOWN_111: "Unknown",
    SpEffectType.UNKNOWN_112: "Unknown",
    SpEffectType.UNKNOWN_113: "Unknown",
    SpEffectType.UNKNOWN_114: "Unknown",
    SpEffectType.UNKNOWN_115: "Unknown",
    SpEffectType.UNKNOWN_116: "Unknown",
    SpEffectType.UNKNOWN_117: "Unknown",
    SpEffectType.UNKNOWN_118: "Unknown",
    SpEffectType.UNKNOWN_119: "Unknown",
    SpEffectType.UNKNOWN_120: "Unknown",
    SpEffectType.UNKNOWN_121: "Unknown",
    SpEffectType.UNKNOWN_122: "Unknown",
    SpEffectType.UNKNOWN_123: "Unknown",
    SpEffectType.SLEEP: "Sleep",
    SpEffectType.MADNESS: "Madness",
    SpEffectType.CURE_SLEEP: "Cure Sleep",
    SpEffectType.CURE_MADNESS: "Cure Madness",
    SpEffectType.PURIFY_MOHGS_CURSE: "Purify Mohg's Curse",
    SpEffectType.MOHGS_GREAT_RUNE: "Mohg's Great Rune",
    SpEffectType.UNKNOWN_124: "Unknown",
    SpEffectType.UNKNOWN_125: "Unknown",
    SpEffectType.UNKNOWN_126: "Unknown",
    SpEffectType.UNKNOWN_127: "Unknown",
    SpEffectType.PHANTOM_GREAT_RUNE: "Phantom Great Rune",
    SpEffectType.HEAL_INVADER_WHEN_BLESSED_ENEMY_KILLS_PLAYER: "Heal Invader when Blessed Enemy Kills Player",
    SpEffectType.MALENIAS_GREAT_RUNE: "Malenia's Great Rune",
    SpEffectType.REDUCE_HEADSHOT_IMPACT: "Reduce Headshot Impact",
    SpEffectType.RECOVERY_DAMAGE: "Recovery Damage",
    SpEffectType.UNKNOWN_128: "Unknown",
    SpEffectType.UNKNOWN_129: "Unknown",
    SpEffectType.UNKNOWN_130: "Unknown",
    SpEffectType.UNKNOWN_131: "Unknown",
    SpEffectType.UNKNOWN_132: "Unknown",
    SpEffectType.ATTEMPT_INVASION: "Attempt Invasion",
    SpEffectType.UNKNOWN_133: "Unknown",
    SpEffectType.UNKNOWN_134: "Unknown",
    SpEffectType.UNKNOWN_135: "Unknown",
    SpEffectType.UNKNOWN_136: "Unknown",
    SpEffectType.UNKNOWN_137: "Unknown",
    SpEffectType.UNKNOWN_138: "Unknown",
    SpEffectType.TRIGGER_ON_CROUCH: "Trigger on Crouch",
    SpEffectType.BULLET_BEHAVIOR: "Bullet Behavior",
    SpEffectType.UNKNOWN_139: "Unknown",
    SpEffectType.UNKNOWN_140: "Unknown",
    SpEffectType.SKIPSPCATEGORYCHECK1: "SkipSpCategoryCheck1",
    SpEffectType.SKIPSPCATEGORYCHECK2: "SkipSpCategoryCheck2",
    SpEffectType.CUSTOM_TRIGGER: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_2: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_3: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_4: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_5: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_6: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_7: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_8: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_9: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_10: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_11: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_12: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_13: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_15: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_16: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_17: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_18: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_19: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_20: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_21: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_22: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_23: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_24: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_25: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_26: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_27: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_28: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_29: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_30: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_31: "Custom Trigger",
    SpEffectType.CUSTOM_TRIGGER_32: "Custom Trigger",
}

class ReinforcementType(str, Enum):
    NO_REINFORCEMENT = "3000"
    STANDARD = "0"
    HEAVY = "100"
    KEEN = "200"
    QUALITY = "300"
    FIRE = "400"
    FLAME_ART = "500"
    LIGHTNING = "600"
    SACRED = "700"
    MAGIC = "800"
    COLD = "900"
    POISON = "1000"
    BLOOD = "1100"
    OCCULT = "1200"
    CATALYST = "1900"
    UNIQUE = "2200"
    UNIQUE_CATALYST = "2400"
    CROSSBOW_BALLISTA = "3100"
    UNIQUE_CROSSBOW_BALLISTA = "3200"
    PULLEY_CROSSBOW = "3300"
    SPECIAL_KEEN = "5000"
    SPECIAL_HEAVY = "6000"
    SMALL_SHIELD = "8000"
    MEDIUM_SHIELD = "8100"
    GREATSHIELD = "8200"
    UNIQUE_GREATSHIELD = "8300"
    COIL_SHIELD = "8500"

    def __str__(self) -> str:
        return _REINFORCEMENT_TYPE[self]

_REINFORCEMENT_TYPE: Dict[ReinforcementType, str] = {
    ReinforcementType.NO_REINFORCEMENT: "No Reinforcement",
    ReinforcementType.STANDARD: "Standard",
    ReinforcementType.HEAVY: "Heavy",
    ReinforcementType.KEEN: "Keen",
    ReinforcementType.QUALITY: "Quality",
    ReinforcementType.FIRE: "Fire",
    ReinforcementType.FLAME_ART: "Flame Art",
    ReinforcementType.LIGHTNING: "Lightning",
    ReinforcementType.SACRED: "Sacred",
    ReinforcementType.MAGIC: "Magic",
    ReinforcementType.COLD: "Cold",
    ReinforcementType.POISON: "Poison",
    ReinforcementType.BLOOD: "Blood",
    ReinforcementType.OCCULT: "Occult",
    ReinforcementType.CATALYST: "Catalyst",
    ReinforcementType.UNIQUE: "Unique",
    ReinforcementType.UNIQUE_CATALYST: "Unique Catalyst",
    ReinforcementType.CROSSBOW_BALLISTA: "Crossbow Ballista",
    ReinforcementType.UNIQUE_CROSSBOW_BALLISTA: "Unique Crossbow Ballista",
    ReinforcementType.PULLEY_CROSSBOW: "Pulley Crossbow",
    ReinforcementType.SPECIAL_KEEN: "Special Keen",
    ReinforcementType.SPECIAL_HEAVY: "Special heavy",
    ReinforcementType.SMALL_SHIELD: "Small Shield",
    ReinforcementType.MEDIUM_SHIELD: "Medium Shield",
    ReinforcementType.GREATSHIELD: "Greatshield",
    ReinforcementType.UNIQUE_GREATSHIELD: "Unique Greatshield",
    ReinforcementType.COIL_SHIELD: "Coil Shield"
}
