import tensorflow as tf
from tensorflow import keras
from tensorflow import optimizers
from tensorflow import losses


class NNModel:
    model_count = 0
    def __init__(self, input_num=2, output_num=1, hidden_layers=[4], name=None, main_activation=tf.nn.relu, last_activation=tf.keras.activations.hard_sigmoid):
        self.nn = keras.Sequential()
        
        if len(hidden_layers) == 0:
            self.nn.add(keras.layers.Dense(output_num, input_dim=input_num, activation=last_activation))
        else:
            self.nn.add(keras.layers.Dense(hidden_layers[0], input_dim=input_num, activation=main_activation))                
            for i in hidden_layers[1:-1]:
                self.nn.add(keras.layers.Dense(i, activation=main_activation))
            self.nn.add(keras.layers.Dense(output_num, activation=last_activation))
        self.nn.compile(optimizer='Adam', loss=losses.mse)
        
        NNModel.model_count += 1
        if name is None:
            self.name = "Model " + str(NNModel.model_count)
        else:
            self.name = str(name)

    def reset_optimiser(self):
        opt = keras.optimizers.Adam()
        self.nn.compile(optimizer=opt, loss=losses.mse)

    # use the model to give a prediction for a given position
    def predict(self, x, y):
        output = self.nn.predict([[x,y]])
        return output[0]


    # train the model using the inputs and outputs provided
    # and return the accuracy
    def train(self, input, output, epochs=5):
        lesson = self.nn.fit(input, output, epochs=epochs, verbose=0)        
        return lesson.history['loss'][-1]


    # save the model's weights to a file
    def save_weights(self, dir):
        self.nn.save_weights(dir)

    # load the model's weights from a file
    def load_weights(self, dir):
        self.nn.load_weights(dir)