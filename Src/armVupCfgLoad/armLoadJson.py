import json
from Src.armVupLogic.VupzLogic import TP, VupzObjectClass, TpWayClass


class ParsejsonCreateTp:
    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            json_data = json.load(f)
        stp_names = json_data['stp_names']
        stp_config = json_data['stp_config']
        self.tp = TP()
        list_of_all_vupz: list[VupzObjectClass] = []

        for id, name in stp_names.items():
            vupz = VupzObjectClass(id, name)
            list_of_all_vupz.append(vupz)

        vupz_cnt = 0
        for cnt, vupz_per_way in enumerate(stp_config):
            way = TpWayClass()
            way.way_num = cnt
            way.vupz_cnt = int(vupz_per_way)
            for _ in range(int(vupz_per_way)):
                if vupz_cnt > len(list_of_all_vupz) - 1:
                    raise NotImplementedError("Тут нужно сделать exeption")
                way.vupz_obj.append(list_of_all_vupz[vupz_cnt])
                vupz_cnt += 1
            self.tp.ways.append(way)

    def create_tp_from_json(self):
        return self.tp
