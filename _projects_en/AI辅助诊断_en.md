---
permalink: /projects/ai-assisted-diagnose
other_lang_link: /projects/AI辅助诊断
layout: single
author_profile: false
language: en
classes: wide
title: "AI-assisted Medical Diagnosis"
year: 2020
intro: "AI analyzes X-ray pictures to assist doctors in medical diagnosis"
info: "AI_assisted_diagnose_en"
english: true
excerpt: "
AI analyzes X-ray pictures to assist doctors in medical diagnosis, including<br>
· Automatically segment different organ regions and accurately calculate proportions or angles<br>
· Identify potential lesions based on different disease characteristics<br>
· Automatic generation of structured diagnostic reports after the doctor reviews the diagnostic results"
header:
  teaser: /assets/images/AI_assisted_diagnose_headimg.jpg
  overlay_image: /assets/images/AI_assisted_diagnose_headimg.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
  caption: "Pic by Wenhua Chen"
  actions:
    - label: "Learn more"
      url: "/projects/ai-assisted-diagnose#background-and-purpose"
sidebar:
  nav: "AI_assisted_diagnose_en"
---

### Background and Purpose

#### What is AI-assisted medical diagnosis?
  - After a patient's x-ray is taken, AI algorithms will analyze the image to assist the doctor in making a medical diagnosis, including
    - Automatically segment different organ regions and accurately calculate proportions or angles
    - Identify potential lesions based on different disease characteristics
    - Automatic generation of structured diagnostic reports after the doctor reviews the diagnostic results
  <table>
    <tr>
      <th>Scoliosis</th>
      <th>Enlarged heart shadow</th>
      <th>Pulmonary nodule</th>
    </tr>
    <tr>
      <td><img src="/assets/images/AI_assisted_diagnose/图片 1.png" alt="图片 1" style="zoom:100%;" /></td>
      <td><img src="/assets/images/AI_assisted_diagnose/心影增大诊断.jpeg" alt="心影增大诊断" style="zoom:15%;" /></td>
      <td><img src="/assets/images/AI_assisted_diagnose/简单器官分割+肺结节检测.jpg" alt="简单器官分割+肺结节检测" style="zoom:18%;" /></td>
    </tr>
  </table>

#### Why do we need AI-assisted diagnosis?
  - Improve efficiency
    - According to experience, it takes 3-5 minutes for a doctor to complete a manual diagnosis. Still, the AI algorithm can give the preliminary diagnosis result in 10 seconds, and it takes less than 1 minute for the doctor to review the result and give the diagnosis report, significantly improving efficiency.
  - Risk Warning
    - During busy hospital hours, the number of doctors available may be insufficient to view the results immediately, resulting in a buildup of x-ray images. Some diseases (e.g., severe emphysema) are time-sensitive and require immediate surgical treatment upon detection. Otherwise, they may be life-threatening.
    - AI-assisted diagnosis can give all patients' initial diagnosis results in real-time and prioritize them according to their conditions, with more severe conditions being given to doctors preferentially and very serious conditions being alerted to doctors for immediate attention
  - Supplementing medical resources in remote areas
  - Teaching use

------

### Overview of The Process

#### Demo
  <img src="/assets/images/AI_assisted_diagnose/软件展示.png" alt="软件展示" style="zoom:100%;" />{:.align-center}

#### Test Results
  <img src="/assets/images/AI_assisted_diagnose/image-20220804160558024_en.png" alt="image-20220804160558024" style="zoom:80%;" />{:.align-center}

#### What is the structure of the whole process?
  - Data filtering first to make sure the input images are clear and valid
  - Then the organ regions were segmented, including the spine, left and right lungs, ribs, etc.
  - For simple diseases, just input the original image or the segmented result for classification
  - For complex diseases, customized object detection or classification model is required
  - Finally, results are aggregated and case reports are generated
    <img src="/assets/images/AI_assisted_diagnose/算法流程图_en.drawio.png" alt="算法流程图" style="zoom:40%;" />{:.align-center}

------

### Challenges - Data Preparation

#### How does the training data been prepared?
  - <span class="span_anchor" id="problems-with-public-datasets">Surveyed public datasets includes [ChestX-ray14(2017)](https://arxiv.org/pdf/1705.02315.pdf)、[CheXpert(2019)](https://arxiv.org/pdf/1901.07031.pdf)、[MIMIC-CXR(2019)](https://arxiv.org/pdf/1901.07042.pdf), etc.</span>
    - Some problems with public datasets: incomplete disease types, inconsistent labeling methods, poor labeling quality, differences in the definition of lesions between domestic and foreign medical communities, etc.
    - There are still many questions about the accuracy of public datasets, such as [question one](https://zhuanlan.zhihu.com/p/37384516), [question two](https://lukeoakdenrayner.wordpress.com/2017/12/18/the- chestxray14-dataset-problems/), [challenge three](https://twitter.com/erictopol/status/930980060835614720), etc.
  <table style="width: 100%;">
    <tr>
      <th>Annotation of public datasets</th>
      <th>Expected annotation</th>
    </tr>
    <tr>
      <td><img src="/assets/images/AI_assisted_diagnose/公开数据集举例_en.png" alt="公开数据集举例" style="zoom:48%;" /></td>
      <td><img src="/assets/images/AI_assisted_diagnose/期望的标注-9511800_en.png" alt="期望的标注" style="zoom:48%;" /></td>
    </tr>
  </table>
  - <span class="span_anchor" id="self-made-dataset"> To comply with the domestic standard and to standardize disease species and labeling methods, it was decided to create a self-made dataset</span>
    - In cooperation with Ruijin Hospital of Shanghai Jiao Tong University (Triple-A), there are 180,000 original radiographs and corresponding case reports in the database, and 153,000 validity data were obtained after in-hospital desensitization and cleaning.
    - The chief radiology physician of Ruijin Hospital's radiology department was in charge of the annotation and was responsible for the annotation results. 
    - We built the annotation system and cleaned the data, obtained 34,000 precision labeled data, and built the Ruijin Hospital DR dataset (not open source) in the end
  - <span class="span_anchor" id="data-annotation">Data Annotation</span>
    - Development of the annotation system
    - Segment the organ area and label the lesion type and location
    - Both rectangular box and polygon labeling are used
      <img src="/assets/images/AI_assisted_diagnose/标注系统.png" alt="标注系统" style="zoom:40%;" />{:.align-center}
  - <span class="span_anchor" id="cost-control">Cost Control</span>
    - Professional datasets are very expensive to produce, especially for physician labeling, averaging 40RMB per image
    - Establishing a two-stage annotation mechanism, in which junior physicians label first and senior physicians review. Using this mechanism, we reduced costs and ensured the accuracy of results at the same time
    - Except for the two-stage mechanism, we also labeled according to demand: some models need a small amount of data to meet the requirements, while models that do not work well were supplied with additional data
      <img src="/assets/images/AI_assisted_diagnose/image-20220803120731568_en.png" alt="image-20220803120731568" style="zoom:40%;" />{:.align-center}

#### How is the data pre-processed?
  - <span class="span_anchor" id="cropping">Cropping</span>
    - Different diseases have different appearing regions, e.g., pulmonary nodules only appear in both lungs, so cutting out the lung region and analyzing it separately has a lot of advantages:
      - More effective information can be retained after image compression to improve recall
      - It can remove irrelevant information and reduce the false positive rate
      <img src="/assets/images/AI_assisted_diagnose/图片裁剪的优势_en.png" alt="图片裁剪的优势" style="zoom:40%;" />{:.align-center}
  - <span class="span_anchor" id="data-enhancement">Data Enhancement</span>
    - Random scaling, random erasing, horizontal flipping, and other standard data enhancement methods
    - CLAHE feature enhancement
      - CLAHE (Contrast Limited Adaptive Histogram Equalization) is a histogram equalization algorithm based on the idea of chunking, which is widely used for data enhancement.
      - We observed that CLAHE processing can significantly affect the contrast of bones on X-ray chest films, for example, the contrast of marginal features such as vertebrae and ribs is stronger
        <img src="/assets/images/AI_assisted_diagnose/图像增强-9513884_en.png" alt="图像增强" style="zoom:40%;margin-top:2em;" />{:.align-center}

------

### Challenges - Algorithm Development

#### How is scoliosis determined?
  - <span class="span_anchor" id="cobb-angle-and-its-definition">Cobb angle and its definition</span>
    - First, find the two vertebrae that cause the maximum angle, then extend the upper edge of the upper vertebrae and the lower edge of the lower vertebrae, and finally, the angle of the vertical line between the two extensions is the Cobb angle (equal to the angle between the two extensions)
    - The Cobb angle is an essential basis for determining scoliosis. Usually, a Cobb angle greater than 10 degrees will be defined as scoliosis
  <table>
    <tr>
      <th>Definition of Cobb angle</th>
      <th>Original image</th>
      <th>CLAHE Data Enhancement</th>
    </tr>
    <tr>
      <td><img src="/assets/images/AI_assisted_diagnose/cobb角png.png" alt="cobb角png" style="zoom:30%;" /></td>
      <td><img src="/assets/images/AI_assisted_diagnose/原图.png" alt="原图" style="zoom:30%;" /></td>
      <td><img src="/assets/images/AI_assisted_diagnose/CLAHE数据增强.png" alt="CLAHE数据增强" style="zoom:30%;" /></td>
    </tr>
  </table>
  - <span class="span_anchor" id="processing-flow">Processing Flow</span>
    - Original image --> CLAHE data enhancement --> MaskRCNN segmentation --> Outer edge point conversion --> Post processing
  <table>
    <tr>
      <th>MaskRCNN segmentation</th>
      <th>Outer edge point conversion</th>
      <th>Post processing</th>
    </tr>
    <tr>
      <td><img src="/assets/images/AI_assisted_diagnose/MaskRCNN结果.png" alt="MaskRCNN结果" style="zoom:48%;" /></td>
      <td><img src="/assets/images/AI_assisted_diagnose/外缘点转换结果.png" alt="外缘点转换结果" style="zoom:48%;" /></td>
      <td><img src="/assets/images/AI_assisted_diagnose/脊柱侧弯后处理-9520406.png" alt="脊柱侧弯后处理" style="zoom:60%;" /></td>
    </tr>
  </table>
  - <span class="span_anchor" id="train-maskrcnn">Train MaskRCNN segmentation model</span>
    - MaskRCNN is a two-stage instance segmentation framework based on RPN to filter the foreground and background, where the foreground refers to the valuable target of the image, and then classifies, locates, and segments the filtered foreground information.
    - The convolution method was replaced with deformable convolution
    - Use advanced HRNet as the backbone
    - output using CascadeRCNN
      <img src="/assets/images/AI_assisted_diagnose/MaskRCNN-9519528_en.png" alt="MaskRCNN" style="zoom:70%;margin:2em auto;" />{:.align-center}
  - <span class="span_anchor" id="post-processing">Post-processing</span>
    - The intervertebral angle is the angle between the superior border of the upper vertebral body and the inferior border of the lower vertebral body
    - Calculate the angle between each vertebra and all other vertebrae; the largest angle is the cobb angle
  - <span class="span_anchor" id="evaluation-of-results">Evaluation of results</span>
    - Found 97 scoliosis cases in 1000 test images; all of them are retained by doctors, 0 added, 100% recall rate, 0% false positive rate
    - Two hundred forty-eight images were selected and manually labeled by two doctors, with an average absolute error of 2.2 degrees between doctors and 3.32 degrees between the algorithm and the doctors.
  - <span class="span_anchor" id="results-show">Results Show</span>
    <img src="/assets/images/AI_assisted_diagnose/脊柱侧弯结果展示_en.png" alt="脊柱侧弯结果展示" style="zoom:50%;" />{:.align-center}

#### How is the pulmonary nodule determined?
  - Pulmonary nodule appears as round, white shadows on chest X-rays, usually between 5 mm and 30 mm in size, and may be a precursor to cancer.
  - Processing Flow
    - Cropped unilateral lung image --> FasterRCNN object detection --> crop out --> classification --> results
  - Training FasterRCNN object detection model
    - The overall architecture is basically the same as MaskRCNN
    - MobileNetV3 is used as the backbone, which requires less computing power and infers faster than HRNet
  <table>
    <tr>
      <th>Unilateral lung images</th>
      <th>Object detection results</th>
      <th>classification</th>
    </tr>
    <tr>
      <td><img src="/assets/images/AI_assisted_diagnose/单侧肺部图像.png" alt="单侧肺部图像" style="zoom:48%;" /></td>
      <td><img src="/assets/images/AI_assisted_diagnose/目标检测结果-9527352.png" alt="目标检测结果" style="zoom:48%;" /></td>
      <td><img src="/assets/images/AI_assisted_diagnose/切图后分类-9527670.png" alt="切图后分类" style="zoom:100%;" /></td>
    </tr>
  </table>

#### Why do we need to train a separate classification model?
  - <span class="span_anchor" id="question">Question</span>
    - It was found that the false positive rate of FasterRCNN was very high (>60%) when high recall (98%) was guaranteed, and the false positive rate only decreased slightly when trying to optimize the network structure or supplement the data.
  - <span class="span_anchor" id="conjecture">Conjecture</span>
    - There's a loss of information during convolution because of the limitation of the feature extraction network itself
    - There's a loss of information about the correlation with surroundings because FasterRCNN's classifier can only classify the recommended region limited by RPN
  - <span class="span_anchor" id="analysis">Analysis</span>
    - The object detection of an ordinary object which has distinctive features is not easily confused with other objects, and as an independent object, it is often distinct from the background, which leads to a partial loss of information in the convolution process and the loss of information about the surrounding association has little effect on the results
    - The determination process of pulmonary nodules is different from that of ordinary objects, and the partial loss of information during convolution and the loss of peripheral correlation information may cause it to be indistinguishable from other similar structures with too little difference, which leads to a consistent failure to reduce the false positive rate.
  - <span class="span_anchor" id="evidence">Evidence</span>
    - In determining pulmonary nodules, the consulting physician will not only observe the appearance of the suspicious area but also observe the texture of the target, the density, and the direction of the surrounding blood vessels and even combine the information with the patient's past cases and lifestyle.
  - <span class="span_anchor" id="solutions">Solutions</span>
    - Customized classification network, accepting multi-dimensional input, as a complement to FasterRCNN
    - Simulate the doctor's diagnosis method, extract geometric, textural, and contextual information of the suspected area, and put it into the model
    - FasterRCNN as "primary filtering", the classification model focuses on reducing the false positive rate
      <img src="/assets/images/AI_assisted_diagnose/肺结节分类模型_en.png" alt="肺结节分类模型" style="zoom:48%;" />{:.align-center}
  - <span class="span_anchor" id="evaluation-of-results_">Evaluation of results</span>
    - Found 162 suspected pulmonary nodules in 1000 test images, with 117 of them retained by doctors and four new ones added
    - 97% recall rate, 28% false positive rate, a significant decrease in false positive rate

------

### Notes

#### Deformable Convolutional Networks
  - Unlike traditional fixed-size convolution kernels, the size of the deformable filter changes according to the feature information.
  - Stronger ability to model the deformation and scale of objects
  - The perceptual field is much larger than normal convolution filters
  - More sensitive to the shape and size of the target
    <img src="/assets/images/AI_assisted_diagnose/可变形卷积-9526064.png" alt="可变形卷积" style="zoom:67%;" />{:.align-center}

#### HRNet
  - Unlike ResNet, which extracts features from high resolution to low resolution and low dimension to high latitude, HRNet can maintain high-resolution representation throughout the process. Specifically designed to improve the accuracy of segmentation
  - Considering that our X-ray image size is usually above 2000*2000, in addition to the input resize adjustment, the entire feature extractor maintains a high-resolution representation can improve the accuracy of segmentation
    <img src="/assets/images/AI_assisted_diagnose/HRNet.png" alt="HRNet" style="zoom:50%;" />{:.align-center}

#### MobileNet
  - By applying deep separable convolution, inverse residual structure, attention mechanism, and other optimizations, the computational effort of feature extraction is significantly reduced while ensuring accuracy, and the performance is good enough for simple targets (e.g., lung region) while lowering the GPU memory usage.
    <img src="/assets/images/AI_assisted_diagnose/MobileNet.png" alt="MobileNet" style="zoom:48%;" />{:.align-center}

#### CascadeRCNN
  - The trainer's performance is best when the threshold value of the proposal itself and the threshold value used for training the trainer are close to each other. The CascadeRCNN uses a 3-layer iterative box regression, which can improve the detection effect
    <img src="/assets/images/AI_assisted_diagnose/CascadeRCNN.png" alt="CascadeRCNN" style="zoom:48%;" />{:.align-center}
