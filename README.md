<h2>
How to make prediction for random dog and cat images if it is a dog or a cat?
</h2>
<p>
1- First grab the absolute path of the image that you are going to use for prediction and go to "main.py" file and modify this line:
<code>
predictions = model.predict(source=r'{absolute_path_to_your_image}')
</code>
</p>
<p>
2- Open command line and write "python -m venv .venv". We are going to use virtual environment for dependencies.
</p>
<p>
3- Then write ".venv\scripts\activate" to activate virtual environment we've created.
</p>
<p>
4- Then write "pip install -r requirements.txt" to install project dependencies.
</p>
<p>
5- Then write "python main.py" to make prediction. You are going to receive an output similar to this:
</p>
<code>
image 1/1 SOME_PATH_TO_YOUR_PREDICTION_IMAGE: 224x224 cat 1.00, dog 0.00, 32.2ms
Speed: 16.6ms preprocess, 32.2ms inference, 0.8ms postprocess per image at shape (1, 3, 224, 224)
Image: SOME_PATH_TO_YOUR_PREDICTION_IMAGE
Predicted Class: cat
Confidence: 1.00
Class Probabilities:
  cat: 1.00
  dog: 0.00
</code>
<hr>
<h2>
How to keep fine tuning this model to improve accuracy and performance of results?
</h2>
<p>
By default, i set the weight path for best weight I generated so far. So when you make prediction, it is going to use my best generated weight but to improve this, follow these steps:
</p>
<p>
1- Go to "train.py" file and change it to this:
</p>
<code>
# Load our generated last weight
model = YOLO(./runs/classify/train/weights/last.pt) # Here we set it to last weight because it contains weight from the final completed training epoch and all training process, including any additional patterns learned. This is the latest state of this model.

# Train the model
model.train(
    data="dataset",  # Path to dataset
    epochs=20,       # Adjust epochs based on requirements
    imgsz=224,       # Input image size
    batch=64,        # Batch size
    name="new_run1",
    exist_ok= True
)
</code>
<p>
2- Go to "https://www.microsoft.com/en-us/download/details.aspx?id=54765" link and download the dataset. It contains 12.5k dog and 12.5k cat images. Pick first 10k dog images starting from 0.jpg and move them into "dataset/train/dog/" folder; then pick first 10k cat images and move them into "dataset/train/cat/" folder. Then pick the rest 2.5k dog images and move them into "dataset/val/dog/" folder; then pick the rest 2.5k cat images and move them into "dataset/val/cat/" folder.
</p>
<p>
3- Now as you can see, inside of "dataset/val/cat" and "dataset/val/dog" folders, file indexes are not starting from 0.jpg because we copies them from the end of dataset. To make them start from 0 index, open command line and run "python rename.py". This is going to enumerate all files under these folders and rename them by starting index 0.
</p>
<p>
4- Then run "python train.py". We set epoch to 20 so it might take few hours depending on your system requirements. We can wait.
</p>
<p>
5- After the training is done, find "new_run1" folder in project directory which is generated after training. Check its subfolders and locate "weights/best.pt" and copy its absolute path.
</p>
<p>
6- Go to "main.py" file and modify this line:
<code>
model = YOLO(r'{your_new_best_weight_path}')  # Paste your new generated best weight path that you copied in previous step.
</code>
</p>
<p>
7- Now you can write "python main.py" to command line to make prediction with your improved model.
</p>