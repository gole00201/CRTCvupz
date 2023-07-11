import Source.armVupExeptions.serialExeptions as ex


class StringParser:
    def __init__(self):
        self.gPr_params_keys = ['bmk', 'pr0',
                                'pr1', 'pr2',
                                'er', 'bmkC',
                                'prC0', 'prC1',
                                'erC', 'cs']

        self.get_status_keys = ['bmk', 'bmkS',
                                'bmkSK', 'pr',
                                'pr0', 'pr1',
                                'temp', 'P05',
                                'P10', 'P15',
                                'P20', 'P25',
                                'P30', 'P35',
                                'Err', 'uPit',
                                'temHeart',
                                'timeW',
                                'prAtmCal0',
                                'prAtmCal1',
                                'Styp', 'l',
                                'temp2', 'timeR',
                                'cs']

    def parse_answ(self, answ):
        self.from_answ_to_string(answ)
        self.check_answ(answ)
        return self.answ_dict

    def check_answ(self, answ):
        if not answ:
            raise ex.GetEmptyString('')
        if not self.check_cs():
            raise ex.ParsingException('Не сошлась контрольная сумма')
        if not self.check_err():
            raise ex.ParsingException('Ошибка в структуре ответа')

    def check_cs(self):
        return True

    def check_err(self):
        for key in self.answ_dict.keys():
            for std_key in self.get_status_keys:
                if key == std_key:
                    continue
                else:
                    break

    def load_err_list(self):
        pass

    def from_answ_to_string(self, answ):
        clear_answ = answ.replace('=', ' ')
        tokens = clear_answ.split()
        self.answ_dict = {}
        for token in tokens:
            if token in self.gPr_params_keys:
                self.answ_dict[token] = tokens[tokens.index(token) + 1]
            elif token in self.get_status_keys:
                self.answ_dict[token] = tokens[tokens.index(token) + 1]
