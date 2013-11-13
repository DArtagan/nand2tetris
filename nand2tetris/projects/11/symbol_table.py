#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 11
# FILENAME:.......... symbol_table.py
# PYTHON VERSION:.... 3.3.0
#============================================================

class SymbolTable():
    segments = {'var': 'local',
                'arg': 'argument',
                'field': 'this',
                'static': 'static',
               }
 
    def __init__(self):
        self.table = {}

    def start_subroutine():
        for key in self.table:
            entry = self.table[key]['kind']
            if (entry == 'local') | (entry == 'argument'):
                del self.table[key]

    def define(self, var_name, var_type, var_kind):
        segment = local.segments[var_kind]
        self.table[var_name] = {'type': var_type,
                                'kind': segment, 
                                'count': self.count(segment),
                               }

    def count(self, segment):
        count = 0
        for key in self.table:
            if self.table[key]['kind'] == segment:
                count += 1
        return count

    def kind_of(self, name):
        return of(name, 'kind')

    def type_of(self, name):
        return of(name, 'type')

    def index_of(self, name):
        return of(name, 'count')

    def of(self, name, key):
        if name in self.table:
            return self.table[name][key]
        return None

    def contains(self, name):
        return name in self.table
