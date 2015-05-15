__author__ = 'moskupols'

__all__ = [
    'Explanator',
    'explanator',
]


from hb_res.explanation_source import sources_registry
from ._explanator import Explanator
bad = [s for s in sources_registry.sources_registered() if s.name != 'Selected']
good = [sources_registry.source_for_name('Selected')]
explanator = Explanator({'bad': bad, 'good': good})

del sources_registry, bad, good
