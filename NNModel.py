import tensorflow as tf
from tensorflow import keras
from tensorflow import optimizers
from tensorflow import losses

class NNModel:
    def __init__(self, input_num=2, output_num=1, hidden_layers=[4], last_activation=tf.keras.activations.hard_sigmoid):
        self.nn = keras.Sequential()
        if len(hidden_layers) == 0:
            self.nn.add(keras.layers.Dense(output_num, input_dim=input_num, activation=last_activation))
        else:
            self.nn.add(keras.layers.Dense(hidden_layers[0], input_dim=input_num, activation=tf.nn.relu))                
            for i in hidden_layers[1:-1]:
                self.nn.add(keras.layers.Dense(i, activation=tf.nn.relu))
            self.nn.add(keras.layers.Dense(output_num, activation=last_activation))
            self.nn.compile(optimizer='Adam', loss=losses.mse)
        
        self.lesson_memory=[]


    def predict(self, x, y):
        output = self.nn.predict([[x,y]])
        return output[0]

    def show_prediction_accuracy(self, inputs, t):
        for i in range(len(inputs)):
            print(str(i)+".", "("+str(inputs[i][0]),str(inputs[i][1])+")",'=', t[i], '>', self.nn.predict([[inputs[i][0],inputs[i][1]]])[0])
    
    def teach(self, input, output, epochs=5):
        lesson = self.nn.fit(input, output, epochs=epochs, verbose=0)
        self.lesson_memory.append(lesson)

    def get_loss_history(self):
        loss_list = []
        for lesson in self.lesson_memory:
            loss_list.append(lesson.history['loss'])
        return loss_list

        