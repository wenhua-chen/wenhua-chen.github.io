---
permalink: /projects/face-live-detection
other_lang_link: /projects/活体检测
layout: single
author_profile: false
language: en
classes: wide
title: "Face Live Detection"
year: 2022
intro: "Determine whether the face in the image is a real person, and block fake face attacks such as masks/screens"
info: "face_anti_spoof_en"
english: true
excerpt: "
· A service to determine whether a face in an image is a real person (live body)<br>
· Often performed in conjunction with Face Recognition in some highly regulated operations<br>
· The criminal industry often uses fake faces (non-live) to try to pass the verification"
header:
  teaser: /assets/images/face_anti_spoof_headimg.jpg
  overlay_image: /assets/images/face_anti_spoof_headimg.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
  caption: "Pic by Wenhua Chen"
  actions:
    - label: "Learn more"
      url: "/projects/face-live-detection#background-and-purpose"
sidebar:
  nav: "face_anti_spoof_en"
---

### Background and Purpose

#### What is Face Live Detection?
  - Face Live Detection is a service for judging whether a face in an image is a real person (living body)
  - In some strictly regulated businesses, we need to verify whether the operator is a real person, so in addition to Face Recognition, we often need to perform a "whether it is a real person (live)" judgment, that is, Face Live Detection
  - The criminal industry often uses fake faces (non-live) to try to pass the verification, some examples of non-live attacks
    <table>
      <tr> 
        <th>Screen</th>
        <th>Photo</th>
        <th>Cutting paper</th>
        <th>Mask</th>
      </tr>
      <tr> 
        <td><img src="/assets/images/face_anti_spoof/0_0_05580_7_002_scene.jpg" alt="0_0_05580_7_001_scene" style="zoom:20%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/0_3_00476_2_001_scene.jpg" alt="0_3_00476_2_001_scene" style="zoom:50%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/0_2_04449_6_001_scene.jpg" alt="0_2_04449_6_001_scene" style="zoom:50%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/0_5_10149_11_001_scene.jpg" alt="0_5_10149_11_001_scene" style="zoom:50%;" /></td>
      </tr>
    </table>

#### Why do we need a self-developed Face Live Detection Service?
  - Many of the company's services require real-name authentication and personal operation, the daily business volume is enormous, and the demand for business expansion continues to grow.
  - In the past, we used Face Live Detection interfaces provided by third-party companies like Tencent or SenseTime, which cost a lot every year
  - Advantages of self-developed Face Live Detection Service
    - Complete or partial replacement of third-party interfaces, resulting in cost savings
    - Join the SaaS platform built by the company and provide services to other companies, which can bring income as well

------
### Achievements

#### Has the product been launched successfully?
  - Yes, it's a successful product and goes as expected
  - It has been embedded in all our company's Apps and works as the primary channel now, which satisfies over 80% of the total requests
  - It has also joined the Yeahka AI cloud platform and provides service to other companies
  - Demo Video
    {% include video id="BV1aa4y1f7Up" provider="bilibili" %}

#### What awards/achievements has it received?
  - Company's Best Project of the Month
  - Patent: "False Face Detection Method, Terminal Device and Computer Readable Storage Media
      - First author
      - Patent publication number: CN113297960A

------
### Overview of The Process

#### What is the process of Face Live Detection?
  - As shown in the figure, there are three steps: **Face quality detection, Action live detection, and Silent live detection**, which is conducted on the mobile side and server side respectively.
    <img src="/assets/images/face_anti_spoof/WechatIMG619_en.drawio.png" alt="WechatIMG619" style="zoom:30%;" />{:.align-center}
  - Flow Chart
        <img src="/assets/images/face_anti_spoof/SDK内部逻辑图_en.drawio.png" alt="SDK内部逻辑图.drawio.png" style="zoom:80%;" />{:.align-center}

#### What do Face quality, Action live, and Silent live detection mean?
  - Face quality detection: Make sure the image is not shaking, faces are present, and the lighting is normal
  - Action live detection: Specify random actions such as mouth opening, eye blinking, and head turning. If the user completes the actions correctly, detection is passed; otherwise, they will be blocked
  - Silent live detection: Detect the material in the picture and whether there are moiré, distortion, screen borders, or other attack features
    <table>
      <tr> 
        <th>Face quality(❌)</th>
        <th>Face quality(❌)</th>
        <th>mouth opening(❌)</th>
        <th>Silent live detect(❌)</th>
        <th>Silent live detect(✅)</th>
      </tr>
      <tr> 
        <td><img src="/assets/images/face_anti_spoof/WechatIMG631.jpeg" alt="WechatIMG631" style="zoom:19%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/0_0_00041_1_000_scene.jpg" alt="0_0_00041_1_000_scene" style="zoom:50%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/0_0_00008_2_000_scene.jpg" alt="0_0_00008_2_000_scene" style="zoom:30%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/0_0_00008_2_002_scene.jpg" alt="0_0_00008_2_001_scene" style="zoom:32%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/0_0_00008_1_001_scene-7006664.jpg" alt="0_0_00008_1_001_scene" style="zoom:50%;" /></td>
      </tr>
    </table>

#### Why is silent live detection conducted on the server side?
  - Small models do not perform well in identifying attack features such as moire or deformation, and large models are required.
  - Large models require high computing power and cannot be deployed on the mobile side

#### Why are there three steps, not one?
  - First step: Face quality detection
    - Ensure that the image illumination is normal and there is no jitter, eliminate abnormal situations and improve subsequent algorithm accuracy
  - Second step: Action live detection
    - By specifying random face actions, most attacks (such as masks with unchanged face action) can be filtered out on the mobile side, which can reduce the pressure on the server side

------

### Challenges - Server Side

#### How was the Action LiveDetect solution determined?

- <span class="span_anchor" id="technology-research">Technology research</span>
  - Evaluation metrics: FRR (False Reject Rate), FAR (False Accept Rate) and HTER
  - Traditional solutions
    - Color texture (best result in the traditional solutions): 2~3%HTER, 
    - Other traditional solutions are usually 14~20%HTER
  - Deep learning solutions
    - CVPR2019、2020: 1~2%HTER
    - The best one before 2021 is proposed by Tencent: 1.24%HTER
  - The impact of datasets distribution differences
    - Through the paper, it is found that the existing cutting-edge models can achieve good results for the same distribution of training tests, and the difference in HTER is not significant.
    - But if the trainset and testset distribution difference is large, it has a significant impact
    - The test results of the worse model, trained on the good data set, far exceed the test results of the better model trained on the bad data set
      <table>
        <tr> 
          <td><img src="/assets/images/face_anti_spoof/Table 6. The results of cross-database testing between CASIA-.png" alt="Table 6. The results of cross-database testing between CASIA-" style="zoom:50%;" /></td>
          <td><img src="/assets/images/face_anti_spoof/Table S FAR indicator cross-tested on public dataset. Here O.png" alt="Table S FAR indicator cross-tested on public dataset. Here O" style="zoom:50%;" /></td>
          <td><img src="/assets/images/face_anti_spoof/Model.png" alt="Model" style="zoom:50%;" /></td>         
        </tr>
      </table>
- <span class="span_anchor" id="experiments">Experiments</span>
    - Try multiple projects, including [FaceBagNet@CVPR19-2nd](https://openaccess.thecvf.com/content_CVPRW_2019/papers/CFS/Shen_FaceBagNet_Bag-Of-Local-Features_Model_for_Multi-Modal_Face_Anti-Spoofing_CVPRW_2019_paper.pdf)、[CDCN@CVPR20-1st,](https://arxiv.org/abs/2003.04092) and [SGTD@CVPR20-2nd; some drawbacks are summarized below
      - the result is not good enough
      - Continuous frames are required; this is infeasible for real-time processing due to bandwidth limitations
      - Depth label is required, which is not easy to obtain. If generate the depth label with PRNet, the inference speed does not meet the real-time requirement
      - Even without generating the depth label, the infer speed is still too slow to meet real-time requirements due to extensive calculation
      - The distribution of the dataset used in the paper is too homogeneous, and the trained model does not perform well in our real dataset (HTER>20%)
      - Works well for 2D fraud problems, but not for 3D masks
    - [MiniFASNet@MiniVision](https://github.com/wenhua-chen/Silent-Face-Anti-Spoofing)
      - Good test result, best performance among all models, cross-dataset result ~10% HTER
        <img src="/assets/images/face_anti_spoof/Pasted Graphic 46.jpg" alt="Pasted Graphic 43" style="zoom:50%;" />{:.align-center}

#### How to make the result better?
  - <span class="span_anchor" id="optimize-from-data">Optimize from data</span>
    - Open-source dataset: including [CASIA_FASD](https://paperswithcode.com/dataset/casia-fasd), [Oulu_npu](https://sites.google.com/site/oulunpudatabase/), [LCC,](https://csit.am/2019/proceedings/PRIP/PRIP3.pdf) and six other open-source datasets, more than 1.5 million images in total
    - Self-made dataset: Yeahka_FAS(private), more than 1.9 million images
    - Cross-distributed datasets
      - Examples of real-face dataset distribution
        <table>
          <tr> 
            <th>Normal</th>
            <th>Too bright</th>
            <th>Too dark</th>
            <th>Backlight</th>
            <th>Fuzzy</th>
          </tr>
          <tr> 
            <td><img src="/assets/images/face_anti_spoof/0_0_00008_1_000_scene.jpg" alt="0_0_00008_1_000_scene" style="zoom:50%;" /></td>
            <td><img src="/assets/images/face_anti_spoof/Pasted Graphic 26.png" alt="Pasted Graphic 26" style="zoom:50%;" /></td>
            <td><img src="/assets/images/face_anti_spoof/0_0_00041_1_000_scene.jpg" alt="0_0_00041_1_000_scene" style="zoom:50%;" /></td>
            <td><img src="/assets/images/face_anti_spoof/0_0_00009_1_000_scene.jpg" alt="0_0_00009_1_000_scene" style="zoom:50%;" /></td>
            <td><img src="/assets/images/face_anti_spoof/0_0_00030_1_001_scene.jpg" alt="0_0_00030_1_001_scene" style="zoom:50%;" /></td>
          </tr>
        </table>
      - Examples of fake-face dataset distribution
        <table>
          <tr> 
            <th>Moore grain</th>
            <th>Screen reflection</th>
            <th>Screen material</th>
            <th>Screen exposure distortion</th>
          </tr>
          <tr> 
            <td><img src="/assets/images/face_anti_spoof/0_0_01708_3_000_scene.jpg" alt="0_0_01708_3_000_scene" style="zoom:50%;" /></td>
            <td><img src="/assets/images/face_anti_spoof/0_0_05580_7_001_scene.jpg" alt="0_0_05580_7_001_scene" style="zoom:50%;" /></td>
            <td><img src="/assets/images/face_anti_spoof/0_0_07465_9_000_scene.jpg" alt="0_0_07465_9_000_scene" style="zoom:50%;" /></td>
            <td><img src="/assets/images/face_anti_spoof/0_0_07469_9_000_scene.jpg" alt="0_0_07469_9_000_scene" style="zoom:50%;" /></td>
          </tr>
        </table>
        <table>
          <tr> 
            <th>Photos</th>
            <th>Cut paper</th>
            <th>Mask</th>
            <th>3D mask</th>
          </tr>
          <tr> 
            <td><img src="/assets/images/face_anti_spoof/0_3_00476_2_001_scene.jpg" alt="0_3_00476_2_001_scene" style="zoom:50%;" /></td>
            <td><img src="/assets/images/face_anti_spoof/0_2_04449_6_001_scene.jpg" alt="0_2_04449_6_001_scene" style="zoom:50%;" /></td>
            <td><img src="/assets/images/face_anti_spoof/Pasted Graphic 37.jpg" alt="Pasted Graphic 34" style="zoom:50%;" /></td>
            <td><img src="/assets/images/face_anti_spoof/0_5_10149_11_001_scene.jpg" alt="0_5_10149_11_001_scene" style="zoom:50%;" /></td>
          </tr>
        </table>
    - Model weakness analysis and creating dataset aimed at those weaknesses
      <img src="/assets/images/face_anti_spoof/Pasted Graphic 47.png" alt="Pasted Graphic 47" style="zoom:100%;" />{:.align-center}
  - <span class="span_anchor" id="voting-mechanism">Voting mechanism</span>
    - Co-voting of models at multiple scales
      <table>
        <tr>
          <th>Scale1.0(full face) model</th>
          <th>Scale1.5(close shot) model</th>
          <th>Scale2.7(long shot) model</th>
        </tr>
        <tr>
          <td>Focus on facial details</td>
          <td>Focus on the transition between the face and the background</td>
          <td>Focus on details like background, edges, etc</td>
        </tr>
        <tr>
          <td><img src="/assets/images/face_anti_spoof/0_0_01708_3_001_scene.jpg" alt="0_0_01708_3_001_scene" style="zoom:30%;" /></td>
          <td><img src="/assets/images/face_anti_spoof/0_2_04449_6_002_scene.jpg" alt="0_2_04449_6_002_scene" style="zoom:50%;" /></td>
          <td><img src="/assets/images/face_anti_spoof/0_0_01708_3_002_scene.jpg" alt="0_0_01708_3_002_scene" style="zoom:10%;" /></td>
        </tr>
      </table>
    - Voting on multiple frames
      - Random actions like mouth opening and eye blinking can increase the difficulty
      - The movement may cause the fake face to move or deflect, thus revealing a flaw
  - <span class="span_anchor" id="introduction-of-third-party-channels">Introduction of third-party channels</span>
    - Raise the threshold of the Yeahka channel to 0.99: FAR<0.01%, FRR~10%
    - Results that Yeahka channel determines to be fake face are then sent to a third-party channel and returned with its result
      <img src="/assets/images/face_anti_spoof/请求通道逻辑_en.drawio.png" alt="请求通道逻辑.drawio" style="zoom:35%;" />{:.align-center}
  - <span class="span_anchor" id="final-result">Final result</span>
    - Test 1000 images with fake faces, all of them were blocked, so the False Accept Rate is FAR=0%
    - Test 16,000 images with real faces, and the False Reject Rate is FRR=0.7%, which is better than the third-party channel, as the figure shows below
    - The requests for third-party channels decreased by 86.3%, which means 86.3 of every 100 requests can be satisfied by ourselves, and only the rest 13.7 requests need to request a third-party channel
      <table>
        <tr>
          <th>FRR(%)</th>
          <th>Demands satisfied by Yeahka channel(%)</th>
        </tr>
        <tr>
          <td><img src="/assets/images/face_anti_spoof/image-20220628160904660.png" alt="image-20220628160904660" style="zoom:50%;" /></td>
          <td><img src="/assets/images/face_anti_spoof/image-20220628160931964.png" alt="image-20220628160931964" style="zoom:50%;" /></td>
        </tr>
      </table>

#### How to improve service stability?
  - <span class="span_anchor" id="module-replacement">Module replacement</span>
    - Replacement between Scale1.0+Scale1.5 and Scale2.7 model
      - If the face is too close for the Scale2.7 model to work, the Scale1.0+Scale1.5 model can also return results, and vice versa
    - Replacement between the Yeahka channel and third-party channels
      - If the Yeahka channel model fails, all requests will be forwarded to a third-party channel and return with its result
  - <span class="span_anchor" id="load-balancing-and-disaster-recovery-system">Load balancing and disaster recovery system</span>
    - Multiple systems are deployed on different backend servers; the middle controller controls the forwarding of requests and evenly forwards them to different servers
    - If a server returns an error/timeout, the middle controller will take it offline until the problem is fixed
    - If multiple servers return an error/timeout, the middle controller will close the service and forwards all requests to a third-party channel
  - <span class="span_anchor" id="monitoring">Monitoring</span>
    - use supervisor service to monitor all processes of Yeahka channel and automatically restarts the process when it fails
    - Regularly scan logs and send warning messages if found any module/system/service exception occurs
    - Periodic request the interface; if the returned result is different from what is expected, a warning message will be sent
      <img src="/assets/images/face_anti_spoof/服务器稳定性_en.drawio.png" alt="服务器稳定性.drawio" style="zoom:25%;"/>{:.align-center}

#### How to increase the concurrency of the service?
  - Use gunicorn service to launch multiple processes, accepts requests concurrently, and evenly distributes CPU, GPU computing power and I/O
  - Establish a TCP long connection between the middle controller and the backend server to transmit data, which can avoid repeated handshakes
  - Cache the data and write once when needed, avoid repeated IO operations
  - Locking mechanism to ensure the atomicity of operations when writing logs for multiple processes
  - Avoid unnecessary calculations to optimize the speed

------

### Challenges - Mobile Side

#### How was the Action Live Detection solution determined?
- <span class="span_anchor" id="classification-model">Classify actions with classification model</span>
  - drawbacks
    - Adding more actions or subtracting actions requires retraining of the model
    - The face differences cause the model prone to misidentify
- <span class="span_anchor" id="mapping-from-2d-to-3d">Mapping from 2D to 3D, using 2D key points to restore their 3D coordinates to determine the action</span>
  - Works well, correct orientation
  - But it needs a large number of key points and is computationally intensive
  - Reducing the number of key points will decrease the accuracy
    <img src="/assets/images/face_anti_spoof/2d_to_3d_compare.gif" alt="2d_to_3d_compare" style="zoom:50%;" />{:.align-center}
- <span class="span_anchor" id="the-relative-position-of-key-points">Guessing that the relative pos</span>ition of key points can infer the action
  - Use the dlib package and find 68 face key points to verify the conjecture
  - Found that nine face key points are enough for face action determination and give the code
    <table>
      <tr>
        <th>Turn left</th>
        <th>Turn right</th>
        <th>bow</th>
        <th>Open mouth</th>
      </tr>
      <tr>
        <td><img src="/assets/images/face_anti_spoof/037.jpg" alt="037" style="zoom:50%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/240.jpg" alt="240" style="zoom:50%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/296.jpg" alt="296" style="zoom:50%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/346.jpg" alt="346" style="zoom:50%;" /></td>
      </tr>
    </table>

#### Any innovations in the algorithm?
  - <span class="span_anchor" id="multi-step-merging">Multi-step merging</span>
    - Steps include face bbox determination, face key points determination, and whether the eyes closed
    - Multiple steps are completed once using one model, which significantly reduces the inference time
  - <span class="span_anchor" id="reduce-unnecessary-calculations">Reduce unnecessary calculations</span>
    - Discard smaller-face candidates while raising the thresholds of the three stages of MTCNN
    - This step can discard those candidate frames with low probability and reduce the computational effort
  - <span class="span_anchor" id="exclusion-of-individual-differences">Exclusion of individual differences</span>
    - Multi-frame averaging to improve the accuracy of action recognition and reduce the false accepted  rate
    - Calculate the average static face, and determine the action by comparing it with the motionless face instead of determining the action directly from the threshold
  - <span class="span_anchor" id="targeted-improvements">Targeted improvements</span>
    - Dark light, shake, and out-of-focus can affect the location of key points and thus affect the judgment of silent live detect model
    - Propose the face quality detection step, which filters first to ensure that the picture is clear and bright

#### What is the structure of the mobile side?
  - APP ---> SDK ---> .so dynamic library
  - The APP can directly launch the SDK for face live detection, and the SDK will return whether the face is real or not
  - The overall process is packed in the SDK, including UI interface, camera call and release, interaction with so dynamic library, interaction with the server, etc.
  - The ".so" dynamic library packs all models and logic codes for face quality and face action detection algorithm, it interacts with outside through a fixed interface
    <img src="/assets/images/face_anti_spoof/移动端调用逻辑_en.drawio-6923315.png" alt="移动端调用逻辑.drawio" style="zoom:25%;" />{:.align-center}

#### Why is the mobile side structure designed this way?
  - The SDK adopts a modular design to package the overall process of face live detection, which is easy to embed in other Apps, also convenient for subsequent upgrades and maintenance
  - The ".so" dynamic library is written in C++ so that Android can interact with it through JNI, and IOS can directly call it. The advantages are as follows
    - Compatible with both Android and IOS systems; no need to repeat development
    - Convenient for subsequent upgrades and maintenance in Apps, which only need to change the ".so" dynamic library
    - Processing is fast

#### What engineering optimizations have been made?
  - <span class="span_anchor" id="memory-management">Memory management</span>
    - Use a fixed number threads pool with independent threads to analyze each frame collected; if all threads are in processing, subsequent frames will be discarded until there is a free thread
    - Symmetric mapping for JNI in Android
      - The Java layer object retains the pointer of the same name object in the C++ layer so that the java object can directly operate the C++ object through the pointer
      - The mapping above replaces redundant copy actions during JNI interaction to speed up the processing
      - The mapping can also be used to destroy the corresponding C++ object when the java object is recycled through  Java Garbage Collection Mechanism, which is convenient for memory management
  - <span class="span_anchor" id="file-size-optimization">File size optimization</span>
    - Rewrite the underlying logic of OpenCV used in image jitter detection so the ".so" library is not dependent on the "OpenCV.so" library anymore, and the SDK size is reduced
  - <span class="span_anchor" id="speed-optimization">Speed optimization</span>
    - Multi-threading for frame analysis in the java layer
    - In the C++ layer, it also enables multi-threading to do forward inference using the ncnn library
  - <span class="span_anchor" id="interaction-optimization">Interaction optimization</span>
    - Model iteration to improve accuracy
    - Modified the user prompt logic, making the interaction more reasonable

------

### Notes

#### ColorTexture
  - Living and non-living faces are difficult to distinguish in RGB space, but there is a clear difference in texture in other color spaces
  - Using face multi-level LBP feature in HSV space and the LPQ feature in YCbCr space, draw the histograms of each channel, send the concated result to SVM for classification
    <img src="/assets/images/face_anti_spoof/v2-fc257d3fdfaa437b6320667ba3ee0c6d_r.jpg" alt="preview" style="zoom:50%;" />{:.align-center}

#### FaceBagNet
  - Train a CNN network with randomly clipped face regions instead of full faces
  - Randomly remove features from a modality during training to enhance generalization
  - The structure of the backbone for extracting features mainly refers to ResNext
    <img src="/assets/images/face_anti_spoof/image-20220706121144275.png" alt="image-20220706121144275" style="zoom:50%;" />{:.align-center}

#### CDCN
  - Propose the central differential convolution (CDC). The ordinary convolution is very easy to be affected by the illumination or input distribution difference; after using the CDC, the CNN can better capture the essential characteristics of spoofing and is not easily affected by the external environment.
  - Introducing NAS to solve the FAS problem
    <img src="/assets/images/face_anti_spoof/image-20220706123054227.png" alt="image-20220706123054227" style="zoom:30%;" />{:.align-center}

#### SGTD
  - To better characterize the spatial information, a Residual Spatial Gradient Block (RSGB) based on spatial gradient magnitude is proposed.
  - To better characterize the temporal information, the Spatio-Temporal Propagation Module (STPM) is proposed.
  - To make CNN better learn the detailed spoofing patterns, a fine-grained supervision loss is proposed: Contrastive Depth Loss (CDL)
    <table>
      <tr>
        <th>RSGB</th>
        <th>STPM</th>
        <th>CDL</th>
      </tr>
      <tr>
        <td><img src="/assets/images/face_anti_spoof/1620.png" alt="img" style="zoom:100%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/1620-20220706125453771.png" alt="img" style="zoom:100%;" /></td>
        <td><img src="/assets/images/face_anti_spoof/1620-20220706125508504.png" alt="img" style="zoom:100%;" /></td>
      </tr>
    </table>

#### MiniFASNet
  - Fourier spectrogram-assisted supervised detection method based on a model architecture consisting of a main classification branch and a Fourier spectrogram-assisted supervised branch
  - [Video introduction](https://www.bilibili.com/video/BV1qZ4y1T7CH?vd_source=623f811f8bdde7871d2c769fe02b4690)
    <img src="/assets/images/face_anti_spoof/framework.jpg" alt="framework.jpg" style="zoom:100%;" />{:.align-center}
