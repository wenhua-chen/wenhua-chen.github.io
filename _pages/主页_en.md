---
permalink: /en
other_lang_link: /
layout: single
author_profile: true
language: en
classes: wide
title: "Wenhua Chen"
excerpt: "I'm a senior algorithm engineer at Yeahka<br>
· My research interest lies in computer vision, including text/image/video understanding and processing<br>
· My project experience involves text recognition/recommendation, image classification/enhancement/object detection, video object tracking/action recognition/short video production, etc<br>
"
header:
  overlay_image: "/assets/images/2018-06-24 171224.JPG"
  overlay_filter: rgba(0, 0, 0, 0.5)
  caption: "Pic by Wenhua Chen"
  actions:
    - label: "More about me"
      url: "/en#recent-news"
---

<script type="text/javascript">
function do_change(){
  button = document.getElementById("showmore");
  content = document.getElementById("morecontent");
  if (content.style.display == "block") {
      content.style.display = "none";
      button.innerHTML = "More ▽";
    } else {
      content.style.display = "block";
      button.innerHTML = "More △";
    }
}
</script>

<h3 id="recent-news" class="section-title">Recent News</h3>

<!-- <div class="news-item">
  <span class="label label-green">11 / 2022</span> <span>[Honor] Awarded company‘s Semi-Annual Best Project - Image and Text Recommendation and AI-assisted Video Editing</span>
</div> -->
<div class="news-item">
  <span class="label label-green">09 / 2022</span> <span>[Patent] Get a patent for AI-assisted Video Editing</span>
</div>
<div class="news-item">
  <span class="label label-green">08 / 2022</span> <span>New project launched, introduction and demo coming soon - Image and Text Recommendation System</span>
</div>
<div class="news-item">
  <span class="label label-green">05 / 2022</span> <span>New project launched, introduction and demo coming soon - AI-assisted Video Editing</span>
</div>
<div class="news-item">
  <span class="label label-green">02 / 2022</span> <span>The project <a href="/projects/face-live-detection" target="_blank">introduction</a> and <a href="https://www.bilibili.com/video/BV1aa4y1f7Up" target="_blank">demo</a> is released - Face Live Detection</span>
</div>
<div class="news-item">
  <span class="label label-blue">12 / 2021</span> <span>[Personal Development] I've been promoted to Senior Algorithm Engineer</span>
</div>
<div class="news-item">
  <span class="label label-blue">11 / 2021</span> <span>[Honor] Awarded company‘s Monthly Best Project - Face Live Detection</span>
</div>
<div class="news-item">
  <span class="label label-blue">10 / 2021</span> <span>[Patent] Get a patent for Face Live Detection</span>
</div>

<div class="recent-news-more">
<button type="button" class="btn--inverse" id="showmore" onclick="do_change(); return false;">
More ▽</button>
</div>

<div id="morecontent" style="display:none;">
  <div class="news-item">
    <span class="label label-blue">09 / 2021</span> <span>Service stability and efficiency optimization - Face Live Detection</span>
  </div>
  <div class="news-item">
    <span class="label label-blue">08 / 2021</span> <span>Passed grayscale test and been deployed to all company apps, replacing the original third-party channel - Face Live Detection</span>
  </div>
  <div class="news-item">
    <span class="label label-blue">05 / 2021</span> <span>Achieved experimental accuracy of 99.65% and started the grayscale test - Face Live Detection</span>
  </div>
  <div class="news-item">
    <span class="label label-blue">02 / 2021</span> <span>The project <a href="/projects/pedestrian-tracking-behavior-recognition" target="_blank">introduction</a> and <a href="https://www.bilibili.com/video/BV1Za411d7tu" target="_blank">demo</a> is released - Pedestrian Tracking and Behavior Recognition</span>
  </div>

  <div class="news-item">
    <span class="label label-green">12 / 2020</span> <span>[Patent] Get a patent for Pedestrian Tracking and Behavior Recognition</span>
  </div>
  <div class="news-item">
    <span class="label label-green">11 / 2020</span> <span>[Honor] Awarded company‘s Monthly Best Project - Pedestrian Tracking and Behavior Recognition</span>
  </div>
  <div class="news-item">
    <span class="label label-green">10 / 2020</span> <span>The project has been deployed in the company's library - Pedestrian Tracking and Behavior Recognitionn</span>
  </div>
  <div class="news-item">
    <span class="label label-green">04 / 2020</span> <span>[Personal Development] I have joined <a href="https://www.yeahka.com/" target="_blank">Yeahka Technology Co., Ltd.</a></span>
  </div>

  <div class="news-item">
    <span class="label label-blue">12 / 2019</span> <span>The project <a href="/projects/ai-assisted-diagnose" target="_blank">introduction</a> is released, including <a href="/assets/images/AI_assisted_diagnose/软件展示.png" target="_blank">demo</a> and <a href="https://www.github.com/wenhua-chen/AI_Assisted_Diagnose/" target="_blank">codes</a> - AI-assisted diagnosis</span>
  </div>
  <div class="news-item">
    <span class="label label-blue">10 / 2019</span> <span>Passed the test at <a href="https://zh.wikipedia.org/wiki/%E4%B8%8A%E6%B5%B7%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6%E5%8C%BB%E5%AD%A6%E9%99%A2%E9%99%84%E5%B1%9E%E7%91%9E%E9%87%91%E5%8C%BB%E9%99%A2" target="_blank">Shanghai Ruijin Hospital</a> and delivered to doctors to use - AI-assisted diagnosis</span>
  </div>
</div>

<h3 id="projects" class="section-title">Projects</h3>

<h4 style="margin:0 0 1em;padding:0;"><div class="section-subtitle">2022</div></h4>

{% for post in site.projects_en %}
  {% if post.year == 2022 %}
    {% include project-single.html %}
  {% endif %}
{% endfor %}

<h4 style="margin:0 0 1em;padding:0;"><div class="section-subtitle">2021</div></h4>

{% for post in site.projects_en %}
  {% if post.year == 2021 %}
    {% include project-single.html %}
  {% endif %}
{% endfor %}

<h4 style="margin:0 0 1em;padding:0;"><div class="section-subtitle">2020</div></h4>

{% for post in site.projects_en %}
  {% if post.year == 2020 %}
    {% include project-single.html %}
  {% endif %}
{% endfor %}