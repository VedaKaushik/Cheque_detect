from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")

# Use of model

results = model.train(data='config.yaml', epochs=100) # train the model



