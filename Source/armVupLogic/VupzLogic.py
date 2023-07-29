from Source.armVupExeptions.configurateException import LoadCfgException


class VupzObjectClass:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def refresh_state(self, vupz_state_dict):
        self.bmkN = vupz_state_dict['bmk']
        self.bmkS = vupz_state_dict['bmkS']
        self.pr = vupz_state_dict['pr']
        self.pt0 = vupz_state_dict['pr0']
        self.pt1 = vupz_state_dict['pr1']
        self.temp = vupz_state_dict['temp']
        self.p05 = vupz_state_dict['p05']
        self.p10 = vupz_state_dict['p10']
        self.p15 = vupz_state_dict['p15']
        self.p20 = vupz_state_dict['p20']
        self.p25 = vupz_state_dict['p25']
        self.p30 = vupz_state_dict['p30']
        self.p35 = vupz_state_dict['p35']
        self.err = vupz_state_dict['Err']
        self.uPit = vupz_state_dict['uPit']
        self.tempHeart = vupz_state_dict['temHeart']
        self.timeW = vupz_state_dict['timeW']
        self.prAtmCal0 = vupz_state_dict['prAtmCal0']
        self.prAtmCal1 = vupz_state_dict['prAtmCal1']
        self.styp = vupz_state_dict['styp']
        self.l_curct = vupz_state_dict['l']
        self.temp2 = vupz_state_dict['temp2']
        self.timeR = vupz_state_dict['timeR']


class TpWayClass:
    def __init__(self):
        self.way_num = None
        self.vupz_cnt = None
        self.vupz_obj: list[VupzObjectClass] = []


class TP:
    def __init__(self):
        self.ways_cnt = None
        self.ways: list[TpWayClass] = []
        self.post_ec: PostEc = None


class PostEc:
    def __init__(self, post_ec_data):
        if post_ec_data == 'ЮГ':
            self.relx = 0.45
            self.rely = 0.85
        elif post_ec_data == 'СЕВЕР':
            self.relx = 0.45
            self.rely = 0.05
        else:
            raise LoadCfgException('Некоректное расположение поста')
