from ultralytics import YOLO

# Load the pretrained YOLOv11n-cls model
model = YOLO("yolo11n-cls.pt")

# Train the model
model.train(
    data="dataset",  # Path to dataset
    epochs=20,       # Adjust epochs based on requirements
    imgsz=224,       # Input image size
    batch=64,        # Batch size
)