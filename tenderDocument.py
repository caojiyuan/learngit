from datetime import datetime
from typing import Optional

class TenderDocument:
    """标书类，用于管理招标项目相关信息"""
    
    def __init__(
        self,
        # ----------------- 必须参数 -----------------
        # 基础时间信息
        baoming_kaishi_shijian: datetime,
        baoming_jieshu_shijian: datetime,
        
        # 保证金相关字段
        zhaobiao_baozhengjin: float,
        baozhengjin_jiaona_jiezhi: datetime,
        feizhongbiao_tuihuan: str,
        zhongbiao_tuihuan: str,
        
        # 流程时间节点
        biangeng_gonggao_jiezhi: datetime,
        toubiao_jiezhi_shijian: datetime,
        
        # 投标技术参数
        toubiaojiemi_fangshi: str,
        
        # 开标信息
        kaibiao_shijian: datetime,
        kaibiao_didian: str,
        
        # 物流信息
        jiaohuo_didian: str,
        xiangmu_suozaidi: str,
        
        # 招标方信息
        zhaobiao_fangmingcheng: str,
        zhaobiao_dizhi: str,
        zhaobiao_lianxiren: str,

        # ----------------- 可选参数（带默认值） -----------------
        # 提问相关字段
        shifou_tianjiatiwen: bool = False,
        tiwen_kaishi_shijian: Optional[datetime] = None,
        tiwen_jiezhi_shijian: Optional[datetime] = None,
        tiwen_xuyao_fujian: bool = False,
        
        # 现场踏勘信息
        xuyao_xianchangtakan: bool = False,
        takan_shijian: Optional[datetime] = None,
        takan_lianxiren: Optional[str] = None,
        takan_lianxifangshi: Optional[str] = None,
        takan_didian: Optional[str] = None,
    ):
        """
        初始化标书对象

        参数说明：
        1. 必须参数在前，可选参数在后
        2. 时间类型字段建议使用datetime对象
        """

        # 报名阶段参数
        self.baoming_kaishi = baoming_kaishi_shijian
        self.baoming_jieshu = baoming_jieshu_shijian

        # 保证金参数
        self.baozhengjin_amount = zhaobiao_baozhengjin
        self.baozhengjin_deadline = baozhengjin_jiaona_jiezhi
        self.refund_nonwinner = feizhongbiao_tuihuan
        self.refund_winner = zhongbiao_tuihuan

        # 流程控制参数
        self.biangeng_deadline = biangeng_gonggao_jiezhi
        self.toubiao_deadline = toubiao_jiezhi_shijian
        self.jiemi_method = toubiaojiemi_fangshi

        # 开标参数
        self.kaibiao_time = kaibiao_shijian
        self.kaibiao_venue = kaibiao_didian

        # 物流参数
        self.delivery_address = jiaohuo_didian
        self.project_location = xiangmu_suozaidi

        # 招标方信息
        self.tender_org = zhaobiao_fangmingcheng
        self.tender_address = zhaobiao_dizhi
        self.tender_contact = zhaobiao_lianxiren

        # ----------------- 可选参数初始化 -----------------
        # 提问环节参数
        self.enable_tiwen = shifou_tianjiatiwen
        self.tiwen_start = tiwen_kaishi_shijian
        self.tiwen_end = tiwen_jiezhi_shijian
        self.tiwen_require_attachment = tiwen_xuyao_fujian

        # 现场踏勘参数
        self.require_takan = xuyao_xianchangtakan
        self.takan_time = takan_shijian
        self.takan_contact_person = takan_lianxiren
        self.takan_contact_info = takan_lianxifangshi
        self.takan_location = takan_didian

    # ...（其他方法保持不变）
    def validate_dates(self):
        """验证时间逻辑有效性"""
        # 这里可以添加时间顺序验证逻辑
        # 示例：验证报名开始时间早于结束时间
        if self.baoming_kaishi > self.baoming_jieshu:
            raise ValueError("报名开始时间不能晚于结束时间")
        # 可继续添加其他时间验证逻辑...

    def to_dict(self):
        """将对象转换为字典（便于序列化）"""
        return self.__dict__