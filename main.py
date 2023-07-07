from Src.armVupCfgLoad.armLoadJson import ParsejsonCreateTp

if __name__ == "__main__":
    json_path = './Cfg/SaintPSortMsk-3/stp.json'
    tp = ParsejsonCreateTp(json_path).create_tp_from_json()
    for way in tp.ways:
        print(f"Путь номер: {way.way_num} содержит {way.vupz_cnt} вупзов: ")
        for vupz in way.vupz_obj:
            print(vupz.name)
