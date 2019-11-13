from . import FuseRule

import re

_IDLE = 0
_DOWNS = 1

class ConvBNRuleByName(FuseRule):
    """Rule for merge BN into Convolution. Equivalence transformation with out loss in accuracy."""

    @staticmethod
    def getInfo(keyword, name):
        res = re.match(f"(.*){keyword}(\d*)", name)
        return res.group(), res.group(1), res.group(2)

    def __init__(self):
        self._name_list = list()
        self._idle()

    def _idle(self):
        self.cur_list = list()
        self.cur_prefix = None
        self.cur_suffix = None
        self.state = _IDLE

    def add_module(self, m):
        m_name = m[0]
        if self.state == _IDLE:
            check, prefix, suffix = self.getInfo("downsample", m_name)
            if check is not None:
                self.cur_prefix = prefix
                self.cur_suffix = suffix
                self.cur_list = [m_name]
                self.state = _DOWNS
        elif self.state == _DOWNS:
            check, prefix, suffix = self.getInfo("downsample", m_name)
            if check is None:
                self._idle()
            elif prefix != self.cur_prefix:
                self._idle()
            else:
                self.cur_list.append(m_name)
                self._name_list.append(self.cur_list)
                self._idle()
        else:
            raise NotImplementedError

    def names_lists(self):
        return self.names_lists
