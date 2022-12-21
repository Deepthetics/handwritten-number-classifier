import pandas as pd
from distance_measures import distance_d22, distance_d23, distance_d23_mod
from image_data_processing import to_array, extract, to_binary
from image_plotting import plot_two_images, plot_classification
from knn import classify_one, classify_many, classification_summary
from ui import UI


# Read MNIST data into 2D-arrays
train_data = pd.read_csv('data/mnist_train.csv')
test_data = pd.read_csv('data/mnist_test.csv')

# Extract image and label data
train_X_grey, train_y = extract(train_data)
test_X_grey, test_y = extract(test_data)

# Convert greyscale image data to binary (black and white) image data
#train_X = to_binary(train_X_grey)
#test_X = to_binary(test_X_grey)

# Store converted data in ./data as 'train_x.csv' and 'test_x.csv'
#train_X.to_csv('train_x.csv')
#test_X.to_csv('test_x.csv')

# Read binary (black and white) image data into 2D-arrays
train_X = pd.read_csv('data/train_x.csv').iloc[:,1:]
test_X = pd.read_csv('data/test_x.csv').iloc[:,1:]

# Plot corresponding greyscale and black and white images side by side
#plot_two_images(to_array(train_X_grey.iloc[0]), to_array(train_X.iloc[0]), 'greyscale', 'black and white')

# Classify an image from test data using k-NN and plot the result
#plot_classification(to_array(test_X.iloc[0]),
#                    classify_one(train_X=train_X, train_y=train_y, image=test_X.iloc[0], k=100, distance_function=distance_d22),
#                    test_y.iloc[0])

# Classify 100 images from test data using k-NN
#predicted_labels = classify_many(train_X.iloc[0:60000], train_y, test_X.iloc[0:50], k=5, distance_function=distance_d22)
#real_labels = list(test_y.iloc[0:50].to_numpy())

# Print classification summary
#print(classification_summary(predicted_labels, real_labels))

ui = UI(train_X, train_y, test_X, test_y)
ui.start()
