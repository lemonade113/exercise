# 使用PyQt5做的人脸表情识别图像化界面，该程序是使用Python3.7开发的，利用Dlib库实现人脸识别以及情绪分析的功能。
# 利用 Dlib 官方训练好的模型 “shape_predictor_68_face_landmarks.dat” 进行 68 个特征点标定，该模型已上传到该资源中，可以直接调用，
# 利用 OpenCv 进行图像化处理，在人脸上画出 68 个特征点，并用红色数字标明特征点的序号。
# 使用嘴巴的张开比例，眼睛的睁开程度，眉毛的倾斜程度作为表情分析的三个指标，
# 通过计算特征点之间的欧氏距离，来判断人脸的表情。该系统主要能够识别惊恐、常态、高兴、生气等四种表情，识别准确率高，速度快。