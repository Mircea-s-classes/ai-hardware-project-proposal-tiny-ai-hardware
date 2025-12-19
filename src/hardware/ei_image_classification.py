import sensor, time, ml, uos, gc, pyb

sensor.reset()
# Using RGB565 to match the trained model input
#sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_pixformat(sensor.RGB565)
# Use QVGA (320x240) to get a wider field of view
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

# Initialize LEDs
red_led = pyb.LED(1)
green_led = pyb.LED(2)
blue_led = pyb.LED(3)

# Load the TFLite model
try:
    # Check memory and load the model file
    net = ml.Model("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024)))
    print('Model loaded successfully!')
except Exception as e:
    raise Exception('Failed to load model: ' + str(e))

# Load class labels
try:
    labels = [line.rstrip('\n') for line in open("labels.txt")]
    print('Labels:', labels)
except:
    pass

clock = time.clock()

while(True):
    clock.tick()

    img = sensor.snapshot()

    # Pre-process the image: Scaling (Squash method)
    # Instead of cropping the center, we scale the full 320x240 image down to 96x96.
    # This prevents the fingers from being cut off if the hand is not perfectly centered.
    # Scaling factors: 96/320 = 0.3, 96/240 = 0.4
    model_input = img.scale(x_scale=0.3, y_scale=0.4, copy=True)

    try:
        # Run inference on the scaled image
        res = net.predict([model_input])[0].flatten().tolist()
        predictions_list = list(zip(labels, res))

        # Sort predictions by confidence
        sorted_list = sorted(predictions_list, key=lambda x: x[1], reverse=True)
        best_label, best_prob = sorted_list[0]

        # Print results to terminal
        print("FPS:%.2f | Best: %s (%.2f)" % (clock.fps(), best_label, best_prob))

        # Update LED status based on the prediction
        # Only turn on LEDs if confidence is > 0.6
        if best_prob > 0.6:
            # Fist / Rock -> Red LED
            if "fist" in best_label or "rock" in best_label:
                red_led.on()
                green_led.off()
                blue_led.off()

            # Palm / Paper -> Green LED
            elif "palm" in best_label or "paper" in best_label:
                red_led.off()
                green_led.on()
                blue_led.off()

            # Pointing / Scissors -> Blue LED
            elif "pointing" in best_label or "scissors" in best_label:
                red_led.off()
                green_led.off()
                blue_led.on()

            else:
                # Turn off if label is unknown
                red_led.off()
                green_led.off()
                blue_led.off()
        else:
            # Turn off if confidence is too low
            red_led.off()
            green_led.off()
            blue_led.off()

    except Exception as e:
        print("Inference error:", e)
