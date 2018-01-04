# keras-log-to-graph

### What's is this ?

A tiny script for visualizing loss and accuracy from Keras training output text.

### Requirements

- Python2 or Python3
- dependency packages
	- matplotlib

### Usage

##### From file

1. Save log text into a file.

	Sample log text:
	
	```
	Train on 50000 samples, validate on 10000 samples
	Epoch 1/4
	50000/50000 [==============================] - 4s - 	loss: 1.1514 - acc: 0.5976 - val_loss: 0.9149 - 	val_acc: 0.6829
	Epoch 2/4
	50000/50000 [==============================] - 4s - 	loss: 1.0144 - acc: 0.6488 - val_loss: 0.9346 - 	val_acc: 0.6722
	Epoch 3/4
	50000/50000 [==============================] - 4s - 	loss: 0.9641 - acc: 0.6665 - val_loss: 0.9359 - 	val_acc: 0.6847
	Epoch 4/4
	50000/50000 [==============================] - 4s - 	loss: 0.9388 - acc: 0.6775 - val_loss: 0.9194 - 	val_acc: 0.6845
	```
	
1. Then, run script. `$ python generate_graph_from_log.py [-o output_filename] log.txt`

##### From clipboard (Mac OSX)

For Mac OSX, you can read data from clipboard.

1. Copy log text into clipboard.

	Sample log text: 
	
	```
	Train on 50000 samples, validate on 10000 samples
	Epoch 1/4
	50000/50000 [==============================] - 4s - 	loss: 1.1514 - acc: 0.5976 - val_loss: 0.9149 - 	val_acc: 0.6829
	Epoch 2/4
	50000/50000 [==============================] - 4s - 	loss: 1.0144 - acc: 0.6488 - val_loss: 0.9346 - 	val_acc: 0.6722
	Epoch 3/4
	50000/50000 [==============================] - 4s - 	loss: 0.9641 - acc: 0.6665 - val_loss: 0.9359 - 	val_acc: 0.6847
	Epoch 4/4
	50000/50000 [==============================] - 4s - 	loss: 0.9388 - acc: 0.6775 - val_loss: 0.9194 - 	val_acc: 0.6845
	```
	
1. Then, run script. `$ python generate_graph_from_log.py [-o output_filename]`

#### Options

- `--n_epoch`, `-n`: number of epochs to plot
