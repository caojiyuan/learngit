# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
from tenderDocument import TenderDocument
from datetime import datetime


# sample_tender = TenderDocument(
#         baoming_kaishi_shijian=datetime(2024, 6, 1),
#         baoming_jieshu_shijian=datetime(2024, 6, 10),
#         zhaobiao_baozhengjin=50000.0,
#         baozhengjin_jiaona_jiezhi=datetime(2024, 6, 15),
#         feizhongbiao_tuihuan="中标公示后7个工作日内退还",
#         zhongbiao_tuihuan="合同签订后15个工作日内退还",
#         biangeng_gonggao_jiezhi=datetime(2024, 6, 5),
#         toubiao_jiezhi_shijian=datetime(2024, 6, 20),
#         toubiaojiemi_fangshi="在线解密",
#         kaibiao_shijian=datetime(2024, 6, 25),
#         kaibiao_didian="XX市公共资源交易中心",
#         jiaohuo_didian="招标方指定仓库",
#         xiangmu_suozaidi="XX省XX市",
#         zhaobiao_fangmingcheng="XX集团有限公司",
#         zhaobiao_dizhi="XX市XX区XX路100号",
#         zhaobiao_lianxiren="张经理"
#     )
# cout ="根据以下内容生成标书文件:{0}".format(sample_tender.__dict__)
# print(cout)

client = OpenAI(api_key="sk-6f8a3dd17777483cac209df838c04aa9", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "根据以下内容生成招标文件:{'baoming_kaishi': datetime.datetime(2024, 6, 1, 0, 0), 'baoming_jieshu': datetime.datetime(2024, 6, 10, 0, 0), 'baozhengjin_amount': 50000.0, 'baozhengjin_deadline': datetime.datetime(2024, 6, 15, 0, 0), 'refund_nonwinner': '中标公示后7个工作日内退还', 'refund_winner': '合同签订后15个工作日内退还', 'biangeng_deadline': datetime.datetime(2024, 6, 5, 0, 0), 'toubiao_deadline': datetime.datetime(2024, 6, 20, 0, 0), 'jiemi_method': '在线解密', 'kaibiao_time': datetime.datetime(2024, 6, 25, 0, 0), 'kaibiao_venue': 'XX市公共资源交易中心', 'delivery_address': '招标方指定仓库', 'project_location': 'XX省XX市', 'tender_org': 'XX集团有限公司', 'tender_address': 'XX市XX区XX路100号', 'tender_contact': '张经理', 'enable_tiwen': False, 'tiwen_start': None, 'tiwen_end': None, 'tiwen_require_attachment': False, 'require_takan': False, 'takan_time': None, 'takan_contact_person': None, 'takan_contact_info': None, 'takan_location': None}"},
    ],
    stream=False
)

print(response.choices[0].message.content)