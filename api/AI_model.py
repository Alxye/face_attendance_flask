from flask import Blueprint, request
import os
import cv2
import numpy as np
import torch
from AI_model.face_sys import FaceSystem
import pymysql
from PIL import Image
import math

def extract(tmp_img_address):
    # 加载MTCNN人脸检测器和FaceNet人脸识别模型
    fs = FaceSystem()
    mtcnn = fs.face_detect
    resnet = fs.get_face_feature

    # 读取员工人脸图像并生成特征向量
    feature = []

    img = Image.open(tmp_img_address)
    # 检测人脸
    boxes = mtcnn(img)
    # print(len(boxes))
    # print(boxes)

    if len(boxes) > 0:
        lm = 0
        tx1, ty1, tx2, ty2 = 0, 0, 0, 0
        for box in boxes:
            x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
            if lm < box[4]:
                lm = box[4]
                tx1, ty1, tx2, ty2 = x1, y1, x2, y2

        # 带有检测框的人脸img
        face_with_boxes = fs.show_face_boxes(img, boxes)
        face_with_boxes.save('face_with_boxes.jpg')

        # 裁剪检测框中的人脸
        # box = boxes[0]
        x1, y1, x2, y2 = tx1, ty1, tx2, ty2
        img = np.array(img)
        face_in_boxes = img[y1: y2, x1: x2, :]
        face_in_boxes = cv2.resize(face_in_boxes, (224, 224))
        # face_in_boxes = cv2.cvtColor(face_in_boxes, cv2.COLOR_BGR2RGB)

        # 人脸特征
        feature = resnet(face_in_boxes)

        res = {
            'code': 1,
            'embedding': feature.tobytes()
        }
    elif len(boxes) == 0:
        res = {
            'code': 0,
            'embedding': feature
        }
    # print(res)
    return res

def calc_similarity(face_embedding, embeddings):
    fs = FaceSystem()
    dist = fs.feature_compare(face_embedding, embeddings)
    return dist