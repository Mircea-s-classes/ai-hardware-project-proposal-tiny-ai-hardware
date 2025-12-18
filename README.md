[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/v3c0XywZ)
# AI Hardware Project Template
ECE 4332 / ECE 6332 — AI Hardware  
Fall 2025

Introduction and Motivation
Hand-gesture recognition enables intuitive, touch-free interaction with embedded systems and has become increasingly viable due to advances in lightweight neural networks and edge-focused machine learning platforms. By allowing users to communicate with hardware through natural hand movements, gesture-based interfaces reduce reliance on traditional input devices such as keyboards, buttons, or touchscreens. This is particularly valuable in embedded and resource-constrained environments, where simplicity, responsiveness, and reliability are critical. As a result, gesture recognition has growing relevance in applications such as human–computer interaction, accessibility systems, robotics, and Internet of Things devices.
Performing gesture recognition directly on embedded hardware further strengthens these benefits by eliminating dependence on cloud computation. On-device inference reduces latency, lowers power consumption, and avoids privacy concerns associated with transmitting image data off the device. This project is motivated by the goal of demonstrating that deep learning–based vision models can operate effectively on low-resource microcontrollers. By implementing an end-to-end, fully embedded gesture recognition pipeline, the work highlights the practicality of deploying intelligent, responsive, and privacy-preserving systems at the edge.

Project Overview
The goal of this project is to implement a hand-gesture recognition system using embedded hardware capable of real-time inference. The system is designed to recognize three distincy hand gestures, fist, palm, and point, and provide immediate hardware feedback. The goal is to have >90% accuracy on our training dataset and >85% accuracy on real-time gesture recognition. 

Related work
	Prior work demonstrates the feasibility and tradeoffs of embedded vision systems. Edge Impulse–based studies show that MobileNetV2 achieves strong accuracy for hand posture recognition at the cost of increased memory usage[2]. Other approaches rely on classical computer vision and rule-based geometry for live gesture recognition, avoiding neural networks but limiting scalability[3]. Research on the OpenMV Cam H7 highlights both the potential and the computational limits of deploying CNNs on low-specification embedded hardware[1]. These works motivate the design choices and constraints considered in this project.

Methodology
TBD

Results
TBD
Future Work
Future improvements to this system include expanding the gesture set beyond three classes to support more expressive interaction. Incorporating temporal or video-based analysis instead of single-image classification could improve stability and reduce misclassification between similar gestures. The system could also be extended to detect and classify multiple gestures simultaneously. Finally, additional work is needed to improve robustness under varying lighting conditions, complex backgrounds, and different hand orientations, which would make the system more reliable in real-world deployment scenarios.

Conclusion
TBD

Bibliography
[1] Asmara, R.A. et al. 2024. An Experimental Study on Deep Learning Technique Implemented on Low Specification OpenMV Cam H7 Device. JOIV : International Journal on Informatics Visualization. 8, 2 (May 2024), 1017–1029. https://doi.org/10.62527/joiv.8.2.2299.
[2] Gui, Y. 2024. Edge impulse-based convolutional neural network for Hand Posture Recognition. Applied and Computational Engineering. 40, (Jan. 2024), 115–119. https://doi.org/10.54254/2755-2721/40/20230636.
[3] Saporiti, N. et al. 2025. Implementing an AI-Driven Gesture Recognition System in MES for Enhanced Efficiency and Human-Centric Operations in Industry 5.0. IFAC-PapersOnLine. 59, 10 (Jan. 2025), 1660–1665. https://doi.org/10.1016/j.ifacol.2025.09.279.
<img width="6218" height="277" alt="image" src="https://github.com/user-attachments/assets/3aa9a9e0-0c02-4e0c-b6db-e8b11e591fcd" />


## 🧭 Overview
This repository provides a structured template for your team project in the AI Hardware class.  
Each team will **clone this template** to start their own project repository.

## 🗂 Folder Structure
- `docs/` – project proposal and documentation  
- `presentations/` – midterm and final presentation slides  
- `report/` – final written report (IEEE LaTeX and DOCX versions included)  
- `src/` – source code for software, hardware, and experiments  
- `data/` – datasets or pointers to data used

## 🧑‍🤝‍🧑 Team Setup
Each team should have **2–4 members (3 preferred)**.  
List all team members in `docs/Project_Proposal.md`.

## 📋 Required Deliverables
1. **Project Proposal** — due Nov. 5, 2025, 11:59 PM  
2. **Midterm Presentation** — Nov. 19,2025, 11:59 PM  
3. **Final Presentation and Report** — Dec. 17, 11:59 PM

## 🚀 How to Use This Template
1. Click **“Use this template”** on GitHub.  
2. Name your repo `ai-hardware-teamXX` (replace XX with your team name or number).  
3. Clone it locally:
   ```bash
   git clone https://github.com/YOUR-ORG/ai-hardware-teamXX.git
   ```
4. Add your work in the appropriate folders.

## 🧾 Submissions
- Commit and push all deliverables before each deadline.
- Tag final submissions with:
   ```bash
   git tag v1.0-final
   git push origin v1.0-final
   ```

## 📜 License
This project is released under the MIT License.
