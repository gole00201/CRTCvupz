from Src.armVupCfgLoad.armLoadJson import LoadJson

if __name__ == "__main__":
    json_path = './Cfg/SaintPSortMsk-3/stp.json'
    tp = LoadJson(json_path).create_tp()
    for way in tp.ways:
        print(f"Путь номер: {way.way_num} содержит {way.vupz_cnt} вупзов: ")
        for vupz in way.vupz_obj:
            print(vupz.name)
