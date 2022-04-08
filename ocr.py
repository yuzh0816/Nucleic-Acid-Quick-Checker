import pandas as pd
import os
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr

row=["",""]
name=[]
tim=[]
res=[]

#开启OCR
ocr = PaddleOCR(enable_mkldnn=True,use_angle_cls=False, use_gpu=True,use_tensorrt=True,
                lang="ch")  # need to run only once to download and load model into memory


img_path = 'C:/Users/Yu Zhehao/Desktop/a/'

# 保存不同模型的目录名(绝对路径)
file_dir = r'C:/Users/Yu Zhehao/Desktop/a/'
for root,dirs,files in os.walk(file_dir):
    for file in files:
        img_path=file_dir+file
        if file=="dic.py" or file=="ocr.py" or file=="result.csv":
            continue
        result = ocr.ocr(img_path, cls=True)
        txts = [line[1][0] for line in result]
        for i in range(len(txts)):
            if txts[i]=="姓名":
                name.append(txts[i+1])
                print("姓名："+txts[i+1])
            elif txts[i]=="检测时间：":
                print("检测时间："+txts[i+1])
                tim.append(txts[i+1])
            elif txts[i]=="检测结果：":
                if(txts[i+1][0]=="【"):
                    print("检测结果："+txts[i+1])
                    res.append(txts[i+1])
                else:
                    print("检测结果："+txts[i-1])
                    res.append(txts[i-1])
                break


data={"姓名":name,"检测时间":tim,"检测结果":res}
data_table=pd.DataFrame(data)
print(data_table)
data_table.to_csv("result.csv",encoding='utf_8_sig')
