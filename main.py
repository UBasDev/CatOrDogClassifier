from ultralytics import YOLO

# Load the fine-tuned model
model = YOLO('./runs/classify/train/weights/best.pt')  # Path to the best weights

# Predict
predictions = model.predict(source='./test_predict_images/cat.0.jpg')

# Process and display predictions
for pred in predictions:
    # Access class probabilities and names
    probs = pred.probs  # Probabilities object
    class_names = pred.names  # Dictionary of class names {index: name}

    # Get the class with the highest probability
    max_index = probs.top1  # Index of the highest probability class
    max_confidence = probs.data[max_index]  # Confidence of the top class
    max_class = class_names[max_index]  # Class name of the top prediction

    # Display the results
    print(f"Image: {pred.path}")
    print(f"Predicted Class: {max_class}")
    print(f"Confidence: {max_confidence:.2f}")
    print("Class Probabilities:")
    for idx, prob in enumerate(probs.data):
        print(f"  {class_names[idx]}: {prob:.2f}")