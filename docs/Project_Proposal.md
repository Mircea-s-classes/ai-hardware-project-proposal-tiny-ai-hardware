# University of Virginia
## Department of Electrical and Computer Engineering

**Course:** ECE 4332 / ECE 6332 — AI Hardware Design and Implementation  
**Semester:** Fall 2025  
**Proposal Deadline:** November 5, 2025 — 11:59 PM  
**Submission:** Upload to Canvas (PDF) and to GitHub (`/docs` folder)

---

# AI Hardware Project Proposal Template

## 1. Project Title
Tiny AI Hardware

Yi Deng(edh4su)

Hand Gesture Recognition on an Embedded Vision System

## 2. Platform Selection

Tiny AI platform: OpenMV H7

## 3. Problem Definition
Gesture-based human interaction is becoming increasingly important in devices that must operate hands-free or in situations where microphones are not ideal. Running vision-based gesture recognition normally requires GPUs or powerful processors, but those systems consume more energy and rely on network connectivity.

This project explores how a small embedded processor can recognize a few common hand gestures using minimal compute and memory. The main focus is to examine how well a microcontroller-class device can perform useful AI-based perception under strict hardware constraints.

## 4. Technical Objectives
The project is expected to accomplish the following measurable goals:
1. Recognize at least three gestures (e.g., open palm, closed fist, pointing).
2. Maintain real-time responsiveness with ≥10 FPS on the OpenMV H7.
3. Keep model size small enough to run on the board’s memory (<500 KB after quantization).
4. Demonstrate reliable classification with ≥85% test accuracy.

## 5. Methodology
The development plan includes:
1. Hardware Setup: OpenMV H7 MCU with built-in image sensor.
2. Model Training: Data collection and model generation using Edge Impulse; quantized neural network optimized for TFLite Micro.
3. Deployment & Integration: Convert the trained model for MCU deployment and run inference through OpenMV IDE.
4. Performance Evaluation: Measure latency, frame rate, memory usage, and classification accuracy using real-world tests under different lighting conditions.
5. Validation: Demonstrate live interaction where detected gestures control local outputs (e.g., LED behavior).
   
The work will focus on balancing model complexity with the processing capabilities of the microcontroller.

## 6. Expected Deliverables
working demo, GitHub repository, documentation, presentation slides, and final report.

## 7. Team Responsibilities
List each member’s main role.

| Name | Role | Responsibilities |
|------|------|------------------|
| Yi Deng | Full contributor | documentation, Setup, Model training, inference, Testing, benchmarking |

## 8. Timeline and Milestones
Provide expected milestones:

| Week | Milestone | Deliverable |
|------|------------|-------------|
| 2 | Proposal | PDF + GitHub submission |
| 4 | Midterm presentation | Slides, preliminary results |
| 6 | System integration | Working prototype |
| Dec. 18 | Final presentation | Report, demo, GitHub archive |

## 9. Resources Required
OpenMV H7 development board
Edge Impulse training platform
Standard computer for model development
LED / buzzer for output demonstration

## 10. References
OpenMV H7 documentation: https://docs.openmv.io/
Relevant TinyML embedded vision research publications
