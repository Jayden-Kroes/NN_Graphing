import tensorflow as tf
from tensorflow import keras
from tensorflow import optimizers
from tensorflow import losses

class NNModel:
    def __init__(self, input_num=2, output_num=1, hidden_layers=[4], main_activation=tf.nn.relu, last_activation=tf.keras.activations.hard_sigmoid):
        self.nn = keras.Sequential()
        if len(hidden_layers) == 0:
            self.nn.add(keras.layers.Dense(output_num, input_dim=input_num, activation=last_activation))
        else:
            self.nn.add(keras.layers.Dense(hidden_layers[0], input_dim=input_num, activation=main_activation))                
            for i in hidden_layers[1:-1]:
                self.nn.add(keras.layers.Dense(i, activation=main_activation))
            self.nn.add(keras.layers.Dense(output_num, activation=last_activation))
            self.nn.compile(optimizer='Adam', loss=losses.mse)
        
        self.lesson_memory=[]
        self.accuracy_history=[]
        self._greatest_accuracy = 1.0


    def predict(self, x, y):
        output = self.nn.predict([[x,y]])
        return output[0]

    def show_prediction_accuracy(self, inputs, t):
        for i in range(len(inputs)):
            print(str(i)+".", "("+str(inputs[i][0]),str(inputs[i][1])+")",'=', t[i], '>', self.nn.predict([[inputs[i][0],inputs[i][1]]])[0])
    
    def teach(self, input, output, epochs=5):
        lesson = self.nn.fit(input, output, epochs=epochs, verbose=0)
        self.lesson_memory.append(lesson)
        latest_accuracy = lesson.history['loss'][-1]
        self.accuracy_history.append(latest_accuracy)
        if latest_accuracy < self._greatest_accuracy:
            self._greatest_accuracy = latest_accuracy

    def get_loss_history(self):
        return self.accuracy_history

    def save_weights(self, dir):
        self.nn.save_weights(dir)

    def load_weights(self, dir):
        self.nn.load_weights(dir) 
        
    def get_lowest_accuracy(self):
        return self._greatest_accuracy