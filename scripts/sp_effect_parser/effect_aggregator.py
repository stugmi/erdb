from types import SimpleNamespace
from typing import List, Dict, Set, NamedTuple
from sp_effect_parser.effect_typing import AttributeName, SchemaEffect

_A = AttributeName

class AttributeAggregatorHint(NamedTuple):
    base: Set[AttributeName]
    effective: AttributeName

class AggregatedSchemaEffect(SimpleNamespace):
    attribute_names: Set[AttributeName]
    example_effect: SchemaEffect

    @classmethod
    def from_effect(cls, effect: SchemaEffect) -> "AggregatedSchemaEffect":
        return cls(attribute_names={effect.attribute}, example_effect=effect)

"""
Specifies which attribute sets can be collapsed into their effective attribute.
ORDER IS IMPORTANT because effective attributes are taken into consideration in
consecutive iterations.
"""
_AGGREGATOR_HINTS: List[AttributeAggregatorHint] = [
    AttributeAggregatorHint(
        base={_A.STANDARD_ABSORPTION, _A.STRIKE_ABSORPTION, _A.SLASH_ABSORPTION, _A.PIERCE_ABSORPTION},
        effective=_A.PHYSICAL_ABSORPTION
    ),
    AttributeAggregatorHint(
        base={_A.MAGIC_ABSORPTION, _A.FIRE_ABSORPTION, _A.LIGHTNING_ABSORPTION, _A.HOLY_ABSORPTION},
        effective=_A.ELEMENTAL_ABSORPTION
    ),
    AttributeAggregatorHint(
        base={_A.PHYSICAL_ABSORPTION, _A.ELEMENTAL_ABSORPTION},
        effective=_A.ABSORPTION
    ),
    AttributeAggregatorHint(
        base={_A.STANDARD_ATTACK_POWER, _A.STRIKE_ATTACK_POWER, _A.SLASH_ATTACK_POWER, _A.PIERCE_ATTACK_POWER},
        effective=_A.PHYSICAL_ATTACK_POWER
    ),
    AttributeAggregatorHint(
        base={_A.MAGIC_ATTACK_POWER, _A.FIRE_ATTACK_POWER, _A.LIGHTNING_ATTACK_POWER, _A.HOLY_ATTACK_POWER},
        effective=_A.ELEMENTAL_ATTACK_POWER
    ),
    AttributeAggregatorHint(
        base={_A.PHYSICAL_ATTACK_POWER, _A.ELEMENTAL_ATTACK_POWER},
        effective=_A.ATTACK_POWER
    ),
]

def _get_aggregated_effects(effects: List[SchemaEffect]) -> Dict[int, AggregatedSchemaEffect]:
    aggregated_effects: Dict[int, AggregatedSchemaEffect] = dict()

    for effect in effects:
        if (key := effect.get_values_hash()) in aggregated_effects:
            aggregated_effects[key].attribute_names.add(effect.attribute)
        else:
            aggregated_effects[key] = AggregatedSchemaEffect.from_effect(effect)

    return aggregated_effects

def _aggregate_attributes(attributes: Set[AttributeName], hints: List[AttributeAggregatorHint]) -> Set[AttributeName]:
    for hint in hints:
        if hint.base.issubset(attributes):
            attributes.difference_update(hint.base)
            attributes.add(hint.effective)

    return attributes

def _aggregated_effects_to_effects(aggregated_effects: Dict[int, AggregatedSchemaEffect]) -> List[SchemaEffect]:
    effects = []

    for aggregated_effect in aggregated_effects.values():
        for attribute_name in aggregated_effect.attribute_names:
            effects.append(aggregated_effect.example_effect.clone(attribute_name))

    return effects

def aggregate_effects(base_effects: List[SchemaEffect]) -> List[SchemaEffect]:
    aggregated_effects = _get_aggregated_effects(base_effects)

    for key, aggregated_effect in aggregated_effects.items():
        aggregated_effects[key].attribute_names = _aggregate_attributes(aggregated_effect.attribute_names, _AGGREGATOR_HINTS)

    return _aggregated_effects_to_effects(aggregated_effects)