from Src.armVupCfgLoad.armLoadJson import ParseJson
from Src.armVupUi.UiEntity.MainWindow import ArmMainwindow

if __name__ == "__main__":
    json_path = './Cfg/SaintPSortMsk-3/stp.json'
    tp = ParseJson(json_path).create_tp_from_json()
    window = ArmMainwindow(tp)
    window.create_context()
    window.mainloop()
