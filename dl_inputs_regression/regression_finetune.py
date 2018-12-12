import numpy as np ;
from kerasAC.metrics import * 

def getModelGivenModelOptionsAndWeightInits(w0,w1,init_weights,checkpoint_weights,checkpoint_arch,ntasks,seed):
    np.random.seed(seed)
    import keras;
    from keras.models import Sequential
    from keras.layers.core import Dropout, Reshape, Dense, Activation, Flatten
    from keras.layers.convolutional import Conv2D, MaxPooling2D
    from keras.optimizers import Adadelta, SGD, RMSprop;
    import keras.losses;
    from keras.constraints import maxnorm;
    from keras.layers.normalization import BatchNormalization
    from keras.regularizers import l1, l2    
    from keras import backend as K
    K.set_image_data_format('channels_last')
    print(K.image_data_format())

    model=Sequential()
    model.add(Conv2D(filters=300,kernel_size=(1,19),input_shape=(1,1000,4),padding="same"))
    model.add(BatchNormalization(axis=-1))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(1,3)))

    model.add(Conv2D(filters=200,kernel_size=(1,11),padding="same"))
    model.add(BatchNormalization(axis=-1))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(1,4)))

    model.add(Conv2D(filters=200,kernel_size=(1,7),padding="same"))
    model.add(BatchNormalization(axis=-1))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(1,4)))

    model.add(Flatten())
    model.add(Dense(1000))
    model.add(BatchNormalization(axis=-1))
    model.add(Activation('relu'))
    model.add(Dropout(0.3))

    model.add(Dense(1000))
    model.add(BatchNormalization(axis=-1))
    model.add(Activation('relu'))
    model.add(Dropout(0.3))
    model.add(Dense(ntasks,name="final_dense"))
    print(model.summary())
    model.load_weights(checkpoint_weights,by_name=True)        
    adam = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
    print("compiling!")
    model.compile(optimizer=adam,loss='mse',metrics=[positive_accuracy,negative_accuracy,precision,recall])
    return model
