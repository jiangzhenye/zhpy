#coding = utf-8
"""
泡沫紅茶店 0.1

1. 茶種 紅 綠 清 抹 烏龍
2. 配料 珍珠 粉圓 百香 檸檬 梅子
3. 糖量 少糖 3/4, 半糖 1/2 微糖 1/4
4. 冰量 去冰 少冰
"""

p_8336_7a2e_v = {"紅茶":15,"綠茶":15, "清茶":15, "抹茶":15, \
       "烏龍":15, "奶茶":20, "奶綠":20} #字典

p_914d_6599_v = {"珍珠":5, "粉圓":5, "百香":5, "檸檬":5, "梅子":5}

p_7cd6_91cf_v = ["少糖","半糖","微糖"] #列表

p_51b0_91cf_v = ["去冰", "少冰"]

def p_98f2_6599_55ae_751f_6210_5668_v():
    """
    產生飲料價目單
    """
    for p_6599_v in p_914d_6599_v.keys(): # 迴圈
        for p_8336_v in p_8336_7a2e_v.keys():
            p_6a19_50f9_v = p_8336_7a2e_v[p_8336_v] + p_914d_6599_v[p_6599_v]
            print p_6599_v+p_8336_v, p_6a19_50f9_v,
            for p_7cd6_v in p_7cd6_91cf_v:
                print p_7cd6_v,
            for p_51b0_v in p_51b0_91cf_v:
                print p_51b0_v,
            print ''

if __name__=="__main__":
    p_98f2_6599_55ae_751f_6210_5668_v()