from datetime import datetime
from typing import Optional
from tenderDocument import TenderDocument


    # 初始化必填字段示例
sample_tender = TenderDocument(
        baoming_kaishi_shijian=datetime(2024, 6, 1),
        baoming_jieshu_shijian=datetime(2024, 6, 10),
        zhaobiao_baozhengjin=50000.0,
        baozhengjin_jiaona_jiezhi=datetime(2024, 6, 15),
        feizhongbiao_tuihuan="中标公示后7个工作日内退还",
        zhongbiao_tuihuan="合同签订后15个工作日内退还",
        biangeng_gonggao_jiezhi=datetime(2024, 6, 5),
        toubiao_jiezhi_shijian=datetime(2024, 6, 20),
        toubiaojiemi_fangshi="在线解密",
        kaibiao_shijian=datetime(2024, 6, 25),
        kaibiao_didian="XX市公共资源交易中心",
        jiaohuo_didian="招标方指定仓库",
        xiangmu_suozaidi="XX省XX市",
        zhaobiao_fangmingcheng="XX集团有限公司",
        zhaobiao_dizhi="XX市XX区XX路100号",
        zhaobiao_lianxiren="张经理"
    )
print(sample_tender.__dict__)